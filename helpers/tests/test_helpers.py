#!/usr/bin/env python

import os
from os import path
import sys
from subprocess import PIPE
sys.path.append(path.join(path.dirname(path.abspath(__file__)), os.pardir))

import helpers as h


def main():
    h.call(['echo', '1'])
    h.check_call('echo 2', shell=True)

    ret = h.check_output(['echo', '3']).strip()
    print ret
    assert ret == '3'

    proc = h.Popen(['echo', '4'], stdout=PIPE)
    ret = proc.communicate()[0].strip()
    print ret
    assert ret == '4'

    print h.parse_remote('ubuntu@8.8.8.8:~/pantheon')
    print h.get_open_port()
    h.make_sure_path_exists(h.pantheon_tmp())
    print h.parse_config()


if __name__ == '__main__':
    main()
