import psutil

def get_memory_info():
    memory = psutil.virtual_memory()
    total_memory = memory.total / (1024 ** 3)  # Chuyển đổi từ byte sang GB
    used_memory = memory.used / (1024 ** 3)    # Chuyển đổi từ byte sang GB
    memory_percentage = memory.percent
    return total_memory, used_memory, memory_percentage

def get_cpu_info():
    cpu_percentage = psutil.cpu_percent(interval=1)  # Đo trong 1 giây
    return cpu_percentage

if __name__ == '__main__':
    total_memory, used_memory, memory_percentage = get_memory_info()
    cpu_percentage = get_cpu_info()

    print(f'Tổng dung lượng RAM: {total_memory:.2f} GB')
    print(f'Dung lượng RAM đang sử dụng: {used_memory:.2f} GB')
    print(f'Phần trăm sử dụng RAM: {memory_percentage}%')
    print(f'Phần trăm sử dụng CPU: {cpu_percentage}%')
