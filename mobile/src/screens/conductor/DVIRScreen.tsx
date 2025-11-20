/**
 * DVIR Screen - CRÍTICO
 * 
 * UX OBJETIVO: ≤5 MINUTOS de tiempo total
 * REQUISITOS:
 * - Máximo 3-4 toques por ítem
 * - Feedback visual inmediato
 * - Captura rápida de fotos
 * - Firma digital simple
 * - Funciona offline
 * 
 * OPTIMIZACIONES:
 * - Checklist colapsable por categorías
 * - Botones grandes y accesibles
 * - Estados persistidos localmente
 * - Scroll optimizado
 */

import { useState, useEffect } from 'react';
import { View, Text, ScrollView, TouchableOpacity, StyleSheet, Alert, ActivityIndicator, TextInput } from 'react-native';
import { useNavigation, useRoute } from '@react-navigation/native';
import { useDVIRStore } from '../../store/dvirStore';
import { useNetworkStatus } from '../../hooks/useNetworkStatus';
import * as Location from 'expo-location';

interface ChecklistItem {
  id: string;
  componente: string;
  categoria: string;
  estado: 'OK' | 'ALERTA' | 'CRITICO' | null;
  requiere_foto: boolean;
  foto_url?: string;
  comentario?: string;
}

export function DVIRScreen() {
  const navigation = useNavigation();
  const route = useRoute();
  const { vehiculo } = route.params as any;
  
  const [items, setItems] = useState<ChecklistItem[]>([]);
  const [odometro, setOdometro] = useState('');
  const [location, setLocation] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const [expandedCategories, setExpandedCategories] = useState<Set<string>>(new Set());
  
  const { isOnline } = useNetworkStatus();
  const { saveDVIRDraft, clearDraft } = useDVIRStore();

  useEffect(() => {
    loadChecklist();
    getLocation();
    // Auto-expand first category
    if (items.length > 0) {
      const firstCat = items[0].categoria;
      setExpandedCategories(new Set([firstCat]));
    }
  }, []);

  const loadChecklist = async () => {
    // In production, load from API or cache
    // For now, mock data
    const mockItems: ChecklistItem[] = [
      { id: '1', componente: 'Motor', categoria: 'Mecánico', estado: null, requiere_foto: false },
      { id: '2', componente: 'Frenos', categoria: 'Mecánico', estado: null, requiere_foto: true },
      { id: '3', componente: 'Luces delanteras', categoria: 'Eléctrico', estado: null, requiere_foto: false },
      { id: '4', componente: 'Luces traseras', categoria: 'Eléctrico', estado: null, requiere_foto: false },
      { id: '5', componente: 'Neumáticos', categoria: 'Seguridad', estado: null, requiere_foto: false },
      { id: '6', componente: 'Extintor', categoria: 'Seguridad', estado: null, requiere_foto: false },
    ];
    setItems(mockItems);
  };

  const getLocation = async () => {
    try {
      const { status } = await Location.requestForegroundPermissionsAsync();
      if (status === 'granted') {
        const loc = await Location.getCurrentPositionAsync({});
        setLocation(loc.coords);
      }
    } catch (error) {
      console.error('Error getting location:', error);
    }
  };

  const updateItemEstado = (itemId: string, estado: 'OK' | 'ALERTA' | 'CRITICO') => {
    setItems(prev => prev.map(item => 
      item.id === itemId ? { ...item, estado } : item
    ));

    // Auto-save draft
    saveDVIRDraft({ vehiculo, items, odometro, location });
  };

  const handleCapturarFoto = (itemId: string) => {
    navigation.navigate('FotoCaptura' as never, { itemId, onCapture: (url: string) => {
      setItems(prev => prev.map(item => 
        item.id === itemId ? { ...item, foto_url: url } : item
      ));
    }} as never);
  };

  const toggleCategory = (categoria: string) => {
    setExpandedCategories(prev => {
      const newSet = new Set(prev);
      if (newSet.has(categoria)) {
        newSet.delete(categoria);
      } else {
        newSet.add(categoria);
      }
      return newSet;
    });
  };

  const canSubmit = () => {
    // All items must have a status
    const allComplete = items.every(item => item.estado !== null);
    // Critical items must have photos
    const criticalItemsOk = items
      .filter(item => item.estado === 'CRITICO' || item.estado === 'ALERTA')
      .filter(item => item.requiere_foto)
      .every(item => item.foto_url);
    
    return allComplete && criticalItemsOk && odometro.length > 0;
  };

  const handleContinuarFirma = () => {
    if (!canSubmit()) {
      Alert.alert('Incompleto', 'Por favor completa todos los ítems del checklist');
      return;
    }

    navigation.navigate('Firma' as never, {
      dvirData: {
        vehiculo_id: vehiculo.id,
        odometro: parseFloat(odometro),
        gps_lat: location?.latitude,
        gps_lng: location?.longitude,
        items: items.map(item => ({
          componente: item.componente,
          categoria: item.categoria,
          estado_item: item.estado,
          foto_url: item.foto_url,
          comentario: item.comentario,
        })),
      }
    } as never);
  };

  // Group items by category
  const categorias = Array.from(new Set(items.map(item => item.categoria)));

  return (
    <View style={styles.container}>
      {/* Header with progress */}
      <View style={styles.header}>
        <Text style={styles.headerTitle}>DVIR - {vehiculo.placa}</Text>
        <View style={styles.progressContainer}>
          <Text style={styles.progressText}>
            {items.filter(i => i.estado).length} / {items.length} completados
          </Text>
          {!isOnline && (
            <Text style={styles.offlineIndicator}>📵 Modo Offline</Text>
          )}
        </View>
      </View>

      <ScrollView style={styles.scrollView}>
        {/* Odometer input */}
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>Odómetro Actual</Text>
          <TextInput
            style={styles.odometroInput}
            keyboardType="numeric"
            placeholder="Ingresa odómetro (km)"
            value={odometro}
            onChangeText={setOdometro}
          />
        </View>

        {/* Checklist by categories */}
        {categorias.map(categoria => {
          const categoryItems = items.filter(item => item.categoria === categoria);
          const isExpanded = expandedCategories.has(categoria);
          const completedCount = categoryItems.filter(i => i.estado).length;

          return (
            <View key={categoria} style={styles.categoryContainer}>
              <TouchableOpacity
                style={styles.categoryHeader}
                onPress={() => toggleCategory(categoria)}
              >
                <Text style={styles.categoryTitle}>{categoria}</Text>
                <Text style={styles.categoryProgress}>
                  {completedCount}/{categoryItems.length} {isExpanded ? '▼' : '▶'}
                </Text>
              </TouchableOpacity>

              {isExpanded && categoryItems.map(item => (
                <View key={item.id} style={styles.checklistItem}>
                  <Text style={styles.itemName}>{item.componente}</Text>
                  
                  <View style={styles.buttonRow}>
                    <TouchableOpacity
                      style={[styles.statusButton, styles.okButton, item.estado === 'OK' && styles.selectedButton]}
                      onPress={() => updateItemEstado(item.id, 'OK')}
                    >
                      <Text style={[styles.buttonText, item.estado === 'OK' && styles.selectedButtonText]}>✓ OK</Text>
                    </TouchableOpacity>

                    <TouchableOpacity
                      style={[styles.statusButton, styles.alertaButton, item.estado === 'ALERTA' && styles.selectedButton]}
                      onPress={() => updateItemEstado(item.id, 'ALERTA')}
                    >
                      <Text style={[styles.buttonText, item.estado === 'ALERTA' && styles.selectedButtonText]}>⚠ ALERTA</Text>
                    </TouchableOpacity>

                    <TouchableOpacity
                      style={[styles.statusButton, styles.criticoButton, item.estado === 'CRITICO' && styles.selectedButton]}
                      onPress={() => updateItemEstado(item.id, 'CRITICO')}
                    >
                      <Text style={[styles.buttonText, item.estado === 'CRITICO' && styles.selectedButtonText]}>✖ CRÍTICO</Text>
                    </TouchableOpacity>
                  </View>

                  {item.requiere_foto && (item.estado === 'ALERTA' || item.estado === 'CRITICO') && (
                    <TouchableOpacity
                      style={styles.fotoButton}
                      onPress={() => handleCapturarFoto(item.id)}
                    >
                      <Text style={styles.fotoButtonText}>
                        {item.foto_url ? '📷 Foto capturada' : '📷 Capturar foto (requerido)'}
                      </Text>
                    </TouchableOpacity>
                  )}
                </View>
              ))}
            </View>
          );
        })}
      </ScrollView>

      {/* Fixed bottom button */}
      <View style={styles.bottomButton}>
        <TouchableOpacity
          style={[styles.submitButton, !canSubmit() && styles.submitButtonDisabled]}
          onPress={handleContinuarFirma}
          disabled={!canSubmit()}
        >
          <Text style={styles.submitButtonText}>
            Continuar a Firma →
          </Text>
        </TouchableOpacity>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
  },
  header: {
    backgroundColor: 'white',
    padding: 16,
    borderBottomWidth: 1,
    borderBottomColor: '#e5e7eb',
  },
  headerTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#111827',
  },
  progressContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginTop: 8,
  },
  progressText: {
    fontSize: 14,
    color: '#6b7280',
  },
  offlineIndicator: {
    fontSize: 12,
    color: '#f59e0b',
    fontWeight: '600',
  },
  scrollView: {
    flex: 1,
  },
  section: {
    backgroundColor: 'white',
    padding: 16,
    marginVertical: 8,
    marginHorizontal: 16,
    borderRadius: 8,
  },
  sectionTitle: {
    fontSize: 16,
    fontWeight: '600',
    marginBottom: 12,
    color: '#111827',
  },
  odometroInput: {
    height: 50,
    borderWidth: 1,
    borderColor: '#d1d5db',
    borderRadius: 8,
    paddingHorizontal: 16,
    fontSize: 18,
    fontWeight: '600',
  },
  categoryContainer: {
    backgroundColor: 'white',
    marginVertical: 4,
    marginHorizontal: 16,
    borderRadius: 8,
    overflow: 'hidden',
  },
  categoryHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: 16,
    backgroundColor: '#f3f4f6',
  },
  categoryTitle: {
    fontSize: 16,
    fontWeight: '600',
    color: '#111827',
  },
  categoryProgress: {
    fontSize: 14,
    color: '#6b7280',
  },
  checklistItem: {
    padding: 16,
    borderBottomWidth: 1,
    borderBottomColor: '#f3f4f6',
  },
  itemName: {
    fontSize: 15,
    fontWeight: '500',
    marginBottom: 12,
    color: '#111827',
  },
  buttonRow: {
    flexDirection: 'row',
    gap: 8,
  },
  statusButton: {
    flex: 1,
    paddingVertical: 12,
    borderRadius: 8,
    borderWidth: 2,
    alignItems: 'center',
  },
  okButton: {
    backgroundColor: '#f0fdf4',
    borderColor: '#86efac',
  },
  alertaButton: {
    backgroundColor: '#fef3c7',
    borderColor: '#fcd34d',
  },
  criticoButton: {
    backgroundColor: '#fee2e2',
    borderColor: '#fca5a5',
  },
  selectedButton: {
    borderWidth: 3,
  },
  buttonText: {
    fontSize: 14,
    fontWeight: '600',
    color: '#374151',
  },
  selectedButtonText: {
    color: '#111827',
  },
  fotoButton: {
    marginTop: 12,
    padding: 12,
    backgroundColor: '#dbeafe',
    borderRadius: 8,
    alignItems: 'center',
  },
  fotoButtonText: {
    fontSize: 14,
    color: '#1e40af',
    fontWeight: '600',
  },
  bottomButton: {
    padding: 16,
    backgroundColor: 'white',
    borderTopWidth: 1,
    borderTopColor: '#e5e7eb',
  },
  submitButton: {
    backgroundColor: '#2563eb',
    paddingVertical: 16,
    borderRadius: 8,
    alignItems: 'center',
  },
  submitButtonDisabled: {
    backgroundColor: '#9ca3af',
  },
  submitButtonText: {
    color: 'white',
    fontSize: 18,
    fontWeight: '700',
  },
});

