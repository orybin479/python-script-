import platform
import psutil

def get_system_info():
    system_info = {}
    system_info["OS"] = platform.system()
    system_info["OS Version"] = platform.release()
    system_info["Processor"] = platform.processor()
    system_info["Architecture"] = platform.machine()
    system_info["RAM (Total)"] = f"{round(psutil.virtual_memory().total / (1024**3), 2)} GB"
    return system_info

def get_cpu_info():
    cpu_info = {}
    cpu_info["CPU Usage (%)"] = psutil.cpu_percent(interval=1)
    cpu_info["CPU Cores"] = psutil.cpu_count(logical=False)
    cpu_info["CPU Threads"] = psutil.cpu_count(logical=True)
    return cpu_info

def get_memory_info():
    memory_info = {}
    mem = psutil.virtual_memory()
    memory_info["Total Memory"] = f"{round(mem.total / (1024**3), 2)} GB"
    memory_info["Used Memory"] = f"{round(mem.used / (1024**3), 2)} GB"
    memory_info["Free Memory"] = f"{round(mem.free / (1024**3), 2)} GB"
    memory_info["Memory Usage (%)"] = mem.percent
    return memory_info

def get_disk_info():
    disk_info = {}
    partitions = psutil.disk_partitions()
    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        disk_info[partition.device] = {
            "Total Space": f"{round(usage.total / (1024**3), 2)} GB",
            "Used Space": f"{round(usage.used / (1024**3), 2)} GB",
            "Free Space": f"{round(usage.free / (1024**3), 2)} GB",
            "Usage (%)": usage.percent
        }
    return disk_info

if __name__ == "__main__":
    system_info = get_system_info()
    cpu_info = get_cpu_info()
    memory_info = get_memory_info()
    disk_info = get_disk_info()

    print("System Health Check:")
    print("====================================")
    print("System Information:")
    for key, value in system_info.items():
        print(f"{key}: {value}")

    print("\nCPU Information:")
    for key, value in cpu_info.items():
        print(f"{key}: {value}")

    print("\nMemory Information:")
    for key, value in memory_info.items():
        print(f"{key}: {value}")

    print("\nDisk Information:")
    for partition, info in disk_info.items():
        print(f"Partition: {partition}")
        for key, value in info.items():
            print(f"  {key}: {value}")
