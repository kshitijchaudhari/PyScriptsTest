import platform
import os
import subprocess

def test():
    p1 = subprocess.run(['dir', '*.*'], capture_output=True, shell=True)
    print(p1.stdout.decode())
    print(p1)

test()