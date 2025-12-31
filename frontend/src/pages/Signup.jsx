import React from 'react';
import { Link } from 'react-router-dom';
import { Circle } from 'lucide-react';
import SignupForm from '../components/auth/SignupForm';

const Signup = () => {
  return (
    <div className="min-h-screen bg-black text-white flex items-center justify-center px-6 relative">
      <Link to="/" className="absolute top-6 left-6 text-sm font-bold hover:text-red-600 transition">
        ← Back
      </Link>

      <div className="w-full max-w-md relative z-10">
        <div className="mb-8">
          <Circle className="w-8 h-8 fill-white mb-4" />
          <h1 className="text-5xl font-bold mb-2">Create account</h1>
          <p className="text-gray-400">Start your journey. Nothing complex.</p>
        </div>

        <SignupForm />

        <div className="text-center mt-6">
          <Link to="/login" className="text-sm hover:text-red-600 transition font-medium">
            Already have an account? <span className="font-bold">Login</span>
          </Link>
        </div>
      </div>
    </div>
  );
};

export default Signup;
