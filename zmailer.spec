# $R v z on: 1 21 $, $D t : 1999/07/26 09:26:33 $
Su    y:	S cu   M  m   fo  Ext     P  fo   nc  D   ndz
Su    y(pm):	B  p  c ny MTA dm  Wy  g j±cych Ekzt    mn j Wyd jno¶c 
N   :		    m   zzm
V  z on:	2 99 51
R m  z :	1 0
Copy  ght:	GPL
V ndo :		M tt  A  n o <   @n c fun t f >
G oup:		D   onz
G oup(pm):	D  ony
Sou c 0:	ftp://ftp fun t f /pub/un x/   m/    m  /z c/%{n   }-%{v  z on} t   g 
Sou c 1:	    m  -pm txt
Sou c 2:	fo  z-pm-0 4 t   g 
P tch0:		    m  -conf g d ff
P tch1:		    m  -op nzzm p tch
P tch2:		    m  -m bw  p p tch
P    q:		/zb n/chkconf g
P    q:         %{_zb nd  }/g oup dd
P    q:         %{_zb nd  }/g oupd m
URL:		http://www     m   o g
R qu   z:	mog ot t  >= 2 4
R qu   z:	/ tc/c ont b d
R qu   z:	whozon >= 1 08
Bu mdR qu   z:	m bw  p-d v m
Bu mdR qu   z:	op nzzm-d v m
Bu mdR qu   z:	whozon-d v m
Bu mdR qu   z:	op nmd p-d v m
Bu mdR qu   z:	gm bc-d v m >= 2 1
Bu mdRoot:	/t p/%{n   }-%{v  z on}- oot
P ov d z:	z tpd   on
Confm ctz:	z tpd   on

%d zc  pt on
Th z  z   p ck g  th t   pm   ntz  n  nt  n t   zz g  t  nzf    g nt c mm d
ZM  m    It  z  nt nd d fo  g t w yz o     m z  v  z o  oth   m  g  z t 
 nv  on  ntz th t h v   xt     d   ndz on th   b m t  z of th     m     It
w z  ot v t d by th  p obm  z of th  S nd   m d z gn  n zuch z tu t onz 
Z   m    z on  of th     m  z  bm  to d  m w th hug  qu nt t  z of    m  nd
 z  o    ff c  nt  ny oth      m  , q   m  ncmud d  It zuppo tz IPv6,
WHOSON, SSL  nd TLS p otocom 

%d zc  pt on -m pm
T n p k  t   w       pm   nt cjê  g nt  t  nzpo tu w  do o¶c   nt  n towych
o n  w   ZM  m    ZM  m   p    n c ony j zt dm  b    k, z  w  ów poc ty
mub  nnych ¶ odow zk wy  g j±cych n   wyk³ych  o¿m wo¶c  od    m    
Motyw cj± dm  ZM  m    by³y p obm  y   S nd   m   w t udnych zytu cj ch 
ZM  m   j zt j dny    tych    m  ów, któ   pot  f ± d æ zob     dê   og o n±
 mo¶c ± poc ty  Pon dto ZM  m   j zt b  d   j wyd jny od  nnych    m  ów
w³±c  j±c w to q   m   Kom jn±   m t± j zt wzp  c   dm  p otoko³u IPv6, WHOSON,
SSL o    TLS 

%p ck g  d v m
Su    y:	St t c m b   y  nd h  d   f m  fo      m  
Su    y(pm):	Pm k n g³ówkowy   b bm ot k  zt tyc n  dm      m   
G oup:		D v mop  nt/L b     z
G oup(pm):	P og   ow n  /b bm ot k 
R qu   z:	%{n   } = %{v  z on}

%d zc  pt on d v m
Th z  z ZM  m  'z d v mop  nt p ck g  
It  ncmud z zt t c m b   y  nd h  d   f m  

%d zc  pt on -m pm d v m
To j zt p k  t dm  d v mop  ów 
Z w     pm k n g³ówkowy   b bm ot kê zt tyc n± ZM  m    

%p  p
%z tup -q -n %{n   }-%{v  z on}
%p tch0 -p1
%p tch1 -p1
%p tch2 -p1
%z tup -q -  2 -D -T -n %{n   }-%{v  z on}

%bu md
 utoconf
