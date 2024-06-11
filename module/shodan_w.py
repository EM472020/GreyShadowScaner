import shodan
import colorama

# 初始化 Colorama
colorama.init(autoreset=True)

# 设置你的 Shodan API 密钥
SHODAN_API_KEY = ''

def shodan_search(query, api=SHODAN_API_KEY):
    usr_shodan = shodan.Shodan(api)
    print(colorama.Fore.BLUE + r"""
          
  ____    _                   _                 
 / ___|  | |__     ___     __| |   __ _   _ __  
 \___ \  | '_ \   / _ \   / _` |  / _` | | '_ \ 
  ___) | | | | | | (_) | | (_| | | (_| | | | | |
 |____/  |_| |_|  \___/   \__,_|  \__,_| |_| |_|
                                                
          
          
          """ + colorama.Style.RESET_ALL)
    
    try:
        result = usr_shodan.search(query)
        total_results = result['total']
        print(f"总数量：{total_results}")

        if total_results == 0:
            return
        
        num_results = int(input(colorama.Fore.BLUE + "(请输入要显示的结果数量)>>>: " + colorama.Style.RESET_ALL))
        user_result_list=[]
        if num_results > total_results:
            num_results = total_results
        
        for i, resul in enumerate(result['matches']):
            if i >= num_results:
                break
            location = resul.get('location', {})
            ip = resul.get('ip_str', 'N/A')
            domains = ', '.join(resul.get('domains', ['N/A']))
            port = resul.get('port', 'N/A')
            city = location.get('city', 'N/A')
            region = location.get('region_code', 'N/A')
            country = location.get('country_name', 'N/A')
            os = resul.get('os', 'N/A')
            hostnames = ', '.join(resul.get('hostnames', ['N/A']))
            service = resul.get('product', 'N/A')
            print(colorama.Fore.RED + "="*100 + colorama.Style.RESET_ALL)
            print(f"IP: {ip}, 域名: {domains}, 端口: {port}, 位置: {city}, {region}, {country}, 操作系统: {os}, 主机名: {hostnames}, 服务: {service}")
            user_result=f"IP: {ip}, 域名: {domains}, 端口: {port}, 位置: {city}, {region}, {country}, 操作系统: {os}, 主机名: {hostnames}, 服务: {service}"+"\n"
            print(i)
            user_result_list.append(user_result)
        return user_result_list
    except shodan.APIError as e:
        print(f"Shodan API 错误: {e}")

if __name__=='__main__':

  while True:
      user_input = input(colorama.Fore.BLUE + "(shodan)>>>" + colorama.Style.RESET_ALL)
      if user_input.lower() == 'exit':
          break
      shodan_search(user_input)
