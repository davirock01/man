import React, { useState, useEffect } from 'react';
import { View, StyleSheet } from 'react-native';
import { Title, Text, Button, ProgressBar } from 'react-native-paper';
import NetInfo from '@react-native-community/netinfo';
import { SyncQueue } from '../../services/offline/syncQueue';

export default function SyncScreen() {
  const [isOnline, setIsOnline] = useState(true);
  const [queueSize, setQueueSize] = useState(0);
  const [syncing, setSyncing] = useState(false);
  const [lastSync, setLastSync] = useState<Date | null>(null);

  useEffect(() => {
    loadQueueSize();
    
    const unsubscribe = NetInfo.addEventListener(state => {
      setIsOnline(state.isConnected || false);
      
      // Auto-sync when connection restored
      if (state.isConnected && queueSize > 0 && !syncing) {
        handleSync();
      }
    });

    return () => unsubscribe();
  }, [queueSize, syncing]);

  const loadQueueSize = async () => {
    const size = await SyncQueue.getQueueSize();
    setQueueSize(size);
  };

  const handleSync = async () => {
    if (!isOnline) {
      return;
    }

    setSyncing(true);
    try {
      const result = await SyncQueue.processQueue();
      await loadQueueSize();
      setLastSync(new Date());
      
      if (result.errores.length > 0) {
        console.error('Sync errors:', result.errores);
      }
    } catch (error) {
      console.error('Sync error:', error);
    } finally {
      setSyncing(false);
    }
  };

  return (
    <View style={styles.container}>
      <Title style={styles.title}>Sincronización</Title>

      <View style={styles.statusCard}>
        <Text style={styles.label}>Estado de conexión:</Text>
        <Text style={[styles.status, isOnline ? styles.online : styles.offline]}>
          {isOnline ? '🟢 ONLINE' : '🔴 OFFLINE'}
        </Text>
      </View>

      <View style={styles.statusCard}>
        <Text style={styles.label}>Registros pendientes:</Text>
        <Text style={styles.value}>{queueSize}</Text>
      </View>

      {lastSync && (
        <View style={styles.statusCard}>
          <Text style={styles.label}>Última sincronización:</Text>
          <Text style={styles.value}>{lastSync.toLocaleString('es-CO')}</Text>
        </View>
      )}

      {syncing && (
        <ProgressBar indeterminate style={styles.progress} />
      )}

      <Button
        mode="contained"
        onPress={handleSync}
        disabled={!isOnline || syncing || queueSize === 0}
        loading={syncing}
        style={styles.button}
      >
        {syncing ? 'Sincronizando...' : 'Sincronizar Ahora'}
      </Button>

      <Text style={styles.helpText}>
        {!isOnline && 'Conéctate a internet para sincronizar'}
        {isOnline && queueSize === 0 && 'No hay datos pendientes'}
        {isOnline && queueSize > 0 && 'Hay datos pendientes de sincronizar'}
      </Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: '#fff',
  },
  title: {
    fontSize: 24,
    marginBottom: 30,
    textAlign: 'center',
  },
  statusCard: {
    padding: 15,
    marginBottom: 15,
    backgroundColor: '#f5f5f5',
    borderRadius: 8,
  },
  label: {
    fontSize: 14,
    color: '#666',
    marginBottom: 5,
  },
  value: {
    fontSize: 18,
    fontWeight: 'bold',
  },
  status: {
    fontSize: 18,
    fontWeight: 'bold',
  },
  online: {
    color: '#4caf50',
  },
  offline: {
    color: '#f44336',
  },
  progress: {
    marginVertical: 20,
  },
  button: {
    marginTop: 20,
    paddingVertical: 8,
  },
  helpText: {
    marginTop: 20,
    textAlign: 'center',
    color: '#666',
  },
});

