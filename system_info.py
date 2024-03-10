# system_info.py

import psutil
from tabulate import tabulate

class SystemInfo:
    @staticmethod
    def get_disk_info():
        """Returns disk partitions along with their usage in a list of tuples."""
        partitions = psutil.disk_partitions()
        disk_info = []
        for partition in partitions:
            usage = psutil.disk_usage(partition.mountpoint)
            total_gb = usage.total / (1024 ** 3)
            used_gb = usage.used / (1024 ** 3)
            free_gb = usage.free / (1024 ** 3)
            disk_info.append((partition.device, partition.mountpoint, partition.fstype, f"{total_gb:.2f} GB", f"{used_gb:.2f} GB", f"{free_gb:.2f} GB"))
        return disk_info

    @staticmethod
    def get_cpu_info():
        """Returns the number of CPU cores."""
        return psutil.cpu_count(logical=False), psutil.cpu_count(logical=True)

    @staticmethod
    def get_ram_info():
        """Returns total and available RAM."""
        ram = psutil.virtual_memory()
        return ram.total, ram.available

    @staticmethod
    def generate_report():
        """Generates a report in tabular format."""
        disk_info = SystemInfo.get_disk_info()
        cpu_physical, cpu_logical = SystemInfo.get_cpu_info()
        ram_total, ram_available = SystemInfo.get_ram_info()
        
        headers = ["Device", "Mountpoint", "Type", "Total", "Used", "Free"]
        disk_table = tabulate(disk_info, headers=headers, tablefmt="grid")
        
        cpu_info = f"Physical cores: {cpu_physical}, Logical cores: {cpu_logical}"
        ram_info = f"Total RAM: {ram_total / (1024 ** 3):.2f} GB, Available RAM: {ram_available / (1024 ** 3):.2f} GB"
        
        return disk_table + "\n\n" + cpu_info + "\n" + ram_info
