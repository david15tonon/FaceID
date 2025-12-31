import React, { useState } from 'react';
import { useFaceRecognition } from '../../hooks/useFaceRecognition';
import FaceUpload from './FaceUpload';
import Button from '../common/Button';

const FaceVerification = () => {
  const [image, setImage] = useState(null);
  const [result, setResult] = useState(null);
  const { verifyFace, loading } = useFaceRecognition();

  const handleVerify = async () => {
    if (!image) return;
    try {
      const data = await verifyFace(image);
      setResult(data);
    } catch (err) {
      setResult({ success: false, message: 'Verification failed' });
    }
  };

  return (
    <div className="space-y-6">
      <FaceUpload onUpload={setImage} />
      {image && (
        <div className="space-y-4">
          <img src={image} alt="Uploaded" className="w-full max-w-md mx-auto border-2 border-black" />
          <Button onClick={handleVerify} disabled={loading} className="w-full">
            {loading ? 'Verifying...' : 'Verify Identity'}
          </Button>
        </div>
      )}
      {result && (
        <div className={`p-6 border-2 ${result.success ? 'border-green-500 bg-green-50' : 'border-red-600 bg-red-50'}`}>
          <h3 className="font-bold mb-2">{result.success ? 'Match Found!' : 'No Match'}</h3>
          <p>{result.message}</p>
        </div>
      )}
    </div>
  );
};

export default FaceVerification;
