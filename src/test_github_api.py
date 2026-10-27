
import requests

url = "https://api.github.com/repos/pandas-dev/pandas"

response = requests.get(url, timeout=30)

print("HTTP status:", response.status_code)

if response.status_code == 200:
    data = response.json()

    print("Repository:", data["full_name"])
    print("Stars:", data["stargazers_count"])
    print("Forks:", data["forks_count"])
    print("Main language:", data["language"])
    print("Last updated:", data["updated_at"])
else:
    print("Request failed:", response.text)
