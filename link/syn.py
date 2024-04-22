#stync(final)  video of avatar by  https://replicate.com/cjwbw/video-retalking/api/learn-more

import replicate
from dotenv import load_dotenv
from pprint import pprint
import base64
import requests

with open(r"C:\Users\neelsheth\Downloads\link\output.mp4", 'rb') as file:
  data = base64.b64encode(file.read()).decode('utf-8')
  face = f"data:application/octet-stream;base64,{data}"


with open(r"C:\Users\neelsheth\Downloads\link\output.wav", 'rb') as file:
  data1 = base64.b64encode(file.read()).decode('utf-8')
  aud = f"data:application/octet-stream;base64,{data1}"

input = {
    "face": face,
    "input_audio": aud
}

output = replicate.run(
    "cjwbw/video-retalking:db5a650c807b007dc5f9e5abe27c53e1b62880d1f94d218d27ce7fa802711d67",
    input=input
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