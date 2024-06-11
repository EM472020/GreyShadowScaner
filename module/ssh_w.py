import paramiko
import paramiko.ssh_exception
from colorama import Fore,Style,init


def ssh_login_check(user,password,ip_w,port_w=22):
    init()
    ssh_co=paramiko.SSHClient()

    ssh_co.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh_co.connect(hostname=ip_w,port=port_w,username=user,password=password,timeout=3)
        print(Fore.GREEN+f"登陆成功:{user},{password}"+ Style.RESET_ALL)
    except Exception as n:
        print(Fore.RED+f"登陆失败：{user},{password}:{n}"+Style.RESET_ALL)
        ssh_co.close()
def main(ip,port,user,password):
    for i in user:
        for j in password:
            ssh_login_check(i,j,ip,port)        
        


