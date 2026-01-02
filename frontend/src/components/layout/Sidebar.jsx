import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { Circle, Activity, Camera, Eye, FileText, User } from 'lucide-react';
import { useAuth } from '../../hooks/useAuth';

const Sidebar = () => {
  const location = useLocation();
  const { logout } = useAuth();

  const menuItems = [
    { path: '/dashboard', icon: Activity, label: 'Dashboard' },
    { path: '/enroll', icon: Camera, label: 'Enroll Face' },
    { path: '/verify', icon: Eye, label: 'Verify' },
    { path: '/reports', icon: FileText, label: 'Reports' },
    { path: '/profile', icon: User, label: 'Profile' },
  ];

  return (
    <aside className="fixed left-0 top-0 h-full w-64 bg-black text-white p-6 flex flex-col">
      <Link to="/" className="flex items-center gap-2 mb-12">
        <Circle className="w-6 h-6 fill-white" />
        <span className="font-bold text-xl">FaceID</span>
      </Link>

      <nav className="space-y-2 flex-1">
        {menuItems.map((item) => {
          const Icon = item.icon;
          const isActive = location.pathname === item.path;
          return (
            <Link
              key={item.path}
              to={item.path}
              className={`w-full text-left px-4 py-3 font-medium transition ${
                isActive ? 'bg-white/10' : 'hover:bg-white/10'
              }`}
            >
              <Icon className="inline w-5 h-5 mr-3" />
              {item.label}
            </Link>
          );
        })}
      </nav>

      <button
        onClick={logout}
        className="text-sm text-gray-400 hover:text-white transition"
      >
        Logout →
      </button>
    </aside>
  );
};

export default Sidebar;
