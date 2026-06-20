import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

# This is the message we want encrypted
message="This will be encrypted!"

# K1 - 16 random bytes
keysize=32
iv = os.urandom(16)

# K2 - 32 random bytes
keysize=32
key = os.urandom(keysize)

# Set padding and unpadding for before and after. 
# Needs due to AES being a block cipher
padder = padding.PKCS7(128).padder()
unpadder = padding.PKCS7(128).unpadder()


try:
    # Create the cipher using AES in XTS mode
	cipher = Cipher(algorithms.AES(key), modes.XTS(iv))
	encryptor = cipher.encryptor()

    # Fix the origional message to bytes and make into blocks
	str=padder.update(message.encode())+padder.finalize()

    # Use the encryptor to create the cipher text
	ciphertext = encryptor.update(str ) + encryptor.finalize()

	# Now decrypt backwars
	decryptor = cipher.decryptor()
	rtn=unpadder.update(decryptor.update(ciphertext) + decryptor.finalize())+unpadder.finalize()	

	print("Type:\t\t\t",cipher.algorithm.name)
	print("Mode:\t\t\t",cipher.mode.name)
	print("Message:\t\t",message)
	print("Message with padding:\t",str)
	print("\nKey:\t\t\t",key.hex())
	print("IV:\t\t\t",iv.hex())
	print("\nCipher:\t\t\t",ciphertext.hex())
	print("Decrypt:\t\t",rtn.decode())
except Exception as msg:
	print(msg)
