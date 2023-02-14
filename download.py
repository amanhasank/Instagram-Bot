from instascrape import Reel
import time
import os

# session id
SESSIONID = "SESSION ID"

# Header with session id
headers = {
	"User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.115 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html) ",
	"cookie": f'sessionid={SESSIONID};'
}
path = os.getcwd()
print(path)

def download(link, file_name):
    insta_reel = Reel(link)
    insta_reel.scrape(headers=headers)

    # Giving path where we want to download reel to the
    fileName = file_name
    print(fileName)
    insta_reel.download(fp=f"{path}\\{fileName}")

    # printing success Message
    print('Downloaded Successfully.')


#Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.115 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html) 