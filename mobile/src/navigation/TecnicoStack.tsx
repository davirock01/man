import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { ListaOTScreen } from '../screens/tecnico/ListaOTScreen';
import { DetalleOTScreen } from '../screens/tecnico/DetalleOTScreen';
import { ActualizarOTScreen } from '../screens/tecnico/ActualizarOTScreen';
import { InventarioScreen } from '../screens/tecnico/InventarioScreen';

const Stack = createNativeStackNavigator();

export function TecnicoStack() {
  return (
    <Stack.Navigator>
      <Stack.Screen 
        name="ListaOT" 
        component={ListaOTScreen}
        options={{ title: 'Mis Órdenes de Trabajo' }}
      />
      <Stack.Screen 
        name="DetalleOT" 
        component={DetalleOTScreen}
        options={{ title: 'Detalle OT' }}
      />
      <Stack.Screen 
        name="ActualizarOT" 
        component={ActualizarOTScreen}
        options={{ title: 'Actualizar OT' }}
      />
      <Stack.Screen 
        name="Inventario" 
        component={InventarioScreen}
        options={{ title: 'Inventario' }}
      />
    </Stack.Navigator>
  );
}

