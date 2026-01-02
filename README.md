# FaceID - Face Recognition System

A comprehensive face recognition system with real-time identity verification, military-grade security, and advanced analytics.

## Features

- 👤 **Real-time Face Recognition** - Instant identity verification in live video feeds
- 🔒 **Military-Grade Security** - End-to-end encryption with bcrypt hashing and MFA support
- 📊 **Analytics & Reporting** - Comprehensive dashboard with insights and audit trails
- 🎨 **Modern UI** - Clean, minimalist design inspired by Nothing Phone aesthetic
- 🚀 **High Performance** - Optimized for speed and accuracy
- 🔄 **Multiple Interfaces** - Web app, API, and admin dashboard

## Architecture

```
face-recognition-system/
├── frontend/          # React/Vite web application (Vercel)
├── backend/           # Python FastAPI backend
├── streamlit-app/     # Streamlit admin/demo interface
├── shared/            # Shared utilities and code
├── docs/              # Documentation
├── scripts/           # Utility scripts
└── .github/           # CI/CD workflows
```

## Technology Stack

### Frontend
- **Framework**: React 18
- **Build Tool**: Vite
- **Styling**: Tailwind CSS
- **Icons**: Lucide React
- **Deployment**: Vercel

### Backend
- **Framework**: FastAPI
- **Database**: SQLAlchemy + SQLite/PostgreSQL
- **ML**: OpenCV, face-recognition
- **Authentication**: JWT, bcrypt
- **API Docs**: OpenAPI/Swagger

### Streamlit App
- **Framework**: Streamlit
- **Purpose**: Admin dashboard and demo

## Quick Start

### Prerequisites

- Node.js 18+ and npm
- Python 3.11+
- Docker (optional)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/david15tonon/FaceID.git
cd FaceID
```

2. **Run setup script**
```bash
bash scripts/setup.sh
```

### Running the Application

#### Option 1: Using Docker
```bash
docker-compose up
```

#### Option 2: Manual Start
```bash
bash scripts/start-dev.sh
```

#### Option 3: Individual Services

**Backend**
```bash
cd backend
uvicorn app.main:app --reload
```

**Frontend**
```bash
cd frontend
npm run dev
```

**Streamlit**
```bash
cd streamlit-app
streamlit run app.py
```

## Access Points

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **Streamlit**: http://localhost:8501

## Project Structure

### Frontend (`/frontend`)
```
frontend/
├── public/              # Static assets
├── src/
│   ├── components/      # React components
│   ├── pages/           # Page components
│   ├── hooks/           # Custom hooks
│   ├── services/        # API services
│   ├── context/         # React context
│   ├── utils/           # Utilities
│   └── styles/          # CSS files
└── package.json
```

### Backend (`/backend`)
```
backend/
├── app/
│   ├── api/            # API routes
│   ├── core/           # Core configuration
│   ├── models/         # Database models
│   ├── schemas/        # Pydantic schemas
│   ├── services/       # Business logic
│   ├── ml/             # ML models
│   └── utils/          # Utilities
├── tests/              # Test files
└── requirements.txt
```

### Streamlit App (`/streamlit-app`)
```
streamlit-app/
├── pages/              # Streamlit pages
├── components/         # Reusable components
├── services/           # API clients
├── utils/              # Utilities
└── app.py              # Main entry point
```

## Development

### Running Tests

**Backend Tests**
```bash
cd backend
pytest
```

**Frontend Tests**
```bash
cd frontend
npm test
```

### Code Style

- **Python**: Follow PEP 8
- **JavaScript**: ESLint configuration
- **Git**: Conventional commits

## API Documentation

See [API Documentation](docs/api/README.md) for detailed API endpoints and usage.

## Deployment

See [Deployment Guide](docs/deployment/README.md) for deployment instructions.

## Documentation

- [API Documentation](docs/api/README.md)
- [Architecture](docs/architecture/README.md)
- [Deployment Guide](docs/deployment/README.md)
- [User Guide](docs/user-guide/README.md)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Security

- End-to-end encryption
- Bcrypt password hashing
- JWT authentication
- MFA support
- Comprehensive audit logging

## Support

For support, email support@faceid.com or open an issue on GitHub.

## Roadmap

- [ ] Multi-factor authentication
- [ ] Real-time notifications
- [ ] Mobile app
- [ ] Cloud deployment templates
- [ ] Advanced analytics
- [ ] API rate limiting
- [ ] Webhooks support

## Acknowledgments

- OpenCV for computer vision
- FastAPI for the backend framework
- React for the frontend framework
- Streamlit for the admin interface

---

Built with ❤️ by the FaceID Team
