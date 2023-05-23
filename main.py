import base64
import codecs
import urllib.parse
import binascii
import re
import quopri
import html
import base58

def base64_decoder(input_str):
    try:
        decoded_bytes = base64.b64decode(input_str)
        return decoded_bytes.decode('utf-8')
    except:
        return "Invalid Base64 input."

def ascii_decoder_octal(input_str):
    try:
        octal_values = input_str.split('\\')[1:]
        decoded_str = ''.join(chr(int(octal, 8)) for octal in octal_values if octal)
        return decoded_str
    except:
        return "Invalid ASCII (Octal) input."

def ascii_decoder_hexadecimal(input_str):
    try:
        hex_values = input_str.split('\\')[1:]
        decoded_str = ''.join(chr(int(hex_value, 16)) for hex_value in hex_values if hex_value)
        return decoded_str
    except:
        return "Invalid ASCII (Hexadecimal) input."

def ascii_decoder_decimal(input_str):
    try:
        decoded_str = ''.join(chr(int(decimal)) for decimal in input_str.split(', '))
        return decoded_str
    except:
        return "Invalid ASCII (Decimal) input."

def url_decoder(input_str):
    try:
        decoded_str = urllib.parse.unquote(input_str)
        return decoded_str
    except:
        return "Invalid URL input."

def hex_decoder(input_str):
    try:
        decoded_str = codecs.decode(input_str, 'hex').decode('utf-8')
        return decoded_str
    except:
        return "Invalid Hex input."

def unicode_decoder(input_str):
    try:
        decoded_str = input_str.encode('utf-8').decode('unicode-escape')
        return decoded_str
    except:
        return "Invalid Unicode input."

def html_entity_decoder(input_str):
    try:
        decoded_str = codecs.decode(input_str, 'html-entities').encode('utf-8').decode('utf-8')
        return decoded_str
    except:
        return "Invalid HTML entity input."

def utf8_decoder(input_str):
    try:
        decoded_bytes = base64.b64decode(input_str)
        decoded_str = decoded_bytes.decode('utf-8')
        return decoded_str
    except:
        return "Invalid UTF-8 input."


def rot13_decoder(input_str):
    try:
        decoded_str = codecs.decode(input_str, 'rot_13')
        return decoded_str
    except:
        return "Invalid ROT13 input."

def binary_decoder(input_str):
    try:
        binary_values = input_str.split(' ')
        decoded_str = ''.join(chr(int(binary, 2)) for binary in binary_values if binary)
        return decoded_str
    except:
        return "Invalid binary input."

def base32_decoder(input_str):
    try:
        decoded_bytes = base64.b32decode(input_str, casefold=True)
        return decoded_bytes.decode('utf-8')
    except:
        return "Invalid Base32 input."

def quoted_printable_decoder(input_str):
    try:
        decoded_str = quopri.decodestring(input_str)
        return decoded_str.decode('utf-8')
    except:
        return "Invalid Quoted-Printable input."

def punycode_decoder(input_str):
    try:
        decoded_str = input_str.encode('ascii').decode('punycode')
        return decoded_str
    except:
        return "Invalid Punycode input."

def reverse_text_decoder(input_str):
    try:
        reversed_str = input_str[::-1]
        return reversed_str
    except:
        return "Invalid input."

def base58_decoder(input_str):
    try:
        decoded_data = base58.b58decode(input_str)
        return decoded_data.decode()
    except ValueError as e:
        return "Invalid Base58 input: " + str(e)

def base85_decoder(input_str):
    try:
        decoded_data = base64.a85decode(input_str)
        return decoded_data.decode()
    except ValueError as e:
        return "Invalid Base85 input: " + str(e)

def main():
    while True:
        print('1. Base64 Decoder')
        print('2. ASCII Decoder (Octal)')
        print('3. ASCII Decoder (Hexadecimal)')
        print('4. ASCII Decoder (Decimal)')
        print('5. URL Decoder')
        print('6. Hex Decoder')
        print('7. Unicode Decoder')
        print('8. HTML Entity Decoder')
        print('9. UTF-8 Decoder')
        print('10. ROT13 Decoder')
        print('11. Binary Decoder')
        print('12. Base58 Decoder')
        print('13. Base32 Decoder')
        print('14. Quoted-Printable Decoder')
        print('15. Reverse Text Decoder')
        print('16. Base85 Decoder / ASCII85')
        print('0. Exit')
        choice = input('Enter your choice (1-20): ')

        if choice == '1':
            input_str = input('Enter the Base64-encoded input: ')
            decoded_str = base64_decoder(input_str)
            print('Decoded output:', decoded_str)
        elif choice == '2':
            input_str = input('Enter the ASCII-encoded input in Octal format (space-separated): ')
            decoded_str = ascii_decoder_octal(input_str)
            print('Decoded output:', decoded_str)
        elif choice == '3':
            input_str = input('Enter the ASCII-encoded input in Hexadecimal format: ')
            decoded_str = ascii_decoder_hexadecimal(input_str)
            print('Decoded output:', decoded_str)
        elif choice == '4':
            input_str = input('Enter the ASCII-encoded input in Decimal format (space-separated): ')
            decoded_str = ascii_decoder_decimal(input_str)
            print('Decoded output:', decoded_str)
        elif choice == '5':
            input_str = input('Enter the input to decode: ')
            decoded_str = url_decoder(input_str)
            print('Decoded output:', decoded_str)
        elif choice == '6':
            input_str = input('Enter the input to decode: ')
            decoded_str = hex_decoder(input_str)
            print('Decoded output:', decoded_str)
        elif choice == '7':
            input_str = input('Enter the input to decode: ')
            decoded_str = unicode_decoder(input_str)
            print('Decoded output:', decoded_str)
        elif choice == '8':
            input_str = input('Enter the input to decode: ')
            decoded_str = html_entity_decoder(input_str)
            print('Decoded output:', decoded_str)
        elif choice == '9':
            input_str = input('Enter the input to decode: ')
            decoded_str = utf8_decoder(input_str)
            print('Decoded output:', decoded_str)
        elif choice == '10':
            input_str = input('Enter the input to decode: ')
            decoded_str = rot13_decoder(input_str)
            print('Decoded output:', decoded_str)
        elif choice == '11':
            input_str = input('Enter the input to decode (space-separated binary values): ')
            decoded_str = binary_decoder(input_str)
            print('Decoded output:', decoded_str)
        elif choice == '12':
            input_str = input('Enter the Base58-encoded input: ')
            decoded_str = base58_decoder(input_str)
            print('Decoded output:', decoded_str)
        elif choice == '13':
            input_str = input('Enter the Base32-encoded input: ')
            decoded_str = base32_decoder(input_str)
            print('Decoded output:', decoded_str)
        elif choice == '14':
            input_str = input('Enter the Quoted-Printable-encoded input: ')
            decoded_str = quoted_printable_decoder(input_str)
            print('Decoded output:', decoded_str)
        elif choice == '15':
            input_str = input('Enter the input to decode: ')
            decoded_str = reverse_text_decoder(input_str)
            print('Decoded output:', decoded_str)
        elif choice == '16':
            input_str = input('Enter the Base85-encoded input: ')
            decoded_str = base85_decoder(input_str)
            print('Decoded output:', decoded_str)
        elif choice == '0':
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
