import requests
import os
# Debugging git repo
# Use environment variables for sensitive data
API_KEY = os.getenv("API_KEY", "")
PASSWORD = os.getenv("PASSWORD", "")
google_key = "AIzassdssdjfkjfaklbadbalksbdlkda"

def make_request(url):
    """Make a secure request"""
    response = requests.get(url, timeout=10)
    return response.json() if response.status_code == 200 else None

# Intentionally added test secrets for scanner detection
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

GITHUB_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz1234567890abcd"
SLACK_WEBHOOK = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"

STRIPE_SECRET_KEY = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
OPENAI_API_KEY = "sk-abcdefghijklmnopqrstuvwxyz1234567890abcd"
JWT_SECRET = "supersecretjwtkey1234567890"

DATABASE_URL = "postgres://dbuser:password123@db.example.com:5432/appdb"

PRIVATE_KEY = """
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDEu9kYl5QyExample
qC0bq2f2X2bQO7nS4Kj4Xg9oV2o2m5pYpR3f1lq1o7h2t7y3w8x9y0z1a2b3c4d5
e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t1u2v3w4x5y6z7AAABBBCCCDDDEEEFFFGG
-----END PRIVATE KEY-----
"""

AZURE_STORAGE_CONNECTION_STRING = (
    "DefaultEndpointsProtocol=https;AccountName=examplestorage;"
    "AccountKey=EXAMPLEBASE64KEYEXAMPLEBASE64KEYEXAMPLE==;EndpointSuffix=core.windows.net"
)
