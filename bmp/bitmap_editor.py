import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class BitmapEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Bitmap Editor")
        
        self.canvas = tk.Canvas(root, width=300, height=300, bg='white')
        self.canvas.grid(row=0, column=0, columnspan=4)
        
        self.canvas.bind("<Button-1>", self.toggle_pixel)

        self.load_button = tk.Button(root, text="Load Image", command=self.load_image)
        self.load_button.grid(row=1, column=0)
        
        self.save_button = tk.Button(root, text="Save Image", command=self.save_image)
        self.save_button.grid(row=1, column=1)
        
        self.image = Image.new("1", (30, 30), 1)
        self.photo = ImageTk.PhotoImage(self.image.resize((300, 300), Image.NEAREST))
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path).convert("1")
            self.update_canvas()

    def save_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".bmp", filetypes=[("Bitmap files", "*.bmp")])
        if file_path:
            self.image.save(file_path)

    def toggle_pixel(self, event):
        x, y = event.x // 10, event.y // 10
        if 0 <= x < 30 and 0 <= y < 30:  # Check if the click is within the image boundaries
            current_color = self.image.getpixel((x, y))
            new_color = 0 if current_color == 255 else 255
            self.image.putpixel((x, y), new_color)
            self.update_canvas()

    def update_canvas(self):
        self.photo = ImageTk.PhotoImage(self.image.resize((300, 300), Image.NEAREST))
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

if __name__ == "__main__":
    root = tk.Tk()
    app = BitmapEditor(root)
    root.mainloop()
