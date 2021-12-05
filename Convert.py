# -*- coding: utf-8 -*-
import requests, re, os, time

banner=(
""" 
\x1b[0;97m
==============================
=TOOLS AMBIL TOKEN DAN COKIE =
=       NEW TOOLS 2021       =
==============================
= AU : RAMADHANI             =
= YT : M ALFIKRI R           =
==============================

\x1b[0;91m WORK python2 dan python3
							""")                                               
urls="https://business.facebook.com/business_locations"
_ses=requests.Session()

def real_time():
	from time import time
	return str(time()).split('.')[0]

def convert(cok):
	__for=(
			'datr='+cok['datr']
		)+';'+(
			'c_user='+cok['c_user']
		)+';'+(
			'fr='+cok['fr']
		)+';'+(
			'xs='+cok['xs'] )
	return __for
	
def save_agent(_agent):
	while True:
		try:
			_choic=raw_input("\x1b[0;93m[●] SIMPAN UA ? [Y/T] :\x1b[0;92m ")
		except:
			_choic=input("\x1b[0;93m[●] SIMPAN UA ? [Y/T] :\x1b[0;92m ")
		if _choic in ['ya', 'y', 'Y']:
			with open('agent.txt', 'w') as f:
				f.write(_agent)
				f.close()
				return
		elif _choic in ['t', 'T']:
			return
		else:
			continue

def email():
	os.system('clear')
	print(banner)
	print ('\x1b[0;96m BACA DULU BARU GUNAKAN ! ')
	
	print (' JIKA TIDAK SESUAI CARA DI BAWAH ')
	print (' AUTHOR TIDAK BERTANGUNG JAWAB ')
	print (' ATAS YANG TERJADI PADA AKUN ANDA ')
	print (' ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●')
	print (' 1.LOGIN AKUN DI BROWSER DULU')
	print (' 2.BUKA GOOGLE KETIK "MY USER AGENT" ')
	print (' 3.JIKA ADA COPY/SALIN !')
	print (' ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●')
	try:
		_agent=open('agent.txt').read()
	except:
		try:
			_agent=raw_input("\x1b[0;93m[●] MASUKAN USER AGENT :\x1b[0;92m ")
			save_agent(_agent)
		except:
			_agent=input("\x1b[0;93m[●] MASUKAN USER AGENT :\x1b[0;92m ")
			save_agent(_agent)
	try:
		user=raw_input("\x1b[0;93m[●] NO/ID/EMAIL :\x1b[0;92m ")
		pw=raw_input("\x1b[0;93m[●] PASWORD       :\x1b[0;92m ")
	except:
		user=input("\x1b[0;93m[●] NO/ID/EMAIL :\x1b[0;92m ")
		pw=input("\x1b[0;93m[●] PASWORD       :\x1b[0;92m ")
	try:
		_head={
			'Host':'m.facebook.com',
				'cache-control':'max-age=0',
			'upgrade-insecure-requests':'1',
				'user-agent':_agent,
			'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'sec-fetch-mode':'navigate',
				'sec-fetch-user':'?1',
			'sec-fetch-dest':'document',
				'accept-encoding':'gzip, deflate',
			'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
		}
		try:
			r=_ses.get("https://m.facebook.com/", headers=_head).text.encode('utf-8')
		except:
			r=_ses.get("https://m.facebook.com/", headers=_head).text
		_head2={
			'Host':'m.facebook.com',
				'user-agent':_agent,
			'content-type':'application/x-www-form-urlencoded',
				'x-fb-lsd':re.search('name="lsd" value="(.*?)"', str(r)).group(1),
			'accept':'*/*',
				'origin':'https://m.facebook.com',
			'sec-fetch-site':'same-origin',
				'sec-fetch-mode':'cors',
			'sec-fetch-dest':'empty',
				'referer':'https://m.facebook.com/',
			'accept-encoding':'gzip, deflate',
				'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
		}
		payload={
			"fb_dtsg":re.search('{"token":"(.*?)"', str(r)).group(1),
				"lsd":re.search('name="lsd" value="(.*?)"', str(r)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(r)).group(1),
				"m_ts":re.search('name="m_ts" value="(.*?)"', str(r)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(r)).group(1),
				"try_number":"0",
			"unrecognized_tries":"0",
				"prefill_contact_point":user,
			"prefill_source":"browser_dropdown",
				"prefill_type":"contact_point",
			"first_prefill_source":"browser_dropdown",
				"first_prefill_type":"contact_point",
			"had_cp_prefilled":True,
				"had_password_prefilled":False,
			"is_smart_lock":False,
				"bi_xrwh":"0",
			"__dyn":"",
				"__csr":"",
			"__req":"2",
				"__a":"",
			"__user":"0",
				"email":user,
			"encpass":"#PWD_BROWSER:0:"+real_time()+":"+pw
		}
		_ses.post("https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100", headers=_head2, data=payload)
		cok=_ses.cookies.get_dict()
		if 'c_user' in (cok):
			_head={
				'Host':'business.facebook.com',
					'cache-control':'max-age=0',
				'upgrade-insecure-requests':'1',
					'user-agent':'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36',
				'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
					'content-type' : 'text/html; charset=utf-8',
				'accept-encoding':'gzip, deflate',
					'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
			}    
			_r=_ses.get(urls, headers=_head)
			_p=re.search('(EAAG\w+)', _r.text)
			_token=_p.group(1)
			print('\n\x1b[0;93m[●] COOKIE :\x1b[0;92m '+convert(cok))
			print('\x1b[0;93m[●] TOKEN   :\x1b[0;92m '+_token )
			exit()
		elif 'checkpoint' in (cok):
			exit('\x1b[0;91m[●] AKUN TERKENA CP !')
		else:
			print('\x1b[0;91m[●] EMAIL/PW SALAH !')
			time.sleep(3)
			menu()
	except AttributeError:
		print('\x1b[0;91m[●] EMAIL/PW SALAH !')
		time.sleep(3)
		menu()

