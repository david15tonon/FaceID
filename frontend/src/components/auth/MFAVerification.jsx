import React, { useState } from 'react';
import Input from '../common/Input';
import Button from '../common/Button';

const MFAVerification = ({ onVerify }) => {
  const [code, setCode] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    try {
      await onVerify(code);
    } catch (err) {
      setError('Invalid verification code');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-6">
      <div>
        <h3 className="text-xl font-bold mb-2">Two-Factor Authentication</h3>
        <p className="text-gray-600 mb-4">Enter the 6-digit code from your authenticator app</p>
      </div>
      <Input
        label="Verification Code"
        type="text"
        value={code}
        onChange={(e) => setCode(e.target.value)}
        placeholder="000000"
        maxLength={6}
        required
      />
      {error && <p className="text-red-600 text-sm">{error}</p>}
      <Button type="submit" className="w-full">
        Verify
      </Button>
    </form>
  );
};

export default MFAVerification;
