import cv2

# Load the encrypted image
img = cv2.imread("encryptedImage.jpg")  # Ensure this is the correct path

# Read the password from the file
with open("password.txt", "r") as f:
    password = f.read().strip()

# Get the password for decryption
pas = input("Enter passcode for Decryption: ")

# Check if the password is correct
if password == pas:
    # Read the length of the message from the file
    with open("message_length.txt", "r") as f:
        msg_length = int(f.read().strip())

    message = ""
    n, m, z = 0, 0, 0

    # Create a dictionary for ASCII to character mapping
    c = {i: chr(i) for i in range(255)}

    # Decrypt the message from the image
    for i in range(msg_length):  # Use the length of the original message
        message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3

    print("Decrypted message:", message)
else:
    print("YOU ARE NOT authorized")