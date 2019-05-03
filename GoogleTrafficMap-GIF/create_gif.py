import datetime
from datetime import datetime as dt
import imageio
import boto3

Bucket_name = "googletrafficmap"
yesterday = dt.now() - datetime.timedelta(days=1)
prefix = yesterday.strftime("%Y%m%d") + "/"
gif_name = yesterday.strftime("%Y%m%d")

#Create low-client connection
client = boto3.client('s3')

#Retrieve all files under folder name = prefix
response = client.list_objects(
    Bucket=Bucket_name,
    Delimiter=',',
    EncodingType='url',
    Prefix=prefix,
    RequestPayer='requester'
)

image_array = []
#Read in image as byte array
for item in response['Contents']:
    path = "https://s3.ca-central-1.amazonaws.com/googletrafficmap/" + item['Key']
    image_array.append(imageio.imread(path))

#Frame Rate in seconds
kargs = { 'duration': 2 }

#Specifying imageio.RETURN_BYTES in mimwrite() forces mimwrite to parse as binary data
#mimwrite(ParseAsBinaryData, list of image files, final image format)
gif = imageio.mimwrite(imageio.RETURN_BYTES, image_array, 'gif', **kargs)

#Pushing to S3
client.put_object(Bucket=Bucket_name, Body=gif, Key=gif_name + ".gif")
