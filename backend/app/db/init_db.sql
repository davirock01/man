-- ============================================================
-- FLEET MAINTENANCE SYSTEM - DATABASE INITIALIZATION
-- ============================================================

-- USUARIOS Y AUTH
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    hash_password VARCHAR(255) NOT NULL,
    rol VARCHAR(50) NOT NULL CHECK (rol IN ('CONDUCTOR', 'COORDINADOR', 'TECNICO', 'ADMIN', 'SISTEMA')),
    estado VARCHAR(50) DEFAULT 'ACTIVO' CHECK (estado IN ('ACTIVO', 'INACTIVO', 'SUSPENDIDO')),
    telefono VARCHAR(50),
    mfa_enabled BOOLEAN DEFAULT FALSE,
    mfa_secret VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_usuarios_email ON usuarios(email);
CREATE INDEX idx_usuarios_rol ON usuarios(rol);

-- VEHICULOS
CREATE TABLE IF NOT EXISTS vehiculos (
    id SERIAL PRIMARY KEY,
    placa VARCHAR(50) UNIQUE NOT NULL,
    vin VARCHAR(100) UNIQUE,
    marca VARCHAR(100),
    modelo VARCHAR(100),
    anio INTEGER,
    tipo VARCHAR(50) NOT NULL CHECK (tipo IN ('PICKUP', 'TURBO', 'CAMION', 'OTRO')),
    estado_operativo VARCHAR(50) DEFAULT 'OPERATIVO' CHECK (estado_operativo IN ('OPERATIVO', 'NO_OPERATIVO', 'EN_MANTENIMIENTO', 'FUERA_SERVICIO')),
    odometro_actual INTEGER DEFAULT 0,
    odometro_ultimo_pm INTEGER DEFAULT 0,
    gps_device_id VARCHAR(100),
    gps_lat DECIMAL(10, 8),
    gps_lng DECIMAL(11, 8),
    gps_ultima_actualizacion TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_vehiculos_placa ON vehiculos(placa);
CREATE INDEX idx_vehiculos_estado ON vehiculos(estado_operativo);

-- CONFIG PM
CREATE TABLE IF NOT EXISTS config_pm (
    id SERIAL PRIMARY KEY,
    vehiculo_tipo VARCHAR(50) NOT NULL UNIQUE,
    descripcion TEXT,
    intervalo_km INTEGER NOT NULL DEFAULT 10000,
    intervalo_dias INTEGER NOT NULL DEFAULT 180,
    umbral_alerta_km DECIMAL(3, 2) DEFAULT 0.90,
    umbral_alerta_dias DECIMAL(3, 2) DEFAULT 0.90,
    duracion_estimada_min INTEGER DEFAULT 240,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- DVIRS
CREATE TABLE IF NOT EXISTS dvirs (
    id SERIAL PRIMARY KEY,
    vehiculo_id INTEGER NOT NULL REFERENCES vehiculos(id) ON DELETE CASCADE,
    conductor_id INTEGER NOT NULL REFERENCES usuarios(id),
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    odometro INTEGER NOT NULL,
    gps_lat DECIMAL(10, 8),
    gps_lng DECIMAL(11, 8),
    estado_resumen VARCHAR(50) NOT NULL CHECK (estado_resumen IN ('OK', 'ALERTA', 'CRITICO')),
    firma_url VARCHAR(500),
    modo_offline BOOLEAN DEFAULT FALSE,
    sync_timestamp TIMESTAMP,
    comentarios TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_dvirs_vehiculo ON dvirs(vehiculo_id);
CREATE INDEX idx_dvirs_timestamp ON dvirs(timestamp DESC);

-- DVIR ITEMS
CREATE TABLE IF NOT EXISTS dvir_items (
    id SERIAL PRIMARY KEY,
    dvir_id INTEGER NOT NULL REFERENCES dvirs(id) ON DELETE CASCADE,
    componente VARCHAR(255) NOT NULL,
    categoria VARCHAR(100),
    estado VARCHAR(50) NOT NULL CHECK (estado IN ('OK', 'ALERTA', 'CRITICO')),
    comentario TEXT,
    foto_url VARCHAR(500),
    orden_item INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_dvir_items_dvir ON dvir_items(dvir_id);
CREATE INDEX idx_dvir_items_estado ON dvir_items(estado);

-- SEED DATA
INSERT INTO config_pm (vehiculo_tipo, intervalo_km, intervalo_dias, duracion_estimada_min)
VALUES 
    ('PICKUP', 10000, 180, 240),
    ('TURBO', 15000, 180, 360)
ON CONFLICT (vehiculo_tipo) DO NOTHING;

-- Crear usuarios de prueba
INSERT INTO usuarios (email, nombre, hash_password, rol, estado)
VALUES 
    ('admin@test.com', 'Admin User', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5lkXN8sK7Y3N2', 'ADMIN', 'ACTIVO'),
    ('coordinador@test.com', 'María González', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5lkXN8sK7Y3N2', 'COORDINADOR', 'ACTIVO'),
    ('conductor@test.com', 'Juan Pérez', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5lkXN8sK7Y3N2', 'CONDUCTOR', 'ACTIVO'),
    ('tecnico@test.com', 'Carlos Méndez', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5lkXN8sK7Y3N2', 'TECNICO', 'ACTIVO')
ON CONFLICT (email) DO NOTHING;

-- Password para todos es: testpass123

-- Crear vehículos de prueba
INSERT INTO vehiculos (placa, vin, marca, modelo, anio, tipo, estado_operativo, odometro_actual, odometro_ultimo_pm)
VALUES 
    ('TEST123', '1HGTEST123456789', 'Toyota', 'Hilux 4x4', 2020, 'PICKUP', 'OPERATIVO', 50000, 40000),
    ('TURBO456', '1HGTURBO456789012', 'Ford', 'Ranger Turbo', 2021, 'TURBO', 'OPERATIVO', 75000, 65000)
ON CONFLICT (placa) DO NOTHING;

