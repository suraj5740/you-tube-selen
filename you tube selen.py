import selenium
import time
import warnings
warnings.filterwarnings("ignore")
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(executable_path="C:\\Users\\ADMIN\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.youtube.com/")


searchbox=driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input")
searchbox.send_keys("Technology Tarka")
searchbox.send_keys(Keys.ENTER)
time.sleep(2)

for i in range(4):
    i=driver.find_element(By.TAG_NAME,"body").send_keys(Keys.PAGE_DOWN)
time.sleep(1)
for i in range(4):
    i=driver.find_element(By.TAG_NAME,"body").send_keys(Keys.PAGE_UP)
time.sleep(2)

driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div[2]/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string").click()
time.sleep(5)

driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[1]/video").click()
time.sleep(2)

driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[1]/yt-icon-button[2]/button/yt-icon").click()
time.sleep(1)

driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/tp-yt-app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[1]/div/ytd-guide-entry-renderer[1]/a/tp-yt-paper-item").click()
time.sleep(5)
