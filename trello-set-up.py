import os
import requests
from dotenv import load_dotenv

load_dotenv()

TRELLO_API_BASE_URL = os.getenv('TRELLO_API_BASE_URL')

def url_builder(route):
    return f"{TRELLO_API_BASE_URL}{route}"

keyParams = {
    'key': os.getenv('TRELLO_API_KEY'),
    'token': os.getenv('TRELLO_API_TOKEN')
}

# Create a board
board_name = 'DevOps Test Board'

queryParams = {
   'name': board_name,
   'defaultLists': 'false'
} | keyParams

response = requests.post(url_builder('/boards'), params=queryParams)

if response.status_code == 200:
    BOARD_ID = response.json()['id']
    print(f"Board created with name {board_name} and id: {BOARD_ID}")
else:
    print("Board creation failed.")
    exit(1)

# Create Lists

lists = ["To do", "In Progress", "Done"]

for title in lists:
    queryParams = {
        'name': title,
    } | keyParams

    response = requests.post(url_builder(f"/boards/{BOARD_ID}/lists"), params=queryParams)

    if response.status_code == 200:
        print(f"List created with name: {title}")


print(f"Set BOARD_ID in .env")
print(f"{BOARD_ID=}")