def cookie():
	os.system('clear')
	print(banner)
	try:
		_cookie=raw_input('\x1b[0;93m[●] Cokie :\x1b[0;92m ')
	except:
		_cookie=input('\x1b[0;93m[●] Cokie :\x1b[0;92m ')
	try:
		_head={
			'Host':'business.facebook.com',
				'cache-control':'max-age=0',
			'upgrade-insecure-requests':'1',
				'user-agent':'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36',
			'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
				'content-type' : 'text/html; charset=utf-8',
			'accept-encoding':'gzip, deflate',
				'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
			'cookie': _cookie
		}         
		_r=_ses.get(urls, headers=_head)
		_p=re.search('(EAAG\w+)', _r.text)
		_h=_p.group(1)
	        exit('\x1b[0;93m(+) Token :\x1b[0;92m '+_h)
	except (AttributeError, requests.exceptions.TooManyRedirects):
		print('\x1b[0;91m(×) cookie salah !')
		time.sleep(3)
		menu()
		
def menu():
	os.system("clear")
	print (banner)
	print("\x1b[0;96m[1] LOGIN CONVERT TOKEN+COOKIE")
	print("[2] COOKIE CONVERT TOKEN")
	print("[3] HAPUS UA/USER AGENT\n")
	while True:
		try:
			_cho=raw_input("[☆] Select : ")
		except:
			_cho=input("[☆] Select : ")
		if _cho in ['01', '1']:
			exit(email())
		elif _cho in ['02', '2']:
			exit(cookie())
		elif _cho in ['03', '3']:
			os.system('rm -rf agent.txt')
			print('[●] DELETED/TERHAPUS !')
			time.sleep(3)
			menu()
		else:
			continue

if __name__ == '__main__':
	menu()
