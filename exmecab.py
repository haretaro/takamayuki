import subprocess
from subprocess import PIPE

def wakati(input):
    cmd = 'mecab -O wakati'
    popen = subprocess.Popen(cmd.strip().split(' '),stdin=PIPE,stdout=PIPE)
    output = popen.communicate(input.encode('utf-8'))
    return output[0].decode('utf-8')
