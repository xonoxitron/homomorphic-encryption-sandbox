# Homomorphic Encryption Sandbox

![Homomorphic Encryption](./homomorphic-encryption.png "Homomorphic Encryption")

## Background

**Homomorphic Encryption** allows data to be manipulated while it is still **encrypted**.
This property is useful when sensitive data needs to be processed, analyzed, or transmitted.
This example uses a **Paillier Cryptosystem**, which is a *probabilistic asymmetric algorithm for public key cryptography*.

The **Paillier Encryption** can perform four types of **Homomorphic** operations:

* Homomorphic Addition: Allows adding two encrypted values to get the encrypted sum or to add an encrypted value to a **constant**.
* Homomorphic Subtraction: Allows subtracting two encrypted values to get the encrypted difference or to subtract a **constant** from an encrypted value.
* Homomorphic Multiplication: Allows us to multiply an encrypted value by a **constant** to get the encrypted product.
* Homomorphic Division: Allows us to divide an encrypted value by a **constant** to get the encrypted division.

The **Homomorphic Encryption** provides a powerful tool for secure computation on sensitive data. **Paillier Encryption** is just one example of a **Homomorphic Encryption scheme**, and there are many other schemes that offer different properties and capabilities.

## Description

In the sandbox script file, we first generate a new public/private key pair using the ***generate_paillier_keypair*** function from the **paillier module**. Then, we use the public key to encrypt the numbers using the ***encrypt*** method. To perform the math operations on the **encrypted numbers/constants**, we can simply use the `+,-,*,/` operators, which overloads the default behavior of the ***paillier.EncryptedNumber*** class. Finally, we can use the private key to decrypt the results and verify that the operations are correct.

## Prerequisites

Before running this script, make sure you have the `phe` library installed. You can install it using the following command:

```console
pip install phe
```

## Script Overview

The script performs the following steps:

1. Generates a public and private keypair for Paillier encryption.
2. Defines plain constants `w`, `x`, `y`, and `z`.
3. Encrypts the plain constants using the generated public key.
4. Performs various mathematical operations on the encrypted variables.
5. Decrypts the results of the mathematical operations using the private key.
6. Prints the decrypted results.

## Script

```python
from phe import paillier

# Generate a public + private keypair
public_key, private_key = paillier.generate_paillier_keypair()

# Plain constants
w = 5
x = 10
y = 20
z = 40

# Encrypted variables
encrypted_w = public_key.encrypt(w)
encrypted_x = public_key.encrypt(x)
encrypted_y = public_key.encrypt(y)
encrypted_z = public_key.encrypt(z)

# Math operations on encrypted variables
encrypted_addition = encrypted_x + encrypted_y
encrypted_subtraction = encrypted_z - encrypted_w
encrypted_multiplication = x * encrypted_y
encrypted_division = encrypted_z / w

# Decrypted math operations results
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
```

## Explanation

1. The script imports the necessary `paillier` module from the `phe` library.
2. The `generate_paillier_keypair()` function is called to generate a public and private keypair for Paillier encryption.
3. The script defines four plain constants: `w`, `x`, `y`, and `z`.
4. The plain constants are encrypted using the `encrypt()` method of the public key object. The resulting encrypted values are stored in variables `encrypted_w`, `encrypted_x`, `encrypted_y`, and `encrypted_z`.
5. Various mathematical operations are performed on the encrypted variables using standard arithmetic operators (`+`, `-`, `*`, `/`). These operations are done directly on the encrypted values.
6. The results of the mathematical operations are decrypted using the `decrypt()` method of the private key object. The decrypted values are stored in variables `decrypted_addition`, `decrypted_subtraction`, `decrypted_multiplication`, and `decrypted_division`.
7. Assertions are used to verify that the decrypted results match the expected values.
8. Finally, the decrypted results are printed to the console.

## Output

When you run the script, you should see the following output:

```console
decrypted_addition:  30
decrypted_subtraction:  35
decrypted_multiplication:  200
decrypted_division:  8
```

The output confirms that the mathematical operations on the encrypted values were performed correctly and the decrypted results match the expected values.

## Conclusion

This script demonstrates the basic usage of a Paillier Cryptosystem for Homomorphic Encryption operations. You can modify the script and explore more complex operations and scenarios supported by the library. Remember to handle key management securely as it is crucial for maintaining the privacy and security of the encrypted data.
