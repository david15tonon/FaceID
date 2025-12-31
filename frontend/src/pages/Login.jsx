import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Circle, Lock } from 'lucide-react';
import DotMatrix from '../components/layout/DotMatrix';
import LoginForm from '../components/auth/LoginForm';

const Login = () => {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen bg-white flex items-center justify-center px-6 relative">
      <DotMatrix />
      
      <Link to="/" className="absolute top-6 left-6 text-sm font-bold hover:text-red-600 transition">
        ← Back
      </Link>

      <div className="w-full max-w-md relative z-10">
        <div className="mb-8">
          <Circle className="w-8 h-8 fill-black mb-4" />
          <h1 className="text-5xl font-bold mb-2">Welcome back</h1>
          <p className="text-gray-600">Nothing to hide. Everything secure.</p>
        </div>

        <LoginForm />

        <div className="text-center mt-6">
          <Link to="/signup" className="text-sm hover:text-red-600 transition font-medium">
            Don't have an account? <span className="font-bold">Sign up</span>
          </Link>
        </div>

        <div className="mt-8 pt-8 border-t border-black/10">
          <div className="flex items-center justify-between text-sm">
            <span className="text-gray-600">MFA Enabled</span>
            <Lock className="w-4 h-4 text-red-600" />
          </div>
        </div>
      </div>
    </div>
  );
};

export default Login;
