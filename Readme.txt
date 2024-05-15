# make sure that you run (chmod +x create_topic.sh) from the directory STOCK_ANALYSIS_APP before run (sudo docker-compose up)
#docker-compose up --build -d

# run this code to check list of Topics (sudo docker-compose exec kafka kafka-topics.sh --list --bootstrap-server localhost:9092)
# run this code to open producer and consumer
#sudo docker-compose exec kafka /opt/bitnami/kafka/bin/kafka-console-producer.sh --topic default_topic --bootstrap-server localhost:9092
#sudo docker-compose exec kafka /opt/bitnami/kafka/bin/kafka-console-consumer.sh --topic default_topic --from-beginning --bootstrap-server localhost:9092













---
https://chat.openai.com/share/6f16a03f-6a78-4ae2-93f7-288ebc43e449

mkdir stock_analysis_app
cd stock_analysis_app

# Backend
mkdir -p backend
touch backend/Dockerfile
touch backend/requirements.txt
touch backend/app.py

# Frontend
mkdir -p frontend
touch frontend/Dockerfile
touch frontend/package.json
mkdir -p frontend/src  # Create src directory
touch frontend/src/sample.js  # Create a sample file inside src

# Spark
mkdir -p spark
touch spark/Dockerfile
touch spark/submit.sh
touch spark/analysis.py

# Docker Compose
touch docker-compose.yml

# Environment Variables
touch .env

# Volumes
mkdir -p volumes

