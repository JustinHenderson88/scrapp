import panda as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='/Users/justin/Documents/chromedriver')
driver.get('https://oxylabs.io/blog')
results = []
other_results = []
content = driver.page_source
soup = BeautifulSoup(content)
driver.quit()

#find name text in selected attritbute
for a in soup.findAll(attrs='blog-card__content-wrapper'):
    name = a.find('h2')
    if name not in results:
        results.append(name.text)

#find date in selected attritbute
for b in soup.findAll(attrs='blog-card__date-wrapper'):
    date = b.find('h2')
    if date not in results:
        other_results.append(date.text)

#create results csv
df = pd.DataFrame({'Names': results, 'Dates': other_results})
df.to_csv('names.csv', index=False, encoding='utf-8')
