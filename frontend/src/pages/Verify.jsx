import React from 'react';
import Sidebar from '../components/layout/Sidebar';
import FaceVerification from '../components/face/FaceVerification';

const Verify = () => {
  return (
    <div className="min-h-screen bg-white">
      <Sidebar />

      <main className="ml-64 p-12">
        <div className="mb-12">
          <div className="text-red-600 font-bold mb-2 tracking-wider text-sm">VERIFICATION</div>
          <h1 className="text-5xl font-bold mb-4">Verify Identity</h1>
          <p className="text-gray-600">Submit an image for instant verification</p>
        </div>

        <div className="max-w-2xl">
          <FaceVerification />

          <div className="mt-12 bg-gray-50 border border-black/10 p-6">
            <h3 className="font-bold mb-4 uppercase tracking-wide text-sm">Recent Verifications</h3>
            <div className="space-y-3">
              <div className="flex justify-between items-center">
                <div className="flex items-center gap-3">
                  <div className="w-2 h-2 bg-green-500 rounded-full"></div>
                  <span className="font-medium">John Doe</span>
                </div>
                <span className="text-sm text-gray-600">98.5% Match</span>
              </div>
              <div className="flex justify-between items-center">
                <div className="flex items-center gap-3">
                  <div className="w-2 h-2 bg-red-600 rounded-full"></div>
                  <span className="font-medium">Unknown</span>
                </div>
                <span className="text-sm text-gray-600">No Match</span>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
};

export default Verify;
