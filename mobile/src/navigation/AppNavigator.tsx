import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { useAuthStore } from '../store/authStore';
import { LoginScreen } from '../screens/LoginScreen';
import { ConductorStack } from './ConductorStack';
import { TecnicoStack } from './TecnicoStack';

const Stack = createNativeStackNavigator();

export function AppNavigator() {
  const { isAuthenticated, user } = useAuthStore();

  if (!isAuthenticated) {
    return (
      <Stack.Navigator screenOptions={{ headerShown: false }}>
        <Stack.Screen name="Login" component={LoginScreen} />
      </Stack.Navigator>
    );
  }

  // Route based on user role
  if (user?.rol === 'CONDUCTOR') {
    return <ConductorStack />;
  } else if (user?.rol === 'TECNICO') {
    return <TecnicoStack />;
  }

  // Default fallback
  return <ConductorStack />;
}

