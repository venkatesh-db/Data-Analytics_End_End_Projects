# Matrimony Platform

## Overview
The Matrimony Platform is a production-grade GenAI-powered matchmaking system designed to provide scalable, explainable, and efficient matchmaking services. It leverages advanced AI techniques, including LLMs, vector databases, and embedding pipelines.

## Features
- **Profile Intelligence Engine**: Extracts personality traits and values.
- **Semantic Matching Engine**: Matches profiles using embeddings.
- **Behavioral Learning System**: Learns user behavior over time.
- **Explainable AI**: Provides reasoning for matches.
- **Advanced Features**:
  - AI Chatbot for matchmaking.
  - Chat Compatibility Analyzer.
  - Red Flag Detection System.
  - Family Compatibility Scoring.

## Setup

### Prerequisites
- Python 3.9+
- Docker
- Kubernetes
- Redis
- PostgreSQL

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd matrimony_platform
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run tests:
   ```bash
   pytest
   ```

### Running Services
- **API Service**:
  ```bash
  python backend/api/main.go
  ```
- **AI Service**:
  ```bash
  python backend/ai_services/app.py
  ```
- **Chatbot Service**:
  ```bash
  python backend/advanced_features/chatbot.py
  ```

### Deployment
1. Build Docker images:
   ```bash
   docker build -t matrimony-platform-api ./backend/api
   docker build -t matrimony-platform-ai ./backend/ai_services
   docker build -t matrimony-platform-chatbot ./backend/advanced_features
   ```

2. Deploy to Kubernetes:
   ```bash
   kubectl apply -f deployment/kubernetes/deployment.yaml
   ```

## CI/CD
The CI/CD pipeline is configured in `deployment/cicd/pipeline.yaml` and supports automated testing, building, and deployment.

## License
This project is licensed under the MIT License.