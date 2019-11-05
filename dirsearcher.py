import os,sys
from threading import Thread

art ='''        |\      _,,,---,,_
ZZZzz /,`.-'`'    -.  ;-;;,_
     |,4-  ) )-,_. ,\ (  `'-'
    '---''(_/--'  `-'\_)  @wezzlaren '''

print(art)
print("")
print ("Enter IP:")
ip = input ()
print("")
class dirsearcher:
        def __init__(self,ip):
                self.ip = ip
        def nmapTarget():
            print('starting nmap scan')
            os.system(f'nmap -p- -Pn -sT -sV {ip} > /root/htb/dirsearcher/output/nmapscan.txt')
            print('nmap scan finished')
        def searchCommon():
            print('starting common.txt scan')
            os.system(f'gobuster -u {ip} -q -np -w /usr/share/wordlists/dirb/common.txt -x .txt,.pdf,.php > /root/htb/dirsearcher/output/common.txt')
            print('common scan finished')
        def searchMedium():
            print('starting medium.txt scan')
            os.system(f'gobuster -u {ip} -q -np -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x .txt,.pdf,.php > /root/htb/dirsearcher/output/medium.txt')
            print('medium scan finished')

if __name__ == '__main__':
        Thread(target = dirsearcher.nmapTarget).start()
        Thread(target = dirsearcher.searchCommon).start()
        Thread(target = dirsearcher.searchMedium).start()      

            

