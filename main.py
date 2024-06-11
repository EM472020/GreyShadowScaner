from module import fofa
from module.read_control import  thread_control
from  module.shodan_w import shodan_search
from module.vuln_scan import vuln_scan_poc
from module.vuln_scan import vuln_scan_exp
import colorama
import datetime




def picture():
    
    # 图片打印
    print(colorama.Fore.YELLOW+r'''
   ____                         ____                                               
  / ___|  _ __    ___   _   _  / ___|    ___    __ _   _ __    _ __     ___   _ __ 
 | |  _  | '__|  / _ \ | | | | \___ \   / __|  / _` | | '_ \  | '_ \   / _ \ | '__|
 | |_| | | |    |  __/ | |_| |  ___) | | (__  | (_| | | | | | | | | | |  __/ | |   
  \____| |_|     \___|  \__, | |____/   \___|  \__,_| |_| |_| |_| |_|  \___| |_|   
                        |___/                                                                
          '''+colorama.Style.RESET_ALL)


if __name__=='__main__':
    
    
    picture()
    # 死循环界面
    while True:
        print(colorama.Fore.YELLOW+"-----------------------------------------模式选择------------------------------------"+colorama.Style.RESET_ALL)
        print(colorama.Fore.RED+r'''
            
            *---------(1)信息收集
            
            *---------(2)漏洞扫描          
            
            *---------(3)退出
            '''+colorama.Style.RESET_ALL)
        # 第一层界面
        user_option1=int(input(colorama.Fore.BLUE+">>>"+colorama.Style.RESET_ALL))
        
        if user_option1==1:
            while True:
                
                          
                print(colorama.Fore.YELLOW+'''
                      
            *---------fofa(1)                          
            
            *---------shadon(2)
            
            *---------退出(3)
                      '''+colorama.Style.RESET_ALL)
                user_option2=int(input(colorama.Fore.BLUE+">>>"+colorama.Style.RESET_ALL))
                # 第二层界面（信息收集）
                if user_option2==1:     
            
                    print(colorama.Fore.RED+"初次使用信息收集模块需要到./module/fofa.py 里面设置好自己的fof api。"+colorama.Style.RESET_ALL)
                    print(colorama.Fore.YELLOW+"输入query进入查询模式。"+colorama.Style.RESET_ALL)
                    print(colorama.Fore.GREEN+"exit 退出"+colorama.Style.RESET_ALL)
                    while True:
                        user_input=input(colorama.Fore.BLUE+">>>"+colorama.Style.RESET_ALL)
                        if  user_input=='exit':
                            print("退出......")
                            break
                        elif user_input=='query':
                            user_querry=input(colorama.Fore.BLUE+"(fofa)>>"+colorama.Style.RESET_ALL)       
                            result=fofa.fofa_search(user_querry)
                            print(colorama.Fore.BLUE+"是否保存？Y/N"+colorama.Style.RESET_ALL)
                            user_input=input(colorama.Fore.BLUE+">>>"+colorama.Style.RESET_ALL)
                            if user_input=='Y':
                                current_time = datetime.datetime.now()
                                file_name = "fofa_" + current_time.strftime("%Y%m%d_%H%M%S") + ".txt"
                                with open(f"./search/{file_name}", "w") as file:                           
                                    print(result[1])
                                    for i in result:                                   
                                        i=str(i)
                                        file.write(i)
                                    file.close
                            else:
                                continue
                    # 信息收集第二层界面
                elif user_option2==2:
                    print(colorama.Fore.RED+"初次使用信息收集模块需要到./module/shodan_w.py 里面设置好自己的shodan api。"+colorama.Style.RESET_ALL)
                    print(colorama.Fore.YELLOW+"输入querry进入查询模式。"+colorama.Style.RESET_ALL)
                    print(colorama.Fore.GREEN+"exit 退出"+colorama.Style.RESET_ALL)
                    user_input=input(colorama.Fore.BLUE+">>>"+colorama.Style.RESET_ALL)
                    if  user_input=='exit':
                            print("退出......")
                            break
                    elif user_input=='query':
                            user_querry=input(colorama.Fore.BLUE+"(shodan)>>"+colorama.Style.RESET_ALL)       
                            result=shodan_search(user_querry)
                            print(colorama.Fore.BLUE+"是否保存？Y/N"+colorama.Style.RESET_ALL)
                            user_input=input(colorama.Fore.BLUE+">>>"+colorama.Style.RESET_ALL)
                            if user_input=='Y':
                                current_time = datetime.datetime.now()
                                file_name = "shodan_" + current_time.strftime("%Y%m%d_%H%M%S") + ".txt"
                                with open(f"./search/{file_name}", "w") as file:                           
                                    print(result[1])
                                    for i in result:                                   
                                        i=str(i)
                                        file.write(i)
                                    file.close
                            else:
                                continue
                    # 第二层（信息收集）退出
                elif user_option2==3:
                    print("退出.....")
                    break
                else:                             
                     print(colorama.Fore.RED+"没有的选项..."+colorama.Style.RESET_ALL)
                     continue
                 # 第一层界面
        elif user_option1==2:
            print(colorama.Fore.YELLOW+r'''
                
                *---------(1)端口服务爆破
                
                *---------(2)漏洞利用和扫描          
                
                *---------(3)退出
                '''+colorama.Style.RESET_ALL)
            while True:
                user_option2=int(input(colorama.Fore.BLUE+"(漏洞利用和扫描)>>>"+colorama.Style.RESET_ALL))
                # 第二层端口爆破界面
                if user_option2==1:
                    print(colorama.Fore.YELLOW+'''
                          
                *---------(1)ssh
                
                *---------(2)mysql          
                
                *---------(3)telnet
                   
                *---------(4)ftp       
                
                *---------(5)exit       
                          '''+colorama.Style.RESET_ALL)
                    while True:
                        # 第三层界面（端口爆破）
                        user_option3=int(input(colorama.Fore.BLUE+"(端口爆破)>>>"+colorama.Style.RESET_ALL))
                    
                        if user_option3==1:
                            user_thread=int(input(colorama.Fore.BLUE+"(ssh,指定爆破线程)>>>"+colorama.Style.RESET_ALL))
                            user_ip=str(input(colorama.Fore.BLUE+"(指定爆破ip)>>>"+colorama.Style.RESET_ALL))
                            user_port=int(input(colorama.Fore.BLUE+"(制定端口)>>>"+colorama.Style.RESET_ALL))
                            thread_control(user_thread,1,user_ip,user_port)
                            print(colorama.Fore.YELLOW+'''
                          
                *---------(1)ssh
                
                *---------(2)mysql          
                
                *---------(3)telnet
                   
                *---------(4)ftp       
                
                *---------(5)exit       
                          '''+colorama.Style.RESET_ALL)
                        # 地三层界面退出
                        elif user_option3==2:
                            user_thread=int(input(colorama.Fore.BLUE+"(mysql,指定爆破线程)>>>"+colorama.Style.RESET_ALL))
                            user_ip=str(input(colorama.Fore.BLUE+"(指定爆破ip)>>>"+colorama.Style.RESET_ALL))
                            user_port=int(input(colorama.Fore.BLUE+"(制定端口)>>>"+colorama.Style.RESET_ALL))
                            thread_control(user_thread,2,user_ip,user_port)
                            print(colorama.Fore.YELLOW+'''
                          
                *---------(1)ssh
                
                *---------(2)mysql          
                
                *---------(3)telnet
                   
                *---------(4)ftp       
                
                *---------(5)exit       
                          '''+colorama.Style.RESET_ALL)
                            
                        elif user_option3==3:
                            user_thread=int(input(colorama.Fore.BLUE+"(telnet,指定爆破线程)>>>"+colorama.Style.RESET_ALL))
                            user_ip=str(input(colorama.Fore.BLUE+"(指定爆破ip)>>>"+colorama.Style.RESET_ALL))
                            user_port=int(input(colorama.Fore.BLUE+"(制定端口)>>>"+colorama.Style.RESET_ALL))
                            thread_control(user_thread,3,user_ip,user_port)
                            print(colorama.Fore.YELLOW+'''
                          
                *---------(1)ssh
                
                *---------(2)mysql          
                
                *---------(3)telnet
                   
                *---------(4)ftp       
                
                *---------(5)exit       
                          '''+colorama.Style.RESET_ALL)
                        elif user_option3==4:
                            user_thread=int(input(colorama.Fore.BLUE+"(ftp,指定爆破线程)>>>"+colorama.Style.RESET_ALL))
                            user_ip=str(input(colorama.Fore.BLUE+"(指定爆破ip)>>>"+colorama.Style.RESET_ALL))
                            user_port=int(input(colorama.Fore.BLUE+"(制定端口)>>>"+colorama.Style.RESET_ALL))
                            thread_control(user_thread,4,user_ip,user_port)
                            print(colorama.Fore.YELLOW+'''
                          
                *---------(1)ssh
                
                *---------(2)mysql          
                
                *---------(3)telnet
                   
                *---------(4)ftp       
                
                *---------(5)exit       
                          '''+colorama.Style.RESET_ALL)
                        
                        elif user_option3==5:
                            print("退出......")
                            
                            break
                        else:
                            print(colorama.Fore.RED+"没有的选项..."+colorama.Style.RESET_ALL)
                            
                            continue
                elif user_option2==2:

                    while True:      
                        print(colorama.Fore.YELLOW+'''
                            
                    *---------(1)exp
                    
                    *---------(2)poc          
                    
                    *---------(3)连接远程数据

                    *---------(4)退出
                    
        
                            '''+colorama.Style.RESET_ALL)      
                        user_option2=int(input(colorama.Fore.BLUE+"(exp)>>>"+colorama.Style.RESET_ALL))
                        
                        # 第二层界面 exp和poc界面选择
                        if user_option2==1:
                            vuln_scan_exp()
                            continue
                        elif user_option2==2:
                            vuln_scan_poc()
                            continue
                        elif user_option2==3:
                            pass
                            continue
                        elif user_option2==4:
                            break
                elif user_option2==3:
                    print(colorama.Fore.YELLOW+r'''
                
                *---------(1)端口服务爆破
                
                *---------(2)漏洞利用和扫描          
                
                *---------(3)退出
                '''+colorama.Style.RESET_ALL)
                    print("退出.....")
                    break
                else:
                    print("没有的选项")
        elif user_option1==3:            
            print("GoodBye~")
            break
        else:
            print(colorama.Fore.RED+"没有的选项..."+colorama.Style.RESET_ALL)
            continue