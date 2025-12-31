import React from 'react';
import { Link } from 'react-router-dom';
import { Camera, Eye, FileText } from 'lucide-react';

const QuickActions = () => {
  const actions = [
    {
      title: 'Enroll Face',
      description: 'Add a new face to the system',
      icon: Camera,
      path: '/enroll',
      color: 'hover:border-red-600',
    },
    {
      title: 'Verify Identity',
      description: 'Check if a face matches',
      icon: Eye,
      path: '/verify',
      color: 'hover:border-blue-600',
    },
    {
      title: 'View Reports',
      description: 'Access analytics and logs',
      icon: FileText,
      path: '/reports',
      color: 'hover:border-green-600',
    },
  ];

  return (
    <div className="grid md:grid-cols-3 gap-6">
      {actions.map((action, index) => {
        const Icon = action.icon;
        return (
          <Link
            key={index}
            to={action.path}
            className={`border-2 border-black p-6 transition ${action.color}`}
          >
            <Icon className="w-10 h-10 mb-4" />
            <h3 className="text-xl font-bold mb-2">{action.title}</h3>
            <p className="text-gray-600 text-sm">{action.description}</p>
          </Link>
        );
      })}
    </div>
  );
};

export default QuickActions;
