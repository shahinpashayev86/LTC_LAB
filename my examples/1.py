import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# --- CONFIGURATION ---
# Your specific search URL for Jeep Wrangler
base_url = 'https://turbo.az/autos?q%5Bsort%5D=&q%5Bmake%5D%5B%5D=36&q%5Bmodel%5D%5B%5D=&q%5Bmodel%5D%5B%5D=346&q%5Bcurrency%5D=azn'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# The specific tags you requested
important_tags = [
    "Şəhər", "Marka", "Model", "Buraxılış ili", "Ban növü",
    "Rəng", "Mühərrik", "Yürüş", "Sürətlər qutusu",
    "Ötürücü", "Yeni", "Yerlərin sayı", "Sahiblər", "Vəziyyəti"
]


def scrape_turbo_wranglers():
    raw_links = []

    # 1. COLLECT ALL LINKS FROM SEARCH PAGES
    # We loop through 6 pages to cover all ~122 results
    for page in range(1, 7):
        print(f"Searching page {page} for links...")
        url = f"{base_url}&page={page}"
        try:
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find car links on the search page
            items = soup.find_all('a', class_='products-i__link')
            for a in items:
                raw_links.append("https://turbo.az" + a['href'])

            time.sleep(1)  # Small delay to be safe
        except Exception as e:
            print(f"Error on search page {page}: {e}")

    # 2. OPTIMIZATION: REMOVE DUPLICATES
    # This removes VIP/Premium duplicates while keeping the original order
    all_car_links = list(dict.fromkeys(raw_links))
    print(f"Total links found: {len(raw_links)} | Unique links to scrape: {len(all_car_links)}")

    # 3. EXTRACT DATA FROM EACH UNIQUE LINK
    results = []
    for index, link in enumerate(all_car_links):
        print(f"[{index + 1}/{len(all_car_links)}] Extracting: {link}")
        try:
            res = requests.get(link, headers=headers)
            res.encoding = 'utf-8'  # Ensure 'ə' and 'ş' display correctly
            item_soup = BeautifulSoup(res.text, 'html.parser')

            car_info = {"Link": link}

            # Extract Price
            price_element = item_soup.find(class_='product-price__i--bold')
            car_info["Qiymət"] = price_element.get_text(strip=True) if price_element else "N/A"

            # Extract Technical Specs
            props = item_soup.find_all('div', class_='product-properties__i')
            for p in props:
                label_tag = p.find('label')
                value_tag = p.find('span')
                if label_tag and value_tag:
                    label = label_tag.text.strip()
                    value = value_tag.text.strip()
                    if label in important_tags:
                        car_info[label] = value

            # Extract Statistics (Yeniləndi / Baxışlar)
            stats = item_soup.find_all('span', class_='product-statistics__i-text')
            for s in stats:
                txt = s.get_text(strip=True)
                if "Yeniləndi:" in txt:
                    car_info["Yeniləndi"] = txt.split(":")[-1].strip()
                if "Baxışların sayı:" in txt:
                    car_info["Baxışların sayı"] = txt.split(":")[-1].strip()

            results.append(car_info)
            time.sleep(1.5)  # Anti-block delay

        except Exception as e:
            print(f"Error on {link}: {e}")

    # 4. SAVE TO EXCEL
    if results:
        df = pd.DataFrame(results)
        # Reordering columns so Price and Link are first
        cols = ['Qiymət', 'Yeniləndi', 'Baxışların sayı'] + [t for t in important_tags if t in df.columns] + ['Link']
        df = df[cols]

        filename = "Turbo_Jeep_Wrangler_Data.xlsx"
        df.to_excel(filename, index=False)
        print(f"\nSUCCESS! Data saved to {filename}")
    else:
        print("No data collected.")


if __name__ == "__main__":
    scrape_turbo_wranglers()