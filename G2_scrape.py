import requests
import json

def fetch_api_data():
    url = "https://data.g2.com/api/v1/products"
    headers = {
        "Authorization": "Token token=84c74188e6f001c306dabf92fc8d09de819bb1ab99346bb228e22f30fbfc6777",
        "Content-Type": "application/vnd.api+json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Assuming the response contains JSON data, parse it.
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

def save_data_to_json(data, filename="data.json"):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    data = fetch_api_data()
    if data is not None:
        save_data_to_json(data)
        print(f"Data saved to data.json")
    else:
        print("No data retrieved.")
