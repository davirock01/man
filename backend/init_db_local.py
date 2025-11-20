"""
Inicializar base de datos SQLite con datos de prueba
"""
from app.db.sqlite_session import init_db, SessionLocal
from app.models.usuario import Usuario
from app.models.vehiculo import Vehiculo
from app.core.security import get_password_hash

def create_test_data():
    """Crear usuarios y vehículos de prueba"""
    db = SessionLocal()
    
    try:
        # Verificar si ya existen usuarios
        existing_user = db.query(Usuario).first()
        if existing_user:
            print("✅ La base de datos ya tiene datos")
            return
        
        print("📝 Creando usuarios de prueba...")
        
        # Crear usuarios
        usuarios = [
            Usuario(
                email="admin@test.com",
                nombre="Admin User",
                hash_password=get_password_hash("testpass123"),
                rol="ADMIN",
                estado="ACTIVO"
            ),
            Usuario(
                email="coordinador@test.com",
                nombre="María González",
                hash_password=get_password_hash("testpass123"),
                rol="COORDINADOR",
                estado="ACTIVO"
            ),
            Usuario(
                email="conductor@test.com",
                nombre="Juan Pérez",
                hash_password=get_password_hash("testpass123"),
                rol="CONDUCTOR",
                estado="ACTIVO",
                telefono="+57 300 1234567"
            ),
            Usuario(
                email="tecnico@test.com",
                nombre="Carlos Méndez",
                hash_password=get_password_hash("testpass123"),
                rol="TECNICO",
                estado="ACTIVO"
            )
        ]
        
        for usuario in usuarios:
            db.add(usuario)
        
        print("✅ Usuarios creados:")
        for usuario in usuarios:
            print(f"   - {usuario.email} (Rol: {usuario.rol})")
        
        print("\n📝 Creando vehículos de prueba...")
        
        # Crear vehículos
        vehiculos = [
            Vehiculo(
                placa="TEST123",
                vin="1HGTEST123456789",
                marca="Toyota",
                modelo="Hilux 4x4",
                anio=2020,
                tipo="PICKUP",
                estado_operativo="OPERATIVO",
                odometro_actual=50000,
                odometro_ultimo_pm=40000
            ),
            Vehiculo(
                placa="TURBO456",
                vin="1HGTURBO456789012",
                marca="Ford",
                modelo="Ranger Turbo",
                anio=2021,
                tipo="TURBO",
                estado_operativo="OPERATIVO",
                odometro_actual=75000,
                odometro_ultimo_pm=65000
            )
        ]
        
        for vehiculo in vehiculos:
            db.add(vehiculo)
        
        db.commit()
        
        print("✅ Vehículos creados:")
        for vehiculo in vehiculos:
            print(f"   - {vehiculo.placa} ({vehiculo.modelo})")
        
        print("\n✅ Base de datos inicializada correctamente!")
        print("\n📋 Usuarios de prueba (password para todos: testpass123):")
        print("   - admin@test.com")
        print("   - coordinador@test.com")
        print("   - conductor@test.com")
        print("   - tecnico@test.com")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    print("\n🚀 Inicializando base de datos Fleet Maintenance System...\n")
    
    # Crear tablas
    print("📝 Creando tablas...")
    init_db()
    print("✅ Tablas creadas\n")
    
    # Crear datos de prueba
    create_test_data()
    
    print("\n✅ ¡Listo! Puedes iniciar el servidor con: python -m uvicorn app.main:app --reload")

