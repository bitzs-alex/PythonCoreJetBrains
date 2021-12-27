#  write your code here
import argparse

class DecodeFile:
    def __init__(self):
        self.encoded_text = "guv Mv MwB AMnM AnArzr'AMr'p,qrqMAurM nzrMDnFMn MAurMv'.BAMsvyrMDn Mr'p,qrqJ"
        self.decoded_text = ''
        self.file = None
        self.offset = -13
        self.alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
        self.parser = argparse.ArgumentParser(description="This is file Decoder Script")
        self.parser.add_argument('--file', help='Add file to be parsed', default=False)

        arguments = self.parser.parse_args()
        if arguments.file:
            self.file = arguments.file

    def decode_Caesar_cipher(self):
        for character in self.encoded_text:
            self.decoded_text += self.alpha[(self.alpha.index(character) + self.offset) % len(self.alpha)]

    def read_file(self):
        with open(self.file) as file:
            self.encoded_text = file.read().strip()

    def run(self):
        if self.file:
            self.read_file()

        self.decode_Caesar_cipher()
        print(self.decoded_text)


decoder = DecodeFile()
decoder.run()
