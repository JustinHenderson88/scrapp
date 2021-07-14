import panda as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='/Users/justin/Documents/chromedriver')
driver.get('https://oxylabs.io/blog')
results = []
content = driver.page_source
soup = BeautifulSoup(content)

for element in soup.findAll(attrs='blog-card__content-wrapper'):
    name = element.find('h2')
    if name not in results:
        results.append(name.text)

print(results)
