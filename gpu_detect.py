import torch

def torch_detect():
    print("CUDA Available: ", torch.cuda.is_available())
    if torch.cuda.is_available():
        print("CUDA Version: ", torch.version.cuda)
        print("Number of GPUs: ", torch.cuda.device_count())
        for i in range(torch.cuda.device_count()):
            print(f"Device {i}: {torch.cuda.get_device_name(i)}")


    # Kiểm tra xem GPU có khả dụng không
    if torch.cuda.is_available():
        device = torch.device("cuda")  # hoặc torch.device("cuda:0") nếu bạn muốn chỉ định GPU cụ thể
        print("CUDA device is available.")
    else:
        device = torch.device("cpu")
        print("CUDA device is not available. Using CPU.")

def tf_detect():
    import tensorflow as tf
    print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))


torch_detect()