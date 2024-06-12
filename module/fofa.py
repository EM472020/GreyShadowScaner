import requests
import base64
from colorama import Fore,Style,init

# 在这里设置你的api
def fofa_search(query, api_key='qLGi7bseJTW1Fl41'):
    text_keeper=[]
    print(Fore.BLUE+r'''
     _____    ___    _____      _    
    |  ___|  / _ \  |  ___|    / \   
    | |_    | | | | | |_      / _ \  
    |  _|   | |_| | |  _|    / ___ \ 
    |_|      \___/  |_|     /_/   \_\ '''+Style.RESET_ALL)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; PCRT00 Build/N2G48H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.158 Safari/537.36 fanwe_app_sdk sdk_type/android sdk_version_name/4.0.1 sdk_version/2020042901 screen_width/720 screen_height/1280',
    }

    b_base64_query = base64.b64encode(query.encode('utf-8')).decode('utf-8') 
    c_url = f"https://fofa.red/api/v1/search/all?key={api_key}&page=1&size=1000&fields=host,ip,domain,port,protocol,server,version&qbase64={b_base64_query}" 
    # 请求
    response = requests.get(url=c_url, headers=headers)
    if response.status_code != 200:
        print("查询失败。")
    else:
        print("查询成功。")
        data = response.json()
        contexts = data.get("results")  # 保存结果
    try:
        for i in contexts:
            
            result=f"结果：主机:{i[0]},ip地址:{i[1]},域名:{i[2]},协议:{i[3]},服务:{i[4]},版本:{i[5]}"
            
            
            print(result)
            text_keeper.append(result+"\n")
        return text_keeper
            
            
            
    except  TypeError as e:
        print(e)   
        return e
       
    





#def huge_check():
    #pass

