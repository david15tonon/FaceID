import React from 'react';
import { Link } from 'react-router-dom';
import { Circle } from 'lucide-react';
import { useAuth } from '../../hooks/useAuth';

const Header = () => {
  const { user } = useAuth();

  return (
    <header className="fixed top-0 w-full z-50 bg-white/80 backdrop-blur-md border-b border-black/10">
      <div className="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
        <Link to="/" className="flex items-center gap-2">
          <Circle className="w-6 h-6 fill-black" />
          <span className="font-bold text-xl">FaceID</span>
        </Link>
        <nav className="hidden md:flex gap-8 font-medium">
          <Link to="/features" className="hover:text-red-600 transition">Features</Link>
          <Link to="/security" className="hover:text-red-600 transition">Security</Link>
          <Link to="/api" className="hover:text-red-600 transition">API</Link>
          <Link to="/docs" className="hover:text-red-600 transition">Docs</Link>
        </nav>
        <div>
          {user ? (
            <Link to="/dashboard" className="bg-black text-white px-6 py-2 hover:bg-red-600 transition">
              Dashboard
            </Link>
          ) : (
            <Link to="/login" className="bg-black text-white px-6 py-2 hover:bg-red-600 transition">
              Login
            </Link>
          )}
        </div>
      </div>
    </header>
  );
};

export default Header;
