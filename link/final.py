import os
import replicate
from dotenv import load_dotenv
from pprint import pprint
import base64
import requests
import subprocess

def final(text_inp):
      # Set the REPLICATE_API_TOKEN environment variable
        os.environ['REPLICATE_API_TOKEN'] = 'API TOKEN'
      # Create the final folder if it doesn't exist
        command = 'SET REPLICATE_API_TOKEN=API TOKEN'

        try:
            subprocess.run(command, shell=True, check=True)
              
            
            
            final_folder = 'final'
            if not os.path.exists(final_folder):
                os.makedirs(final_folder)

            # Text to speech code
            import pyttsx3

            # Initialize the engine
            engine = pyttsx3.init()

            # Text to be converted to speech
            text = str(text_inp)

            # Set properties (optional)
            engine.setProperty('rate', 150)  # Speed of speech
            engine.setProperty('volume', 1.0)  # Volume level (0.0 to 1.0)

            # Convert text to speech and save to file
            engine.save_to_file(text, os.path.join(final_folder, 'output.wav'))

            # Wait for the speech to finish
            engine.runAndWait()

            print("-----------text to speech done--------------")
            # Lipsing code
            with open(r"C:\Users\neelsheth\Downloads\hackathon\link\john_hr.png", 'rb') as file:
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

            # Download video
            url = output
            file_name = os.path.join(final_folder, 'output_lipsing.mp4')

            # Send a GET request to the URL to download the video
            response = requests.get(url)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Open the file in binary mode and write the content of the response to it
                with open(file_name, "wb") as file:
                    file.write(response.content)
                print("Lipsing video downloaded successfully!")
            else:
                return("Failed to download the lipsing video. Status code")


            # Sync code
            with open(r"C:\Users\neelsheth\Downloads\hackathon\link\final\output_lipsing.mp4", 'rb') as file:
                data = base64.b64encode(file.read()).decode('utf-8')
                face = f"data:application/octet-stream;base64,{data}"

            with open(os.path.join(final_folder, 'output.wav'), 'rb') as file:
                data1 = base64.b64encode(file.read()).decode('utf-8')
                aud = f"data:application/octet-stream;base64,{data1}"

            input_data = {
                "face": face,
                "input_audio": aud
            }

            output = replicate.run(
                "cjwbw/video-retalking:db5a650c807b007dc5f9e5abe27c53e1b62880d1f94d218d27ce7fa802711d67",
                input=input_data
            )
            pprint(output)

            # Download synced video
            url = output
            file_name = os.path.join(final_folder, 'final0.mp4')  # Initial filename

            # Check for existing files in the final folder to determine the unique filename
            i = 0
            while os.path.exists(file_name):
                i += 1
                file_name = os.path.join(final_folder, f'final{i}.mp4')

            # Send a GET request to the URL to download the video
            response = requests.get(url)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Open the file in binary mode and write the content of the response to it
                with open(file_name, "wb") as file:
                    file.write(response.content)
                return("Synced video downloaded successfully!")
            else:
                print("Failed to download the synced video. Status code")
                return "error"
            
        except subprocess.CalledProcessError as e:
                return("Error executing command")
