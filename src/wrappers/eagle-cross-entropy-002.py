#!/usr/bin/env python
from os import path
from subprocess import check_call
import subprocess

import arg_parser
import context

def main():
        args = arg_parser.sender_first()
        cc_repo = path.join(context.third_party_dir, 'gold-IRL')
        send_src = path.join(cc_repo, 'sender-receiver/sender-receiver/sender_receiver/envs', 'example_xentropy.py')
        recv_src = path.join(cc_repo, 'sender-receiver/sender-receiver/sender_receiver/envs', 'run_receiver.py')
        model_name = 'Eagle-Cross-Entropy-002-model-xentropy-60spe_bs_5_pc_70-670iter-rw209.pt'#'model-xentropy-0.01decay10iter-770iter.pt' # change - also look at directories involved
        #dependencies = path.join(cc_repo, 'dependencies.sh')
        if args.option == 'setup':
            #check_call(dependencies, shell = True)
            return

        if args.option == 'sender':
            cmd = ['python3', send_src, args.port, '--model=' + model_name, '--expert', 'synthesizedBBR'] # change
            subprocess.check_output(cmd)
            return

        if args.option == 'receiver':
            cmd = ['python3', recv_src, args.ip, args.port]
            subprocess.check_output(cmd)
            return

if __name__ == "__main__":
        main()
