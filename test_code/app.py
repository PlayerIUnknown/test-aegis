import requests
import os
# Debugging git repo
# Use environment variables for sensitive data
API_KEY = os.getenv("API_KEY", "")
PASSWORD = os.getenv("PASSWORD", "")

def make_request(url):
    """Make a secure request"""
    response = requests.get(url, timeout=10)
    return response.json() if response.status_code == 200 else None


# Run again