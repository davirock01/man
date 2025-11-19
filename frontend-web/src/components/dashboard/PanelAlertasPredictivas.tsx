interface AlertaPredictiva {
  id: string;
  tipo: string;
  mensaje: string;
  criticidad: string;
  creado_en: string;
}

interface Props {
  alertas: AlertaPredictiva[];
}

export default function PanelAlertasPredictivas({ alertas }: Props) {
  return (
    <div className="panel panel-alertas-predictivas">
      <h2 style={{ marginBottom: '20px' }}>Alertas Predictivas (PM Próximas)</h2>
      
      <div className="alertas-list">
        {alertas.length === 0 && (
          <p style={{ color: '#999', textAlign: 'center', padding: '20px' }}>
            No hay alertas predictivas pendientes
          </p>
        )}
        
        {alertas.map(alerta => (
          <div 
            key={alerta.id} 
            className={`alerta-card criticidad-${alerta.criticidad.toLowerCase()}`}
          >
            <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '8px' }}>
              <span style={{ fontWeight: '600' }}>{alerta.tipo}</span>
              <span className={`badge badge-${alerta.criticidad.toLowerCase()}`}>
                {alerta.criticidad}
              </span>
            </div>
            <p style={{ color: '#666', fontSize: '14px' }}>{alerta.mensaje}</p>
            <div style={{ marginTop: '8px', fontSize: '12px', color: '#999' }}>
              <span>{new Date(alerta.creado_en).toLocaleString('es-CO')}</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

