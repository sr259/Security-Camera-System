# Linux BLE Security Monitoring System



A motion-activated security system built using an Arduino Nano, STHS34PF80 infrared motion sensor, Bluetooth Low Energy (BLE), and a Linux server.



When motion is detected, the Arduino sends a BLE notification to a Linux host, which records video, converts it to a Discord-compatible format, and uploads both a timestamped alert and recording to a Discord channel.



## Features



* Interrupt-driven motion detection using the STHS34PF80
* Bluetooth Low Energy communication via HM-10
* Linux-based monitoring service using Python and Bleak
* Automatic webcam recording using OpenCV
* FFmpeg video conversion to H.264 MP4
* Discord webhook notifications and video uploads
* Protection against duplicate recordings using asyncio locks



## System Architecture



```text

STHS34PF80 Motion Sensor

         ↓

    Arduino Nano

         ↓

     HM-10 BLE

         ↓

    Linux Server

         ↓

    OpenCV Webcam

         ↓

   FFmpeg Convert

         ↓

Discord Notification

```



## Technologies Used



### Embedded



* Arduino Nano
* Adafruit STHS34PF80 Library
* Hardware Interrupts
* SoftwareSerial



### Linux / Software



* Python
* asyncio
* Bleak
* OpenCV
* FFmpeg
* Discord Webhooks



## Example Workflow



1. Motion is detected by the STHS34PF80.
2. The sensor asserts its interrupt pin.
3. The Arduino sends a BLE notification.
4. The Linux service receives the event.
5. A video recording begins automatically.
6. FFmpeg converts the recording to H.264 MP4.
7. A timestamped alert and video are uploaded to Discord.



## Future Improvements



* Automatic startup with systemd
* BLE reconnection handling
* Final Recording after BLE disconnect/powerloss
* Multiple camera support
* Local event database
* Battery-backed operation



## Lessons Learned



This project provided experience with:



* Embedded firmware development
* Hardware interrupts
* BLE communication
* Linux systems programming
* Asynchronous Python programming
* Video processing pipelines
* End-to-end embedded system integration

