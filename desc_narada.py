import base64

def string_to_binary(input_string):
    return ''.join(format(ord(char), '08b') for char in input_string)

def binary_to_string(binary_string):
    char_array = [chr(int(binary_string[i:i+8], 2)) for i in range(0, len(binary_string), 8)]
    return ''.join(char_array)

def invert_binary(binary_string):
    return ''.join('1' if bit == '0' else '0' for bit in binary_string)

def reverse_binary(binary_string):
    return binary_string[::-1]

def xor_with_fixed_vector(binary_string, fixed_vector):
    fixed_vector = fixed_vector[:len(binary_string)]
    return ''.join(str(int(a) ^ int(b)) for a, b in zip(binary_string, fixed_vector))

def binary_to_base64(binary_string):
    byte_array = bytearray(int(binary_string[i:i+8], 2) for i in range(0, len(binary_string), 8))
    return base64.b64encode(byte_array).decode()

def base64_to_binary(base64_string):
    byte_array = base64.b64decode(base64_string)
    return ''.join(format(byte, '08b') for byte in byte_array)

def decrypt(encrypted_string, fixed_vector):
    # 1. Converter de base64 para binário
    binary = base64_to_binary(encrypted_string)
    
    # 2. Desfazer o XOR (XOR é sua própria operação inversa)
    unxored = xor_with_fixed_vector(binary, fixed_vector)
    
    # 3. Desfazer a reversão
    unreversed = reverse_binary(unxored)
    
    # 4. Desfazer a inversão
    uninverted = invert_binary(unreversed)
    
    # 5. Converter de binário para string
    decrypted = binary_to_string(uninverted)
    
    return decrypted

if __name__ == "__main__":
    encrypted_string = input("Digite a string criptografada em Base64: ")
    fixed_vector = "10101010101010101010101010101010" * 10
    decrypted = decrypt(encrypted_string, fixed_vector)
    print("Texto descriptografado:", decrypted)
