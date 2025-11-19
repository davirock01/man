import React from 'react';
import { View, StyleSheet, ScrollView } from 'react-native';
import { Title, Text, Button } from 'react-native-paper';

export default function OrdenDetalleScreen({ route }: any) {
  const { orden } = route.params;

  return (
    <ScrollView style={styles.container}>
      <Title style={styles.title}>Detalle OT</Title>
      <Text>ID: {orden.id}</Text>
      <Text>Tipo: {orden.tipo}</Text>
      <Text>Estado: {orden.estado}</Text>
      <Text>Prioridad: {orden.prioridad}</Text>
      
      <Button mode="contained" style={styles.button}>
        Iniciar Trabajo
      </Button>
      
      {/* TODO: Implement full OT detail and actions */}
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
  button: {
    marginTop: 20,
  },
});

