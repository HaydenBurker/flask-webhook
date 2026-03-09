import uuid

def generate_webhook_secret():
    return uuid.uuid4()

if __name__ == "__main__":
    print(f"Webhook Secret: {generate_webhook_secret()}")
