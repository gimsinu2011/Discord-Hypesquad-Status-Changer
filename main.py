import requests

payload = {
    "house_id": "1",
    "identity_enabled": True,
}

headers = {
    "accept": "*/*",
    "accept-language": "ko",
    "authorization": "YOUR_DISCORD_TOKEN_HERE",
    "content-type": "application/json",
}

response = requests.post("https://discord.com/api/v9/hypesquad/online", headers=headers, json=payload)

if response.status_code == 200:
    print(response.json())
else: 
    print(f"Failed to fetch data: {response.status_code}")
