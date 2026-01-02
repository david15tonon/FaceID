import React, { useEffect } from 'react';
import { useCamera } from '../../hooks/useCamera';
import Button from '../common/Button';

const FaceCapture = ({ onCapture }) => {
  const { videoRef, stream, error, startCamera, stopCamera, captureImage } = useCamera();

  useEffect(() => {
    startCamera();
    return () => stopCamera();
  }, []);

  const handleCapture = () => {
    const image = captureImage();
    if (image) {
      onCapture(image);
    }
  };

  return (
    <div className="space-y-4">
      <div className="aspect-video bg-black relative overflow-hidden border-2 border-white/20">
        {error ? (
          <div className="absolute inset-0 flex items-center justify-center text-white">
            <p>{error}</p>
          </div>
        ) : (
          <video
            ref={videoRef}
            autoPlay
            playsInline
            className="w-full h-full object-cover"
          />
        )}
      </div>
      <Button onClick={handleCapture} disabled={!stream} className="w-full" variant="danger">
        Capture Face
      </Button>
    </div>
  );
};

export default FaceCapture;
