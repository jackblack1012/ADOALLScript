import requests

def download_azure_ip_ranges(url):
    response = requests.get(url)
    ip_ranges = response.json()
    return ip_ranges  # You would add parsing logic here to filter as needed

# Example URL - Replace with the actual URL for Azure IP ranges
azure_ip_ranges_url = 'URL_TO_AZURE_IP_RANGES_JSON'
ip_ranges = download_azure_ip_ranges(azure_ip_ranges_url)
print(ip_ranges)
