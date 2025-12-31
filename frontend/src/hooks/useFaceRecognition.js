import { useState } from 'react';
import { faceService } from '../services/face.service';

export const useFaceRecognition = () => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const enrollFace = async (imageData, userId) => {
    setLoading(true);
    setError(null);
    try {
      const result = await faceService.enroll(imageData, userId);
      return result;
    } catch (err) {
      setError(err.message);
      throw err;
    } finally {
      setLoading(false);
    }
  };

  const verifyFace = async (imageData) => {
    setLoading(true);
    setError(null);
    try {
      const result = await faceService.verify(imageData);
      return result;
    } catch (err) {
      setError(err.message);
      throw err;
    } finally {
      setLoading(false);
    }
  };

  return { enrollFace, verifyFace, loading, error };
};
