from selenium import webdriver
from datetime import datetime
import os
import time

now = datetime.now()
folder_name = now.strftime("%Y%m%d")
image_name = "traffic_" + now.strftime("%Y%m%d") + "-" + now.strftime("%H-%M") + ".png"

#Create folder if not exist
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

#Get map snapshot
driver = webdriver.PhantomJS(service_log_path=os.path.devnull)
driver.set_window_size(1920, 1080) # set the window size that you need
driver.get('http://googletrafficmap.s3-website.ca-central-1.amazonaws.com')
driver.save_screenshot(folder_name + "/" + image_name)

time.sleep(60)
driver.close()
driver.quit()
