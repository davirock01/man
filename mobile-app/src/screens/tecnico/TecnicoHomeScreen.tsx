import React, { useEffect, useState } from 'react';
import { View, StyleSheet, FlatList } from 'react-native';
import { Card, Title, Paragraph, Button, Chip } from 'react-native-paper';
import api from '../../services/api';

export default function TecnicoHomeScreen({ navigation }: any) {
  const [ordenes, setOrdenes] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadOrdenes();
  }, []);

  const loadOrdenes = async () => {
    try {
      const response = await api.get('/tecnico/ordenes-trabajo?tecnico_id=me');
      setOrdenes(response.data);
    } catch (error) {
      console.error('Error loading ordenes:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleOpenOrden = (orden: any) => {
    navigation.navigate('OrdenDetalle', { orden });
  };

  const renderOrden = ({ item }: any) => (
    <Card style={styles.card}>
      <Card.Content>
        <View style={styles.cardHeader}>
          <Title>OT-{item.id.substring(0, 8)}</Title>
          <Chip mode="outlined" style={getPrioridadStyle(item.prioridad)}>
            {item.prioridad}
          </Chip>
        </View>
        <Paragraph>Vehículo: {item.vehiculo_id}</Paragraph>
        <Paragraph>Tipo: {item.tipo}</Paragraph>
        <Paragraph>Estado: {item.estado}</Paragraph>
      </Card.Content>
      <Card.Actions>
        <Button onPress={() => handleOpenOrden(item)}>Ver Detalle</Button>
      </Card.Actions>
    </Card>
  );

  const getPrioridadStyle = (prioridad: string) => {
    switch (prioridad) {
      case 'URGENTE':
        return { backgroundColor: '#f44336' };
      case 'ALTA':
        return { backgroundColor: '#ff9800' };
      default:
        return { backgroundColor: '#2196f3' };
    }
  };

  return (
    <View style={styles.container}>
      <Title style={styles.title}>Mis Órdenes de Trabajo</Title>
      <FlatList
        data={ordenes}
        renderItem={renderOrden}
        keyExtractor={(item: any) => item.id}
        refreshing={loading}
        onRefresh={loadOrdenes}
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

