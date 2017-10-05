import base64


def hex_to_b64(text_in):
    return base64.b64encode(bytes.fromhex(text_in))


def fixed_xor(text_x, text_y):
    s_x = bytes.fromhex(text_x)
    s_y = bytes.fromhex(text_y)
    L = [x^y for x,y in zip(s_x, s_y)]
    return bytes(L).hex()


# Challenge 1
s_hex = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
s_b64 = b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
assert hex_to_b64(s_hex) == s_b64

# Challenge 2
x = '1c0111001f010100061a024b53535009181c'
y = '686974207468652062756c6c277320657965'
assert fixed_xor(x, y) == '746865206b696420646f6e277420706c6179'
