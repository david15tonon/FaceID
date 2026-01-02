#!/bin/bash

echo "🚀 Deploying Frontend to Vercel"

cd frontend

# Install dependencies
npm install

# Build
npm run build

# Deploy to Vercel
vercel --prod

echo "✅ Frontend deployed successfully"
