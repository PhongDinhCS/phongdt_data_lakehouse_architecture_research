#make sure that you run (chmod +x create_topic.sh) from the directory STOCK_ANALYSIS_APP
#run this code after (docker compose up) to check list of Topics (sudo docker-compose exec kafka kafka-topics.sh --list --bootstrap-server localhost:9092)

#!/bin/bash 

/opt/bitnami/kafka/bin/kafka-topics.sh --create --topic $DEFAULT_TOPIC --bootstrap-server kafka:9092 
echo "topic $DEFAULT_TOPIC was created"


# Define the list of topic names as you want to create
#TOPIC_LIST=("topic1-example" "topic2-example")

# Loop through the topic names and create each topic
for topic in "${TOPIC_LIST[@]}"; do /opt/bitnami/kafka/bin/kafka-topics.sh --create --topic "$topic" --bootstrap-server kafka:9092; echo "Topic $topic was created"; done


# run this code to open producer and consumer
#sudo docker-compose exec kafka /opt/bitnami/kafka/bin/kafka-console-producer.sh --topic default_topic --bootstrap-server localhost:9092
#sudo docker-compose exec kafka /opt/bitnami/kafka/bin/kafka-console-consumer.sh --topic default_topic --from-beginning --bootstrap-server localhost:9092
