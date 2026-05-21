# Image Manipulation Program

A desktop image editor built with Python, Tkinter, and Pillow. It can open common image formats, preview edits, and save the final result.

## Features

- Open PNG, JPEG, BMP, GIF, and WEBP images
- Save as PNG, JPEG, BMP, or WEBP
- Undo, redo, and reset to the original image
- Grayscale conversion
- Rotate left and right
- Flip horizontally or vertically
- Brightness and contrast adjustments
- Red, green, and blue tint effects
- Sharpen, blur, and resize
- Responsive preview area with a status bar

## Setup

Install the dependency:

```bash
python -m pip install -r requirements.txt
```

## Run

```bash
python image_gui.py
```

## Windows Executable

Windows users can run the packaged app without installing Python:

```text
dist/ImageEditor.exe
```

To rebuild the executable from source:

```bash
python -m pip install pyinstaller
python -m PyInstaller --onefile --windowed --name ImageEditor image_gui.py
```
