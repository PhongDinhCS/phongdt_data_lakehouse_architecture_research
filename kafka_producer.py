import requests
from bs4 import BeautifulSoup
from kafka import KafkaProducer
import time

# Kafka broker address
bootstrap_servers = '172.18.0.8:9092'
# bootstrap_servers = 'kafka:9092'

# Kafka topic
topic = 'html_topic'

# Create KafkaProducer instance
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

try:
    while True:
        # Fetch the webpage content
        currency_page = requests.get('https://www.dailyfx.com/forex-rates#currencies')

        # Parse the HTML content
        currency_content = BeautifulSoup(currency_page.text, 'html.parser')

        # Find the specific divs
        currency_content_div = currency_content.find_all('div', {'class': 'dfx-instrumentTiles row'})

        # Convert the content of divs to a string
        div_content = ''.join(str(div) for div in currency_content_div)

        # Get the first 50,000 characters
        div_content_2000 = div_content[:2000]

        # Message to send
        message = "this will be html data"

        # Add timestamp to the message
        timestamp = time.time()
        message_with_timestamp = f"{message} - Timestamp: {timestamp}\n\n{div_content_2000}"

        # Convert message to bytes
        message_bytes = message_with_timestamp.encode('utf-8')

        # Produce message to Kafka topic
        producer.send(topic, value=message_bytes)

        # Print the message sent
        print("Message sent successfully to Kafka topic:", topic, "- Timestamp:", timestamp)
        print("First 2000 characters of div content:\n", div_content_2000[:2000], "...")  # Print first 500 characters of the first 50,000 characters

        # Sleep for 10 seconds before sending the next message
        time.sleep(10)

except KeyboardInterrupt:
    print("Keyboard interrupt detected. Stopping the Kafka producer.")
    # Close producer
    producer.close()
