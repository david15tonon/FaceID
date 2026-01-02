import React from 'react';
import Sidebar from '../components/layout/Sidebar';
import StatsCard from '../components/dashboard/StatsCard';
import ActivityFeed from '../components/dashboard/ActivityFeed';
import QuickActions from '../components/dashboard/QuickActions';

const Dashboard = () => {
  const mockActivities = [
    { action: 'Face Verified', user: 'John Doe', time: '2 min ago', status: 'success' },
    { action: 'Face Enrolled', user: 'Jane Smith', time: '15 min ago', status: 'success' },
    { action: 'Verification Failed', user: 'Unknown', time: '1 hour ago', status: 'failed' },
    { action: 'Face Verified', user: 'Mike Johnson', time: '2 hours ago', status: 'success' },
  ];

  return (
    <div className="min-h-screen bg-white">
      <Sidebar />

      <main className="ml-64 p-12">
        <div className="mb-12">
          <div className="text-red-600 font-bold mb-2 tracking-wider text-sm">OVERVIEW</div>
          <h1 className="text-5xl font-bold mb-4">Dashboard</h1>
          <p className="text-gray-600">Monitor your recognition activities</p>
        </div>

        {/* Stats Grid */}
        <div className="grid grid-cols-3 gap-6 mb-12">
          <StatsCard title="Total Recognitions" value="1,247" />
          <StatsCard title="Accuracy Rate" value="98.7%" />
          <StatsCard title="Enrolled Faces" value="12" />
        </div>

        {/* Quick Actions */}
        <div className="mb-12">
          <h2 className="text-2xl font-bold mb-6">Quick Actions</h2>
          <QuickActions />
        </div>

        {/* Recent Activity */}
        <div>
          <h2 className="text-2xl font-bold mb-6">Recent Activity</h2>
          <ActivityFeed activities={mockActivities} />
        </div>
      </main>
    </div>
  );
};

export default Dashboard;
