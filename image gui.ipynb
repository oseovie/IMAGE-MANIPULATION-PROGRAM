import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk


# Image manipulation functions

def to_grayscale(image):
    return np.mean(image[:, :, :3], axis=2)


def adjust_brightness(image, factor):
    return np.clip(image * factor, 0, 1)


def flip_image(image, direction='horizontal'):
    return np.fliplr(image) if direction == 'horizontal' else np.flipud(image)


def add_tint(image, color='red'):
    tinted = image.copy()
    if color == 'red':
        tinted[:, :, 0] = np.clip(tinted[:, :, 0] * 1.4, 0, 1)
    elif color == 'green':
        tinted[:, :, 1] = np.clip(tinted[:, :, 1] * 1.4, 0, 1)
    elif color == 'blue':
        tinted[:, :, 2] = np.clip(tinted[:, :, 2] * 1.4, 0, 1)
    return tinted



# MAIN APP CLASS

class ModernImageEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("🖼️ Modern Image Editor")
        self.root.geometry("900x600")
        self.root.configure(bg="#2a2d2e")   # dark background

        self.image = None
        self.original = None

        
        # Sidebar (left panel)
        
        self.sidebar = Frame(root, bg="#1e1f22", width=200)
        self.sidebar.pack(side=LEFT, fill=Y)

        Label(
            self.sidebar, text="Tools", bg="#1e1f22", fg="white",
            font=("Segoe UI", 14, "bold"), pady=20
        ).pack()

        
        # Modern styled buttons
        
        def add_button(text, cmd):
            return Button(
                self.sidebar,
                text=text,
                command=cmd,
                bg="#3a3f44",
                fg="white",
                activebackground="#4a4f55",
                relief="flat",
                bd=0,
                padx=10,
                pady=8,
                font=("Segoe UI", 10, "bold"),
                width=18
            )

        add_button("Open Image", self.load_image).pack(pady=5)
        add_button("Save Image", self.save_image).pack(pady=5)
        add_button("Reset", self.reset_image).pack(pady=5)
        add_button("Grayscale", self.apply_grayscale).pack(pady=5)
        add_button("Flip Horizontal", lambda: self.apply_flip("horizontal")).pack(pady=5)
        add_button("Flip Vertical", lambda: self.apply_flip("vertical")).pack(pady=5)
        add_button("Brighter", lambda: self.apply_brightness(1.2)).pack(pady=5)
        add_button("Darker", lambda: self.apply_brightness(0.8)).pack(pady=5)
        add_button("Red Tint", lambda: self.apply_tint("red")).pack(pady=5)
        add_button("Green Tint", lambda: self.apply_tint("green")).pack(pady=5)
        add_button("Blue Tint", lambda: self.apply_tint("blue")).pack(pady=5)

        
        # Image display frame (right panel)
       
        self.display_frame = Frame(root, bg="#2a2d2e")
        self.display_frame.pack(side=RIGHT, fill=BOTH, expand=True)

        self.image_container = Frame(
            self.display_frame, bg="white",
            bd=3, relief="ridge"
        )
        self.image_container.pack(pady=20)

        self.img_label = Label(self.image_container, bg="white")
        self.img_label.pack()

    
    # Core functions
    
    def load_image(self):
        path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
        )
        if not path:
            return

        self.image = mpimg.imread(path).astype("float32")
        if self.image.max() > 1:
            self.image = self.image / 255.0

        self.original = self.image.copy()
        self.display_image()
        messagebox.showinfo("Loaded", "Image loaded successfully!")

    def save_image(self):
        if self.image is None:
            return

        path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")]
        )
        if path:
            img_to_save = (self.image * 255).astype("uint8")
            mpimg.imsave(path, img_to_save)
            messagebox.showinfo("Saved", "Image saved successfully!")

    def reset_image(self):
        if self.original is None:
            return
        self.image = self.original.copy()
        self.display_image()

    def apply_grayscale(self):
        if self.image is None:
            return
        self.image = to_grayscale(self.image)
        self.display_image(grayscale=True)

    def apply_flip(self, direction):
        if self.image is None:
            return
        self.image = flip_image(self.image, direction)
        self.display_image()

    def apply_brightness(self, factor):
        if self.image is None:
            return
        self.image = adjust_brightness(self.image, factor)
        self.display_image()

    def apply_tint(self, color):
        if self.image is None:
            return
        self.image = add_tint(self.image, color)
        self.display_image()

    
    # Display image
    
    def display_image(self, grayscale=False):
        plt.imsave("temp.png", self.image, cmap="gray" if grayscale else None)

        img = Image.open("temp.png")
        img.thumbnail((550, 500))

        img_tk = ImageTk.PhotoImage(img)
        self.img_label.configure(image=img_tk)
        self.img_label.image = img_tk



# Run App

root = Tk()
app = ModernImageEditor(root)
root.mainloop()
