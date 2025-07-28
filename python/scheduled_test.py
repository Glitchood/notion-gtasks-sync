# scheduled_test.py
import os
import requests
import json
from datetime import datetime

print("🚀 Starting scheduled test...")

# Get the Cloudflare Worker URL from a GitHub Secret
worker_url = os.getenv('CF_WORKER_URL')

if not worker_url:
    print("🔥 Error: CF_WORKER_URL is not set as a secret.")
    exit(1)

# Create a dynamic payload so each test is unique
payload = {
    "source": "Scheduled GitHub Action",
    "timestamp": datetime.now().isoformat()
}

print(f"📡 Pinging Cloudflare Worker at {worker_url}")

try:
    # Make the POST request
    response = requests.post(worker_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})

    # Check the response from the worker
    response.raise_for_status()  # This will raise an error for bad responses (4xx or 5xx)
    print(f"✅ Success! Worker responded with status {response.status_code}:")
    print(response.text)

except requests.exceptions.RequestException as e:
    print(f"🔥 Error making request: {e}")
    exit(1)