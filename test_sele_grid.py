from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

urls = {
    "XAU/USD": "https://www.investing.com/currencies/xau-usd-historical-data",
}

def get_price(link, currency):
    desired_capabilities = DesiredCapabilities.FIREFOX.copy()
    hub_url = "http://4444:4444/wd/hub"  
    driver = webdriver.Remote(
        command_executor=hub_url,
        desired_capabilities=desired_capabilities,
    )
    driver.get(link)
    price_element = driver.find_elements(By.CLASS_NAME, "historical-data-v2_price__atUfP")
    price = price_element[0].text.replace(' ', '##')
    print(f"{currency} Price: {price}")
    driver.quit()
    return price

prices = {}
for currency, link in urls.items():
    prices[currency] = get_price(link, currency)


for currency, price in prices.items():
    print(f"{currency} Price: {price}")

print("ok")
