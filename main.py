import requests

api_key = "ec8ffcbcfc224f52be815024c8cdd259"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023" \
      "-07-22&sortBy=publishedAt&apiKey=ec8" \
      "ffcbcfc224f52be815024c8cdd259"

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and descriptions
for article in content["articles"]:
    print(content["articles"])