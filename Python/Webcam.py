import cv2
import time
import datetime


class Webcam:
    
    def __init__(self, camera_index=0, file_destination='output'):
        self.file_destination = file_destination
        self.camera_index = camera_index
        self.cap = None

        

    def start(self):
        self.cap = cv2.VideoCapture(self.camera_index)
        if not self.cap.isOpened():
            raise Exception("Could not open webcam")
        
    def stop(self):
        if self.cap:
            self.cap.release()

        cv2.destroyAllWindows()

    def record(self, seconds = 5, fps=30.0, trailing =  ""):
        if self.cap is None:
            raise Exception("Webcam not started")
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        filename = self.file_destination + trailing + '.mp4'
        ret, frame = self.cap.read()
        frameSize = frame.shape[1], frame.shape[0]
        out = cv2.VideoWriter(filename, fourcc, fps, frameSize)
        
        start_time = time.time()
        frame_count = 0
        while time.time() - start_time < seconds:
            ret, frame = self.cap.read()

            if not ret:
                print("Frame read failed!")
                break
            out.write(frame)
            frame_count += 1
        print(f"Recorded {frame_count} frames in {seconds} seconds.")
        out.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    webcam = Webcam()
    try:
        webcam.start()
        webcam.record(10,30.0)
    except Exception as e:
        print(f"Webcam error: {e}")
    finally:
        webcam.stop()
    
