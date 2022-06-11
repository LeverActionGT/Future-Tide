import os
import sys

def configs():
    #establish running directory
    crd = sys.path[0]

    #opens tokes.ini as a evaluated dict
    with open (os.path.join(crd,'configs.ini'), 'r') as configfile:
        configlist = configfile.readlines()
        configs = eval(''.join(configlist))
    return configs

#access configs by using:
#
#import config_reader
#config_reader.configs['key']
#
configs()