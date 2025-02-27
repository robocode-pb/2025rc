import tkinter as tk
from tkinter import filedialog, Button, Canvas, Label
from PIL import Image, ImageTk
import cv2
import numpy as np
import tensorflow as tf
from PIL import ImageDraw

# Завантаження моделі
model = tf.keras.models.load_model("myModel.keras")

def process_image(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Перетворення в чорно-біле
    img = cv2.resize(img, (28, 28))  # Зміна розміру
    img = img / 255.0  # Нормалізація
    img = np.expand_dims(img, axis=(0, -1))  # Додаємо batch dimension і канал
    prediction = model.predict(img)
    result_label.config(text=f"Prediction: {np.argmax(prediction)}")

def clear_canvas():
    canvas.delete("all")
    canvas.image = None  # Видаляємо зображення

def load_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not file_path: return
    
    img = Image.open(file_path)
    img = img.resize((200, 200))
    img_tk = ImageTk.PhotoImage(img)

    # Очищаємо канвас і вставляємо зображення
    canvas.delete("all")
    canvas.image = img_tk  # Зберігаємо посилання, щоб зображення не зникло
    canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
    predict_canvas()
    
    # Обробка та передбачення
    image_cv = cv2.imread(file_path)
    process_image(image_cv)

def start_paint(event):
    canvas.old_x, canvas.old_y = event.x, event.y

def paint(event):
    x, y = event.x, event.y
    canvas.create_line(canvas.old_x, canvas.old_y, x, y, width=10, fill='black', capstyle=tk.ROUND, smooth=tk.TRUE)
    canvas.old_x, canvas.old_y = x, y

def predict_canvas():
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    
    # Створення білого зображення
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    for item in canvas.find_all():
        if canvas.type(item) == "line":  # Перевіряємо, чи це лінія
            coords = canvas.coords(item)
            fill = canvas.itemcget(item, "fill")  # Отримуємо колір лінії
            draw.line(coords, fill=fill, width=10)

    image = image.convert("L")  # Градації сірого
    image = image.resize((28, 28))
    image = np.array(image)
    image = np.invert(image)  # Інвертування кольорів для моделі
    process_image(cv2.cvtColor(image, cv2.COLOR_GRAY2BGR))


# Інтерфейс Tkinter
root = tk.Tk()
root.title("Image Classifier")
root.geometry("300x330")

btn_load = Button(root, text="Load Image", command=load_image)
btn_load.pack()

canvas = Canvas(root, width=200, height=200, bg="white")
canvas.pack()
canvas.bind("<Button-1>", start_paint)
canvas.bind("<B1-Motion>", paint)

btn_clear = Button(root, text="Clear", command=clear_canvas)
btn_clear.pack()
btn_predict = Button(root, text="Predict Drawing", command=predict_canvas)
btn_predict.pack()

result_label = Label(root, text="Prediction: ")
result_label.pack()

root.mainloop()
