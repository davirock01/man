import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { VehiculosScreen } from '../screens/conductor/VehiculosScreen';
import { DVIRScreen } from '../screens/conductor/DVIRScreen';
import { ChecklistScreen } from '../screens/conductor/ChecklistScreen';
import { FotoCapturaScreen } from '../screens/conductor/FotoCapturaScreen';
import { FirmaScreen } from '../screens/conductor/FirmaScreen';
import { ReportarDefectoScreen } from '../screens/conductor/ReportarDefectoScreen';
import { FinJornadaScreen } from '../screens/conductor/FinJornadaScreen';

const Stack = createNativeStackNavigator();

export function ConductorStack() {
  return (
    <Stack.Navigator>
      <Stack.Screen 
        name="Vehiculos" 
        component={VehiculosScreen}
        options={{ title: 'Mis Vehículos' }}
      />
      <Stack.Screen 
        name="DVIR" 
        component={DVIRScreen}
        options={{ title: 'Inspección Preoperativa' }}
      />
      <Stack.Screen 
        name="Checklist" 
        component={ChecklistScreen}
        options={{ title: 'Checklist DVIR' }}
      />
      <Stack.Screen 
        name="FotoCaptura" 
        component={FotoCapturaScreen}
        options={{ title: 'Capturar Foto' }}
      />
      <Stack.Screen 
        name="Firma" 
        component={FirmaScreen}
        options={{ title: 'Firma Digital' }}
      />
      <Stack.Screen 
        name="ReportarDefecto" 
        component={ReportarDefectoScreen}
        options={{ title: 'Reportar Defecto' }}
      />
      <Stack.Screen 
        name="FinJornada" 
        component={FinJornadaScreen}
        options={{ title: 'Fin de Jornada' }}
      />
    </Stack.Navigator>
  );
}

