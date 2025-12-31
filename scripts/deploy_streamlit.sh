#!/bin/bash

echo "🚀 Deploying Streamlit App to Streamlit Cloud"

cd streamlit-app

echo "ℹ️  To deploy to Streamlit Cloud:"
echo "1. Push this repository to GitHub"
echo "2. Go to https://streamlit.io/cloud"
echo "3. Connect your GitHub repository"
echo "4. Select streamlit-app/app.py as the main file"
echo "5. Configure environment variables in Streamlit Cloud settings"
echo "6. Deploy!"

echo ""
echo "Environment variables to set:"
echo "- API_URL"
echo "- API_KEY"
echo "- ENABLE_CAMERA"
