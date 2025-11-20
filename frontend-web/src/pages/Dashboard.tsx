/**
 * Dashboard Principal - Coordinador
 */
import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuthStore } from '../store/authStore';

export const Dashboard: React.FC = () => {
  const user = useAuthStore((state) => state.user);
  const logout = useAuthStore((state) => state.logout);
  const navigate = useNavigate();

  const [stats] = useState({
    flota: {
      total: 50,
      operativos: 45,
      no_operativos: 3,
      en_mantenimiento: 2,
    },
    alertas: {
      predictivas: 8,
      reactivas: 5,
      patrones: 2,
    },
    ot: {
      pendientes: 12,
      en_progreso: 8,
      vencidas: 2,
    },
    kpis: {
      cumplimiento_pm: 87.5,
      disponibilidad: 90.0,
      mtbf: 45.2,
      mttr: 6.5,
    },
  });

  useEffect(() => {
    if (!user) {
      navigate('/login');
    }
  }, [user, navigate]);

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  if (!user) return null;

  return (
    <div style={{ minHeight: '100vh', background: '#f5f7fa' }}>
      {/* Header */}
      <header style={{
        background: 'white',
        borderBottom: '1px solid #e5e7eb',
        padding: '16px 24px',
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center'
      }}>
        <div>
          <h1 style={{ margin: 0, fontSize: '24px', color: '#111' }}>
            🚗 Fleet Maintenance System
          </h1>
          <p style={{ margin: '4px 0 0 0', fontSize: '14px', color: '#666' }}>
            Dashboard de Operaciones
          </p>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: '16px' }}>
          <span style={{ fontSize: '14px', color: '#666' }}>
            {user.nombre} ({user.rol})
          </span>
          <button
            onClick={handleLogout}
            style={{
              padding: '8px 16px',
              background: '#ef4444',
              color: 'white',
              border: 'none',
              borderRadius: '6px',
              cursor: 'pointer',
              fontSize: '14px'
            }}
          >
            Cerrar Sesión
          </button>
        </div>
      </header>

      {/* Main Content */}
      <div style={{ padding: '24px' }}>
        {/* KPIs Grid */}
        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))',
          gap: '20px',
          marginBottom: '30px'
        }}>
          <KPICard
            title="Cumplimiento PM"
            value={`${stats.kpis.cumplimiento_pm}%`}
            target="90%"
            color="#10b981"
          />
          <KPICard
            title="Disponibilidad Flota"
            value={`${stats.kpis.disponibilidad}%`}
            target="95%"
            color="#3b82f6"
          />
          <KPICard
            title="MTBF"
            value={`${stats.kpis.mtbf} días`}
            color="#8b5cf6"
          />
          <KPICard
            title="MTTR"
            value={`${stats.kpis.mttr} horas`}
            target="< 8h"
            color="#f59e0b"
          />
        </div>

        {/* Fleet Status */}
        <div style={{
          background: 'white',
          borderRadius: '12px',
          padding: '24px',
          marginBottom: '30px',
          boxShadow: '0 1px 3px rgba(0,0,0,0.1)'
        }}>
          <h2 style={{ margin: '0 0 20px 0', fontSize: '18px', color: '#111' }}>
            Estado de la Flota
          </h2>
          <div style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(150px, 1fr))',
            gap: '16px'
          }}>
            <StatCard label="Total Vehículos" value={stats.flota.total} color="#6366f1" />
            <StatCard label="Operativos" value={stats.flota.operativos} color="#10b981" />
            <StatCard label="No Operativos" value={stats.flota.no_operativos} color="#ef4444" />
            <StatCard label="En Mantenimiento" value={stats.flota.en_mantenimiento} color="#f59e0b" />
          </div>
        </div>

        {/* Alerts Grid */}
        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
          gap: '20px'
        }}>
          <AlertPanel
            title="Alertas Predictivas"
            subtitle="PM Próximos"
            count={stats.alertas.predictivas}
            color="#3b82f6"
            icon="🔮"
          />
          <AlertPanel
            title="Alertas Reactivas"
            subtitle="Defectos HOY"
            count={stats.alertas.reactivas}
            color="#ef4444"
            icon="🚨"
          />
          <AlertPanel
            title="Patrones Recurrentes"
            subtitle="Últimos 30 días"
            count={stats.alertas.patrones}
            color="#f59e0b"
            icon="📊"
          />
        </div>

        {/* Work Orders Summary */}
        <div style={{
          background: 'white',
          borderRadius: '12px',
          padding: '24px',
          marginTop: '30px',
          boxShadow: '0 1px 3px rgba(0,0,0,0.1)'
        }}>
          <h2 style={{ margin: '0 0 20px 0', fontSize: '18px', color: '#111' }}>
            Órdenes de Trabajo
          </h2>
          <div style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(150px, 1fr))',
            gap: '16px'
          }}>
            <StatCard label="Pendientes" value={stats.ot.pendientes} color="#6366f1" />
            <StatCard label="En Progreso" value={stats.ot.en_progreso} color="#10b981" />
            <StatCard label="Vencidas" value={stats.ot.vencidas} color="#ef4444" />
          </div>
        </div>
      </div>
    </div>
  );
};

// ============================================================
// COMPONENTES AUXILIARES
// ============================================================

interface KPICardProps {
  title: string;
  value: string;
  target?: string;
  color: string;
}

const KPICard: React.FC<KPICardProps> = ({ title, value, target, color }) => (
  <div style={{
    background: 'white',
    borderRadius: '12px',
    padding: '20px',
    boxShadow: '0 1px 3px rgba(0,0,0,0.1)'
  }}>
    <div style={{ fontSize: '14px', color: '#666', marginBottom: '8px' }}>
      {title}
    </div>
    <div style={{ fontSize: '32px', fontWeight: 'bold', color, marginBottom: '4px' }}>
      {value}
    </div>
    {target && (
      <div style={{ fontSize: '12px', color: '#999' }}>
        Objetivo: {target}
      </div>
    )}
  </div>
);

interface StatCardProps {
  label: string;
  value: number;
  color: string;
}

const StatCard: React.FC<StatCardProps> = ({ label, value, color }) => (
  <div style={{ textAlign: 'center' }}>
    <div style={{ fontSize: '36px', fontWeight: 'bold', color, marginBottom: '4px' }}>
      {value}
    </div>
    <div style={{ fontSize: '14px', color: '#666' }}>
      {label}
    </div>
  </div>
);

interface AlertPanelProps {
  title: string;
  subtitle: string;
  count: number;
  color: string;
  icon: string;
}

const AlertPanel: React.FC<AlertPanelProps> = ({ title, subtitle, count, color, icon }) => (
  <div style={{
    background: 'white',
    borderRadius: '12px',
    padding: '24px',
    boxShadow: '0 1px 3px rgba(0,0,0,0.1)',
    cursor: 'pointer',
    transition: 'transform 0.2s',
  }}
  onMouseEnter={(e) => e.currentTarget.style.transform = 'translateY(-2px)'}
  onMouseLeave={(e) => e.currentTarget.style.transform = 'translateY(0)'}
  >
    <div style={{ fontSize: '36px', marginBottom: '12px' }}>
      {icon}
    </div>
    <h3 style={{ margin: '0 0 4px 0', fontSize: '16px', color: '#111' }}>
      {title}
    </h3>
    <p style={{ margin: '0 0 12px 0', fontSize: '12px', color: '#666' }}>
      {subtitle}
    </p>
    <div style={{ fontSize: '36px', fontWeight: 'bold', color }}>
      {count}
    </div>
  </div>
);

export default Dashboard;

