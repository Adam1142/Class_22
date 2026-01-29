# Importing the library
import requests

# Hugging face API URL for sentiment analysis
api_url = "https://api-inference.huggingface.co/models/distilbert-bas-uncased"

# Replace with your Hugging Face API token
headers = {
    "Authorisation": "Bearer YOUR_API_KEY_HERE"
}

#  text for sentiment analysis
text = "I love this move! It was fantastic"

#  POST Requests to the Hugging Face API
response = requests.post(api_url, headres = headers, json=("Inputs": text))

# Checking the status of the response
if response.status_code == 200:
    # Parse the response JSON
    result = response.json()
    print(f"Sentiment: {result[0]['label']} with confidence score: {result[0]['score']}")
else:
    print(f"Error: {response.status_code}")