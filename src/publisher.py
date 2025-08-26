import json
from confluent_kafka import Producer
from .config import KAFKA_BROKER, KAFKA_TOPIC


def delivery_report(err, msg):
    if err is not None:
        print(f"Delivery failed: {err}")
    else:
        print(f"Delivered to {msg.topic()} [{msg.partition()}] @ offset {msg.offset()}")


class KafkaPublisher:
    def __init__(self, broker: str = KAFKA_BROKER, topic: str = KAFKA_TOPIC):
        self.producer = Producer({"bootstrap.servers": broker})
        self.topic = topic

    def publish_batch(self, records: list[dict]):
        for record in records:
            self.producer.produce(
                topic=self.topic,
                value=json.dumps(record).encode("utf-8"),
                callback=delivery_report
            )
        self.producer.flush()
