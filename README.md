# Image Manipulation Program

A Python desktop image editor evolving toward a Remini + Snapseed + Lightroom style AI editor. The current runnable app is still `image_gui.py`, while the new `ai_image_editor/` package contains the professional architecture for filters, transforms, enhancement, AI model integrations, background tools, object tools, batch processing, export, API, and metadata.

## Run Current App

```bash
python image_gui.py
```

You can also use the new app entry point:

```bash
python app.py
```

## Current Working Features

- Open PNG, JPEG, BMP, GIF, and WEBP images
- Save as PNG, JPEG, BMP, or WEBP
- Undo, redo, and reset to the original image
- Grayscale conversion
- Rotate left and right
- Flip horizontally or vertically
- Brightness and contrast adjustments
- Auto contrast and clarity enhancement
- Background blur with a soft subject mask
- Prompt-based editing for common commands
- Red, green, and blue tint effects
- Sharpen, blur, and resize
- Responsive preview area with a status bar

## New Architecture

```text
ai_image_editor/
  app.py
  assets/
  gui/
  core/
  filters/
  transform/
  enhancement/
  ai/
  face_tools/
  background_tools/
  object_tools/
  effects/
  batch/
  export/
  api/
  database/
  utils/
```

## AI Roadmap

The AI folders are scaffolded but do not yet ship model weights. Heavyweight features such as Real-ESRGAN, SwinIR, GFPGAN, CodeFormer, Restormer, Zero-DCE, DeOldify, Segment Anything, YOLO, and LaMa need their dependencies and model files added before inference can run.

## Setup

Install the normal app dependencies:

```bash
python -m pip install -r requirements.txt
```

Optional AI dependencies are listed in `requirements-ai.txt` as comments so they do not accidentally install large packages.

## Windows Executable

Windows users can run the packaged app without installing Python:

```text
dist/ImageEditor.exe
```

The `.exe` has not been rebuilt for the newest source-only changes unless you run PyInstaller again.

To rebuild the executable from source:

```bash
python -m pip install pyinstaller
python -m PyInstaller --onefile --windowed --name ImageEditor image_gui.py
```
