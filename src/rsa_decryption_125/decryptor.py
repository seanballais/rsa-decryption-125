import math


symbol_encoding = {
    '00': ' ',
    '27': '.',
    '28': ':',
    '29': '\''
}


def obtain_pq(n):
    p = 0.1
    k = math.ceil(math.sqrt(n))
    while not p.is_integer():
        p = k - math.sqrt((k ** 2) - n)
        k += 1

    q = int(n / p)
    p = int(p)

    return p, q


def compute_phi(p, q):
    return (p - 1) * (q - 1)


def obtain_d(e, phi):
    # Reference: https://www.youtube.com/watch?v=4-HSjLXrfPs
    gcd, x, y = extended_euclidean_algorithm(e, phi)

    return x


def decrypt(cipher, n, e):
    p, q = obtain_pq(n)
    phi = compute_phi(p, q)
    d = obtain_d(e, phi)

    if len(cipher) % 2 != 0:
        # The front of the string should prolly be a zero.
        # Add a zero in front then.
        cipher = '0' + cipher

    decrypted_message = ''
    block_counter = 0
    block_length = 6
    while block_counter < len(cipher):
        block = cipher[block_counter: block_counter + block_length]

        decrypted_block = str((int(block) ** d) % n)

        if len(decrypted_block) != block_length:
            decrypted_block = '0' * (block_length - len(decrypted_block)) + decrypted_block

        decrypted_message += decrypted_block
        block_counter += block_length

    return decrypted_message
    

def decode_message(message):
    message_str = str(message)

    if len(message_str) % 2 != 0:
        # The front of the string should prolly be a zero.
        # Add a zero in front then.
        message_str = '0' + message_str

    letter_counter = 0
    message = ''
    letter_length = 2
    while letter_counter < len(message_str):
        encoded_char = message_str[letter_counter:letter_counter + letter_length]

        if 1 <= int(encoded_char) <= 26:
            message += chr(int(encoded_char) + 96)  # We start at 96 since a == '01'.
        else:
            try:
                message += symbol_encoding[encoded_char]
            except KeyError:
                raise ValueError('Unknown encoded character, \'{}\'. Limit encoding from 00 to 29.'.format(encoded_char))

        letter_counter += letter_length

    return message


def extended_euclidean_algorithm(b, a):
    # Code from:
    # https: // en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
    # Still trying to understand the math behind this.
    x0, x1, y0, y1 = 1, 0, 0, 1
    while a != 0:
        q, b, a = b // a, a, b % a
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1

    return  b, x0, y0
