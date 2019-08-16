import os 
import subprocess
# command = 'echo "hello world"'
# os.system(command)
# result = subprocess.check_output(command)
# print(result)
# subprocess.run(command, stdout=PIPE, shell=True).stdout
command = 'python '

args = ['xterm','-e',command]
# 第一个结束后，才能起第二个进程
# subprocess.run(args)
# subprocess.run(args)

# 同时进两个进程
subprocess.Popen(args)
subprocess.Popen(args)