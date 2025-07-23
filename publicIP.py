import http.client
import requests

def get():
  """Retrieves the public IP address using ip4only.me."""
  try:
    response = requests.get("https://ip4only.me/api/")
    response.raise_for_status()  # Raise an exception for bad status codes
    return response.text.strip()
  except requests.exceptions.RequestException as e:
    return f"Error retrieving IP: {e}"