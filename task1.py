import random
import time
from itertools import count
from queue import Queue

# Створити чергу заявок
queue = Queue()

# Генератор унікальних номерів заявок
request_ids = count(1)

ISSUES = [
    "Не вмикається ноутбук",
    "Розбитий екран смартфона",
    "Не працює Wi-Fi",
    "Заміна батареї",
    "Встановлення ПЗ",
    "Чистка від пилу",
]


def generate_request():
    """Створює нову заявку та додає її до черги."""
    request = {"id": next(request_ids), "issue": random.choice(ISSUES)}
    queue.put(request)
    print(f"[+] Нова заявка #{request['id']}: {request['issue']} "
          f"(у черзі: {queue.qsize()})")


def process_request():
    """Видаляє заявку з черги та обробляє її."""
    if not queue.empty():
        request = queue.get()
        print(f"[-] Оброблено заявку #{request['id']}: {request['issue']} "
              f"(у черзі: {queue.qsize()})")
    else:
        print("[!] Черга пуста, заявок для обробки немає")


def main():
    """Генерує та обробляє заявки, доки користувач не вийде (Ctrl+C)."""
    print("Сервісний центр запущено. Для виходу натисніть Ctrl+C.\n")
    try:
        while True:
            # За один цикл надходить від 0 до 2 нових заявок
            for _ in range(random.randint(0, 2)):
                generate_request()
            process_request()
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\nРоботу завершено. Необроблених заявок у черзі: {queue.qsize()}")


if __name__ == "__main__":
    main()
