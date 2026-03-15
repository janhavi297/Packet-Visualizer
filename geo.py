import requests

def ip_to_location(ip):
    try:
        url = f"https://ipinfo.io/{ip}?token=d24f5561140b55"
        response = requests.get(url)
        data = response.json()

        city = data.get("city")
        region = data.get("region")
        country = data.get("country")
        lat = data.get("latitude")
        long = data.get("longitude")

        return f"{city}, {region}, {country}, ({lat}, {long})"

    except Exception as e:
        return f"Location lookup failed: {e}"
