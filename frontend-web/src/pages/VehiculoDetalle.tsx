import { useParams } from 'react-router-dom';

export default function VehiculoDetalle() {
  const { id } = useParams();

  return (
    <div className="container">
      <h1>Detalle del Vehículo {id}</h1>
      <p>Aquí se mostrará el contexto completo del vehículo con score de salud, predicciones PM, DVIR history, etc.</p>
    </div>
  );
}

