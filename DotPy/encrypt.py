import os
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

def encrypt(key, filename):
	chunksize = 64*1024
	output_file = filename + "_encrypted"
	filesize = str(os.path.getsize(filename)).zfill(16)
	IV = Random.new().read(16)

	
