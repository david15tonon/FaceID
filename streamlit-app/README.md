# FaceID Streamlit App

Streamlit-based admin interface for the FaceID face recognition system.

## Features

- Interactive dashboard with real-time metrics
- Face enrollment with camera or upload
- Face verification interface
- Analytics and reporting
- System logs and audit trail
- Settings management

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

Update the API URL and other settings in `.env`.

## Running

```bash
streamlit run app.py
```

The app will be available at `http://localhost:8501`

## Pages

- **Dashboard** - System overview and metrics
- **Face Enrollment** - Register new faces
- **Face Verification** - Verify identities
- **Analytics** - Performance metrics and insights
- **Logs** - Audit trail and activity logs
- **Settings** - System configuration

## Deployment

### Streamlit Cloud

1. Push code to GitHub
2. Connect repository on [streamlit.io](https://streamlit.io)
3. Set `streamlit-app/app.py` as the main file
4. Configure environment variables in Streamlit Cloud settings

### Docker

```bash
docker build -t faceid-streamlit .
docker run -p 8501:8501 faceid-streamlit
```

## License

MIT
