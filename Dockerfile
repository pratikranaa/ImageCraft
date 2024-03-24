FROM node:18.17.1

WORKDIR /app/frontend

COPY AI-frontend/package*.json ./

RUN npm install

COPY AI-frontend/ .

RUN npm run build

# Backend stage
FROM python:3.9 AS backend

# Set working directory for backend
WORKDIR /app/backend

# Copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the backend files
COPY . .

# Expose the port flask is running on
EXPOSE 5000

# Run Flask
CMD ["flask", "--app", "main", "run"]