import { create } from 'zustand';
import AsyncStorage from '@react-native-async-storage/async-storage';

interface User {
  id: number;
  nombre: string;
  email: string;
  rol: string;
}

interface AuthState {
  user: User | null;
  accessToken: string | null;
  refreshToken: string | null;
  isAuthenticated: boolean;
  setAuth: (user: User, accessToken: string, refreshToken: string) => Promise<void>;
  clearAuth: () => Promise<void>;
  loadAuth: () => Promise<void>;
}

export const useAuthStore = create<AuthState>((set) => ({
  user: null,
  accessToken: null,
  refreshToken: null,
  isAuthenticated: false,
  
  setAuth: async (user, accessToken, refreshToken) => {
    await AsyncStorage.setItem('auth_user', JSON.stringify(user));
    await AsyncStorage.setItem('auth_access_token', accessToken);
    await AsyncStorage.setItem('auth_refresh_token', refreshToken);
    set({ user, accessToken, refreshToken, isAuthenticated: true });
  },
  
  clearAuth: async () => {
    await AsyncStorage.removeItem('auth_user');
    await AsyncStorage.removeItem('auth_access_token');
    await AsyncStorage.removeItem('auth_refresh_token');
    set({ user: null, accessToken: null, refreshToken: null, isAuthenticated: false });
  },
  
  loadAuth: async () => {
    try {
      const userStr = await AsyncStorage.getItem('auth_user');
      const accessToken = await AsyncStorage.getItem('auth_access_token');
      const refreshToken = await AsyncStorage.getItem('auth_refresh_token');
      
      if (userStr && accessToken && refreshToken) {
        const user = JSON.parse(userStr);
        set({ user, accessToken, refreshToken, isAuthenticated: true });
      }
    } catch (error) {
      console.error('Error loading auth:', error);
    }
  },
}));

