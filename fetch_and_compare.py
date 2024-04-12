import os
import requests
import json
import csv
from fuzzywuzzy import process
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def fetch_g2_data(page_size=25, page_number=9):
    url = f"https://data.g2.com/api/v1/products?page[size]={page_size}&page[number]={page_number}"
    headers = {
        "Authorization": "Token token=84c74188e6f001c306dabf92fc8d09de819bb1ab99346bb228e22f30fbfc6777",
        "Content-Type": "application/vnd.api+json"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return [product['attributes'] for product in data['data']]
    else:
        print(f"Failed to fetch G2 data. Status code: {response.status_code}")
        return []


def fetch_producthunt_data():
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer UBcVJ7cz5c8xBMtf46DJGCVEvfRnaf6BbbFTvTJdZDo',
        'Host': 'api.producthunt.com'
    }

    query = """
    {
      posts(order: NEWEST, first: 30) {
        edges {
          node {
            id
            name
            url
            tagline
            description
            createdAt
          }
        }
      }
    }
    """

    response = requests.post('https://api.producthunt.com/v2/api/graphql', headers=headers, json={'query': query})
    if response.status_code == 200:
        data = json.loads(response.text)
        return [product['node'] for product in data['data']['posts']['edges']]
    else:
        print(f"Failed to fetch Product Hunt data. Status code: {response.status_code}")
        return []

def is_meaningful(name):
    # Check if the name is too short
    if len(name) < 3:
        return False
    # Check if the name contains only common words
    words = name.lower().split()
    for word in words:
        if word not in stop_words:
            return True
    return False


def compare_data(g2_data, producthunt_data):
    names_g2 = [product['name'] for product in g2_data]
    names_producthunt = [product['name'] for product in producthunt_data]

    unique_names = []
    threshold = 90
    for name in names_producthunt:
        match, score = process.extractOne(name, names_g2)
        if score < threshold and is_meaningful(name):
            unique_names.append(name)
    
    return unique_names

def save_to_csv(data, filename="unique_names.csv"):
    if os.path.exists(filename):
        # Read existing unique names from the file
        existing_names = set()
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header row
            for row in reader:
                if row:  # Check if row is not empty
                    existing_names.add(row[0])

        # Add only new unique names to the existing set
        new_unique_names = [name for name in data if name not in existing_names]
    else:
        new_unique_names = data

    # Append new unique names to the CSV file
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not os.path.exists(filename):
            writer.writerow(['Unique Names'])  # Write header row if file is new
        for name in new_unique_names:
            writer.writerow([name])



if __name__ == "__main__":
    g2_data = fetch_g2_data()
    producthunt_data = fetch_producthunt_data()
    unique_names = compare_data(g2_data, producthunt_data)
    save_to_csv(unique_names)
    print("Process completed. Unique names have been saved.")
