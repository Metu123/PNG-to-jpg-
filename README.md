PNG to JPG Converter (Python Script)

Overview

This script is a simple command-line utility that converts PNG images to JPG format using the Python Imaging Library (Pillow). It supports both single-file conversion and batch conversion of all PNG files inside a directory (including subdirectories).

It also handles PNG transparency by automatically adding a white background before converting to JPEG, since JPEG does not support transparency.


---

Features

Convert a single PNG file to JPG

Convert all PNG files inside a folder recursively

Handles transparent PNG images (RGBA / LA modes)

Allows user-defined JPEG quality (1–100)

Safe file validation and error handling

Preserves original filenames while changing extension to .jpg



---

Requirements

Python 3.7+

Pillow library


Install dependencies:

pip install pillow


---

How It Works

1. Input Handling

The script accepts a path from the user:

If the path is a file:

It processes only that file if it is a .png


If the path is a directory:

It searches recursively for all .png files


If the path is invalid:

It prints an error message and exits




---

2. Image Processing

For each PNG file found:

Transparency Handling

PNG images may contain transparency (alpha channel). Since JPEG does not support transparency, the script handles it like this:

If image mode is RGBA or LA:

A white background is created

The PNG is pasted onto it using the alpha channel as a mask


Otherwise:

The image is directly converted to RGB




---

3. Conversion

Each image is saved as a JPEG:

Output filename: same name as original, but .jpg extension

Format: JPEG

Options:

quality (user-defined, default 95)

optimize=True for smaller file size




---

4. Error Handling

The script safely handles:

Invalid file paths

Missing PNG files

Corrupted images

Unexpected processing errors per file


Each failure is printed without stopping the entire process.


---

Usage

Run the script:

python script.py

You will be prompted for:

1. Path input

Example:

Enter PNG file or folder path: /home/user/images

Or:

Enter PNG file or folder path: image.png


---

2. JPEG Quality

Example:

Enter JPEG quality (1-100, default 95): 85

If you press Enter without input, it defaults to 95.


---

Example Output

Converted: /home/user/images/photo1.jpg
Converted: /home/user/images/photo2.jpg
Failed: /home/user/images/broken.png -> cannot identify image file


---

Code Structure

Main Function

convert_png_to_jpg(input_path: str, quality: int = 95)

Handles:

Path validation

File discovery

Conversion loop



---

Entry Point

if __name__ == "__main__":

Handles:

User input

Quality parsing

Function execution



---

Key Design Decisions

1. Recursive directory scanning

Uses:

path.rglob("*.png")

This ensures all nested PNG files are included.


---

2. Transparency fix

JPEG does not support alpha channels, so the script replaces transparency with a white background instead of black or failure.


---

3. Safety-first conversion

Each file is wrapped in a try/except block so one corrupted image does not stop the process.


---

Limitations

Only supports PNG input

Output is always JPEG

Transparency is flattened to white background only

No parallel processing (sequential execution)



---

Possible Improvements

Add CLI arguments using argparse

Support output directory selection

Add parallel processing for large batches

Allow background color customization

Add PNG optimization before conversion



---

License

This script is free to use and modify for personal or commercial projects.
