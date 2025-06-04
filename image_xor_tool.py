from PIL import Image

def key_to_bytes(key: str) -> list[int]:
    """Convert key string to list of ASCII byte values."""
    if not key:
        raise ValueError("Key cannot be empty.")
    return [ord(c) for c in key]

def swap_pixels(pixels: list[tuple], reverse=False) -> list[tuple]:
    """Swap every pair of adjacent pixels. Reverse if decrypting."""
    swapped = pixels.copy()
    step = 2 if not reverse else -2
    for i in range(0, len(pixels) - 1, 2):
        swapped[i], swapped[i + 1] = swapped[i + 1], swapped[i]
    return swapped

def encrypt_decrypt_image(input_path: str, output_path: str, key: str, mode: str) -> None:
    key_bytes = key_to_bytes(key)
    img = Image.open(input_path).convert('RGB')
    pixels = list(img.getdata())
    key_len = len(key_bytes)

    # Step 1: Swap pixels for more scrambling
    if mode == 'e':
        pixels = swap_pixels(pixels, reverse=False)
    elif mode == 'd':
        pixels = swap_pixels(pixels, reverse=True)

    # Step 2: Apply XOR per pixel
    new_pixels = []
    for i, (r, g, b) in enumerate(pixels):
        k = key_bytes[i % key_len]
        new_pixels.append((r ^ k, g ^ k, b ^ k))

    img_new = Image.new('RGB', img.size)
    img_new.putdata(new_pixels)
    img_new.save(output_path)
    print(f"Image saved as '{output_path}'")

def main():
    print("🔐 Image Encrypt/Decrypt Tool with XOR + Pixel Swap")
    choice = input("Choose (e) encrypt or (d) decrypt: ").lower()
    if choice not in ['e', 'd']:
        print("Invalid choice. Please enter 'e' or 'd'.")
        return

    input_file = input("Enter image filename (e.g., image.jpg): ").strip()
    key = input("Enter encryption key (any string): ").strip()

    try:
        if choice == 'e':
            encrypt_decrypt_image(input_file, "encrypted.png", key, 'e')
            print("✅ Image encrypted and saved as 'encrypted.png'.")
        else:
            encrypt_decrypt_image(input_file, "decrypted.png", key, 'd')
            print("✅ Image decrypted and saved as 'decrypted.png'.")
    except FileNotFoundError:
        print(f"❌ File '{input_file}' not found.")
    except ValueError as ve:
        print(f"❌ Error: {ve}")
    except Exception as ex:
        print(f"❌ Unexpected error: {ex}")

if __name__ == "__main__":
    main()
