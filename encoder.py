import base64
import argparse
import time
import urllib.parse

def get_arguments():
    """ Parses the arguments provided by user. """
    parser = argparse.ArgumentParser(prog="encoder.py", usage='%(prog)s [--encode | --decode] SCHEME DATA',
                                     description="encodes or decodes data. Use a scheme built into the program. "
                                                 "Supply the data as a string. Reference --help for more info.")
    parser.print_usage = parser.print_help
    group = parser.add_mutually_exclusive_group()

    parser.add_argument('-help', action="help")

    parser.add_argument("--encode", "-e", action='store_true', help="encodes the data provided! You will not have to "
                                                                    "worry about anyone snooping on you anymore...")
    parser.add_argument("--decode", "-d", action='store_true', help="NEW! Use this to decode the data. Still in "
                                                                    "testing. Make sure you have supplied properly "
                                                                    "encoded data before attempting OR program will "
                                                                    "crash.")
    parser.add_argument("scheme", choices=(["base64", "url"]), type=str, help="base64: In computer "
                                                                       "programming, Base64 is a group of "
                                                                       "binary-to-text encoding schemes that "
                                                                       "represent binary "
                                                                       "data in an ASCII string format by translating "
                                                                              "the data into a radix-64 "
                                                                              "representation. The term "
                                                                       "Base64 originates from a specific MIME "
                                                                              "content transfer encoding. url: Use "
                                                                              "URL Encoding when you're calling a "
                                                                              "remote API with additional query "
                                                                              "strings or path parameters. This makes "
                                                                              "it network friendly!")
    parser.add_argument("data", type=str, help="String data that you want to encode or decrypt. Use quotation marks "
                                               "for multiword strings or it will not work! Enter HOCKEYLINE to use "
                                               "the hockeyline microservice. This will take longer to process!")

    args = parser.parse_args()

    return args


def encoder(input, scheme):
    """ Receives an input and encoding scheme. Returns encoded data. """
    if scheme == "base64":
        output = base64.urlsafe_b64encode(input.encode())
        return output.decode()
    elif scheme == "url":
        output = urllib.parse.quote_plus(input)
        return output


def decoder(input, scheme):
    """ Receives an input and encoding scheme. Returns the decoded form of that data. """
    if scheme == "base64":
        output = base64.urlsafe_b64decode(input.encode())
        return output.decode()


def requestHockeyLine():
    with open("OTBMicro.txt", "w") as outfile:
        outfile.write("start")
    time.sleep(10)
    hockey_data = ""
    with open("OTBMicro.txt", "r") as infile:
        for line in infile:
            hockey_data += line

    return hockey_data

def main():
    args = get_arguments()

    data = args.data
    if data == "HOCKEYLINE":
        data = requestHockeyLine()

    if args.encode:
        output = encoder(data, args.scheme)
        print(output)
    elif args.decrypt:
        output = decoder(data, args.scheme)
        print(output)
    else:
        print("I don't know what you're trying to do here!")


if __name__ == "__main__":
    main()
