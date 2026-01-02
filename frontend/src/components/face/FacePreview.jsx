import React from 'react';
import { X } from 'lucide-react';

const FacePreview = ({ image, onClear, onConfirm }) => {
  return (
    <div className="space-y-4">
      <div className="relative">
        <img src={image} alt="Captured face" className="w-full border-2 border-black" />
        <button
          onClick={onClear}
          className="absolute top-2 right-2 bg-red-600 text-white p-2 hover:bg-red-700"
        >
          <X className="w-5 h-5" />
        </button>
      </div>
      <div className="flex gap-4">
        <button
          onClick={onClear}
          className="flex-1 border-2 border-black px-6 py-3 font-bold hover:bg-black hover:text-white transition"
        >
          Retake
        </button>
        <button
          onClick={onConfirm}
          className="flex-1 bg-black text-white px-6 py-3 font-bold hover:bg-red-600 transition"
        >
          Confirm
        </button>
      </div>
    </div>
  );
};

export default FacePreview;
