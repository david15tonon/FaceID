import React, { useRef } from 'react';
import { Camera } from 'lucide-react';

const FaceUpload = ({ onUpload }) => {
  const fileInputRef = useRef(null);

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onloadend = () => {
        onUpload(reader.result);
      };
      reader.readAsDataURL(file);
    }
  };

  return (
    <div
      onClick={() => fileInputRef.current?.click()}
      className="border-2 border-dashed border-black/20 p-12 text-center hover:border-red-600 transition cursor-pointer"
    >
      <Camera className="w-16 h-16 mx-auto mb-4 text-black/20" />
      <div className="font-bold mb-2">Drop image here or click to browse</div>
      <div className="text-sm text-gray-600">PNG, JPG up to 10MB</div>
      <input
        ref={fileInputRef}
        type="file"
        accept="image/*"
        onChange={handleFileChange}
        className="hidden"
      />
    </div>
  );
};

export default FaceUpload;
