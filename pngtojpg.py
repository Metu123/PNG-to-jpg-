from PIL import Image
import os

def png_to_jpg():
    png_path = input("Enter the path to the PNG file: ").strip()

    if not os.path.exists(png_path) or not png_path.lower().endswith(".png"):
        print("Invalid PNG file path.")
        return

    try:
        img = Image.open(png_path)
        rgb_img = img.convert("RGB")

        directory = os.path.dirname(png_path)
        base_name = os.path.splitext(os.path.basename(png_path))[0]
        jpg_path = os.path.join(directory, base_name + ".jpg")

        rgb_img.save(jpg_path, "JPEG")
        print(f"Converted image saved as: {jpg_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    png_to_jpg()