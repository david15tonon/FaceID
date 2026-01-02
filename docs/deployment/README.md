# Deployment Guide

## Frontend Deployment (Vercel)

1. Connect your GitHub repository to Vercel
2. Set environment variables in Vercel dashboard
3. Deploy

## Backend Deployment

### Using Docker

```bash
docker-compose up -d
```

### Manual Deployment

```bash
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Streamlit Deployment

```bash
streamlit run app.py
```
