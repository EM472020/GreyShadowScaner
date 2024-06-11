import mysql.connector
from colorama import Fore,Style,init

def mysql_login(user,passwd,ip,port):
    
    init()
    try:
        conn=mysql.connector.connect(host=ip,port=port,user=user,password=passwd)
        print(Fore.GREEN+f"登陆成功:{user},{passwd}"+Style.RESET_ALL)
    except mysql.connector.Error as n:
        print(Fore.RED+f"登陆失败：{n},{user},{passwd}"+Style.RESET_ALL)

def main(user,password,ip,port=3306):
    for i in user:
        for j in password:
            mysql_login(i,j,ip,port)