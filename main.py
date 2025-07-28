# test_script.py
import os
import json

print("✅ Python script was executed by GitHub Actions!")

# GitHub Actions passes the webhook payload in a file specified by this env var
event_path = os.getenv('GITHUB_EVENT_PATH')
if event_path:
    with open(event_path, 'r') as f:
        event_data = json.load(f)
        print("\n--- Received Payload ---")
        # The 'client_payload' is where our data from Cloudflare will be
        print(json.dumps(event_data.get('client_payload'), indent=2))
        print("------------------------")
else:
    print("🔥 No event payload found.")