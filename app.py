import os

import requests
from dotenv import load_dotenv
from flask import Flask, request

load_dotenv('.env')

webhook_url = os.environ.get('SLACK_WEBHOOK_URL', '')

app = Flask(__name__)

@app.route('/')
def home():
    return "Home page"

@app.route('/health', methods=['GET'])
def health_check():
    return 'OK', 200

@app.route('/test-notify', methods=['GET'])
def test_notify_slack_api():
    text = "Test message sent with cron jobs"
    response = send_to_slack(text)
    if response.status_code == 200:
        return 'Success', 200
    else:
        return 'Failed to send message to Slack', response.status_code

@app.route('/notify', methods=['POST'])
def notify_slack_api():
    data = request.get_json()
    text = data.get('text', '')
    response = send_to_slack(text)
    if response.status_code == 200:
        return 'Success', 200
    else:
        return 'Failed to send message to Slack', response.status_code

def send_to_slack(text):
    if not webhook_url:
        print("Slack webhook URL not configured")
        return

    payload = {"text": text}
    response = requests.post(webhook_url, json=payload)
    return response

if __name__ == '__main__':
    app.run()
