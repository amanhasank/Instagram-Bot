from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import pyautogui
from selenium.webdriver.common.action_chains import ActionChains

# Replace "USERNAME" and "PASSWORD" with your Instagram login credentials
username = "USERNAME"
password = "PASSWORD"

# Replace "My reel" with your desired caption for the reel
captiondata = "Like and Share this with Anime Fans... " + "\n" + "." + "\n" + "." "\n" + "." + "\n" + "#demonslayer #anime #kimetsunoyaiba #naruto #manga #onepiece #otaku #myheroacademia #attackontitan #nezuko #animememes #animeedits #blackclover #bleach #tokyoghoul #narutoshippuden #nezukokamado #animeedit #weeb"

num = input("how many reels you want to upload? ")
start = input("You want to start from which reel number? ")

# Start the Chrome browser
options = webdriver.ChromeOptions()
profile = "C:\\Users\\USERNAME\\AppData\\Local\\Google\\Chrome\\User Data\\"
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
options.add_argument(f"--user-data-dir={profile}")
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

# Navigate to the Instagram login page
driver.get("https://www.instagram.com/")
time.sleep(5)

# #LOGIN 
# element = driver.find_element(By.XPATH, "//input[@name='username']")
# element.send_keys(username)
# driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
# driver.find_element(By.XPATH, "//button[@type='submit']").click()


# # Wait for the page to load
i=int(start)
end = int(num)+i

for i in range(int(start),end):   
    print(i)
    select =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/div/a/div")))
    select.click()
    upload =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Select from computer']")))
    upload.click()

    simp_path = "reels/reel{}.mp4".format(str(i))
    abs_path = os.path.abspath(simp_path)
    time.sleep(2)

    #give path
    pyautogui.typewrite(abs_path)
    pyautogui.press('enter')

    #select crop 
    crop = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@aria-label='Select crop']")))
    crop.click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[1]/div/button[1]/div/div[1]/div').click()

    #next button
    nxt = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Next']")))
    nxt.click()

    #next button
    nxt2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Next']")))
    nxt2.click()

    #caption
    caption = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@aria-label='Write a caption...']")))
    caption.send_keys(captiondata)

    #share button
    share = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Share']")))
    share.click()

    #closing the win2dow
    time.sleep(2)
    WebDriverWait(driver, 50).until(EC.text_to_be_present_in_element((By.XPATH, "//div[text()='Reel shared']"), "Reel shared"))
    close = driver.find_element(By.XPATH, "//*[@aria-label='Close']")
    close.click()
    driver.refresh()

    print("Reel uploaded")
    i = i+1


