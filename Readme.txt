 Secret Message Encrypter/Decrypter in Images

This project implements a simple encryption and decryption technique that hides a secret message within an image. The encryption process modifies pixel values of an image to encode a message, while the decryption process extracts the hidden message.



 Features

 Message Encryption: 
   Encodes a userprovided secret message into an image by modifying pixel values.
   Saves the resulting image with hidden data as `encryptedImage.jpg`.

 Message Decryption: 
   Extracts the encoded message from the modified image.
   Requires the correct passcode for decryption.
  
 Passcode Protection: Ensures the decryption process can only be completed if the correct passcode is provided.



 Requirements

 Python 3.x
 OpenCV (cv2) library



 Installation

1. Clone or download the repository to your local machine.
2. Install dependencies using pip:

pip install opencvpython



 How It Works

1. Encryption Process:
    The script takes two inputs from the user:
      A secret message to encrypt.
      A passcode to protect the decryption process.
    Modifies specific pixel values of an input image (`mypic.jpg`) based on the ASCII values of the characters in the secret message.
    Outputs the image with the encoded message as `encryptedImage.jpg`.

2. Decryption Process:
    Accepts the same passcode used during encryption.
    Retrieves the original secret message from `encryptedImage.jpg` by decoding the modified pixel values.
    If the provided passcode is incorrect, the decryption process is terminated with an error message.



 Usage

1. Prepare an image named `mypic.jpg` in the project folder (the image where the secret message will be encoded).
2. Run the script:
python script.py

3. Enter your secret message and passcode when prompted.
    The encrypted image will be saved as `encryptedImage.jpg` and automatically opened for preview.
4. To decrypt the message, provide the correct passcode when prompted.



 Limitations

 The image must have sufficient size to store the entire message. Each character of the message will take one pixel’s data.
 The encryption method is simple and is not suitable for use in highsecurity applications.



 Notes

 The script uses pixel manipulation to encode the message into the image.
 It uses three color channels (Red, Green, and Blue) to sequentially encode characters of the message.
 If the passcode provided during decryption does not match the one used during encryption, the message will not be retrieved.



 Example Workflow

1. User provides an input message (e.g., `"Hello"`).
2. User sets a passcode (e.g., `"1234"`).
3. The script modifies pixel values of `mypic.jpg` and saves the new image as `encryptedImage.jpg`.
4. To decrypt, rerun the program with the newly generated `encryptedImage.jpg` and provide the passcode `"1234"`.
5. If the passcode is correct, the hidden message (`"Hello"`) is revealed.



 Author
This project demonstrates the use of OpenCV in Python for basic cryptographic operations. It is ideal for educational purposes and basic data hiding techniques.



 Disclaimer
This project is not meant for productionlevel encryption. It is a basic implementation intended for educational purposes to demonstrate concepts of steganography and pixel manipulation in an image.