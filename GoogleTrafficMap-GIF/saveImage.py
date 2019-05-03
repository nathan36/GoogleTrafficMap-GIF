from selenium import webdriver
from datetime import datetime
import boto3
import os
import time

now = datetime.now()
folder_name = now.strftime("%Y%m%d")
image_name = "traffic_" + now.strftime("%Y%m%d") + "-" + now.strftime("%H-%M") + ".png"
Bucket_name = "googletrafficmap"
prefix = folder_name + "/"

#Get map snapshot
driver = webdriver.PhantomJS(service_log_path=os.path.devnull)
driver.set_window_size(1920, 1080) # set the window size that you need
driver.get('http://googletrafficmap.s3-website.ca-central-1.amazonaws.com')
# driver.save_screenshot(folder_name + "/" + image_name)
screenshotPNG = driver.get_screenshot_as_png() #Get screenshot in binary data

#Create low-client connection
client = boto3.client('s3')
#Uploading image to s3 bucket and creating folder structure at the same time
client.put_object(
    Bucket = Bucket_name,
    Body = screenshotPNG,
    Key = folder_name + "/" + image_name
)

time.sleep(60)
driver.close()
driver.quit()
