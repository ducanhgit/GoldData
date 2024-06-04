from selenium import webdriver
from selenium.webdriver.common.by import By

urls = {
        "SJC":"https://giavang.org/"
}
def get_price(link):
    driver = webdriver.Chrome()
    driver.get(link)
    price_element = driver.find_elements(By.CLASS_NAME,"gold-price")
    #price = price_element[0].text.replace(' ','##')
    prices = [element.text.replace(' ', '##') for element in price_element]
    driver.quit()
    return prices


prices = get_price(urls["SJC"])
for price in prices:
    print(price)
'''
'''
with open("gia.txt", "w",encoding='utf-8') as file:
    for price in prices:
        file.write(price + "\n")

print("ok")
