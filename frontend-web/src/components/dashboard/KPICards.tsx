interface Props {
  otActivas: number;
  vehiculosNoOperativos: number;
  pmVencidos: number;
}

export default function KPICards({ otActivas, vehiculosNoOperativos, pmVencidos }: Props) {
  return (
    <div style={{
      display: 'grid',
      gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
      gap: '20px',
      marginBottom: '30px'
    }}>
      <div className="panel" style={{ textAlign: 'center' }}>
        <h3 style={{ color: '#667eea', fontSize: '36px', margin: '10px 0' }}>{otActivas}</h3>
        <p style={{ color: '#666' }}>OT Activas</p>
      </div>

      <div className="panel" style={{ textAlign: 'center' }}>
        <h3 style={{ color: '#f44336', fontSize: '36px', margin: '10px 0' }}>{vehiculosNoOperativos}</h3>
        <p style={{ color: '#666' }}>Vehículos No Operativos</p>
      </div>

      <div className="panel" style={{ textAlign: 'center' }}>
        <h3 style={{ color: '#ff9800', fontSize: '36px', margin: '10px 0' }}>{pmVencidos}</h3>
        <p style={{ color: '#666' }}>PM Vencidos</p>
      </div>
    </div>
  );
}

