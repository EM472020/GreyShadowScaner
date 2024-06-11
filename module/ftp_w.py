from ftplib import FTP
import socket
from colorama import Fore, Style, init

def ftp_login_check(users, passwords, ip, port):
    init()
    num = 0
    max_retries = 3

    def connect_ftp():
        ftp_co = FTP()
        try:
            ftp_co.connect(ip, port, timeout=5)
            print(f"连接 {ip}:{port}")
            return ftp_co
        except socket.timeout:
            print("连接超时...")
            exit()
        except Exception as e:
            print(f"无法连接到 {ip}:{port}，错误: {e}")
            exit()

    ftp_co = connect_ftp()

    for user in users:
        for password in passwords:
            try:
                if num >= max_retries:
                    ftp_co = connect_ftp()
                    num = 0

                ftp_co.login(user, password)
                print(Fore.GREEN + f"登录成功: 用户名: {user}, 密码: {password}" + Style.RESET_ALL)
                ftp_co.quit()
                num = 0
                ftp_co = connect_ftp()
            except Exception as e:
                print(Fore.RED + f"登录失败: {e}, 用户名: {user}, 密码: {password}" + Style.RESET_ALL)
                num += 1

    ftp_co.quit()

