import React from 'react';

const Input = ({ label, type = 'text', placeholder, value, onChange, error, className = '', ...props }) => {
  return (
    <div className={className}>
      {label && (
        <label className="block text-sm font-bold mb-2 uppercase tracking-wide">
          {label}
        </label>
      )}
      <input
        type={type}
        placeholder={placeholder}
        value={value}
        onChange={onChange}
        className={`w-full border-2 px-4 py-3 focus:outline-none transition ${
          error ? 'border-red-600' : 'border-black focus:border-red-600'
        }`}
        {...props}
      />
      {error && <p className="text-red-600 text-sm mt-1">{error}</p>}
    </div>
  );
};

export default Input;
