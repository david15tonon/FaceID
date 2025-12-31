import React from 'react';

const DotMatrix = () => (
  <div className="absolute inset-0 opacity-5 pointer-events-none">
    <div className="grid grid-cols-20 gap-4 h-full">
      {[...Array(400)].map((_, i) => (
        <div key={i} className="w-1 h-1 bg-black rounded-full" />
      ))}
    </div>
  </div>
);

export default DotMatrix;
