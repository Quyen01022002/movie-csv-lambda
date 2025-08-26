import os
from dotenv import load_dotenv

load_dotenv()

KAFKA_BROKER = os.getenv("KAFKA_BROKER", "localhost:9092")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "movies_topic")
CSV_FILE = os.getenv("CSV_FILE", "./data/movies_metadata.csv")
BATCH_SIZE = int(os.getenv("BATCH_SIZE", 100))
