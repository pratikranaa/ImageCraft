# Frontend stage
FROM node:20-alpine AS frontend

WORKDIR /app/frontend

COPY AI-frontend/package*.json ./

RUN npm install

COPY AI-frontend/ .

EXPOSE 5173

# Build React app
RUN npm run build

# Backend stage
FROM python:3.9-slim AS backend

# Set working directory for backend
WORKDIR /app/backend

# Copy and install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy rest of the backend files
COPY . .



# Expose the port Flask is running on
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=main.py

# Copy built React files from frontend stage to backend directory
COPY --from=frontend /app/frontend/dist /app/backend/dist

# Run Flask
CMD ["flask", "run"]
