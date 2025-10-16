def algo1(plaintext):
    ciphertext = ''.join(chr((ord(char) + 3) % 256) for char in plaintext)
    return ciphertext

def algo2(plaintext):
    reversed_text = plaintext[::-1]
    ciphertext = ''.join(chr((ord(char) + 15) % 256) for char in reversed_text)
    return ciphertext

def algo3(plaintext):
    plaintext = 2 * plaintext[::-1]
    ciphertext = ''.join(chr((ord(char) + 70) % 256) for char in plaintext)
    return ciphertext

def algo4(plaintext):
    # Convert the UTF-8 bytes of the plaintext into a big integer
    byte_data = plaintext.encode('utf-8')
    bits = ''.join(format(byte, '08b') for byte in byte_data)
    integer = int(bits, 2) if bits else 0
    # Store the integer together with the plaintext length so decryption can reverse the multiplication
    # Format: "<integer>:<length>"
    ciphertext = f"{integer}:{len(plaintext)}"
    return ciphertext

def dealgo1(ciphertext):
    plaintext = ''.join(chr((ord(char) - 3) % 256) for char in ciphertext)
    return plaintext

def dealgo2(ciphertext):
    reversed_text = ''.join(chr((ord(char) - 15) % 256) for char in ciphertext)
    plaintext = reversed_text[::-1]
    return plaintext

def dealgo3(ciphertext):
    intermediate = ''.join(chr((ord(char) - 70) % 256) for char in ciphertext)
    plaintext = intermediate[:len(intermediate)//2][::-1]
    return plaintext

def dealgo4(ciphertext):
    # New format: "<integer>:<length>"
    if ':' in ciphertext:
        integer_str, length_str = ciphertext.split(':', 1)
        try:
            integer = int(integer_str)
            length = int(length_str)
        except ValueError:
            raise ValueError("Invalid ciphertext format for dealgo4")
        # Recover bits from the integer
        bits = bin(integer)[2:]
        bits = bits.zfill((len(bits) + 7) // 8 * 8)
        byte_array = bytearray(int(bits[i:i+8], 2) for i in range(0, len(bits), 8))
        plaintext = byte_array.decode('utf-8', errors='ignore')
        # In case the decoded string includes extra padding bytes, truncate to the original length
        return plaintext[:length]

    # Fallback for old-style ciphertexts (just a numeric string): try plausible lengths
    # Old format used integer * (len(plaintext) * 16), but didn't include length, so we try guesses.
    try:
        big_int = int(ciphertext)
    except ValueError:
        raise ValueError("Invalid ciphertext for dealgo4")

    # Try plausible lengths up to a reasonable limit
    for length_guess in range(1, 513):
        denom = length_guess * 16
        if denom == 0:
            continue
        integer = big_int // denom
        if integer == 0:
            # if integer becomes zero, further larger lengths will also give zero -> break
            break
        bits = bin(integer)[2:]
        bits = bits.zfill((len(bits) + 7) // 8 * 8)
        try:
            byte_array = bytearray(int(bits[i:i+8], 2) for i in range(0, len(bits), 8))
            candidate = byte_array.decode('utf-8')
        except Exception:
            continue
        # If the decoded candidate has the guessed length, accept it
        if len(candidate) == length_guess:
            return candidate

    # If no guess matched, return best-effort decode from the integer // 16 (assume length 1)
    integer = big_int // 16
    bits = bin(integer)[2:]
    bits = bits.zfill((len(bits) + 7) // 8 * 8)
    byte_array = bytearray(int(bits[i:i+8], 2) for i in range(0, len(bits), 8))
    plaintext = byte_array.decode('utf-8', errors='ignore')
    return plaintext