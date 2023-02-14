import time, os
import undetected_chromedriver as webdriver
# from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
profile = "C:\\Users\\USERNAME\\AppData\\Local\\Google\\Chrome\\User Data\\"
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
options.add_argument(f"--user-data-dir={profile}")
options.add_argument("--detach")

num = input("how many reels you want to upload? ")
start = input("You want to start from which reel number? ")

i=int(start)
end = int(num)+i

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=options, use_subprocess=True)
driver.get("https://studio.youtube.com/channel/UCRU8VJFbVu5kQNJU72wCZuQ")
time.sleep(3)

for i in range(int(start),end):   
    upload_button = driver.find_element(By.XPATH, '//*[@id="upload-icon"]')
    upload_button.click()
    time.sleep(5)

    file_input = driver.find_element(By.XPATH, '//*[@id="content"]/input')
    simp_path = "reels/reel{}.mp4".format(str(i))
    abs_path = os.path.abspath(simp_path)
    file_input.send_keys(abs_path)

    next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(((By.XPATH, '//*[@id="next-button"]'))))
    for i in range(3):
        next_button.click()
        time.sleep(3)

    done_button = driver.find_element(By.XPATH, '//*[@id="done-button"]')
    done_button.click()
    time.sleep(5)
    driver.refresh()
