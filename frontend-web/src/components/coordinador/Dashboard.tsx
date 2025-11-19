import { useEffect, useState } from 'react';
import { coordinadorAPI } from '@/services/api';
import { AlertasPredictivas } from './AlertasPredictivas';
import { AlertasReactivas } from './AlertasReactivas';
import { PatronesRecurrentes } from './PatronesRecurrentes';

export function Dashboard() {
  const [dashboardData, setDashboardData] = useState<any>(null);
  const [kpis, setKpis] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadDashboard();
  }, []);

  const loadDashboard = async () => {
    try {
      const [dashRes, kpisRes] = await Promise.all([
        coordinadorAPI.getDashboard(),
        coordinadorAPI.getKPIs(),
      ]);
      setDashboardData(dashRes.data);
      setKpis(kpisRes.data);
    } catch (error) {
      console.error('Error loading dashboard:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <div className="flex items-center justify-center h-screen">Loading...</div>;
  }

  return (
    <div className="p-6 max-w-7xl mx-auto">
      <h1 className="text-3xl font-bold mb-6">Dashboard Coordinador</h1>

      {/* KPIs Summary */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8">
        <div className="bg-white p-4 rounded-lg shadow">
          <div className="text-sm text-gray-600">PM Compliance</div>
          <div className="text-2xl font-bold">{kpis?.pm_compliance_pct}%</div>
        </div>
        <div className="bg-white p-4 rounded-lg shadow">
          <div className="text-sm text-gray-600">Fleet Availability</div>
          <div className="text-2xl font-bold">{kpis?.disponibilidad_flota_pct}%</div>
        </div>
        <div className="bg-white p-4 rounded-lg shadow">
          <div className="text-sm text-gray-600">MTBF</div>
          <div className="text-2xl font-bold">{kpis?.mtbf_hours}h</div>
        </div>
        <div className="bg-white p-4 rounded-lg shadow">
          <div className="text-sm text-gray-600">MTTR</div>
          <div className="text-2xl font-bold">{kpis?.mttr_hours}h</div>
        </div>
      </div>

      {/* Three Panels */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Panel A: Alertas Predictivas */}
        <div className="bg-white p-4 rounded-lg shadow">
          <h2 className="text-xl font-bold mb-4">PM Próximas</h2>
          <AlertasPredictivas />
        </div>

        {/* Panel B: Alertas Reactivas */}
        <div className="bg-white p-4 rounded-lg shadow">
          <h2 className="text-xl font-bold mb-4">Defectos Críticos</h2>
          <AlertasReactivas />
        </div>

        {/* Panel C: Patrones Recurrentes */}
        <div className="bg-white p-4 rounded-lg shadow">
          <h2 className="text-xl font-bold mb-4">Patrones Recurrentes</h2>
          <PatronesRecurrentes />
        </div>
      </div>
    </div>
  );
}


