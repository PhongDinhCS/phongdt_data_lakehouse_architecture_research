# make sure that you run (chmod +x create_topic.sh) from the directory STOCK_ANALYSIS_APP before run (sudo docker-compose up)
#docker-compose up --build -d

# run this code to check list of Topics (sudo docker-compose exec kafka kafka-topics.sh --list --bootstrap-server localhost:9092)
# run this code to open producer and consumer
#sudo docker-compose exec kafka /opt/bitnami/kafka/bin/kafka-console-producer.sh --topic default_topic --bootstrap-server localhost:9092
#sudo docker-compose exec kafka /opt/bitnami/kafka/bin/kafka-console-consumer.sh --topic default_topic --from-beginning --bootstrap-server localhost:9092

Instructions:
Ensure you run chmod +x create_topic.sh before starting the services.
Use docker-compose up -d to start all services.
Check the list of topics with sudo docker-compose exec kafka kafka-topics.sh --list --bootstrap-server localhost:9092.
Use docker exec -it hiveserver2 beeline -u 'jdbc:hive2://hiveserver2:10000/' to interact with Hive.

---
git clone https://github.com/PhongDinhCS/phongdt_data_lakehouse_architecture_research.git
docker compose down
docker stop $(docker ps -aq) && docker rm $(docker ps -aq)
docker volume prune
docker container prune
docker-compose down -v --remove-orphans
docker-compose up -d
docker network ls
docker network prune
docker network inspect phongdt_data_lakehouse_architecture_research_lakehouse_network
docker network rm phongdt_data_lakehouse_architecture_research_lakehouse_network
docker exec -it hiveserver2 bash
docker exec -it metastore beeline -u 'jdbc:hive2://localhost:10002'
docker exec -it hiveserver2 beeline -u 'jdbc:hive2://hiveserver2:10000/'


git commit
git commit -m "install and run kafka to scrape htlm"
git add .
git push origin main


---
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


