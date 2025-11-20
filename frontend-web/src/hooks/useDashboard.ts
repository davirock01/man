import { useQuery } from '@tanstack/react-query';
import api from '../services/api';

export interface DashboardData {
  alertas_predictivas: any[];
  alertas_reactivas: any[];
  patrones_recurrentes: any[];
  ot_activas: number;
  vehiculos_no_operativos: number;
  pm_vencidos: number;
}

export function useDashboard() {
  return useQuery<DashboardData>({
    queryKey: ['dashboard'],
    queryFn: async () => {
      const response = await api.get('/coordinador/dashboard');
      return response.data;
    },
    refetchInterval: 60000, // Refresh every minute
  });
}

