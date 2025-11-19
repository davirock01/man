/**
 * API Client para comunicación con el backend
 */
import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000';

// Crear instancia de Axios
export const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Interceptor para agregar token JWT
apiClient.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('access_token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Interceptor para manejar errores
apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Token inválido o expirado
      localStorage.removeItem('access_token');
      localStorage.removeItem('user');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

// ============================================================
// AUTH API
// ============================================================

export interface LoginRequest {
  email: string;
  password: string;
}

export interface LoginResponse {
  access_token: string;
  token_type: string;
  user: {
    id: number;
    email: string;
    nombre: string;
    rol: string;
  };
}

export const authApi = {
  login: async (data: LoginRequest): Promise<LoginResponse> => {
    const response = await apiClient.post('/api/v1/auth/login', data);
    return response.data;
  },
};

// ============================================================
// VEHICLES API
// ============================================================

export const vehiclesApi = {
  getAll: async () => {
    const response = await apiClient.get('/api/v1/vehicles');
    return response.data;
  },
};

// ============================================================
// DASHBOARD API
// ============================================================

export const dashboardApi = {
  getOverview: async () => {
    const response = await apiClient.get('/api/v1/dashboard/overview');
    return response.data;
  },
};

