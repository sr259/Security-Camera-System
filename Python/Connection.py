import asyncio
import Webcam
from bleak import BleakClient
import ConvertMP4
import datetime
import DiscordCommunication
import time
import dotenv
import os

#import dotenv environment to get BLE address and CHAR_UUID
dotenv.load_dotenv()
ADDRESS = os.getenv("BLE_ADDRESS")
CHAR_UUID = os.getenv("CHAR_UUID")
HOOK = os.getenv("DISCORD_WEBHOOK_URL")

recording_lock = asyncio.Lock()
def notification_handler(sender, data):
    try:
        # Decode bytes to text string and strip newlines (\r\n)
        message = data.decode('utf-8').strip()
        if message == "Motion Detected":
            asyncio.create_task(start_recording())
            
    except UnicodeDecodeError:
        print(f"Raw binary packet: {data}")

async def start_recording():
    if recording_lock.locked():
        print("Already recording, ignoring new trigger.")
        return
    async with recording_lock:
        webcam = Webcam.Webcam(0, "../../../Videos/Security/output") #be sure to put in whatever file destination you want
        webcam.start()
        try:
            await asyncio.to_thread(webcam.record, seconds=5)
        finally:
            webcam.stop()
            print("Webcam stopped.")

            file_time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            text_time_stamp = datetime.datetime.now().strftime('%a %d %b %Y, %I:%M%p')
            final_destination = webcam.file_destination + file_time_stamp + ".mp4"

            #FORMATTING THE MP4 SO DISCORD CAN READ IT, DELETING OLD FILE
            ConvertMP4.ConvertMP4.convert(webcam.file_destination + ".mp4", final_destination)
            ConvertMP4.ConvertMP4.remove_file(webcam.file_destination + ".mp4")

            #SENDING TO DISCORD
            comm = DiscordCommunication.DiscordCommunication(HOOK)
            comm.send_message(f"Motion detected at {text_time_stamp}!")
            comm.send_mp4(final_destination)

async def main():
    print(f"Connecting to {ADDRESS}...")
    async with BleakClient(ADDRESS) as client:
        print("Connected successfully!")

        # Start listening for the serial data stream
        await client.start_notify(CHAR_UUID, notification_handler)
        
        # Keep the script running to listen for incoming serial prints
        while True:
            await asyncio.sleep(1)

if __name__ == "__main__":
    try:
        print("Arming security camera...")
        seconds = 1
        start_time = time.time()
        while time.time() - start_time < seconds:
            print("Connecting in: " + str(seconds - int(time.time() - start_time)) + " seconds", end="\r")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nDisconnected.")

