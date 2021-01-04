import requests
from utils import constants

response = requests.get(url="https://world.openfoodfacts.org/api/v0/product/737628064502.json", params=constants.LOAD_DATA)
data = response.json()
print(data)
