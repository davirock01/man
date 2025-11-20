import React, { useState, useEffect } from 'react';
import { View, StyleSheet, ScrollView, Alert } from 'react-native';
import { Title, TextInput, Button, RadioButton, Text } from 'react-native-paper';
import { SyncQueue } from '../../services/offline/syncQueue';
import api from '../../services/api';
import NetInfo from '@react-native-community/netinfo';

export default function DVIRChecklistScreen({ route, navigation }: any) {
  const { vehiculo } = route.params;
  const [checklist, setChecklist] = useState<any[]>([]);
  const [odometro, setOdometro] = useState('');
  const [items, setItems] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);
  const [isOnline, setIsOnline] = useState(true);

  useEffect(() => {
    loadChecklist();
    
    const unsubscribe = NetInfo.addEventListener(state => {
      setIsOnline(state.isConnected || false);
    });

    return () => unsubscribe();
  }, []);

  const loadChecklist = async () => {
    try {
      const response = await api.get(`/conductor/checklists/${vehiculo.tipo}`);
      const checklistItems = response.data.items;
      setChecklist(checklistItems);
      setItems(checklistItems.map((item: any) => ({
        componente: item.componente,
        estado_item: 'OK',
        comentario: '',
        foto_url: '',
      })));
    } catch (error) {
      console.error('Error loading checklist:', error);
      // Load from cache if offline
    }
  };

  const handleItemChange = (index: number, field: string, value: any) => {
    const newItems = [...items];
    newItems[index] = { ...newItems[index], [field]: value };
    setItems(newItems);
  };

  const handleSubmit = async () => {
    if (!odometro) {
      Alert.alert('Error', 'Debes ingresar el odómetro');
      return;
    }

    setLoading(true);
    
    const dvirData = {
      vehiculo_id: vehiculo.id,
      tipo: 'PREOPERATIVO',
      odometro: parseInt(odometro),
      items,
      modo_offline: !isOnline,
    };

    try {
      if (isOnline) {
        await api.post('/conductor/dvir', dvirData);
        Alert.alert('Éxito', 'DVIR enviado correctamente');
      } else {
        await SyncQueue.add('DVIR', dvirData);
        Alert.alert('Sin conexión', 'DVIR guardado. Se sincronizará automáticamente.');
      }
      navigation.goBack();
    } catch (error: any) {
      Alert.alert('Error', error.response?.data?.detail || 'No se pudo guardar el DVIR');
    } finally {
      setLoading(false);
    }
  };

  return (
    <ScrollView style={styles.container}>
      <Title style={styles.title}>DVIR - {vehiculo.placa}</Title>

      {!isOnline && (
        <View style={styles.offlineBanner}>
          <Text style={styles.offlineText}>Modo Offline - Los datos se sincronizarán luego</Text>
        </View>
      )}

      <TextInput
        label="Odómetro (km)"
        value={odometro}
        onChangeText={setOdometro}
        keyboardType="numeric"
        mode="outlined"
        style={styles.input}
      />

      <Title style={styles.subtitle}>Checklist de Inspección</Title>

      {items.map((item, index) => (
        <View key={index} style={styles.itemCard}>
          <Text style={styles.itemTitle}>{item.componente}</Text>
          
          <RadioButton.Group
            onValueChange={value => handleItemChange(index, 'estado_item', value)}
            value={item.estado_item}
          >
            <View style={styles.radioRow}>
              <RadioButton.Item label="OK" value="OK" />
              <RadioButton.Item label="ALERTA" value="ALERTA" />
              <RadioButton.Item label="CRÍTICO" value="CRITICO" />
            </View>
          </RadioButton.Group>

          {item.estado_item !== 'OK' && (
            <TextInput
              label="Comentario"
              value={item.comentario}
              onChangeText={value => handleItemChange(index, 'comentario', value)}
              mode="outlined"
              style={styles.input}
              multiline
            />
          )}
        </View>
      ))}

      <Button
        mode="contained"
        onPress={handleSubmit}
        loading={loading}
        disabled={loading}
        style={styles.submitButton}
      >
        {isOnline ? 'Enviar DVIR' : 'Guardar DVIR (Offline)'}
      </Button>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: '#fff',
  },
  title: {
    fontSize: 24,
    marginBottom: 20,
  },
  subtitle: {
    fontSize: 18,
    marginTop: 20,
    marginBottom: 10,
  },
  input: {
    marginBottom: 15,
  },
  itemCard: {
    padding: 15,
    marginBottom: 15,
    backgroundColor: '#f5f5f5',
    borderRadius: 8,
  },
  itemTitle: {
    fontSize: 16,
    fontWeight: 'bold',
    marginBottom: 10,
  },
  radioRow: {
    flexDirection: 'row',
    justifyContent: 'space-around',
  },
  submitButton: {
    marginTop: 20,
    marginBottom: 40,
    paddingVertical: 8,
  },
  offlineBanner: {
    backgroundColor: '#ff9800',
    padding: 10,
    borderRadius: 5,
    marginBottom: 15,
  },
  offlineText: {
    color: '#fff',
    textAlign: 'center',
    fontWeight: 'bold',
  },
});

