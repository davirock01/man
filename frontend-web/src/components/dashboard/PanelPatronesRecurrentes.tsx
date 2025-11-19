interface PatronRecurrente {
  id: string;
  componente: string;
  veces_30d: number;
  criticidad: string;
}

interface Props {
  patrones: PatronRecurrente[];
}

export default function PanelPatronesRecurrentes({ patrones }: Props) {
  return (
    <div className="panel panel-patrones-recurrentes">
      <h2 style={{ marginBottom: '20px' }}>Patrones Recurrentes</h2>
      
      <div className="alertas-list">
        {patrones.length === 0 && (
          <p style={{ color: '#999', textAlign: 'center', padding: '20px' }}>
            No hay patrones recurrentes detectados
          </p>
        )}
        
        {patrones.map(patron => (
          <div 
            key={patron.id} 
            className={`alerta-card criticidad-${patron.criticidad?.toLowerCase() || 'media'}`}
          >
            <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '8px' }}>
              <span style={{ fontWeight: '600' }}>{patron.componente}</span>
              <span style={{ 
                background: '#ff9800', 
                color: 'white', 
                padding: '2px 8px', 
                borderRadius: '12px',
                fontSize: '12px'
              }}>
                {patron.veces_30d}x en 30d
              </span>
            </div>
            <p style={{ color: '#666', fontSize: '14px' }}>
              Este componente ha fallado {patron.veces_30d} veces en los últimos 30 días
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}

