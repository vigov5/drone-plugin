#!/usr/bin/python

import sys
import os
import json
import subprocess

try:
    argv = sys.argv[2]
    argv = json.loads(argv)
    privateKey = argv['workspace']['keys']['private']
    print '[+] Setup injected private key'
    with open("/root/.ssh/id_rsa", "w") as privateKeyFile:
        os.chmod("/root/.ssh/id_rsa", 0600)
        privateKeyFile.write(privateKey)
    # cd to path
    src_path = argv['workspace']['path']
    if src_path:
        print '[+] cd to', src_path
        os.chdir(src_path)
        print os.getcwd()
    # run commands
    print '[+] Running commands'
    commands = argv['vargs']['commands']
    print '[+] Running following commands'
    for command in commands:
        print '[+]', command
    process = subprocess.Popen(";".join(commands), stdout=subprocess.PIPE, shell=True)
    print process.communicate()[0].strip()

except Exception, e:
    print e
