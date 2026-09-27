import os
import sys
from pathlib import Path

from PIL import Image, ImageDraw


CONFIG_FILE = os.getenv("CONFIG_FILE", "/input/config.txt")
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "/output")


PATTERNS = {
    "A": [
        "01110",
        "10001",
        "10001",
        "11111",
        "10001",
        "10001",
        "10001",
    ],
    "B": [
        "11110",
        "10001",
        "10001",
        "11110",
        "10001",
        "10001",
        "11110",
    ],
    "C": [
        "11111",
        "10000",
        "10000",
        "10000",
        "10000",
        "10000",
        "11111",
    ],
    "E": [
        "11111",
        "10000",
        "10000",
        "11110",
        "10000",
        "10000",
        "11111",
    ],
    "H": [
        "10001",
        "10001",
        "10001",
        "11111",
        "10001",
        "10001",
        "10001",
    ],
    "L": [
        "10000",
        "10000",
        "10000",
        "10000",
        "10000",
        "10000",
        "11111",
    ],
    "N": [
        "10001",
        "11001",
        "11001",
        "10101",
        "10011",
        "10011",
        "10001",
    ],
    "O": [
        "01110",
        "10001",
        "10001",
        "10001",
        "10001",
        "10001",
        "01110",
    ],
    "U": [
        "10001",
        "10001",
        "10001",
        "10001",
        "10001",
        "10001",
        "11111",
    ],
    "Y": [
        "10001",
        "10001",
        "01010",
        "00100",
        "00100",
        "00100",
        "00100",
    ],
}


COLOURS = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "lime": (156, 255, 0),
    "green": (0, 255, 0),
    "cyan": (0, 255, 255),
    "magenta": (255, 0, 255),
}


def load_config(path):
    config = {}

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            key, value = line.split("=", 1)
            config[key.strip()] = value.strip()

    return config


def generate_image(text, pixel_size, background, foreground, output_path):
    gap = max(2, pixel_size // 4)
    letter_gap = pixel_size
    padding = pixel_size * 2

    letter_width = (5 * pixel_size) + (4 * gap)
    letter_height = (7 * pixel_size) + (6 * gap)

    width = (
        padding * 2
        + len(text) * letter_width
        + max(0, len(text) - 1) * letter_gap
    )

    height = padding * 2 + letter_height

    image = Image.new("RGB", (width, height), background)
    draw = ImageDraw.Draw(image)

    rendered_pixels = 0
    x_offset = padding

    for character in text:
        if character not in PATTERNS:
            print(f"[!] Unsupported character skipped: {character}")
            x_offset += letter_width + letter_gap
            continue

        pattern = PATTERNS[character]

        for row_index, row in enumerate(pattern):
            for column_index, cell in enumerate(row):
                if cell != "1":
                    continue

                x = x_offset + column_index * (pixel_size + gap)
                y = padding + row_index * (pixel_size + gap)

                draw.rectangle(
                    [
                        x,
                        y,
                        x + pixel_size - 1,
                        y + pixel_size - 1,
                    ],
                    fill=foreground,
                )

                rendered_pixels += 1

        x_offset += letter_width + letter_gap

    image.save(output_path)

    return width, height, rendered_pixels


def main():
    print("=" * 46)
    print("          CYBUNNY // PIXELFORGE")
    print("=" * 46)
    print()

    print(f"[+] Reading configuration: {CONFIG_FILE}")

    if not os.path.exists(CONFIG_FILE):
        print(f"[ERROR] Configuration file not found: {CONFIG_FILE}")
        sys.exit(1)

    config = load_config(CONFIG_FILE)

    text = config.get("TEXT", "CYBUNNY").upper()
    pixel_size = int(config.get("PIXEL_SIZE", "18"))

    background_name = config.get("BACKGROUND", "black").lower()
    foreground_name = config.get("FOREGROUND", "lime").lower()

    output_name = config.get("OUTPUT", "pixelforge.png")

    if background_name not in COLOURS:
        print(f"[ERROR] Unknown background colour: {background_name}")
        sys.exit(1)

    if foreground_name not in COLOURS:
        print(f"[ERROR] Unknown foreground colour: {foreground_name}")
        sys.exit(1)

    background = COLOURS[background_name]
    foreground = COLOURS[foreground_name]

    print()
    print("Configuration")
    print("-" * 46)
    print(f"Text:          {text}")
    print(f"Pixel size:    {pixel_size}px")
    print(f"Background:    {background_name}")
    print(f"Foreground:    {foreground_name}")
    print(f"Output file:   {output_name}")
    print("-" * 46)
    print()

    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

    output_path = os.path.join(OUTPUT_DIR, output_name)

    print("[+] Generating pixel matrix...")
    print("[+] Rendering artwork...")

    width, height, pixel_count = generate_image(
        text,
        pixel_size,
        background,
        foreground,
        output_path,
    )

    print("[+] Saving output...")
    print()
    print("Render Summary")
    print("-" * 46)
    print(f"Dimensions:    {width} x {height}")
    print(f"Pixels drawn:  {pixel_count}")
    print(f"Output:        {output_path}")
    print("-" * 46)
    print()
    print("[SUCCESS] PixelForge completed successfully.")


if __name__ == "__main__":
    main()
