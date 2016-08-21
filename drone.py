#!/usr/bin/python

import sys
import os
import json
import subprocess
import shlex

try:
    argv = sys.argv[2]
    print argv
    argv = json.loads(argv)
    privateKey = argv['workspace']['keys']['private']
    print '[+] Setup injected private key'
    with open("/root/.ssh/id_rsa", "w") as privateKeyFile:
        os.chmod("/root/.ssh/id_rsa", 0600)
        privateKeyFile.write(privateKey)
    os.system("ssh-keygen -f ~/.ssh/id_rsa -y > ~/.ssh/id_rsa.pub")
    os.system("eval \"$(ssh-agent -s)\"")
    os.system("ssh-add ~/.ssh/id_rsa")
    # run pre commands
    print '[+] Running pre commands'
    pre_commands = argv['vargs']['pre_commands']
    for command in pre_commands:
        print '[+] Running:', command
        print subprocess.check_output(shlex.split(command))
    print '[+] Running ssh commands'

except Exception, e:
    print e
