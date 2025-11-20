#!/bin/bash
# Inicializar base de datos con esquema y datos de prueba

echo "Esperando a que PostgreSQL esté listo..."
sleep 5

echo "Ejecutando SQL de inicialización..."
PGPASSWORD=postgres psql -h localhost -U postgres -d fleet_maintenance -f app/db/init_db.sql

echo "Base de datos inicializada!"

