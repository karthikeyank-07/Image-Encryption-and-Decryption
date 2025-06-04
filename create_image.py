from PIL import Image
import numpy as np

def encrypt_image(path, key=50):
    img = Image.open(path).convert('RGB')
    arr = np.array(img)

    arr = arr ^ key
    arr[[0, -1]] = arr[[-1, 0]]

    encrypted_img = Image.fromarray(arr)
    encrypted_img.save("encrypted.png")
    print("🔒 Image encrypted and saved as 'encrypted.png'.")

def decrypt_image(path, key=50):
    img = Image.open(path).convert('RGB')
    arr = np.array(img)

    arr[[0, -1]] = arr[[-1, 0]]
    arr = arr ^ key

    decrypted_img = Image.fromarray(arr)
    decrypted_img.save("decrypted.png")
    print("🔓 Image decrypted and saved as 'decrypted.png'.")

# Run both functions
encrypt_image("input.jpg")
decrypt_image("encrypted.png")
