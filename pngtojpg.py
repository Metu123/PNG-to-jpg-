
from PIL import Image
from pathlib import Path


def convert_png_to_jpg(input_path: str, quality: int = 95):
    path = Path(input_path).expanduser().resolve()

    if not path.exists():
        print("this is not a path.")
        return

    files = []

    if path.is_file() and path.suffix.lower() == ".png":
        files.append(path)
    elif path.is_dir():
        files.extend(path.rglob("*.png"))
    else:
        print("put a png file or a directory.")
        return

    if not files:
        print(" No PNG found.")
        return

    for png_file in files:
        try:
            with Image.open(png_file) as img:
                # Handle transparency (important!)
                if img.mode in ("RGBA", "LA"):
                    background = Image.new("RGB", img.size, (255, 255, 255))
                    background.paste(img, mask=img.split()[-1])
                    rgb_img = background
                else:
                    rgb_img = img.convert("RGB")

                jpg_file = png_file.with_suffix(".jpg")

                rgb_img.save(
                    jpg_file,
                    "JPEG",
                    quality=quality,
                    optimize=True
                )

                print(f" Converted: {jpg_file}")

        except Exception as e:
            print(f" Failed: {png_file} -> {e}")


if __name__ == "__main__":
    user_input = input("Enter PNG file or folder path: ").strip()
    
    try:
        quality = int(input("Enter JPEG quality (1-100, default 95): ") or 95)
        quality = max(1, min(100, quality))
    except ValueError:
        quality = 95

    convert_png_to_jpg(user_input, quality)
