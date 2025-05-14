# this one was not THAT fun to do but it was still nice :)

from Crypto.Cipher import AES
from Crypto.Hash import HMAC, SHA256
from Crypto.Random import get_random_bytes
from colorama import init
from termcolor import colored
import base64

init()

def encode():

# gets input
    data = input(colored("encode", "white", "on_dark_grey")+" -> ").encode()

# generates random keys 
    aes_key = get_random_bytes(16)
    hmac_key = get_random_bytes(16)

# encrypts the input
    cipher = AES.new(aes_key, AES.MODE_CTR)
    ciphertext = cipher.encrypt(data)

# assigns values to the following
    hmac = HMAC.new(hmac_key, digestmod=SHA256)
    tag = hmac.update(cipher.nonce + ciphertext).digest()
    nonce = cipher.nonce

# prints the things
    print(colored("hmac key", "grey", "on_light_magenta") + " -> " + "\033[4m" + base64.b64encode(hmac_key).decode() + "\033[0m")
    print(colored("tag", "grey", "on_light_green") + " -> " + "\033[4m" + base64.b64encode(tag).decode() + "\033[0m")
    print(colored("cipher", "grey", "on_light_red") + " -> " + "\033[4m" + base64.b64encode(ciphertext).decode() + "\033[0m")
    print(colored("nonce", "grey", "on_light_blue") + " -> " + "\033[4m" + base64.b64encode(nonce).decode() + "\033[0m")
    print(colored("aes key", "grey", "on_light_yellow") + " -> " + "\033[4m" + base64.b64encode(aes_key).decode() + "\033[0m")

def decode():
    from base64 import b64decode
# gets input as base64 then decodes base64
    hmac_key = b64decode(input(colored("hmac key*", "grey", "on_light_magenta") + " -> "))
    tag = b64decode(input(colored("tag*", "grey", "on_light_green") + " -> "))
    ciphertext = b64decode(input(colored("cipher", "grey", "on_light_red") + " -> "))
    nonce = b64decode(input(colored("nonce", "grey", "on_light_blue") + " -> "))
    aes_key = b64decode(input(colored("aes key", "grey", "on_light_yellow") + " -> "))

# decrpyts the input
    cipher = AES.new(aes_key, AES.MODE_CTR, nonce=nonce)
    message = cipher.decrypt(ciphertext)

# prints
    print(colored("decoded", "white", "on_dark_grey") + " -> " + str(message.decode()))

print(colored("welcome, please choose an action [d/e]", "white", "on_dark_grey"))

# loops until correct command given
while True:
    userChoice = input(colored("", "white", "on_dark_grey")+"-> ")
    if str(userChoice) == "d":
        decode()
        break
    elif str(userChoice) == "e":
        encode()
        break
    else:
        print("type again")


























