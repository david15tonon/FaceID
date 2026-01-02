import api from './api';

export const faceService = {
  enroll: async (imageData, userId) => {
    const formData = new FormData();
    formData.append('image', imageData);
    formData.append('user_id', userId);

    const response = await api.post('/faces/enroll', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data;
  },

  verify: async (imageData) => {
    const formData = new FormData();
    formData.append('image', imageData);

    const response = await api.post('/faces/verify', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data;
  },

  getFaces: async (userId) => {
    const response = await api.get(`/faces/user/${userId}`);
    return response.data;
  },

  deleteFace: async (faceId) => {
    const response = await api.delete(`/faces/${faceId}`);
    return response.data;
  },
};
