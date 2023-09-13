import math

# SHA-256 constants (in hexadecimal)
K = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
    0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
    0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
    0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
    0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
    0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
    0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
    0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
    0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
]

# Initial hash values (in hexadecimal)
H = [
    0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
    0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
]

def sha256(message):
    # Pre-processing: pad the message
    message = bytearray(message, 'utf-8')
    original_length = len(message) * 8
    message.append(0x80)  # Add a single 1 bit
    while len(message) % 64 != 56:
        message.append(0x00)
    message += original_length.to_bytes(8, byteorder='big')

    # Process the message in 512-bit chunks
    for chunk_start in range(0, len(message), 64):
        chunk = message[chunk_start:chunk_start + 64]
        w = [0] * 64

        # Initialize the message schedule
        for t in range(16):
            w[t] = int.from_bytes(chunk[t * 4:(t + 1) * 4], byteorder='big')

        for t in range(16, 64):
            s0 = (right_rotate(w[t - 15], 7) ^ right_rotate(w[t - 15], 18) ^ (w[t - 15] >> 3))
            s1 = (right_rotate(w[t - 2], 17) ^ right_rotate(w[t - 2], 19) ^ (w[t - 2] >> 10))
            w[t] = (w[t - 16] + s0 + w[t - 7] + s1) & 0xFFFFFFFF

        # Initialize working variables
        a, b, c, d, e, f, g, h = H

        # Compression function
        for t in range(64):
            S1 = (right_rotate(e, 6) ^ right_rotate(e, 11) ^ right_rotate(e, 25))
            ch = (e & f) ^ ((~e) & g)
            temp1 = (h + S1 + ch + K[t] + w[t]) & 0xFFFFFFFF
            S0 = (right_rotate(a, 2) ^ right_rotate(a, 13) ^ right_rotate(a, 22))
            maj = (a & b) ^ (a & c) ^ (b & c)
            temp2 = (S0 + maj) & 0xFFFFFFFF

            h = g
            g = f
            f = e
            e = (d + temp1) & 0xFFFFFFFF
            d = c
            c = b
            b = a
            a = (temp1 + temp2) & 0xFFFFFFFF

        # Update hash values
        H[0] = (H[0] + a) & 0xFFFFFFFF
        H[1] = (H[1] + b) & 0xFFFFFFFF
        H[2] = (H[2] + c) & 0xFFFFFFFF
        H[3] = (H[3] + d) & 0xFFFFFFFF
        H[4] = (H[4] + e) & 0xFFFFFFFF
        H[5] = (H[5] + f) & 0xFFFFFFFF
        H[6] = (H[6] + g) & 0xFFFFFFFF
        H[7] = (H[7] + h) & 0xFFFFFFFF

    # Final hash value
    return ''.join(f'{h:08x}' for h in H)

def right_rotate(x, n):
    return ((x >> n) | (x << (32 - n))) & 0xFFFFFFFF

# Test the SHA-256 function
message = "Hello, SHA-256!"
hashed_message = sha256(message)
print("Message:", message)
print("SHA-256 Hash:", hashed_message)
