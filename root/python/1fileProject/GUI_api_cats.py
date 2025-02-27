import customtkinter as ctk
import requests
from PIL import Image, ImageTk
from io import BytesIO

def display_cat(cat_url, label):
    # Завантаження зображення
    response = requests.get(cat_url)
    if response.status_code != 200: return

    img_data = response.content

    photo = ImageTk.PhotoImage(
        Image.open(BytesIO(img_data)).resize((300, 300), 
        Image.Resampling.LANCZOS))

    # Оновлення зображення в Label
    label.configure(image=photo)
    label.image = photo


# Функція для завантаження посилвння кота
def get_url_cat():
    # Отримання даних з API
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    
    if response.status_code != 200: return

    cat_data = response.json()[0]
    cat_url = cat_data['url']
    return cat_url
    
def display():
    display_cat(get_url_cat(), image_label)


# Створення головного вікна
root = ctk.CTk()
root.geometry("300x350")
root.title("Random Cat Viewer")

# Розміщення кнопки
btn = ctk.CTkButton(root, text="Show Random Cat", command=display)
btn.pack(pady=20)

# Розміщення Label для відображення зображення
image_label = ctk.CTkLabel(root, text='')
image_label.pack(pady=20)

display()

# Запуск головного циклу
root.mainloop()
