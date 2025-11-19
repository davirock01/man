import React from 'react';
import { createStackNavigator } from '@react-navigation/stack';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import LoginScreen from '../screens/LoginScreen';
import ConductorHomeScreen from '../screens/conductor/ConductorHomeScreen';
import DVIRChecklistScreen from '../screens/conductor/DVIRChecklistScreen';
import FinJornadaScreen from '../screens/conductor/FinJornadaScreen';
import TecnicoHomeScreen from '../screens/tecnico/TecnicoHomeScreen';
import OrdenDetalleScreen from '../screens/tecnico/OrdenDetalleScreen';
import SyncScreen from '../screens/common/SyncScreen';

const Stack = createStackNavigator();
const Tab = createBottomTabNavigator();

function ConductorTabs() {
  return (
    <Tab.Navigator>
      <Tab.Screen name="Home" component={ConductorHomeScreen} options={{ title: 'Inicio' }} />
      <Tab.Screen name="Sync" component={SyncScreen} options={{ title: 'Sincronizar' }} />
    </Tab.Navigator>
  );
}

function TecnicoTabs() {
  return (
    <Tab.Navigator>
      <Tab.Screen name="Ordenes" component={TecnicoHomeScreen} options={{ title: 'Órdenes' }} />
      <Tab.Screen name="Sync" component={SyncScreen} options={{ title: 'Sincronizar' }} />
    </Tab.Navigator>
  );
}

export default function AppNavigator() {
  // TODO: Check if user is logged in and get role
  const userRole = null; // Replace with actual auth check

  return (
    <Stack.Navigator screenOptions={{ headerShown: false }}>
      <Stack.Screen name="Login" component={LoginScreen} />
      <Stack.Screen name="ConductorApp" component={ConductorTabs} />
      <Stack.Screen name="TecnicoApp" component={TecnicoTabs} />
      <Stack.Screen name="DVIRChecklist" component={DVIRChecklistScreen} />
      <Stack.Screen name="FinJornada" component={FinJornadaScreen} />
      <Stack.Screen name="OrdenDetalle" component={OrdenDetalleScreen} />
    </Stack.Navigator>
  );
}

