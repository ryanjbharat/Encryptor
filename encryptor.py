import base64
import argparse

def get_arguments():
    """ Parses the arguments provided by user. """
    parser = argparse.ArgumentParser(prog="encryptor.py", usage='%(prog)s [--encrypt | --decrypt] SCHEME DATA',
                                     description="Encrypts or decrypts data. Use a scheme built into the program. Supply the data as a string. Reference --help for more info.")
    parser.print_usage = parser.print_help
    group = parser.add_mutually_exclusive_group()

    parser.add_argument('-help', action="help")

    parser.add_argument("--encrypt", "-e", action='store_true', help="encrypt the data")
    parser.add_argument("--decrypt", "-d", action='store_true', help="decrypt the data")
    parser.add_argument("scheme", choices=(["base64"]), type=str, help="base64: In computer "
                                                                       "programming, Base64 is a group of "
                                                                       "binary-to-text encoding schemes that "
                                                                       "represent binary "
                                                                       "data in an ASCII string format by translating the data into a radix-64 representation. The term "
                                                                       "Base64 originates from a specific MIME content transfer encoding.")
    parser.add_argument("data", type=str, help="String data that you want to encrypt or decrypt. Use quotation marks "
                                               "for multiword strings or it will not work! Enter HOCKEYLINE to use "
                                               "the hockeyline microservice. This will take longer to process!")

    args = parser.parse_args()

    return args


def encryption(input, scheme):
    """ Receives an input and encryption scheme. Returns encrypted data. """
    if scheme == "base64":
        output = base64.urlsafe_b64encode(input.encode())
        return output


def decryption(input, scheme):
    """ Receives an input and encryption scheme. Returns the decoded form of that data. """
    if scheme == "base64":
        output = base64.urlsafe_b64decode(input.encode())
        return output


def requestHockeyLine():
    return "Hockey line data"


def main():
    args = get_arguments()

    data = args.data
    if data == "HOCKEYLINE":
        data = requestHockeyLine()

    if args.encrypt:
        output = encryption(data, args.scheme)
        print(output.decode())
    elif args.decrypt:
        output = decryption(data, args.scheme)
        print(output.decode())
    else:
        print("I don't know what you're trying to do here!")


if __name__ == "__main__":
    main()