r"""
if __name__ == '__main__':
    
    init()
    #在这里修改你的api
    api = 'qLGi7bseJTW1Fl41'
    print(Fore.BLUE+r'''
  _____    ___    _____      _    
 |  ___|  / _ \  |  ___|    / \   
 | |_    | | | | | |_      / _ \  
 |  _|   | |_| | |  _|    / ___ \ 
 |_|      \___/  |_|     /_/   \_\ '''+Style.RESET_ALL)
    
    while True:
    
        words = str(input(Fore.RED+'输入fofa查询语法:'+Style.RESET_ALL))

        if words=='exit' or words=='quit':
            print("退出")
            break
        elif not words:
            print(Fore.GREEN+">_'     Go ahead!"+Style.RESET_ALL)
            continue
        elif words=='help' or words=='h':
            print('''

                  
=      匹配，=""时，可查询不存在字段或者值为空的情况。 
==     完全匹配，==""时，可查询存在且值为空的情况。 
&&      与 
||      或 
!=      不匹配，!=""时，可查询值不为空的情况。 
*=      模糊匹配，使用*或者?进行搜索，比如banner*="mys??" (个人版及以上可用)。 
()       确认查询优先级，括号内容优先级最高。 
 

关于建站软件的搜索语法请参考：组件列表
基础类（General）
语法 	        例句 	                                             用途说明 	           
ip 	            ip="1.1.1.1" 	                                    通过单一IPv4地址进行查询 	
            ip="220.181.111.1/24" 	                                通过IPv4 C段进行查询 	
            ip="2600:9000:202a:2600:18:4ab7:f600:93a1" 	            通过单一Ipv6地址进行查询 	

                  
语法 	        例句 	                                             用途说明 	                 
port 	      port="6379" 	                                        通过端口号进行查询 

domain 	      domain="qq.com" 	                                    通过根域名进行查询 	
host 	      host=".fofa.info" 	                                通过主机名进行查询 
os 	          os="centos" 	                                        通过操作系统进行查询 	
server 	      server="Microsoft-IIS/10" 	                        通过服务器进行查询 
asn 	      asn="19551" 	                                        通过自治系统号进行搜索 	
org 	      org="LLC Baxet" 	                                    通过所属组织进行查询 	
is_domain 	  is_domain=true 	                                    筛选拥有域名的资产 	
              is_domain=false 	                                    筛选没有域名的资产 	
is_ipv6 	is_ipv6=true 	                                        筛选是ipv6的资产 	
            is_ipv6=false 	                                        筛选是ipv4的资产 

                  
标记类（Special Label）
语法 	            例句 	                                             用途说明 	
app 	    app="Microsoft-Exchange" 	                               通过FOFA整理的规则进行查询 	
fid 	    fid="sSXXGNUO2FefBTcCLIT/2Q==" 	                           通过FOFA聚合的站点指纹进行查询 	
product 	    product="NGINX" 	                                   通过FOFA标记的产品名进行查询 	
category 	    category="服务" 	                                    通过FOFA标记的分类进行查询 	
type 	        type="service" 	                                           筛选协议资产 	
                type="subdomain" 	                                       筛选服务（网站类）资产 	
cloud_name 	    cloud_name="Aliyundun" 	                                   通过云服务商进行查询 	
is_cloud 	    is_cloud=true 	                                           筛选是云服务的资产 	
                is_cloud=false 	                                           筛选不是云服务的资产 	
is_fraud 	    is_fraud=true 	                                           筛选是仿冒垃圾站群的资产 （专业版及以上） 	
                is_fraud=false 	                                           筛选不是仿冒垃圾站群的资产（已默认筛选） 	
is_honeypot 	is_honeypot=true 	                                       筛选是蜜罐的资产 （专业版及以上） 	
                is_honeypot=false 	                                       筛选不是蜜罐的资产（已默认筛选） 	


协议类 （type=service)
语法 	                    例句 	                                    用途说明 	
protocol 	                protocol="quic" 	                        通过协议名称进行查询 	
banner 	                        banner="users"                         	通过协议返回信息进行查询 	
base_protocol 	                base_protocol="udp" 	                查询传输层为udp协议的资产 	
                                base_protocol="tcp" 	                查询传输层为tcp协议的资产 	

网站类（type=subdomain）
语法 	                       例句 	                                            用途说明 	
title 	                       title="beijing" 	                                通过网站标题进行查询 	
header 	                       header="elastic" 	                            通过响应标头进行查询 	
header_hash 	                header_hash="1258854265" 	                    通过http/https响应头计算的hash值进行查询 （个人版及以上） 	
body 	                        body="网络空间测绘" 	                          通过HTML正文进行查询 	
body_hash 	                    body_hash="-2090962452" 	                    通过HTML正文计算的hash值进行查询 	
js_name 	                    js_name="js/jquery.js"                    	    通过HTML正文包含的JS进行查询 	
js_md5 	                        js_md5="82ac3f14327a8b7ba49baa208d4eaa15" 	    通过JS源码进行查询 	
cname 	                        cname="ap21.inst.siteforce.com" 	            通过别名记录进行查询 	
cname_domain 	                cname_domain="siteforce.com" 	                通过别名记录解析的主域名进行查询 	
icon_hash 	                    icon_hash="-247388890" 	                        通过网站图标的hash值进行查询 	
status_code 	                status_code="402" 	                            筛选服务状态为402的服务（网站）资产 	
icp 	                        icp="京ICP证030173号" 	                        通过HTML正文包含的ICP备案号进行查询 
sdk_hash 	                    sdk_hash=="Mkb4Ms4R96glv/T6TRzwPWh3UDatBqeF" 	通过网站嵌入的第三方代码计算的hash值进行查询 （商业版及以上） 	

                  
地理位置（Location）
语法 	                            例句 	                                        用途说明 	
country 	                        country="CN" 	                                通过国家的简称代码进行查询 	
                                    country="中国"                                 	通过国家中文名称进行查询 	
region 	                            region="Zhejiang" 	                            通过省份/地区英文名称进行查询 	
                                    region="浙江" 	                                通过省份/地区中文名称进行查询（仅支持中国地区） 	
city 	                            city="Hangzhou" 	                            通过城市英文名称进行查询 	


                  
证书类
语法 	                            例句 	                                                               用途说明 	
cert 	                            cert="baidu" 	                                                    通过证书进行查询 	
cert.subject 	                    cert.subject="Oracle Corporation" 	                                通过证书的持有者进行查询 	
cert.issuer 	                    cert.issuer="DigiCert" 	                                            通过证书的颁发者进行查询 	
cert.subject.org 	                cert.subject.org="Oracle Corporation" 	                            通过证书持有者的组织进行查询 	
cert.subject.cn 	                cert.subject.cn="baidu.com" 	                                    通过证书持有者的通用名称进行查询 	
cert.issuer.org 	                cert.issuer.org="cPanel, Inc." 	                                    通过证书颁发者的组织进行查询 	
cert.issuer.cn 	                    cert.issuer.cn="Synology Inc. CA" 	                                通过证书颁发者的通用名称进行查询 	
cert.is_valid 	                    cert.is_valid=true 	                                                筛选证书是有效证书的资产 （个人版及以上） 	
                                    cert.is_valid=false 	                                            筛选证书是无效证书的资产 （个人版及以上） 	
cert.is_match 	                    cert.is_match=true 	                                                筛选证书和域名匹配的资产 （个人版及以上） 	
                                    cert.is_match=false 	                                            筛选证书和域名不匹配的资产 （个人版及以上） 	
cert.is_expired 	                cert.is_expired=true 	                                            筛选证书已过期的资产 （个人版及以上） 	
                                    cert.is_expired=false 	                                            筛选证书未过期的资产 （个人版及以上） 	
jarm 	        jarm="2ad2ad0002ad2ad22c2ad2ad2ad2ad2eac92ec34bcc0cf7520e97547f83e81" 	                通过JARM指纹进行查询 	
tls.version 	                    tls.version="TLS 1.3" 	                                            通过tls的协议版本进行查询 	
tls.ja3s 	                tls.ja3s="15af977ce25de452b96affa2addb1036" 	                            通过tls的ja3s指纹进行查询 	
                  

                  
时间类（Last update time）
语法 	                                例句 	                                                            用途说明 	
after 	                        after="2023-01-01" 	                                                筛选某一时间之后有更新的资产 	
before 	                        before="2023-12-01" 	                                            筛选某一时间之前有更新的资产 	
after&before 	                after="2023-01-01" && before="2023-12-01" 	                        筛选某一时间区间有更新的资产 

                  
独立IP语法（独立IP系列语法，不可和上面其他语法共用）

语法 	                             例句 	                                                                    用途说明 	
port_size 	                        port_size="6" 	                                                筛选开放端口数量等于6个的独立IP （个人版及以上） 	
port_size_gt 	                    port_size_gt="6" 	                                            筛选开放端口数量大于6个的独立IP （个人版及以上） 	
port_size_lt 	                    port_size_lt="12" 	                                            筛选开放端口数量小于12个的独立IP （个人版及以上）
ip_ports 	                        ip_ports="80,161" 	                                            筛选同时开放不同端口的独立IP 	
ip_country 	                        ip_country="CN" 	                                            通过国家的简称代码进行查询独立IP 	
ip_region 	                        ip_region="Zhejiang" 	                                        通过省份/地区英文名称进行查询独立IP 	
ip_city 	                        ip_city="Hangzhou"  	                                        通过城市英文名称进行查询独立IP 	
ip_after 	                        ip_after="2021-03-18" 	                                        筛选某一时间之后有更新的独立IP 	
ip_before 	                        ip_before="2019-09-09" 	                                        筛选某一时间之前有更新的独立IP 	 
''')
        else:
            fofa_search(words, api)
            continue
            """