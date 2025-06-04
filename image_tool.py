from PIL import Image
import os

def encrypt_decrypt(image, key):
    pixels = list(image.getdata())
    new_pixels = []
    for pixel in pixels:
        new_pixel = tuple([channel ^ key for channel in pixel])
        new_pixels.append(new_pixel)
    new_image = Image.new(image.mode, image.size)
    new_image.putdata(new_pixels)
    return new_image

def main():
    while True:
        image_path = input("Enter the image filename to encrypt (e.g., image.png): ")
        if os.path.isfile(image_path):
            break
        print("File not found. Please try again.")

    while True:
        key_input = input("Enter an encryption key (0-255): ")
        if key_input.isdigit():
            key = int(key_input)
            if 0 <= key <= 255:
                break
        print("Invalid key. Please enter a number between 0 and 255.")

    image = Image.open(image_path)

    encrypted_image = encrypt_decrypt(image, key)
    encrypted_image.save("encrypted.png")
    print("🔒 Image encrypted and saved as 'encrypted.png'.")

    decrypted_image = encrypt_decrypt(encrypted_image, key)
    decrypted_image.save("decrypted.png")
    print("🔓 Image decrypted and saved as 'decrypted.png'.")

if __name__ == "__main__":
    main()