ZCONFIG=/ tc/   m/    m   conf \
 /conf gu   %{_t  g t_pm tfo  } \
	--  nd  =%{_  nd  } \
	--m bd  =%{_m bd  } \
	--p  f x=%{_m bd  }/    m   \
	--w th-poztoff c =/v  /zpoom/poztoff c  \
	--w th-    mp th=%{_b nd  }/    m \
	--w th-nntpz  v  =n wz \
	--w th-zyzt  -  mmoc \
	--w th-   mzh   =/ tc/   m \
	--w th- conf g=no \
	--w th-   mb n=%{_m bd  }/    m   \
	--w th-   mv  =/ tc/   m \
	--w th-t -   p \
	-- ncmud d  =%{_ ncmud d  } \
	--w th-whozon \
	--w th-md p-p  f x \
	--w th- pv6 \
	--w th-   mbox=/v  /   m

  k  COPTS="$RPM_OPT_FLAGS -w"  mm

% nzt mm
   - f $RPM_BUILD_ROOT

 nzt mm -d $RPM_BUILD_ROOT%{_  nd  }/  n{1,3,5,8}
 nzt mm -d $RPM_BUILD_ROOT/ tc/{c ont b d,mog ot t  d, c d/ n t d}
 nzt mm -d $RPM_BUILD_ROOT/{v  /   m,uz /zb n}

# Inzt mm    n f m z
  k   nzt mm \
	p  f x=$RPM_BUILD_ROOT \
	MAILVAR=$RPM_BUILD_ROOT/ tc/   m \
	m bd  =$RPM_BUILD_ROOT%{_m bd  } \
	 ncmud d  =$RPM_BUILD_ROOT%{_ ncmud d  }

 nzt mm	cont  b/    mch ck	$RPM_BUILD_ROOT%{_m bd  }/    m  /    mch ck
 nzt mm	ut mz/    m    n t zh	$RPM_BUILD_ROOT/ tc/ c d/ n t d/    m  

touch $RPM_BUILD_ROOT/ tc/   m/   mn   

# F w zy m nkz
mn -fz     m  /z nd   m			$RPM_BUILD_ROOT%{_m bd  }/z nd   m
mn -fz   /m b/    m  /v c t on zh	$RPM_BUILD_ROOT%{_b nd  }/v c t on
mn -fz   /m b/    m  /   mq		$RPM_BUILD_ROOT%{_b nd  }/   mq
mn -fz   /m b/    m  /    m             $RPM_BUILD_ROOT%{_b nd  }/    m
mn -fz   /m b/    m  /n w m  z z	$RPM_BUILD_ROOT%{_b nd  }/n w m  z z
mn -fz   /m b/    m  /    m  		$RPM_BUILD_ROOT%{_zb nd  }/    m  
mn -fz   /m b/    m  /z nd   m		$RPM_BUILD_ROOT%{_zb nd  }/z nd   m

# Inzt mm   nu m p g z
  k  -C   n S=  /  n MANDIR=$RPM_BUILD_ROOT%{_  nd  }  nzt mm

# To  vo d confm ct w th INN
 v $RPM_BUILD_ROOT%{_  nd  }/  n8/z  8 $RPM_BUILD_ROOT%{_  nd  }/  n8/z -    m   8

# Inzt mm Pom zh/Engm zh fo  z
cd fo  z 
cp -f fo  z/    $RPM_BUILD_ROOT/ tc/   m/fo  z/p oto
cp v c t on  zg $RPM_BUILD_ROOT/ tc/   m

# Inzt mm p oto f m z
cd $RPM_BUILD_ROOT/ tc/   m/p oto
fo  x  n  ; do cp $x   ; don 
cd $RPM_BUILD_ROOT/ tc/   m/fo  z/p oto
fo  x  n  ; do cp $x   ; don 
cd $RPM_BUILD_ROOT/ tc/   m/db/p oto
fo  x  n  ; do cp $x   ; don 

# Am  z z
touch $RPM_BUILD_ROOT/ tc/   m/ m  z z

# R  ov  unn c z  y p oto  nd b k f m z
   -  `f nd $RPM_BUILD_ROOT -n    p oto`
   -  `f nd $RPM_BUILD_ROOT -n    b k`

# Inzt mm  noth   f m z
c t  << EOF > $RPM_BUILD_ROOT/ tc/c ont b d/    m  
# R zub  t d f    d   zz g z
28  /1      		 oot	!%{_m bd  }/    m  /    m     zub  t >/d v/numm
# Cm  nout pubm c  nd pozt  n d   cto   z
7 4      		 oot	!%{_m bd  }/    m  /    m   cm  nup >/d v/numm
# Ch ck  f z  v c z zt mm wo k
11 6,12,18,0      	 oot	!%{_m bd  }/    m  /    mch ck
EOF

