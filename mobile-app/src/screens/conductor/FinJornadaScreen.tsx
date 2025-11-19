import React from 'react';
import { View, StyleSheet } from 'react-native';
import { Title, Text } from 'react-native-paper';

export default function FinJornadaScreen() {
  return (
    <View style={styles.container}>
      <Title>Fin de Jornada</Title>
      <Text>Funcionalidad de cierre de jornada - Por implementar</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

