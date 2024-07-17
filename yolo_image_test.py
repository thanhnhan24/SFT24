import os
from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt

def load_image(image_path):
    """Load an image from a file path."""
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Chuyển đổi từ BGR sang RGB
    return image

def display_image(image, results):
    """Display the image with detected bounding boxes."""
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = box.conf[0]
            class_id = int(box.cls[0])
            label = f"{result.names[class_id]} {conf:.2f}"
            
            # Vẽ bounding box và nhãn
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    plt.figure(figsize=(10, 10))
    plt.imshow(image)
    plt.axis('off')
    plt.show()

def test_model_on_directory(model_path, image_dir):
    """Test the YOLOv8 model with images from a specified directory."""
    # Tải mô hình YOLOv8
    model = YOLO(model_path)

    # Duyệt qua tất cả các tệp tin trong thư mục ảnh
    for image_name in os.listdir(image_dir):
        image_path = os.path.join(image_dir, image_name)
        if os.path.isfile(image_path):
            # Load và hiển thị ảnh
            image = load_image(image_path)
            results = model(image)
            display_image(image, results)

def test_model_on_image(model_path, image_path):
    """Test the YOLOv8 model with a specified image."""
    # Tải mô hình YOLOv8
    model = YOLO(model_path)

    # Load và hiển thị ảnh
    image = load_image(image_path)
    results = model(image)
    display_image(image, results)

# Đường dẫn đến mô hình YOLOv8 và thư mục chứa ảnh kiểm tra
model_path = 'F:/Code/Python/YOLO_SFT24/runs/detect/train7/weights/best.pt'
image_dir = 'F:/Code/Python/YOLO_SFT24/SFT24-facedetect-4/test/images'
image_path = 'F:/Code/Python/YOLO_SFT24/419874006_925757482450589_7632101751253349623_n.jpg'

# Kiểm tra mô hình với ảnh từ thư mục
#test_model_on_directory(model_path, image_dir)

# Kiểm tra mô hình với ảnh chỉ định
test_model_on_image(model_path, image_path)
