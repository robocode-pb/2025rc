import tkinter as tk
from tkinter import colorchooser

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Простой графический редактор")
        
        self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.color = "black"
        self.brush_size = 5

        self.canvas.bind("<B1-Motion>", self.paint)
        
        self.create_ui()

    def create_ui(self):
        frame = tk.Frame(self.root)
        frame.pack(side=tk.BOTTOM, fill=tk.X)
        
        tk.Button(frame, text="Цвет", command=self.choose_color).pack(side=tk.LEFT)
        tk.Button(frame, text="+", command=self.increase_brush).pack(side=tk.LEFT)
        tk.Button(frame, text="-", command=self.decrease_brush).pack(side=tk.LEFT)
        tk.Button(frame, text="Очистить", command=self.clear_canvas).pack(side=tk.LEFT)

    def paint(self, event):
        x1, y1 = event.x - self.brush_size, event.y - self.brush_size
        x2, y2 = event.x + self.brush_size, event.y + self.brush_size
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)

    def choose_color(self):
        self.color = colorchooser.askcolor(color=self.color)[1]

    def increase_brush(self):
        self.brush_size += 2

    def decrease_brush(self):
        if self.brush_size > 2:
            self.brush_size -= 2

    def clear_canvas(self):
        self.canvas.delete("all")

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
