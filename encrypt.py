def encrypt(message, key):
    "Encrypt message with key."
    result = ''

    # encrpyt

    for letter in message:
        if letter.isalpha():

            # Letters

            num = ord(letter)

            if letter.isupper():
                base = ord('A')
            else:
                assert letter.islower()
                base = ord('a')

            # The encryption equation:

            num = (num - base + key) % 26 + base

            result += chr(num)

        elif letter.isdigit():

            # TODO: Encrypt digits.
            result += letter

        else:
            result += letter

    return result


def decrypt(message, key):
    "Decrypt message with key."
    return encrypt(message, -key)


def decode(message):
    "Decode message without key."
    pass  # TODO


def get_key():
    "Get key from user."
    try:
        text = input('Enter a key (1 - 25): ')
        key = int(text)
        return key
    except:
        print('Invalid key. Using key: 0.')
        return 0


print('message')
choice = input()

if choice == 'encrypt':
    phrase = input('Message: ')
    code = get_key()
    print('Encrypted message:', encrypt(phrase, code))
