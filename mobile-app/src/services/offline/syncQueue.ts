import { OfflineStorage, STORAGE_KEYS } from './storage';
import api from '../api';

export interface SyncItem {
  id: string;
  type: 'DVIR' | 'EVENTO' | 'OT_UPDATE';
  data: any;
  timestamp: string;
  attempts: number;
}

export class SyncQueue {
  static async add(type: SyncItem['type'], data: any): Promise<void> {
    const queue = await this.getQueue();
    const item: SyncItem = {
      id: `${type}_${Date.now()}_${Math.random()}`,
      type,
      data,
      timestamp: new Date().toISOString(),
      attempts: 0,
    };
    queue.push(item);
    await OfflineStorage.set(STORAGE_KEYS.SYNC_QUEUE, queue);
  }

  static async getQueue(): Promise<SyncItem[]> {
    const queue = await OfflineStorage.get(STORAGE_KEYS.SYNC_QUEUE);
    return queue || [];
  }

  static async processQueue(): Promise<{ sincronizados: number; errores: any[] }> {
    const queue = await this.getQueue();
    if (queue.length === 0) {
      return { sincronizados: 0, errores: [] };
    }

    const results: any[] = [];
    const newQueue: SyncItem[] = [];

    for (const item of queue) {
      try {
        // Send to sync endpoint
        await api.post('/conductor/sync', {
          items: [{ tipo: item.type, data: item.data }],
        });
        
        results.push({ id: item.id, status: 'success' });
      } catch (error: any) {
        item.attempts += 1;
        
        if (item.attempts < 5) {
          newQueue.push(item); // Retry later
        }
        
        results.push({ 
          id: item.id, 
          status: 'error', 
          error: error.message 
        });
      }
    }

    await OfflineStorage.set(STORAGE_KEYS.SYNC_QUEUE, newQueue);

    const sincronizados = results.filter(r => r.status === 'success').length;
    const errores = results.filter(r => r.status === 'error');

    return { sincronizados, errores };
  }

  static async clear(): Promise<void> {
    await OfflineStorage.set(STORAGE_KEYS.SYNC_QUEUE, []);
  }

  static async getQueueSize(): Promise<number> {
    const queue = await this.getQueue();
    return queue.length;
  }
}

