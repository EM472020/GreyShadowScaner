import threading
import colorama
from collections import Counter

from module import ssh_w
from module import mysql_w
from module import telnet_w
from module import ftp_w

#import ssh_w
#import mysql_w
#import telnet_w
#import ftp_w

def thread_control(nums, choices,ip, port=None):
        # 打开用户文本
    if choices==1:
        with open('../dict/admin.txt', 'r') as file:
            admin = file.read().splitlines()
        
        # 打开密码本
        with open('../dict/passwd.txt', 'r') as file:
            passwd = file.read().splitlines()
        
        # 分割 admin 列表到多个子列表
        k, m = divmod(len(admin), nums)
        admin_list = []
        for i in range(nums):
            start_index = i * k + min(i, m)
            end_index = (i + 1) * k + min(i + 1, m)
            admin_list.append(admin[start_index:end_index])
        print(admin_list)
        
        thread_list = []
        # 创建线程
        for i in range(nums):
            for user in admin_list:
                burp_thread = threading.Thread(target=ssh_w.main, kwargs={'user':user, 'password':passwd, 'ip':ip, 'port':port})
                burp_thread.start()
                thread_list.append(burp_thread)
        
        # 等待所有线程结束
        for burp_thread in thread_list:
            burp_thread.join()
    elif choices==2:
        with open('../dict/admin.txt', 'r') as file:
            admin = file.read().splitlines()
        
        # 打开密码本
        with open('../dict/passwd.txt', 'r') as file:
            passwd = file.read().splitlines()
        
        # 分割 admin 列表到多个子列表
        k, m = divmod(len(admin), nums)
        admin_list = []
        for i in range(nums):
            start_index = i * k + min(i, m)
            end_index = (i + 1) * k + min(i + 1, m)
            admin_list.append(admin[start_index:end_index])
        print(admin_list)
        
        thread_list = []
        # 创建线程
        for i in range(nums):
            for user in admin_list:
                burp_thread = threading.Thread(target=mysql_w.main, kwargs={'user':user, 'password':passwd, 'ip':ip, 'port':port})
                burp_thread.start()
                thread_list.append(burp_thread)
        
        # 等待所有线程结束
        for burp_thread in thread_list:
            burp_thread.join()
    elif choices==3:
        with open('../dict/admin.txt', 'r') as file:
            admin = file.read().splitlines()
        
        # 打开密码本
        with open('../dict/passwd.txt', 'r') as file:
            passwd = file.read().splitlines()
        
        # 分割 admin 列表到多个子列表
        k, m = divmod(len(admin), nums)
        admin_list = []
        for i in range(nums):
            start_index = i * k + min(i, m)
            end_index = (i + 1) * k + min(i + 1, m)
            admin_list.append(admin[start_index:end_index])
        print(admin_list)
        
        thread_list = []
        # 创建线程
        for i in range(nums):
            for user in admin_list:
                burp_thread = threading.Thread(target=telnet_w.telnet_login, kwargs={'users':user, 'passwords':passwd, 'ip':ip, 'port':port})
                burp_thread.start()
                thread_list.append(burp_thread)
        
        # 等待所有线程结束
        for burp_thread in thread_list:
            burp_thread.join()
    elif choices==4:
        with open('../dict/admin.txt', 'r') as file:
            admin = file.read().splitlines()
        
        # 打开密码本
        with open('../dict/passwd.txt', 'r') as file:
            passwd = file.read().splitlines()
        
        # 分割 admin 列表到多个子列表
        k, m = divmod(len(admin), nums)
        admin_list = []
        for i in range(nums):
            start_index = i * k + min(i, m)
            end_index = (i + 1) * k + min(i + 1, m)
            admin_list.append(admin[start_index:end_index])
        print(admin_list)
        
        thread_list = []
        # 创建线程
        for i in range(nums):
            for user in admin_list:
                burp_thread = threading.Thread(target=ftp_w.ftp_login_check, kwargs={'users':user, 'passwords':passwd, 'ip':ip, 'port':port})
                burp_thread.start()
                thread_list.append(burp_thread)
    else:
        print(colorama.Fore.RED+"没有的选项....."+colorama.Style.RESET_ALL)
        
        # 等待所有线程结束
        for burp_thread in thread_list:
            burp_thread.join()
