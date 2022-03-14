import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import pandas as pd

driver = webdriver.Chrome('/Users/jadsa/Desktop/Jad/Ynov/Cours/B3/Python/Cours/chromedriver')
options = webdriver.ChromeOptions() 
options.add_argument("--disable-popup-blocking")
options.add_argument('--no-default-browser-check')
options.add_argument('--log-level=3')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--start-maximized')
options.add_experimental_option("detach", True)
service = Service('/Users/jadsa/Desktop/Jad/Ynov/Cours/B3/Python/Cours/chromedriver')
driver = webdriver.Chrome(options=options, service=service)

driver.get('https://genius.com/Genius-france-discographie-rap-2021-annotated')
WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//p/b")))
ListAlbumsDF = []
ListMusicsDF = []
ListMusicsAlbumRow = []
for k in driver.find_elements(By.XPATH, "//span[contains(@class, 'ReferentFragmentVariantdesktop__Highlight')]"):
    try:
        k.click()
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'Annotation__Container')]")))
        for i in driver.find_elements(By.XPATH, "//div[contains(@class, 'Annotation__Container')]//li"):
            ListMusicsAlbumRow.append(str(i.text))
    except:
        pass
    ListAlbumsDF.append(str(k.text))
    ListMusicsDF.append(ListMusicsAlbumRow[:])
    ListMusicsAlbumRow.clear()

    # to track the progress:
    print("{:.0%}".format(len(ListAlbumsDF)/len(driver.find_elements(By.XPATH, "//span[contains(@class, 'ReferentFragmentVariantdesktop__Highlight')]"))))

df = pd.DataFrame(ListMusicsDF, index=ListAlbumsDF)    
df.columns += 1 
df.to_csv('result.csv')

df2 = pd.read_csv("./result.csv")
