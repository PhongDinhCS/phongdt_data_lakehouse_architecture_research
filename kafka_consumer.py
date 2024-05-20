from kafka import KafkaConsumer

# Kafka broker address
bootstrap_servers = '172.18.0.8:9092'
# bootstrap_servers = 'kafka:9092'

# Kafka topic
topic = 'html_topic'

# Create KafkaConsumer instance
consumer = KafkaConsumer(
    topic,
    bootstrap_servers=bootstrap_servers,
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: x.decode('utf-8')
)

print("Starting the Kafka consumer...")

try:
    for message in consumer:
        # Print the message value
        print(f"Received message: {message.value[:2000]}\n")
except KeyboardInterrupt:
    print("Keyboard interrupt detected. Stopping the Kafka consumer.")
finally:
    consumer.close()
