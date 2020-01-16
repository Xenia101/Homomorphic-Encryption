from phe import paillier

public_key, private_key = paillier.generate_paillier_keypair()

# Encryption
secret_number_list = [3.141592653, 300, -4.6e-12]
encrypted_number_list = [public_key.encrypt(x) for x in secret_number_list]
print(encrypted_number_list)

# Decryption
print([private_key.decrypt(x) for x in encrypted_number_list])

# Calculation
a = encrypted_number_list[0]-3
b = encrypted_number_list[1]+5
c = encrypted_number_list[2]*-2

# Decryption
print(private_key.decrypt(a))
print(private_key.decrypt(b))
print(private_key.decrypt(c))
