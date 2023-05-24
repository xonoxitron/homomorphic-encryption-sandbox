from phe import paillier

#  generate a public + private keypair
public_key, private_key = paillier.generate_paillier_keypair()

# plain constants
w = 5
x = 10
y = 20
z = 40

# encrypted variables
encrypted_w = public_key.encrypt(w)
encrypted_x = public_key.encrypt(x)
encrypted_y = public_key.encrypt(y)
encrypted_z = public_key.encrypt(z)

# math operations on encrypted variables
encrypted_addition = encrypted_x + encrypted_y
encrypted_subtraction = encrypted_z - encrypted_w
encrypted_multiplication = x * encrypted_y
encrypted_division = encrypted_z / w

# decrypted math operations results
decrypted_addition = private_key.decrypt(encrypted_addition)
assert decrypted_addition == 30
decrypted_subtraction = private_key.decrypt(encrypted_subtraction)
assert decrypted_subtraction == 35
decrypted_multiplication = private_key.decrypt(encrypted_multiplication)
assert decrypted_multiplication == 200
decrypted_division = private_key.decrypt(encrypted_division)
assert decrypted_division == 8

print("decrypted_addition: ", decrypted_addition)
print("decrypted_subtraction: ", decrypted_subtraction)
print("decrypted_multiplication: ", decrypted_multiplication)
print("decrypted_division: ", decrypted_division)
