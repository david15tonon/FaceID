import React from 'react';

const ActivityFeed = ({ activities = [] }) => {
  return (
    <div className="space-y-3">
      {activities.map((activity, index) => (
        <div
          key={index}
          className="border border-black/10 p-4 flex justify-between items-center hover:border-red-600 transition"
        >
          <div className="flex items-center gap-4">
            <div
              className={`w-2 h-2 rounded-full ${
                activity.status === 'success' ? 'bg-green-500' : 'bg-red-600'
              }`}
            ></div>
            <div>
              <div className="font-bold">{activity.action}</div>
              <div className="text-sm text-gray-600">{activity.user}</div>
            </div>
          </div>
          <div className="text-sm text-gray-600">{activity.time}</div>
        </div>
      ))}
      {activities.length === 0 && (
        <p className="text-center text-gray-500 py-8">No recent activity</p>
      )}
    </div>
  );
};

export default ActivityFeed;
