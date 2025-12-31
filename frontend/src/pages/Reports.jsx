import React from 'react';
import Sidebar from '../components/layout/Sidebar';
import { BarChart3, TrendingUp, Users } from 'lucide-react';

const Reports = () => {
  return (
    <div className="min-h-screen bg-white">
      <Sidebar />

      <main className="ml-64 p-12">
        <div className="mb-12">
          <div className="text-red-600 font-bold mb-2 tracking-wider text-sm">ANALYTICS</div>
          <h1 className="text-5xl font-bold mb-4">Reports</h1>
          <p className="text-gray-600">View detailed analytics and insights</p>
        </div>

        <div className="space-y-8">
          {/* Summary Cards */}
          <div className="grid grid-cols-3 gap-6">
            <div className="border-2 border-black p-6">
              <BarChart3 className="w-8 h-8 mb-4" />
              <div className="text-3xl font-bold mb-2">1,247</div>
              <div className="text-sm text-gray-600">Total Verifications</div>
            </div>
            <div className="border-2 border-black p-6">
              <TrendingUp className="w-8 h-8 mb-4" />
              <div className="text-3xl font-bold mb-2">+24%</div>
              <div className="text-sm text-gray-600">Growth This Month</div>
            </div>
            <div className="border-2 border-black p-6">
              <Users className="w-8 h-8 mb-4" />
              <div className="text-3xl font-bold mb-2">156</div>
              <div className="text-sm text-gray-600">Active Users</div>
            </div>
          </div>

          {/* Charts Placeholder */}
          <div className="border-2 border-black p-8">
            <h3 className="text-xl font-bold mb-6">Verification Trends</h3>
            <div className="h-64 bg-gray-100 flex items-center justify-center">
              <p className="text-gray-500">Chart visualization would go here</p>
            </div>
          </div>

          {/* Data Table */}
          <div className="border-2 border-black overflow-hidden">
            <div className="bg-black text-white p-4">
              <h3 className="text-xl font-bold">Recent Reports</h3>
            </div>
            <table className="w-full">
              <thead className="border-b-2 border-black">
                <tr>
                  <th className="text-left p-4 font-bold">Date</th>
                  <th className="text-left p-4 font-bold">Type</th>
                  <th className="text-left p-4 font-bold">Status</th>
                  <th className="text-left p-4 font-bold">Actions</th>
                </tr>
              </thead>
              <tbody>
                {[1, 2, 3, 4, 5].map((i) => (
                  <tr key={i} className="border-b border-black/10">
                    <td className="p-4">2024-01-{20 + i}</td>
                    <td className="p-4">Daily Summary</td>
                    <td className="p-4">
                      <span className="bg-green-100 text-green-800 px-3 py-1 text-sm font-bold">
                        Complete
                      </span>
                    </td>
                    <td className="p-4">
                      <button className="text-red-600 hover:underline font-bold">View</button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </main>
    </div>
  );
};

export default Reports;
