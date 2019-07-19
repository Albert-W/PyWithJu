import os 
import sys
# 
if os.getuid() == 0:
    pass
else:
    print('当前用户不是root, 请以root身分执行脚本 ')
    sys.exit(1)    
version = input('请输入想安装的版本')
if version == '2.7':
    url = '2.7'
elif version == '3.5':
    url = '3.5'
else: 
    print('please input ')
    sys.exit(1)

cmd = 'wget '+url 
res = os. system(cmd)
if res != 0 :
    print('download failure.')
    sys.exit(1)

if version == '2.7':
    package_name = 'Python-2.7.12'
else:
    package_name = 'Python-3.5.2'
cmd = 'tar xf '+package_name+'.tgz'
res = os.system(cmd)
if res !=0:
    os.system('rm '+package_name+'.tgz')
    print('please redownload again')
    sys.exit(1)

cmd = 'cd '+package_name+' && ./configure --prefix=/usr/local/python && make && make install'
res = os.system(cmd)
if res !=0 :
    print('complie failure')
    sys.exit(1)