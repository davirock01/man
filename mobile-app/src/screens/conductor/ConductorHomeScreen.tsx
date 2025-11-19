import React, { useEffect, useState } from 'react';
import { View, StyleSheet, FlatList } from 'react-native';
import { Card, Title, Paragraph, Button, Chip } from 'react-native-paper';
import api from '../../services/api';

export default function ConductorHomeScreen({ navigation }: any) {
  const [vehiculos, setVehiculos] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadVehiculos();
  }, []);

  const loadVehiculos = async () => {
    try {
      const response = await api.get('/conductor/vehiculos');
      setVehiculos(response.data);
    } catch (error) {
      console.error('Error loading vehiculos:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleStartDVIR = (vehiculo: any) => {
    navigation.navigate('DVIRChecklist', { vehiculo });
  };

  const renderVehiculo = ({ item }: any) => (
    <Card style={styles.card}>
      <Card.Content>
        <View style={styles.cardHeader}>
          <Title>{item.placa}</Title>
          <Chip mode="outlined" style={getScoreStyle(item.score_salud)}>
            Score: {item.score_salud?.toFixed(1) || 'N/A'}
          </Chip>
        </View>
        <Paragraph>{item.tipo} - {item.marca} {item.modelo}</Paragraph>
        <Paragraph>Odómetro: {item.odometro_actual} km</Paragraph>
        <Paragraph>Estado: {item.estado_operativo}</Paragraph>
      </Card.Content>
      <Card.Actions>
        <Button onPress={() => handleStartDVIR(item)}>Iniciar DVIR</Button>
      </Card.Actions>
    </Card>
  );

  const getScoreStyle = (score: number) => {
    if (score >= 80) return { backgroundColor: '#4caf50' };
    if (score >= 60) return { backgroundColor: '#ff9800' };
    return { backgroundColor: '#f44336' };
  };

  return (
    <View style={styles.container}>
      <Title style={styles.title}>Mis Vehículos</Title>
      <FlatList
        data={vehiculos}
        renderItem={renderVehiculo}
        keyExtractor={(item: any) => item.id}
        refreshing={loading}
        onRefresh={loadVehiculos}
        contentContainerStyle={styles.list}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
  },
  title: {
    padding: 20,
    fontSize: 24,
  },
  list: {
    padding: 10,
  },
  card: {
    marginBottom: 15,
  },
  cardHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 10,
  },
});

