import React from 'react';

const Card = ({ children, title, className = '' }) => {
  return (
    <div className={`border-2 border-black p-6 ${className}`}>
      {title && <h3 className="text-xl font-bold mb-4">{title}</h3>}
      {children}
    </div>
  );
};

export default Card;
