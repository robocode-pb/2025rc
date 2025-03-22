# pip install prettytable
import socket
import os
import ipaddress
import subprocess
from concurrent.futures import ThreadPoolExecutor
from prettytable import PrettyTable
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # записуємо початковий час
        result = func(*args, **kwargs)
        end_time = time.time()  # записуємо час після виконання функції
        print(f"Час виконання функції {func.__name__}: {end_time - start_time:.4f} секунд")
        return result
    return wrapper

def get_default_gateway():
    """Отримати IP-адресу шлюзу (роутера)"""
    if os.name == "nt":
        result = subprocess.run(["ipconfig"], capture_output=True, text=True)
        for line in result.stdout.split("\n"):
            if "Default Gateway" in line:
                return line.split(":")[-1].strip()
    else:
        import netifaces
        gws = netifaces.gateways()
        return gws['default'][netifaces.AF_INET][0]

def ping_device(ip):
    """Перевірити, чи пристрій доступний через пінг"""
    param = "-n" if os.name == "nt" else "-c"
    try:
        result = subprocess.run(["ping", param, "1", "-w", "500", ip], stdout=subprocess.DEVNULL)
        return result.returncode == 0  # 0 означає, що пристрій відповідає
    except Exception:
        return False

def is_port_open(ip, port=80, timeout=1):
    """Перевірити, чи відкритий порт"""
    try:
        with socket.create_connection((ip, port), timeout=timeout):
            return True
    except (socket.timeout, ConnectionRefusedError):
        return False

def get_device_name(ip):
    """Отримати ім'я пристрою (якщо можливо) через DNS"""
    try:
        hostname, _, _ = socket.gethostbyaddr(ip)
        return hostname
    except (socket.herror, socket.gaierror):
        return None  # Якщо ім'я не знайдено

def get_mac_address(ip):
    """Отримати MAC-адресу пристрою через ARP"""
    try:
        if os.name == "nt":
            # Використовуємо arp для Windows
            result = subprocess.run(["arp", "-a", ip], capture_output=True, text=True)
            for line in result.stdout.split("\n"):
                if ip in line:
                    return line.split()[3]
        else:
            # Для Linux використовуємо команду arp-scan (потрібно, щоб було встановлено)
            result = subprocess.run(["arp-scan", ip], capture_output=True, text=True)
            for line in result.stdout.split("\n"):
                if ip in line:
                    return line.split()[1]
    except Exception as e:
        pass
    return None

def scan_ip(ip):
    """Перевірити IP: спочатку пінг, потім порт"""
    device_replied = ping_device(ip)  # Пінгуємо пристрій

    if not device_replied:
        return None, False, None, None  # Пристрій не відповідає

    port_open = is_port_open(ip, 80)  # Перевіряємо порт 80
    device_name = get_device_name(ip)  # Отримуємо ім'я пристрою через DNS
    mac_address = get_mac_address(ip)  # Отримуємо MAC-адресу
    return ip, device_replied and port_open, device_name, mac_address

@timer
def scan_network():
    """Сканувати всі пристрої в мережі (багатопотоково)"""
    router_ip = get_default_gateway()
    if not router_ip:
        print("❌ Не вдалося знайти шлюз")
        return

    network = ipaddress.ip_network(router_ip + "/24", strict=False)
    open_ports = []
    replied_devices = []

    # Ініціалізація таблиці
    table = PrettyTable()
    table.field_names = ["IP Адреса", "Назва пристрою", "MAC Адреса", "Відкритий порт 80"]

    with ThreadPoolExecutor(max_workers=50) as executor:
        results = executor.map(scan_ip, (str(ip) for ip in network.hosts()))

    # Збираємо пристрої з відкритим портом 80 та ті, які відповіли на пінг
    for ip, is_open, device_name, mac_address in results:
        if ip:
            if is_open:
                table.add_row([ip, device_name if device_name else "Невідомо", mac_address if mac_address else "Невідомо", f"http://{ip}"])
                open_ports.append(ip)
            else:
                table.add_row([ip, device_name if device_name else "Невідомо", mac_address if mac_address else "Невідомо", "-"])
                replied_devices.append(ip)

    print(table)  # Вивести таблицю в консоль

    print(f"\n✅ Знайдено {len(open_ports)} пристроїв з відкритим портом 80")
    print(f"🔹 Загалом пристроїв, які відповіли на пінг: {len(replied_devices)}")


print('Пошук пристроїв в локальній мережі')
scan_network()
