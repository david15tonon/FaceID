import React from 'react';
import Sidebar from '../components/layout/Sidebar';
import { Search, Filter } from 'lucide-react';

const Logs = () => {
  return (
    <div className="min-h-screen bg-white">
      <Sidebar />

      <main className="ml-64 p-12">
        <div className="mb-12">
          <div className="text-red-600 font-bold mb-2 tracking-wider text-sm">AUDIT TRAIL</div>
          <h1 className="text-5xl font-bold mb-4">Logs</h1>
          <p className="text-gray-600">Track all system activities</p>
        </div>

        {/* Filters */}
        <div className="mb-8 flex gap-4">
          <div className="flex-1 relative">
            <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 w-5 h-5 text-gray-400" />
            <input
              type="text"
              placeholder="Search logs..."
              className="w-full pl-12 pr-4 py-3 border-2 border-black focus:outline-none focus:border-red-600"
            />
          </div>
          <button className="border-2 border-black px-6 py-3 font-bold hover:bg-black hover:text-white transition flex items-center gap-2">
            <Filter className="w-5 h-5" />
            Filter
          </button>
        </div>

        {/* Logs Table */}
        <div className="border-2 border-black overflow-hidden">
          <div className="bg-black text-white p-4">
            <h3 className="text-xl font-bold">System Logs</h3>
          </div>
          <div className="overflow-x-auto">
            <table className="w-full">
              <thead className="border-b-2 border-black bg-gray-50">
                <tr>
                  <th className="text-left p-4 font-bold">Timestamp</th>
                  <th className="text-left p-4 font-bold">Event</th>
                  <th className="text-left p-4 font-bold">User</th>
                  <th className="text-left p-4 font-bold">IP Address</th>
                  <th className="text-left p-4 font-bold">Status</th>
                </tr>
              </thead>
              <tbody>
                {Array.from({ length: 15 }, (_, i) => (
                  <tr key={i} className="border-b border-black/10 hover:bg-gray-50">
                    <td className="p-4 text-sm">2024-01-25 14:{30 + i}:22</td>
                    <td className="p-4">Face Verification</td>
                    <td className="p-4">john.doe@example.com</td>
                    <td className="p-4 text-sm text-gray-600">192.168.1.{100 + i}</td>
                    <td className="p-4">
                      <span className={`px-3 py-1 text-sm font-bold ${
                        i % 3 === 0 
                          ? 'bg-red-100 text-red-800' 
                          : 'bg-green-100 text-green-800'
                      }`}>
                        {i % 3 === 0 ? 'Failed' : 'Success'}
                      </span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>

          {/* Pagination */}
          <div className="p-4 border-t-2 border-black flex justify-between items-center">
            <div className="text-sm text-gray-600">Showing 1-15 of 247 logs</div>
            <div className="flex gap-2">
              <button className="border-2 border-black px-4 py-2 font-bold hover:bg-black hover:text-white transition">
                Previous
              </button>
              <button className="border-2 border-black px-4 py-2 font-bold hover:bg-black hover:text-white transition">
                Next
              </button>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
};

export default Logs;