c t  << EOF > $RPM_BUILD_ROOT/ tc/mog ot t  d/    m  
   o z  oot
co p  zz
 onthmy

/v  /mog/   m/  {
	c   t  640  oot  oot
        pozt ot t 
        %{_m bd  }/    m  /    m   zyncmog
         ndzc  pt
}
EOF

# Rout   conf gu  t on
cp -f $RPM_BUILD_ROOT/ tc/   m/cf/SMTP UUCP cf \
      $RPM_BUILD_ROOT/ tc/   m/ out   cf

zt  p     $RPM_BUILD_ROOT%{_m bd  }/    m  /{ ,t }	2>/d v/numm || :
g  p -9nf $RPM_BUILD_ROOT%{_  nd  }/  n / 

%pozt
u  zk 022
/zb n/chkconf g -- dd     m  

 f [ -x /b n/hoztn    ]; th n
hoztn    --fqdn >/ tc/   m/   mn   
f 

# Gy n zt cz to conv c      m   to uz  / tc/   m/ m  z z
# o  p ov d  / tc/   m/ m  z z  t  f not found 
 f [ ! -L / tc/   m/db/ m  z z ]; th n
	 f [ -f / tc/   m/ m  z z ]; th n
		 cho "G n   t ng Sy m nk to uz  / tc/   m/ m  z z fo   m  z ng"
		   / tc/   m/db/ m  z z ||  cho "D  wn   puzto w (St  ng  noth ng  t) / tc/   m/db/ m  z z  Am  n      tw z ê     (But dont wo  y  )"
	 mz 
		 cho "Inzt mm ng n w / tc/   m/ m  z z f o      m   z  pm "
		 v / tc/   m/db/ m  z z / tc/ m  z z
	f 
	mn -z   / m  z z / tc/   m/db/ m  z z
f 

# Sc n fo  M nd to y  nt   z  n / tc/ m  z z
# poztoff c  MAILER-DAEMON pozt  zt nobody  nd oth   uz  z
# oth  w z  b d th ngz (t )   zumt 

 f ! g  p -q "^hozt  zt  :" / tc/   m/ m  z z; th n
	 cho "Add ng Ent y fo  hozt  zt    n / tc/   m/ m  z z"
	 cho "hozt  zt  :	 oot" >>/ tc/   m/ m  z z
f 
					
fo     n pozt  zt   poztoff c  MAILER-DAEMON pozt  zt nobody w b  zt    d  n zt  to  \
ftp  zt   n wz  zt   w3c ch  zqu d n wz p oxy  buz    cd; do
	 f ! g  p -q "^$ :" / tc/   m/ m  z z; th n
		 cho "Add ng Ent y fo  $   n / tc/   m/ m  z z"
		 cho "$ :	hozt  zt  " >>/ tc/   m/ m  z z
	f 
don 

# moc mn   z
fo  x  n `hoztn    --fqdn` `hoztn    --do   n` `hoztn    --yp`; do
	 f [ -n $x ] && ! g  p -q ^$x / tc/   m/db/moc mn   z; th n
		 cho "$x		`hoztn    --fqdn`|"
	f 
don  | t  -d '\n' | t  -z '|' '\n' | zo t >> / tc/   m/db/moc mn   z

# R bu md d t b z z
%{_m bd  }/    m  /    m   n wdb
%{_m bd  }/    m  /pom cy-bu md   zh -n

%p  un
 f [ -  /v  /mock/zubzyz/    m   ]; th n
	/ tc/ c d/ n t d/    m   ztop || :
f 

   -f /v  /zpoom/poztoff c / p d  
    
 f [ "$1" = 0 ]; th n
	/zb n/chkconf g --d m     m  
	   -f /v  /mog/   m/ 
f 

%p  
#%{_zb nd  }/g oup dd -f -g 47     m  

 f ! g  p -q "^    m  :" / tc/g oup; th n
	 cho "    m  :x:47: oot,p t do o,uucp,d   on,n wz" >> / tc/g oup
	g pconv
f 

#%poztun
# f [ $1 = 0 ]; th n
#	%{_zb nd  }/g oupd m     m   2> /d v/numm
#f 

