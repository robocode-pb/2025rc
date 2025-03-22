import cv2 as cv
import tkinter as tk
from tkinter import Label, Checkbutton
from PIL import Image, ImageTk
from deepface import DeepFace  # Import DeepFace for face recognition

cap = cv.VideoCapture(0)

root = tk.Tk()
root.title("Live Camera Feed")

# Initialize checkbox variables
ch_ai_var = tk.IntVar()
chdf_ai_var = tk.IntVar()
ch_video_var = tk.IntVar()

# Create the checkboxes and link them to the variables
ch_video = Checkbutton(root, text='Захоплювати відео', variable=ch_video_var)
ch_video.pack() 

ch_ai = Checkbutton(root, text='Розпізнавати лице', variable=ch_ai_var)
ch_ai.pack() 

chdf_ai = Checkbutton(root, text='Розпізнавати людину', variable=chdf_ai_var)
chdf_ai.pack() 

label = Label(root)
label.pack()

# Load OpenCV's pre-trained face detector
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

def update_frame():
    # if ch_video_var.get(): 
    #     return
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        cap.release()
        cv.destroyAllWindows()
        return

    frame = cv.flip(frame, 1)  # Flip the frame horizontally

    # Convert the frame to grayscale for face detection
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    if ch_ai_var.get(): 
        # Detect faces in the image
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw rectangle
    if chdf_ai_var.get():  # Check if the "Розпізнавати людину" checkbox is checked
        try:
            # Perform face recognition (DeepFace emotion recognition)
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

            # Annotate the frame with the result and draw rectangles
            for face in result:
                for key, value in face.items():
                    if key == "dominant_emotion":
                        emotion = value
                        cv.putText(frame, emotion, (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        except Exception as e:
            print("Error during face recognition:", e)

    frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    img = Image.fromarray(frame_rgb)
    img_tk = ImageTk.PhotoImage(image=img)

    label.img_tk = img_tk
    label.config(image=img_tk)

    root.after(10, update_frame)

update_frame()
root.mainloop()

cap.release()
