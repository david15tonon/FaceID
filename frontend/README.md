# FaceID Frontend

React application for the FaceID face recognition system.

## Features

- Modern React with Hooks
- React Router for navigation
- Tailwind CSS for styling
- Axios for API calls
- Real-time face capture with webcam
- Face enrollment and verification
- User authentication with MFA support
- Dashboard with analytics
- Responsive design

## Getting Started

### Prerequisites

- Node.js 18+ and npm

### Installation

```bash
npm install
```

### Configuration

Copy `.env.example` to `.env.local` and update the values:

```bash
cp .env.example .env.local
```

### Development

```bash
npm run dev
```

The app will be available at `http://localhost:3000`

### Build

```bash
npm run build
```

### Deployment

The app is configured to deploy to Vercel:

```bash
vercel --prod
```

## Project Structure

- `src/components/` - Reusable components
- `src/pages/` - Page components
- `src/hooks/` - Custom React hooks
- `src/services/` - API and service integrations
- `src/context/` - React context providers
- `src/utils/` - Utility functions
- `src/styles/` - Global styles

## API Integration

The frontend connects to the backend API via the `VITE_API_URL` environment variable.

## License

MIT