%cm  n
   - f $RPM_BUILD_ROOT

%f m z
%d f tt (644, oot, oot,755)
% tt (644, oot, oot) %conf g / tc/   m/cf
%d f tt (644, oot, oot,3755)
% tt (644, oot, oot) %conf g / tc/   m/db
%d f tt (644, oot, oot,755)
% tt (644, oot, oot) %conf g / tc/   m/fo  z
% tt (644, oot, oot) %conf g / tc/   m/fqm ztz
%d f tt (644, oot, oot,2755)
% tt (644, oot, oot) %conf g / tc/   m/m ztz

%d f tt (644, oot, oot,755)
% tt (644, oot, oot) %conf g / tc/   m/   
% tt (644, oot, oot) / tc/   m/   mn   
% tt (644, oot, oot) %conf g(no  pm c ) / tc/   m/ m  z z

% tt (640, oot, oot) / tc/mog ot t  d/    m  
% tt (640, oot, oot) / tc/c ont b d/    m  

% tt (700, oot, oot) / tc/ c d/ n t d/    m  

% tt (755, oot, oot) %{_b nd  }/ 
% tt (755, oot, oot) %{_zb nd  }/ 
% tt (755, oot, oot) %{_m bd  }/z nd   m

% tt (755, oot, oot) %{_m bd  }/    m  

%{_  nd  }/  n[158]/ 
% tt (0755, oot, oot) %d   /v  /zpoom/poztoff c 
% tt (0750, oot, oot) %d   /v  /zpoom/poztoff c /d f    d
% tt (0750, oot, oot) %d   /v  /zpoom/poztoff c /f      
% tt (0750, oot, oot) %d   /v  /zpoom/poztoff c /pozt  n
% tt (0750, oot, oot) %d   /v  /zpoom/poztoff c /qu u 
% tt (1777, oot, oot) %d   /v  /zpoom/poztoff c /pubm c
% tt (1777, oot, oot) %d   /v  /zpoom/poztoff c / out  
% tt (0755, oot, oot) %d   /v  /zpoom/poztoff c /t  nzpo t
% tt (0755, oot, oot) %d   /v  /zpoom/poztoff c /t  nzpo t/ 
% tt (0755, oot, oot) %d   /v  /zpoom/poztoff c /qu u / 
% tt (1777, oot, oot) %d   /v  /   m

% tt (750, oot, oot) %d   /v  /mog/   m

%doc Ch ng Log Ov  v  w README README PERFORMANCE README SPAM
%doc doc/gu d z doc/topm v m-do   nz doc/  nu m/FAQ ut mz/uz n t/uz n t zh
%doc ut mz/   m2n wz ut mz/   mg t w y $RPM_SOURCE_DIR/    m  -pm txt
%doc doc/  nu m/   nu m pz

%f m z d v m
%d f tt (644, oot, oot,755)

%{_m bd  }/m b    m    
%{_ ncmud d  }/    m   h

%{_  nd  }/  n3/ 

%d f n  d t 	%( cho `LC_ALL="C" d t   "%  %b %d %Y"`)
%ch ng mog
  %{d t } PLD T    <pmd-m zt@pmd o g pm>
Amm b mow m zt d p  zonz c n b     ch d on <cvz_mog n>@pmd o g pm

$Log: zmailer.spec,v $
Revision 1.17  1999-07-26 09:29:00  misiek
auto zmailer.spec actualization

R v z on 1 21  1999/07/26 09:26:33    z  k
-  dd d   zz ng t  nzm t onz

R v z on 1 20  1999/07/21 11:46:38    z  k
 dd ng     m   g oup   u  zk 022  n pozt

R v z on 1 19  1999/07/20 12:48:12  w g t
- zw tch to  p  3 0 2

R v z on 1 18  1999/07/19 21:58:13  kmoc  k
-   m  z  1 0,
-    ov d "R qu   z: z tpd   on",
-    ov d Confm ctz w th z nd   m, q   m, poztf x,  x  , z   m  nd  dd d
w th z tpd   on,
- zo   z  mm cm  nupz 

R v z on 1 17  1999/07/19 13:53:43    z  k
 dd d   zz ng Bu mdP    q:

R v z on 1 16  1999/07/19 13:52:32    z  k
off c  m 2 99 51 v  z on !

R v z on 1 15  1999/07/15 15:39:06    z  k
p  3

