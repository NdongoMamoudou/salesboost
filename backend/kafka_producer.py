from kafka import KafkaProducer
import json, random, time

producer = KafkaProducer(
    bootstrap_servers="kafka:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

products = [f"p{i}" for i in range(1, 11)]
event_types = ["view", "click", "buy"]

print("🚀 Start sending events to Kafka topic: user_events")

while True:
    event = {
        "user_id": random.randint(1, 3),
        "product_id": random.choice(products),
        "event_type": random.choice(event_types),
        "timestamp": time.time()
    }
    
    producer.send("user_events", event)
    print("✅ Event sent:", event)
    time.sleep(1)
