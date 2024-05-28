import requests

# URL for motivational quotes API
quotes_api_url = "https://zenquotes.io/api/random"

def get_motivational_quote():
  """Fetches a motivational quote using a free API"""
  response = requests.get(quotes_api_url)
  if response.status_code == 200:
    # Parse the JSON response to get the quote and author
    data = response.json()
    quote = data[0]["q"]
    author = data[0]["a"] if data[0]["a"] else "Unknown"  # Handle missing author
    return f"{quote} - {author}"  # Combine quote and author
  else:
    print(f"Error: API request failed with status code {response.status_code}")
    return "Sorry, couldn't retrieve a motivational quote at this time."
  
print(get_motivational_quote())