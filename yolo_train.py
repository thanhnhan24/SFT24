from ultralytics import YOLO
import os
# Load a COCO-pretrained YOLOv8n model
model = YOLO("yolov8n.pt")

# Display model information (optional)
#model.info()

if __name__ == '__main__':
    # Train the model on the COCO8 example dataset for 100 epochs
    results = model.train(data="thnhan.yaml", epochs = 50, imgsz=640,batch = 2, device=0)
    os.system("shutdown /s /t 1")
