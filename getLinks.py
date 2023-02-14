import csv
import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from moviepy.editor import *
import random
import multiprocessing
import moviepy.editor as mymovie
from moviepy.editor import *
import download
from itertools import islice
from moviepy.config import change_settings

url = "https://www.instagram.com/sayonarc/reels/"
time.sleep(2)
video_links = []

#getting all video links
def getting_links():
    vids = input("How many reels you want to download? ")
    options = webdriver.ChromeOptions()
    options.add_argument("--lang=en")
    profile = "C:\\Users\\amhasan\\AppData\\Local\\Google\\Chrome Beta\\User Data\\"
    options.binary_location = "C:\\Program Files\\Google\\Chrome Beta\\Application\\chrome.exe"
    options.add_argument(f"--user-data-dir={profile}")
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    browser.maximize_window()
    time.sleep(2)
    browser.get(url)
    time.sleep(5)
    
    if int(vids)>12:
      vids = int(vids)
      #setting a scrool func. to load enough reels we want to download
      num = (vids / 12) + 3
      print(num)

      # Use a loop to scroll down the pa3ge multiple times
      for i in range(int(num)):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
    else:
      print("no need to load pages")    
    
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    links = soup.find_all('a', href=lambda x: x and '/reel/' in x)
   
    for link in islice(links, int(vids)):
        reel_url = link['href']
        str = "https://www.instagram.com" + reel_url
        video_links.append(str)

        
    print(vids)    
    print("Reels will be downloaded...")
    return video_links    

def downloading_videos(downloadedLinks):
    i=1
    for link in downloadedLinks:
      fn = link.split('/')  
      file_name = fn[4] + ".mp4"
      print ("Downloading reel: %s"%file_name)
      download.download(link, file_name) 
      print("file downloaeded  ********************************************************")

      clip = mymovie.VideoFileClip(file_name)
      image = ImageClip('top.png', duration= clip.duration)
      final_clip = CompositeVideoClip([clip, image.set_pos(('center', 'top'))])
      final_clip.write_videofile(f"reels/cool{i}.mp4", fps=60)
      i=i+1
                


if __name__ == "__main__":
  
  #getting all video links
    downloadedLinks = getting_links()
    print(downloadedLinks)

    with multiprocessing.Pool() as pool:
        pool.map(downloading_videos(downloadedLinks))
   

  # #download reels
    #downloading_videos(downloadedLinks)  
    