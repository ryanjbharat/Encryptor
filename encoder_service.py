"""
This is the encoder microservice for CS361.
This will read the contents of a microservice communication file "service.txt" and base64 encode the file's contents.
This program assumes the data in the file will be read in as string data.
It also assumes that the data in the file is not already base64 encoded.

HOW TO USE:
1.  Ensure you have a text file named "service.txt" in the same folder as this file.
    This is where the program will read/write from.
2.  Run this program as a different process, e.g. "python3 encoder_service.py"

"""

import base64
import time

def isbase64(text):
    try:
        return base64.b64encode(base64.b64decode(text)).decode() == text
    except Exception:
        return False


while True:
    time.sleep(2)
    encoderServiceFile = open('service.txt', 'r+')
    fileText = encoderServiceFile.read()
    if not isbase64(fileText): # Check file for if contents are already base64 encoded
        encryptedFileText = base64.urlsafe_b64encode(fileText.encode()) # Encode contents of file into variable
        encoderServiceFile.seek(0)
        encoderServiceFile.truncate() # Remove data from file
        encoderServiceFile.write(encryptedFileText.decode()) # Write encoded data to file
    encoderServiceFile.close()
