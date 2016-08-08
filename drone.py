#!/usr/bin/python

import sys
import os
import json

try:
    argv = sys.argv[2]
    argv = json.loads(argv)
    # print str(argv)
    privateKey = argv['workspace']['keys']['private']
    # print 'Argv: ', privateKey
    with open("/root/.ssh/id_rsa", "w") as privateKeyFile:
        os.chmod("/root/.ssh/id_rsa", 0600)
        privateKeyFile.write(privateKey)
    os.system("ssh-keygen -f ~/.ssh/id_rsa -y > ~/.ssh/id_rsa.pub")
    os.system("eval \"$(ssh-agent -s)\"")
    os.system("ssh-add ~/.ssh/id_rsa")

except IndexError:
    print 'Not enough input arguments'