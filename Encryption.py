import cv2
import os

# Load the image
img = cv2.imread("mypic.jpg")  # Replace with the correct image path

# Get the secret message and password from the user
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Save the password to a file
with open("password.txt", "w") as f:
    f.write(password)

# Save the length of the message to a file
with open("message_length.txt", "w") as f:
    f.write(str(len(msg)))

# Create dictionaries for character to ASCII and ASCII to character mapping
d = {chr(i): i for i in range(255)}
c = {i: chr(i) for i in range(255)}

# Initialize coordinates
n, m, z = 0, 0, 0

# Encrypt the message into the image
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n += 1
    m += 1
    z = (z + 1) % 3

# Save the encrypted image
cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  # Use 'start' to open the image on Windows