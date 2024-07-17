import cv2
import time
from ultralytics import YOLO
import threading

class CameraThread(threading.Thread):
    def __init__(self, camera_id, model):
        super().__init__()
        self.camera_id = camera_id
        self.model = model
        self.cap = cv2.VideoCapture(camera_id)
        self.running = True
        self.frame_count = 0
        self.total_time = 0

    def run(self):
        while self.running and self.cap.isOpened():
            start_time = time.time()
            success, frame = self.cap.read()

            if success:
                # Run YOLOv8 inference on the frame
                results = self.model(frame)

                # Visualize the results on the frame
                annotated_frame = results[0].plot()

                # Display the annotated frame
                cv2.imshow(f"YOLOv8 Inference - Camera {self.camera_id}", annotated_frame)

                # Update timing information
                end_time = time.time()
                self.total_time += (end_time - start_time)
                self.frame_count += 1

                # Break the loop if 'q' is pressed
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    self.running = False
            else:
                # Break the loop if the end of the video is reached
                break

        self.cap.release()

    def stop(self):
        self.running = False

    def get_average_processing_time(self):
        if self.frame_count > 0:
            return self.total_time / self.frame_count
        return 0

# Load the YOLOv8 model
model = YOLO("F:/Code/Python/YOLO_SFT24/runs/detect/train11/weights/best.pt")

# Create camera threads for two cameras (camera IDs 0 and 1)
camera_thread1 = CameraThread(0, model)
camera_thread2 = CameraThread(1, model)

# Start the camera threads
camera_thread1.start()
camera_thread2.start()

# Wait for the camera threads to finish
camera_thread1.join()
camera_thread2.join()

# Calculate and display the average processing times
avg_time_cam1 = camera_thread1.get_average_processing_time()
avg_time_cam2 = camera_thread2.get_average_processing_time()
print(f"Average processing time for Camera 0: {avg_time_cam1:.4f} seconds/frame")
print(f"Average processing time for Camera 1: {avg_time_cam2:.4f} seconds/frame")

# Close the display windows
cv2.destroyAllWindows()
