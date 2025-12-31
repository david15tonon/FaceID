import React from 'react';
import Sidebar from '../components/layout/Sidebar';
import { User } from 'lucide-react';

const Profile = () => {
  return (
    <div className="min-h-screen bg-white">
      <Sidebar />

      <main className="ml-64 p-12">
        <div className="mb-12">
          <div className="text-red-600 font-bold mb-2 tracking-wider text-sm">ACCOUNT</div>
          <h1 className="text-5xl font-bold mb-4">Profile</h1>
          <p className="text-gray-600">Manage your account settings</p>
        </div>

        <div className="max-w-2xl space-y-6">
          <div className="border-2 border-black p-8">
            <div className="flex items-center gap-6 mb-8">
              <div className="w-24 h-24 bg-gray-200 border-2 border-black flex items-center justify-center">
                <User className="w-12 h-12 text-gray-400" />
              </div>
              <div>
                <h2 className="text-2xl font-bold">John Doe</h2>
                <p className="text-gray-600">john.doe@example.com</p>
              </div>
            </div>

            <div className="space-y-4">
              <div>
                <label className="block text-sm font-bold mb-2 uppercase tracking-wide">Full Name</label>
                <input
                  type="text"
                  defaultValue="John Doe"
                  className="w-full border-2 border-black px-4 py-3 focus:outline-none focus:border-red-600"
                />
              </div>
              <div>
                <label className="block text-sm font-bold mb-2 uppercase tracking-wide">Email</label>
                <input
                  type="email"
                  defaultValue="john.doe@example.com"
                  className="w-full border-2 border-black px-4 py-3 focus:outline-none focus:border-red-600"
                />
              </div>
              <button className="w-full bg-black text-white py-3 font-bold hover:bg-red-600 transition">
                Save Changes
              </button>
            </div>
          </div>

          <div className="border-2 border-black p-8">
            <h3 className="text-xl font-bold mb-4">Security</h3>
            <div className="space-y-4">
              <div className="flex justify-between items-center py-3 border-b border-black/10">
                <div>
                  <div className="font-bold">Two-Factor Authentication</div>
                  <div className="text-sm text-gray-600">Add an extra layer of security</div>
                </div>
                <button className="bg-black text-white px-4 py-2 text-sm font-bold hover:bg-red-600 transition">
                  Enable
                </button>
              </div>
              <div className="flex justify-between items-center py-3">
                <div>
                  <div className="font-bold">Change Password</div>
                  <div className="text-sm text-gray-600">Update your password regularly</div>
                </div>
                <button className="border-2 border-black px-4 py-2 text-sm font-bold hover:bg-black hover:text-white transition">
                  Change
                </button>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
};

export default Profile;