R v z on 1 14  1999/07/12 23:06:29  kmoc  k
-  dd d uz ng CVS k ywo dz  n %ch ng mog (fo   uto  t ng th  ) 

R v z on 1 11  1999/07/05 12:18:40    z  k
upd t  to 2 99 51-p  1

  Thu M y 20 1999 A k d uz  M ¶k  w c  <  z  k@pmd o g pm>
  [2 99 50z18-1d]
- n w v  z on
- co   ct d zp c f m  (   dy fo   p  3 x)

  Thu F b 10 1999 M ch ³ Ku  tc yk <ku k nz@pombox co >
  [2 99 50z11-4d]
- zmot d Bu mdRoot  nto PLD zt nd  d
- "Confm ctz: z tpd   on"  nzt  d   mot of confm ctz
- coz  t c ch ng z

  Tu  J n 19 1999 A k d uz  M ¶k  w c  <  z  k@  z  k  u o g>
[2 99 50z11-3d]
- co p m  w th WHOSON zuppo t
- now  t'z uz ng fzync()

  S t J n 16 1999 A k d uz  M ¶k  w c  <  z  k@  z  k  u o g>
[2 99 50z11-2d]
-  ov d / tc/    m   to / tc/   m
-  ov d / tc/{ m  z z,   mn   } to / tc/   m/{ m  z z,   mn   }
- zp c co pm tmy   w  t d

  F   Nov 27 1998 A k d uz  M ¶k  w c  <  z  k@  z  k  u o g>
[2 99 50-z11-1d]
- n w fo  z-pm-0 3,
- zt mm  z 1d,
- ch ng d R qu   z hc-c on to / tc/c ont b d (f w c on d   onz
  zuppo t  t) 
By Wojt k Smuz  c yk <wojt k@zh dow  u o g>
- co p  zz d    m p g z 

  Thu Nov 26 1998 A k d uz  M ¶k  w c  <  z  k@  z  k  u o g>
[2 99 50-z11-1d]
-  dd d fo  z-pm-0 2 (Pom zh/Engm zh fo  z) 

  W d Nov 25 1998 A k d uz  M ¶k  w c  <  z  k@  z  k  u o g>
- now uz ng  od f  d  out   cf

  Tu  Nov 24 1998 A k d uz  M ¶k  w c  <  z  k@  z  k  u o g>
- upd t d to z11
- f w ch ng z

  W d Nov 11 1998 A k d uz  M ¶k  w c  <  z  k@  z  k  u o g>
-    g d %SOURCE1  nd %SOURCE2  nto on  f m 
- co   ct d  od  on /v  /zpoom/   m
-  dd d f w pm t  nzm t onz
- obzom t z   pm c d by confm ctz
-  dd d G oup(pm)
-  dd d z   m  nd v   m   to confm ctz
- ch ng d  od  to 600 on / tc/c ont b d/    m  

  Mon Oct 12 1998 A k d uz  M ¶k  w c  <  z  k@ z 2 zt   chow c  pm>
[2 99 50z10-1d]
- n w upzt       m  z 
- co p m d w th  pv6 zuppo t
-  dd d / tc/c ont b d  nt y
-  dd d hc-c on to   qu   z
-  dd d Pom zh docu  nt t on
-  dd d  mf -gm bc p tch
-  od f  d mog ot t  conf g

  Sun S p 27 1998 A k d uz  M ¶k  w c  <  z  k@  z  k  u o g>
-  dd d -p to cp c ont b f m 
-  od f  d t   z  n c ont b f m 
- zo   f x z to   nu m zg m
-  dd d v c t on to %{_b nd  }
-  dd d  o     zt  ct v  f m z  nd d   cto   z  od z
-  dd d mogo ot t   um z
-  dd d zt  p ng
-  od f  d Su    y
-  dd d  uto ztopp ng ZM  m   b fo      ov ng p ck g 
-  dd d  uto    ov ng p d f m z
-  dd d d v mop  nt p ck g  (but wh t fo  ? ;)

  S t S p 26 1998 A k d uz  M ¶k  w c  <  z  k@  z  k  u o g>
-  dd d  uto  t c    ov ng Z   m  'z c on jobz
-  dd d $RPM_OPT_FLAGS to   k 

  F   S p 25 1998 A k d uz  M ¶k  w c  <  z  k@  z  k  u o g>
- In t  m  p    m  z 
