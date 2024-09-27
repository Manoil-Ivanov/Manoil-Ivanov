# from bs4 import BeautifulSoup
# import requests
# import pandas as pd

# url = "https://www.cars.com/shopping/results/?stock_type=all&makes%5B%5D=mercedes_benz&models%5B%5D=&maximum_distance=30&zip="

# response = requests.get(url)
# soup = BeautifulSoup(response.content, "html.parser")
# print(response.status_code)

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.cars.com/shopping/results/?stock_type=all&makes%5B%5D=mercedes_benz&models%5B%5D=&maximum_distance=30&zip="

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}

response = requests.get(url, headers=headers, timeout=10)
print(response.status_code)  # Print the status code to check the response

soup = BeautifulSoup(response.content, "html.parser")

