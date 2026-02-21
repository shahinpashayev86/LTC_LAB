import requests
from bs4 import BeautifulSoup

url = 'https://turbo.az/autos/10080922-byd-leopard-7'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

important_tags = [
    "Şəhər", "Marka", "Model", "Buraxılış ili", "Ban növü",
    "Rəng", "Mühərrik", "Yürüş", "Sürətlər qutusu",
    "Ötürücü", "Yeni", "Yerlərin sayı", "Sahiblər", "Vəziyyəti"
]

response = requests.get(url, headers=headers)
response.encoding = 'utf-8'  # Handle Azerbaijani characters

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    car_data = {}

    # 1. Price extraction (using your bold class)
    price_element = soup.find(class_='product-price__i--bold')
    if price_element:
        car_data["Qiymət"] = price_element.get_text(strip=True)

    # 2. Statistics extraction (Yeniləndi and Baxışların sayı)
    # These are usually in a container like 'product-statistics' or separate spans
    stats = soup.find_all('span', class_='product-statistics__i-text')
    for stat in stats:
        text = stat.get_text(strip=True)
        if "Yeniləndi:" in text:
            car_data["Yeniləndi"] = text.replace("Yeniləndi:", "").strip()
        elif "Baxışların sayı:" in text:
            car_data["Baxışların sayı"] = text.replace("Baxışların sayı:", "").strip()

    # 3. Technical Specifications extraction
    properties = soup.find_all('div', class_='product-properties__i')
    for prop in properties:
        label = prop.find('label', class_='product-properties__i-name').text.strip()
        value = prop.find('span', class_='product-properties__i-value').text.strip()

        if label in important_tags:
            car_data[label] = value

    # Result Output
    for key, val in car_data.items():
        print(f"{key}: {val}")
else:
    print(f"Error: {response.status_code}")