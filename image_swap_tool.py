from PIL import Image
import random

def encrypt_image(image_path, key):
    image = Image.open(image_path)
    pixels = list(image.getdata())
    width, height = image.size

    # Create a list of all pixel positions
    pixel_indices = list(range(len(pixels)))
    random.Random(key).shuffle(pixel_indices)

    # Swap pixels
    encrypted_pixels = [pixels[i] for i in pixel_indices]

    # Create new image
    encrypted_image = Image.new(image.mode, image.size)
    encrypted_image.putdata(encrypted_pixels)
    encrypted_image.save("encrypted.png")
    print("🔒 Image encrypted and saved as 'encrypted.png'.")

    return pixel_indices  # Needed for decryption

def decrypt_image(encrypted_path, key):
    encrypted_image = Image.open(encrypted_path)
    encrypted_pixels = list(encrypted_image.getdata())
    width, height = encrypted_image.size

    # Generate the same shuffled indices
    pixel_indices = list(range(len(encrypted_pixels)))
    random.Random(key).shuffle(pixel_indices)

    # Create a list to hold decrypted pixels
    decrypted_pixels = [None] * len(encrypted_pixels)

    # Undo the shuffle
    for i, shuffled_index in enumerate(pixel_indices):
        decrypted_pixels[shuffled_index] = encrypted_pixels[i]

    # Create new image
    decrypted_image = Image.new(encrypted_image.mode, encrypted_image.size)
    decrypted_image.putdata(decrypted_pixels)
    decrypted_image.save("decrypted.png")
    print("🔓 Image decrypted and saved as 'decrypted.png'.")

# ---- Main program ----
if __name__ == "__main__":
    choice = input("Choose (e) encrypt or (d) decrypt: ").lower()
    if choice == 'e':
        path = input("Enter image filename (e.g., image.jpg): ")
        key = input("Enter encryption key (any string): ")
        encrypt_image(path, key)
    elif choice == 'd':
        path = input("Enter encrypted image filename (e.g., encrypted.png): ")
        key = input("Enter encryption key used: ")
        decrypt_image(path, key)
    else:
        print("❌ Invalid choice. Please enter 'e' or 'd'.")
