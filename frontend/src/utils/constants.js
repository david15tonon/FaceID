export const API_ENDPOINTS = {
  AUTH: {
    LOGIN: '/auth/login',
    SIGNUP: '/auth/signup',
    LOGOUT: '/auth/logout',
    ME: '/auth/me',
  },
  FACES: {
    ENROLL: '/faces/enroll',
    VERIFY: '/faces/verify',
    LIST: '/faces',
  },
  USERS: {
    PROFILE: '/users/profile',
    LIST: '/users',
  },
  REPORTS: {
    LIST: '/reports',
  },
  LOGS: {
    LIST: '/logs',
  },
};

export const FACE_RECOGNITION_TOLERANCE = 0.6;
export const MAX_FILE_SIZE = 10 * 1024 * 1024; // 10MB
export const ALLOWED_IMAGE_TYPES = ['image/jpeg', 'image/jpg', 'image/png'];
