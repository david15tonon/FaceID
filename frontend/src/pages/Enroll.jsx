import React, { useState } from 'react';
import { Camera, User } from 'lucide-react';
import Sidebar from '../components/layout/Sidebar';
import FaceCapture from '../components/face/FaceCapture';
import FaceUpload from '../components/face/FaceUpload';

const Enroll = () => {
  const [capturedImage, setCapturedImage] = useState(null);

  return (
    <div className="min-h-screen bg-black text-white">
      <Sidebar />

      <main className="ml-64 p-12">
        <div className="mb-12">
          <div className="text-red-600 font-bold mb-2 tracking-wider text-sm">ENROLLMENT</div>
          <h1 className="text-5xl font-bold mb-4">Capture Your Face</h1>
          <p className="text-gray-400">Position yourself in the frame. Nothing complicated.</p>
        </div>

        <div className="grid md:grid-cols-2 gap-12">
          {/* Camera Capture */}
          <div>
            <h3 className="text-xl font-bold mb-4">Live Capture</h3>
            <FaceCapture onCapture={setCapturedImage} />
          </div>

          {/* Instructions & Upload */}
          <div className="space-y-8">
            <div>
              <h3 className="text-2xl font-bold mb-4">Instructions</h3>
              <div className="space-y-4 text-gray-400">
                <div className="flex gap-4">
                  <div className="text-red-600 font-bold">01</div>
                  <div>Position your face within the frame markers</div>
                </div>
                <div className="flex gap-4">
                  <div className="text-red-600 font-bold">02</div>
                  <div>Ensure proper lighting on your face</div>
                </div>
                <div className="flex gap-4">
                  <div className="text-red-600 font-bold">03</div>
                  <div>Remove glasses and look directly at camera</div>
                </div>
                <div className="flex gap-4">
                  <div className="text-red-600 font-bold">04</div>
                  <div>Stay still when capturing</div>
                </div>
              </div>
            </div>

            <div className="border-t border-white/20 pt-8">
              <h3 className="text-xl font-bold mb-4">Upload Image</h3>
              <FaceUpload onUpload={setCapturedImage} />
            </div>
          </div>
        </div>
      </main>
    </div>
  );
};

export default Enroll;
