#mute audio video of avatar by  https://github.com/yoyo-nb/Thin-Plate-Spline-Motion-Model

import replicate
from dotenv import load_dotenv
from pprint import pprint
import base64
import requests

with open(r"C:\Users\neelsheth\Downloads\link\john_hr.png", 'rb') as file:
  data = base64.b64encode(file.read()).decode('utf-8')
  source_image = f"data:application/octet-stream;base64,{data}"
output = replicate.run(
    "yoyo-nb/thin-plate-spline-motion-model:382ceb8a9439737020bad407dec813e150388873760ad4a5a83a2ad01b039977",
    input={
      
        "source_image": source_image,
        "driving_video": "https://replicate.delivery/mgxm/005e32a9-ff8e-4dfd-bcfd-bbbf3791ca94/driving.mp4"
    }
)
pprint(output)


#download video
url = output
file_name = "output.mp4"

# Send a GET request to the URL to download the video
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Open the file in binary mode and write the content of the response to it
    with open(file_name, "wb") as file:
        file.write(response.content)
    print("Video downloaded successfully!")
else:
    print(f"Failed to download the video. Status code: {response.status_code}")