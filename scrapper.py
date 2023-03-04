# Info containing product -> RICE

import requests
import json

# Endpoint
url = "https://www.bigbasket.com/listing-svc/v2/products?type=ps&slug=rice&page=3"
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 9; AOSP on IA Emulator Build/PSR1.180720.122) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36',
    'Cookie': '_bb_locSrc=default; x-channel=pwa; PWA=1; _bb_loid=301; _bb_bhid=; _bb_nhid=1723; _bb_vid=ODA1NDA0MDc3NQ==; _bb_dsevid=1722; _bb_dsid=1720; csrftoken=210kv262HoVV6VKl9P2FSoRvlRhrxtLwxEHBlorCLt2iQTTcZepRr6YGkuYH6d39; _bb_home_cache=706d7324.1.visitor; csurftoken=u7KxOQ.ODA1NDA0MDc3NQ==.1677901580819.zLYvuuM8qTohivDqNmZkryIwiI9TvYVR1NevZGD1B7g=; _gid=GA1.2.1569184749.1677901585; _gat_gtag_UA_27455376_1=1; adb=0; _sp_van_encom_hid=1722; _client_version=2642; _bb_hid=1723; _sp_bike_hid=1720; sessionid=f9b9w911rtjjvn75x4n0yqiaj13lguej; _bb_tc=1; _bb_rdt="MzEzMDI0MDExNg==.1"; _bb_rd=1; bb_home_cache=706d7324.1.visitor; bigbasket.com=16e3a3f4-7222-40c9-8b45-1e8932e4e4ca; ReferrerBannerSlideID=6459026; _gcl_au=1.1.53180253.1677901587; _fbp=fb.1.1677901587856.259100178; _ga=GA1.1.1801779024.1677901585; ufi=1; _bb_cid=5; _bb_aid="Mjk4ODk1NzI0MA=="; data=%7B%22referrerInPageContext%22%3A%22backbtn%22%7D; _bb_bb2.0=1; is_global=0; _bb_sa_ids=10242; bb2_enabled=true; _bb_bb2.0=1; is_global=0; _bb_sa_ids=10242; ts="2023-03-04 09:16:42.542"; _ga_414F8KRWNG=GS1.1.1677901588.1.1.1677901603.0.0.0; _ga_FRRYG5VKHX=GS1.1.1677901588.1.1.1677901603.45.0.0',
}

response = requests.get(url, headers=headers)

# Converting data to JSON
data = json.loads(response.text)

no_of_prods = len(data['tabs'][0]['product_info']['products'])

# Accessing Products
products = data['tabs'][0]['product_info']['products']

# Creating a list that will contain dictionary in each dict we'll have a key-value pair for product name, img-url, price
product_items = []
for product in products:
    product_temp = {}
    product_name = product['desc']
    product_price =f"₹{product['pricing']['discount']['mrp']}"
    product_img = product['absolute_url']
    product_temp.update({'product_name':product_name, 'product_img': product_img, 'product_price': product_price})
    product_items.append(product_temp)

# Results
print(f"No of products: {no_of_prods}")
print(f"List of items containing Product Name, IMG, Price:\n{product_items}")
