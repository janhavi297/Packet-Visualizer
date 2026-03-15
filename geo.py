import requests

def ip_to_location(ip):
    try:
        url = f"https://ipinfo.io/{ip}/json"
        response = requests.get(url)
        data = response.json()

        city = data.get("city")
        region = data.get("region")
        country = data.get("country")

        return f"{city}, {region}, {country}"

    except Exception as e:
        return f"Location lookup failed: {e}"
