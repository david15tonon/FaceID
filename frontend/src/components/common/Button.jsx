import React from 'react';

const Button = ({ children, variant = 'primary', onClick, disabled, className = '', ...props }) => {
  const baseClasses = 'px-6 py-3 font-bold transition duration-200 disabled:opacity-50 disabled:cursor-not-allowed';
  
  const variants = {
    primary: 'bg-black text-white hover:bg-red-600',
    secondary: 'border-2 border-black text-black hover:bg-black hover:text-white',
    danger: 'bg-red-600 text-white hover:bg-red-700',
  };

  return (
    <button
      className={`${baseClasses} ${variants[variant]} ${className}`}
      onClick={onClick}
      disabled={disabled}
      {...props}
    >
      {children}
    </button>
  );
};

export default Button;
