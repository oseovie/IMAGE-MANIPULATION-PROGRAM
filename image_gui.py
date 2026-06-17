import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, simpledialog

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageOps, ImageTk


IMAGE_TYPES = [
    ("Image files", "*.jpg *.jpeg *.png *.bmp *.gif *.webp"),
    ("All files", "*.*"),
]


class ModernImageEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Image Editor")
        self.root.geometry("1000x680")
        self.root.minsize(820, 560)
        self.root.configure(bg="#25282b")

        self.image = None
        self.original = None
        self.preview = None
        self.current_path = None
        self.undo_stack = []
        self.redo_stack = []
        self.tool_buttons = []

        self._build_layout()
        self._set_tools_state(tk.DISABLED)
        self._set_status("Open an image to start editing.")

    def _build_layout(self):
        self.sidebar = tk.Frame(self.root, bg="#191b1f", width=220)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
        self.sidebar.pack_propagate(False)

        tk.Label(
            self.sidebar,
            text="Image Editor",
            bg="#191b1f",
            fg="#f4f6f8",
            font=("Segoe UI", 16, "bold"),
            pady=18,
        ).pack(fill=tk.X)

        self._add_button("Open Image", self.load_image).pack(fill=tk.X, padx=18, pady=(0, 8))
        self._add_button("Prompt Edit", self.prompt_edit, managed=True).pack(fill=tk.X, padx=18, pady=4)
        self._add_button("Save As", self.save_image, managed=True).pack(fill=tk.X, padx=18, pady=4)

        self._add_separator()
        self._add_button("Undo", self.undo, managed=True).pack(fill=tk.X, padx=18, pady=4)
        self._add_button("Redo", self.redo, managed=True).pack(fill=tk.X, padx=18, pady=4)
        self._add_button("Reset", self.reset_image, managed=True).pack(fill=tk.X, padx=18, pady=4)

        self._add_separator()
        self._add_button("Grayscale", self.apply_grayscale, managed=True).pack(fill=tk.X, padx=18, pady=4)
        self._add_button("Rotate Left", lambda: self.apply_rotate(90), managed=True).pack(fill=tk.X, padx=18, pady=4)
        self._add_button("Rotate Right", lambda: self.apply_rotate(-90), managed=True).pack(fill=tk.X, padx=18, pady=4)
        self._add_button("Flip Horizontal", lambda: self.apply_flip("horizontal"), managed=True).pack(fill=tk.X, padx=18, pady=4)
        self._add_button("Flip Vertical", lambda: self.apply_flip("vertical"), managed=True).pack(fill=tk.X, padx=18, pady=4)

        self._add_separator()
        self._add_button("Brighter", lambda: self.apply_enhancement("brightness", 1.2), managed=True).pack(fill=tk.X, padx=18, pady=4)
        self._add_button("Darker", lambda: self.apply_enhancement("brightness", 0.8), managed=True).pack(fill=tk.X, padx=18, pady=4)
        self._add_button("More Contrast", lambda: self.apply_enhancement("contrast", 1.2), managed=True).pack(fill=tk.X, padx=18, pady=4)
        self._add_button("Less Contrast", lambda: self.apply_enhancement("contrast", 0.8), managed=True).pack(fill=tk.X, padx=18, pady=4)
        self._add_button("Auto Contrast", self.apply_auto_contrast, managed=True).pack(fill=tk.X, padx=18, pady=4)

        self._add_separator()
        self._add_button("Red Tint", lambda: self.apply_tint("red"), managed=True).pack(fill=tk.X, padx=18, pady=4)
        self._add_button("Green Tint", lambda: self.apply_tint("green"), managed=True).pack(fill=tk.X, padx=18, pady=4)
        self._add_button("Blue Tint", lambda: self.apply_tint("blue"), managed=True).pack(fill=tk.X, padx=18, pady=4)

        self._add_separator()
        self._add_button("Clarity", self.apply_clarity, managed=True).pack(fill=tk.X, padx=18, pady=4)
        self._add_button("Sharpen", self.apply_sharpen, managed=True).pack(fill=tk.X, padx=18, pady=4)
        self._add_button("Blur Background", self.blur_background, managed=True).pack(fill=tk.X, padx=18, pady=4)
        self._add_button("Blur", self.apply_blur, managed=True).pack(fill=tk.X, padx=18, pady=4)
        self._add_button("Resize", self.resize_image, managed=True).pack(fill=tk.X, padx=18, pady=4)

        self.content = tk.Frame(self.root, bg="#25282b")
        self.content.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(
            self.content,
            bg="#303438",
            highlightthickness=0,
            bd=0,
        )
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=18, pady=(18, 8))
        self.canvas.bind("<Configure>", lambda _event: self.display_image())

        self.status_var = tk.StringVar()
        self.status_bar = tk.Label(
            self.content,
            textvariable=self.status_var,
            anchor="w",
            bg="#1f2226",
            fg="#dbe1e6",
            padx=12,
            pady=8,
            font=("Segoe UI", 10),
        )
        self.status_bar.pack(fill=tk.X, padx=18, pady=(0, 18))

    def _add_button(self, text, command, managed=False):
        button = tk.Button(
            self.sidebar,
            text=text,
            command=command,
            bg="#353a40",
            fg="#f7f9fb",
            activebackground="#4c535b",
            activeforeground="#ffffff",
            disabledforeground="#8c949c",
            relief=tk.FLAT,
            bd=0,
            padx=12,
            pady=8,
            font=("Segoe UI", 10, "bold"),
            cursor="hand2",
        )
        if managed:
            self.tool_buttons.append(button)
        return button

    def _add_separator(self):
        tk.Frame(self.sidebar, height=1, bg="#30343a").pack(fill=tk.X, padx=18, pady=10)

    def _set_status(self, message):
        self.status_var.set(message)

    def _set_tools_state(self, state):
        for button in self.tool_buttons:
            button.configure(state=state)

    def _require_image(self):
        if self.image is None:
            messagebox.showwarning("No Image", "Open an image before using this tool.")
            return False
        return True

    def _push_history(self):
        if self.image is None:
            return
        self.undo_stack.append(self.image.copy())
        self.redo_stack.clear()

    def load_image(self):
        path = filedialog.askopenfilename(filetypes=IMAGE_TYPES)
        if not path:
            return

        try:
            loaded = Image.open(path)
            self.image = ImageOps.exif_transpose(loaded).convert("RGBA")
        except OSError as error:
            messagebox.showerror("Open Failed", f"Could not open that image.\n\n{error}")
            return

        self.original = self.image.copy()
        self.current_path = Path(path)
        self.undo_stack.clear()
        self.redo_stack.clear()
        self._set_tools_state(tk.NORMAL)
        self.display_image()
        self._set_status(f"Loaded {self.current_path.name} - {self.image.width} x {self.image.height}px")

    def save_image(self):
        if not self._require_image():
            return

        path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[
                ("PNG image", "*.png"),
                ("JPEG image", "*.jpg *.jpeg"),
                ("BMP image", "*.bmp"),
                ("WEBP image", "*.webp"),
            ],
        )
        if not path:
            return

        try:
            image_to_save = self.image
            suffix = Path(path).suffix.lower()
            if suffix in {".jpg", ".jpeg", ".bmp"}:
                image_to_save = self.image.convert("RGB")
            image_to_save.save(path)
        except OSError as error:
            messagebox.showerror("Save Failed", f"Could not save the image.\n\n{error}")
            return

        self._set_status(f"Saved {Path(path).name}")
        messagebox.showinfo("Saved", "Image saved successfully.")

    def reset_image(self):
        if not self._require_image() or self.original is None:
            return
        self._push_history()
        self.image = self.original.copy()
        self.display_image()
        self._set_status("Image reset to the original.")

    def undo(self):
        if not self.undo_stack:
            self._set_status("Nothing to undo.")
            return
        self.redo_stack.append(self.image.copy())
        self.image = self.undo_stack.pop()
        self.display_image()
        self._set_status("Undid the last edit.")

    def redo(self):
        if not self.redo_stack:
            self._set_status("Nothing to redo.")
            return
        self.undo_stack.append(self.image.copy())
        self.image = self.redo_stack.pop()
        self.display_image()
        self._set_status("Redid the last edit.")

    def apply_grayscale(self):
        if not self._require_image():
            return
        self._push_history()
        alpha = self.image.getchannel("A")
        self.image = ImageOps.grayscale(self.image).convert("RGBA")
        self.image.putalpha(alpha)
        self.display_image()
        self._set_status("Applied grayscale.")

    def apply_rotate(self, degrees):
        if not self._require_image():
            return
        self._push_history()
        self.image = self.image.rotate(degrees, expand=True)
        self.display_image()
        self._set_status("Rotated image.")

    def apply_flip(self, direction):
        if not self._require_image():
            return
        self._push_history()
        method = Image.Transpose.FLIP_LEFT_RIGHT if direction == "horizontal" else Image.Transpose.FLIP_TOP_BOTTOM
        self.image = self.image.transpose(method)
        self.display_image()
        self._set_status(f"Flipped {direction}.")

    def apply_enhancement(self, kind, factor):
        if not self._require_image():
            return
        self._push_history()
        enhancer_class = ImageEnhance.Brightness if kind == "brightness" else ImageEnhance.Contrast
        self.image = enhancer_class(self.image).enhance(factor)
        self.display_image()
        self._set_status(f"Adjusted {kind}.")

    def apply_auto_contrast(self):
        if not self._require_image():
            return

        self._push_history()
        alpha = self.image.getchannel("A")
        enhanced = ImageOps.autocontrast(self.image.convert("RGB"), cutoff=1).convert("RGBA")
        enhanced.putalpha(alpha)
        self.image = enhanced
        self.display_image()
        self._set_status("Applied auto contrast.")

    def apply_clarity(self):
        if not self._require_image():
            return

        self._push_history()
        self.image = self.image.filter(
            ImageFilter.UnsharpMask(radius=2, percent=165, threshold=3)
        )
        self.display_image()
        self._set_status("Improved image clarity.")

    def apply_tint(self, color):
        if not self._require_image():
            return

        tint_colors = {
            "red": (255, 70, 70),
            "green": (70, 210, 110),
            "blue": (70, 130, 255),
        }
        self._push_history()
        alpha = self.image.getchannel("A")
        base = self.image.convert("RGB")
        overlay = Image.new("RGB", self.image.size, tint_colors[color])
        tinted = Image.blend(base, overlay, 0.22).convert("RGBA")
        tinted.putalpha(alpha)
        self.image = tinted
        self.display_image()
        self._set_status(f"Applied {color} tint.")

    def apply_sharpen(self):
        if not self._require_image():
            return
        self._push_history()
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.display_image()
        self._set_status("Sharpened image.")

    def apply_blur(self):
        if not self._require_image():
            return
        self._push_history()
        self.image = self.image.filter(ImageFilter.GaussianBlur(radius=1.5))
        self.display_image()
        self._set_status("Blurred image.")

    def blur_background(self):
        if not self._require_image():
            return

        self._push_history()
        self.image = self._make_background_blur(self.image)
        self.display_image()
        self._set_status("Blurred the background with a soft center subject mask.")

    def _make_background_blur(self, image):
        blurred = image.filter(ImageFilter.GaussianBlur(radius=8))
        width, height = image.size
        mask = Image.new("L", image.size, 0)
        mask_box = (
            int(width * 0.18),
            int(height * 0.12),
            int(width * 0.82),
            int(height * 0.90),
        )
        mask_draw = Image.new("L", image.size, 0)
        draw = ImageDraw.Draw(mask_draw)
        draw.ellipse(mask_box, fill=255)
        mask = mask_draw.filter(ImageFilter.GaussianBlur(radius=max(18, min(width, height) // 18)))
        return Image.composite(image, blurred, mask)

    def prompt_edit(self):
        if not self._require_image():
            return

        prompt = simpledialog.askstring(
            "Prompt Edit",
            "Tell the editor what to do:",
            parent=self.root,
        )
        if not prompt:
            return

        self.apply_prompt_command(prompt)

    def apply_prompt_command(self, prompt):
        command = prompt.lower().strip()

        if any(word in command for word in ("background", "backdrop")) and "blur" in command:
            self.blur_background()
        elif any(word in command for word in ("clear", "clarity", "enhance", "sharp")):
            self.apply_clarity()
        elif "auto" in command and "contrast" in command:
            self.apply_auto_contrast()
        elif "contrast" in command:
            factor = 0.8 if any(word in command for word in ("less", "reduce", "lower")) else 1.2
            self.apply_enhancement("contrast", factor)
        elif any(word in command for word in ("bright", "light", "lighter")):
            self.apply_enhancement("brightness", 1.2)
        elif any(word in command for word in ("dark", "darker", "dim")):
            self.apply_enhancement("brightness", 0.8)
        elif any(word in command for word in ("gray", "grey", "black and white", "monochrome")):
            self.apply_grayscale()
        elif "rotate" in command and "left" in command:
            self.apply_rotate(90)
        elif "rotate" in command and "right" in command:
            self.apply_rotate(-90)
        elif "flip" in command and any(word in command for word in ("vertical", "up", "down")):
            self.apply_flip("vertical")
        elif "flip" in command:
            self.apply_flip("horizontal")
        elif "blur" in command:
            self.apply_blur()
        elif "red" in command and "tint" in command:
            self.apply_tint("red")
        elif "green" in command and "tint" in command:
            self.apply_tint("green")
        elif "blue" in command and "tint" in command:
            self.apply_tint("blue")
        else:
            messagebox.showinfo(
                "Prompt Not Understood",
                "Try prompts like: make it clearer, blur background, brighten image, rotate left, or make grayscale.",
            )
            self._set_status("Prompt was not recognized.")

    def resize_image(self):
        if not self._require_image():
            return

        width = simpledialog.askinteger(
            "Resize Image",
            "New width:",
            initialvalue=self.image.width,
            minvalue=1,
            parent=self.root,
        )
        if width is None:
            return

        height = simpledialog.askinteger(
            "Resize Image",
            "New height:",
            initialvalue=self.image.height,
            minvalue=1,
            parent=self.root,
        )
        if height is None:
            return

        self._push_history()
        self.image = self.image.resize((width, height), Image.Resampling.LANCZOS)
        self.display_image()
        self._set_status(f"Resized to {width} x {height}px.")

    def display_image(self):
        self.canvas.delete("all")

        if self.image is None:
            width = max(self.canvas.winfo_width(), 1)
            height = max(self.canvas.winfo_height(), 1)
            self.canvas.create_text(
                width // 2,
                height // 2,
                text="No image loaded",
                fill="#dbe1e6",
                font=("Segoe UI", 18, "bold"),
            )
            return

        canvas_width = max(self.canvas.winfo_width() - 40, 1)
        canvas_height = max(self.canvas.winfo_height() - 40, 1)
        preview = self.image.copy()
        preview.thumbnail((canvas_width, canvas_height), Image.Resampling.LANCZOS)

        self.preview = ImageTk.PhotoImage(preview)
        x = max(self.canvas.winfo_width() // 2, 1)
        y = max(self.canvas.winfo_height() // 2, 1)
        self.canvas.create_image(x, y, image=self.preview, anchor=tk.CENTER)


def main():
    root = tk.Tk()
    app = ModernImageEditor(root)
    root.mainloop()


if __name__ == "__main__":
    main()
