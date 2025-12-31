import React from 'react';

const StatsCard = ({ title, value, subtitle }) => {
  return (
    <div className="border-2 border-black p-6">
      <div className="text-4xl font-bold mb-2">{value}</div>
      <div className="text-gray-600 text-sm uppercase tracking-wide">{title}</div>
      {subtitle && <div className="text-xs text-gray-500 mt-1">{subtitle}</div>}
    </div>
  );
};

export default StatsCard;
