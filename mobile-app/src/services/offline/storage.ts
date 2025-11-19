import AsyncStorage from '@react-native-async-storage/async-storage';

export const STORAGE_KEYS = {
  ACCESS_TOKEN: '@access_token',
  REFRESH_TOKEN: '@refresh_token',
  USER: '@user',
  SYNC_QUEUE: '@sync_queue',
  CACHED_CHECKLISTS: '@cached_checklists',
  PENDING_DVIRS: '@pending_dvirs',
};

export class OfflineStorage {
  static async get(key: string): Promise<any | null> {
    try {
      const value = await AsyncStorage.getItem(key);
      return value ? JSON.parse(value) : null;
    } catch (error) {
      console.error('Error reading from storage:', error);
      return null;
    }
  }

  static async set(key: string, value: any): Promise<void> {
    try {
      await AsyncStorage.setItem(key, JSON.stringify(value));
    } catch (error) {
      console.error('Error writing to storage:', error);
    }
  }

  static async remove(key: string): Promise<void> {
    try {
      await AsyncStorage.removeItem(key);
    } catch (error) {
      console.error('Error removing from storage:', error);
    }
  }

  static async clear(): Promise<void> {
    try {
      await AsyncStorage.clear();
    } catch (error) {
      console.error('Error clearing storage:', error);
    }
  }

  // Specific helpers
  static async getUser(): Promise<any | null> {
    return this.get(STORAGE_KEYS.USER);
  }

  static async setUser(user: any): Promise<void> {
    return this.set(STORAGE_KEYS.USER, user);
  }

  static async getAccessToken(): Promise<string | null> {
    return this.get(STORAGE_KEYS.ACCESS_TOKEN);
  }

  static async setAccessToken(token: string): Promise<void> {
    return this.set(STORAGE_KEYS.ACCESS_TOKEN, token);
  }
}

