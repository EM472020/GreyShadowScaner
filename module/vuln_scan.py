import os
from importlib import util
import colorama
import sys

def vuln_scan_poc():
    
    # 获取制定目录下面的所有文件。
    files=os.listdir(r'./vulnerability/poc')
    files=list(files)
    #转换为列表
    for i in files:
        print(f"{files.index(i)},{i}")    
    while True:
        #用户选择文件
        try:
            user_choice=int(input(colorama.Fore.BLUE+"(选择一个执行poc)>>>"+colorama.Style.RESET_ALL))
            if 0<=user_choice<len(files):
                choices=files[user_choice]
                break
            else:
                print(colorama.Fore.RED+"没这个文件"+colorama.Style.RESET_ALL)            
        except ValueError:
            print(colorama.Fore.RED+f"{user_choice}这可不是一个有效的数字。"+colorama.Style.RESET_ALL)
        #动态加载用户选择的文件，并运行其中的main函数。（动态加载模块由chatgpt4o 指导修改。）
    
    file_path=os.path.join(r'./vulnerability/poc',choices)
    spec=util.spec_from_file_location("module",file_path)
    module=util.module_from_spec(spec)
    sys.modules["module"]=module
    #执行模块
    spec.loader.exec_module(module)
    if hasattr(module,"main"):
        module.main()
    else:
        print(colorama.Fore.RED+"该模块尚未规范化"+colorama.Style.RESET_ALL)

def vuln_scan_exp():
        # 获取制定目录下面的所有文件。
    files=os.listdir(r'./vulnerability/exp')
    files=list(files)
    #转换为列表
    for i in files:
        print(f"{files.index(i)},{i}")    
    while True:
        #用户选择文件
        try:
            user_choice=int(input(colorama.Fore.BLUE+"(选择一个执行exp)>>>"+colorama.Style.RESET_ALL))
            if 0<=user_choice<len(files):
                choices=files[user_choice]
                break
            else:
                print(colorama.Fore.RED+"没这个文件"+colorama.Style.RESET_ALL)            
        except ValueError:
            print(colorama.Fore.RED+f"{user_choice}这可不是一个有效的数字。"+colorama.Style.RESET_ALL)
        #动态加载用户选择的文件，并运行其中的main函数。（动态加载模块由chatgpt4o 指导修改。）
    
    file_path=os.path.join(r'./vulnerability/poc',choices)
    spec=util.spec_from_file_location("module",file_path)
    module=util.module_from_spec(spec)
    sys.modules["module"]=module
    #执行模块
    spec.loader.exec_module(module)
    if hasattr(module,"main"):
        module.main()
    else:
        print(colorama.Fore.RED+"该模块尚未规范化"+colorama.Style.RESET_ALL)

def sniper_mode():
    print(colorama.Fore.YELLOW+'''
          
          
          
          '''+colorama.Style.RESET_ALL)

