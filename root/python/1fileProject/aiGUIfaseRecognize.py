'''
python -m venv venv
venv/Scripts/activate.bat
pip install deepface tf-keras tk customtkinter pyinstaller
pyinstaller --onefile --noconsole aiGUIfaseRecognize.py
rmdir  C:\Users\user\.deepface\weights
'''
import customtkinter as tk
from customtkinter import filedialog
from PIL import Image, ImageTk
from deepface import DeepFace
from json import dumps

def load_img(title, label):
    file_path = filedialog.askopenfilename(title=f"Вибір {title} зображення", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    if not file_path: return None
    print(file_path)

    img = Image.open(file_path)
    img = img.resize((100, 100))
    img_tk = ImageTk.PhotoImage(img)
    label.configure(image=img_tk)
    label.image = img_tk

    return file_path


def load_image1():
    global img1_path, label_img1
    img1_path = load_img(1, label_img1)

def load_image2():
    global img2_path, label_img2
    img2_path = load_img(2, label_img2)

def recognize():
    global img1_path, img2_path, result_label
    print(img1_path, img2_path)
    if img1_path and img2_path:
        try:
            res = DeepFace.verify(img1_path, img2_path)
            print(dumps(res, indent=4))
            if res["verified"]:
                result_label.configure(text= 'Розпiзнано, це одна людина (напевно)')
            else:
                result_label.configure(text= 'Розпiзнано, це не одна людина (напевно)')
        except Exception as e:
            result_label.configure(text= 'Не розпiзнано')
            print(f'Виключення: {e}')


root = tk.CTk()
root.title("Face Recognition App")
root.geometry("400x400")

button1 = tk.CTkButton(root, text="Вибрати 1 зображення", command=load_image1)
button1.pack(pady=5)

button2 = tk.CTkButton(root, text="Вибрати 2 зображення", command=load_image2)
button2.pack(pady=5)

батон = tk.CTkButton(root, text="Розпiзнати", command=recognize)
батон.pack(pady=5)


result_label = tk.CTkLabel(root)
result_label.configure(text='Додайте зображення потiм натиснiть кнопку розпiзнати')
result_label.pack(pady=5)

label_img1 = tk.CTkLabel(root)
label_img1.configure(text=' ')
label_img1.pack(pady=5)

label_img2 = tk.CTkLabel(root)
label_img2.configure(text=' ')
label_img2.pack(pady=5)

img1_path = None
img2_path = None

root.mainloop()
