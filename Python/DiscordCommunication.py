import requests
import os
import dotenv

class DiscordCommunication:
    def __init__(self, hook):
        self._webhook_url = hook
    
    def send_mp4(self, file_path):
        if not os.path.exists(file_path):
            print(file_path + " not found.")
            return
        
        with open(file_path, "rb") as f:
            files = {'file': f}
            response = requests.post(self._webhook_url, files=files)
        
        if response.status_code == 204 or response.status_code == 200:
            print("MP4 sent successfully.")
        else:
            print(f"Failed to send MP4. Status code: {response.status_code}")

    def send_message(self, message):
        data = {"content": message}
        response = requests.post(self._webhook_url, json=data)
        
        if response.status_code == 204 or response.status_code == 200:
            print("Message sent successfully.")
        else:
            print(f"Failed to send message. Status code: {response.status_code}")

if __name__ == "__main__":
    dotenv.load_dotenv()
    hook = os.getenv("DISCORD_WEBHOOK_URL")
    print(hook)
    comm = DiscordCommunication(hook)
    comm.send_message("hello")
