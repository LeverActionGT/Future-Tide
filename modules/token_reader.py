import os
import sys

def tokens():
    #establish running directory
    crd = sys.path[0]

    #opens tokes.ini as a evaluated dict
    with open (os.path.join(crd, '../tokens.ini'), 'r') as tokenfile:
        tokenlist = tokenfile.readlines()
        tokens = eval(''.join(tokenlist))
    return tokens

#access tokens by using:
#
#import token_reader
#x = token_reader.tokens()['key']
#
tokens()