import datetime
from datetime import datetime as dt
import imageio
import glob

Bucket_name = "googletrafficmap"
yesterday = dt.now() - datetime.timedelta(days=1)
prefix = yesterday.strftime("%Y%m%d") + "/"
gif_name = yesterday.strftime("%Y%m%d")
#folder = dt.now().strftime("%Y%m%d")
folder = "image list"
path = folder + "/*.png"

file_list = glob.glob(path)
list = sorted(file_list, key=lambda x: x.split("\\")[1].split("_")[1].split(".")[0])

image_array = []
#Read in image as byte array
for item in list:
    path = item
    image_array.append(imageio.imread(path))

#Frame Rate in seconds
kargs = { 'duration': 2 }

#Specifying imageio.RETURN_BYTES in mimwrite() forces mimwrite to parse as binary data
#mimwrite(ParseAsBinaryData, list of image files, final image format)
gif = imageio.mimwrite(imageio.RETURN_BYTES, image_array, 'gif', **kargs)