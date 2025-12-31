import React from 'react';
import { Link } from 'react-router-dom';
import { Camera, Eye, Lock, Activity, Circle } from 'lucide-react';
import DotMatrix from '../components/layout/DotMatrix';

const Landing = () => {
  return (
    <div className="min-h-screen bg-white text-black relative overflow-hidden">
      <DotMatrix />
      
      {/* Header */}
      <header className="fixed top-0 w-full z-50 bg-white/80 backdrop-blur-md border-b border-black/10">
        <div className="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
          <div className="flex items-center gap-2">
            <Circle className="w-6 h-6 fill-black" />
            <span className="font-bold text-xl">FaceID</span>
          </div>
          <nav className="hidden md:flex gap-8 font-medium">
            <a href="#features" className="hover:text-red-600 transition">Features</a>
            <a href="#security" className="hover:text-red-600 transition">Security</a>
            <a href="#api" className="hover:text-red-600 transition">API</a>
            <a href="#docs" className="hover:text-red-600 transition">Docs</a>
          </nav>
          <Link to="/login" className="bg-black text-white px-6 py-2 hover:bg-red-600 transition">
            Login
          </Link>
        </div>
      </header>

      {/* Hero Section */}
      <section className="pt-32 pb-20 px-6">
        <div className="max-w-7xl mx-auto">
          <div className="grid md:grid-cols-2 gap-16 items-center">
            <div>
              <div className="text-red-600 font-bold mb-4 tracking-wider">NOTHING TO HIDE</div>
              <h1 className="text-7xl md:text-8xl font-bold leading-none mb-6">
                Face<br/>Recognition<br/>Redefined
              </h1>
              <p className="text-xl text-gray-600 mb-8 max-w-md">
                Real-time identity verification with military-grade security. Nothing unnecessary. Everything essential.
              </p>
              <div className="flex gap-4">
                <Link to="/signup" className="bg-black text-white px-8 py-4 text-lg font-bold hover:bg-red-600 transition">
                  Start Free
                </Link>
                <button className="border-2 border-black px-8 py-4 text-lg font-bold hover:bg-black hover:text-white transition">
                  View Demo
                </button>
              </div>
            </div>
            
            {/* Visual Element */}
            <div className="relative">
              <div className="aspect-square bg-gradient-to-br from-gray-100 to-gray-200 relative overflow-hidden">
                <div className="absolute inset-0 flex items-center justify-center">
                  <div className="w-64 h-64 border-4 border-black relative">
                    <div className="absolute top-0 left-0 w-8 h-8 border-t-4 border-l-4 border-red-600"></div>
                    <div className="absolute top-0 right-0 w-8 h-8 border-t-4 border-r-4 border-red-600"></div>
                    <div className="absolute bottom-0 left-0 w-8 h-8 border-b-4 border-l-4 border-red-600"></div>
                    <div className="absolute bottom-0 right-0 w-8 h-8 border-b-4 border-r-4 border-red-600"></div>
                    <Camera className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-24 h-24 text-black/20" />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-20 bg-black text-white">
        <div className="max-w-7xl mx-auto px-6">
          <div className="text-red-600 font-bold mb-4 tracking-wider">CAPABILITIES</div>
          <h2 className="text-5xl font-bold mb-16">Nothing but power</h2>
          
          <div className="grid md:grid-cols-3 gap-8">
            <div className="border border-white/20 p-8 hover:border-red-600 transition">
              <Eye className="w-12 h-12 mb-4" />
              <h3 className="text-2xl font-bold mb-4">Real-time Recognition</h3>
              <p className="text-gray-400">Instant identity verification in live video feeds with sub-second accuracy.</p>
            </div>
            
            <div className="border border-white/20 p-8 hover:border-red-600 transition">
              <Lock className="w-12 h-12 mb-4" />
              <h3 className="text-2xl font-bold mb-4">Military Security</h3>
              <p className="text-gray-400">End-to-end encryption with bcrypt hashing and MFA support.</p>
            </div>
            
            <div className="border border-white/20 p-8 hover:border-red-600 transition">
              <Activity className="w-12 h-12 mb-4" />
              <h3 className="text-2xl font-bold mb-4">Analytics & Logs</h3>
              <p className="text-gray-400">Comprehensive reporting and audit trails for compliance.</p>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Landing;
