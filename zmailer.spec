Summary:	Secure Mailer for Extreme Performance Demands
Summary(pl):	Bezpieczny MTA dla Wymagaj±cych Ekstremalnej Wydajno¶ci
Name:		zmailer
Version:	2.99.54
Release:	2
License:	GPL
Vendor:		Matti Aarnio <mea@nic.funet.fi>
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Source0:	ftp://ftp.funet.fi/pub/unix/mail/zmailer/src/%{name}-%{version}.tar.gz
Source1:	%{name}-pl.txt
Source2:	forms-pl-0.4.tar.gz
Source3:	%{name}.logrotate
Patch0:		%{name}-config.diff
Patch1:		%{name}-libwrap.patch
BuildRequires:	libwrap-devel
BuildRequires:	openssl-devel
BuildRequires:	whoson-devel
BuildRequires:	openldap-devel
BuildRequires:	glibc-devel >= 2.1
URL:		http://www.zmailer.org/
Requires:	logrotate >= 2.4
Requires:	/etc/cron.d
Requires:	whoson >= 1.08
Prereq:		/sbin/chkconfig
Prereq:		%{_sbindir}/groupadd
Prereq:		%{_sbindir}/groupdel
Provides:	smtpdaemon
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	exim
Obsoletes:	postfix
Obsoletes:	sendmail
Obsoletes:	sendmail-cf
Obsoletes:	sendmail-doc
Obsoletes:	smail
Obsoletes:	smtpdaemon
Obsoletes:	qmail

%description
This is a package that implements an internet message transfer agent
called ZMailer. It is intended for gateways or mail servers or other
large site environments that have extreme demands on the abilities of
the mailer. It was motivated by the problems of the Sendmail design in
such situations. Zmailer is one of the mailers able to deal with huge
quantities of mail and is more efficient any other mailer, qmail
included. It supports IPv6, WHOSON, SSL and TLS protocol.

%description -l pl
Ten pakiet zawiera implementacjê agenta transportu wiadomo¶ci
internetowych o nazwie ZMailer. ZMailer przeznaczony jest dla bramek,
serwerów poczty lub innych ¶rodowisk wymagaj±cych niezwyk³ych
mo¿liwo¶ci od mailera. Motywacj± dla ZMailera by³y problemy z
Sendmailem w trudnych sytuacjach. ZMailer jest jednym z tych mailerów,
które potrafi± daæ sobie radê z ogromn± ilo¶ci± poczty. Ponadto
ZMailer jest bardziej wydajny od innych mailerów w³±czaj±c w to
qmaila. Kolejn± zalet± jest wsparcie dla protoko³u IPv6, WHOSON, SSL
oraz TLS.

%package devel
Summary:	Static library and header file for zmailer
Summary(pl):	Plik nag³ówkowy i biblioteka statyczna dla zmailera
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
This is ZMailer's development package. It includes static library and
header file.

%description -l pl devel
To jest pakiet dla developerów. Zawiera plik nag³ówkowy i bibliotekê
statyczn± ZMailera.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1
%setup -q -a 2 -D -T -n %{name}-%{version}

%build
autoconf
ZCONFIG=%{_sysconfdir}/mail/zmailer.conf \
%configure
	--with-postoffice=/var/spool/postoffice \
	--with-rmailpath=%{_bindir}/rmail \
	--with-nntpserver=news \
	--with-system-malloc \
	--with-mailshare=%{_sysconfdir}/mail \
	--with-zconfig=no \
	--with-mailbin=%{_libdir}/zmailer \
	--with-mailvar=%{_sysconfdir}/mail \
	--with-ta-mmap \
	--with-whoson \
	--with-ldap-prefix \
	--with-openssl-prexix=%{_prefix} \
	--with-tcp-wrappers \
	--with-ipv6 \
	--with-mailbox=/var/mail
#	--with-yp \
#	--with-yp-lib='-lyp'
#	--prefix=%{_libdir}/zmailer \

%{__make} COPTS="%{rpmcflags} -w" all

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/man{1,3,5,8} \
	$RPM_BUILD_ROOT%{_sysconfdir}/{cron.d,logrotate.d,rc.d/init.d} \
	$RPM_BUILD_ROOT/{var/mail,usr/sbin} \
	$RPM_BUILD_ROOT/var/log/archiv/mail

# Install main files
%{__make} install \
	prefix=$RPM_BUILD_ROOT \
	MAILVAR=$RPM_BUILD_ROOT%{_sysconfdir}/mail \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	includedir=$RPM_BUILD_ROOT%{_includedir}

install	contrib/zmailcheck	$RPM_BUILD_ROOT%{_libdir}/zmailer/zmailcheck
install	utils/zmailer.init.sh	$RPM_BUILD_ROOT/etc/rc.d/init.d/zmailer

touch $RPM_BUILD_ROOT%{_sysconfdir}/mail/mailname

# Few symlinks
ln -fs zmailer/sendmail			$RPM_BUILD_ROOT%{_libdir}/sendmail
ln -fs ../lib/zmailer/vacation.sh	$RPM_BUILD_ROOT%{_bindir}/vacation
ln -fs ../lib/zmailer/mailq		$RPM_BUILD_ROOT%{_bindir}/mailq
ln -fs ../lib/zmailer/rmail             $RPM_BUILD_ROOT%{_bindir}/rmail
ln -fs ../lib/zmailer/newaliases	$RPM_BUILD_ROOT%{_bindir}/newaliases
ln -fs ../lib/zmailer/zmailer		$RPM_BUILD_ROOT%{_sbindir}/zmailer
ln -fs ../lib/zmailer/sendmail		$RPM_BUILD_ROOT%{_sbindir}/sendmail

# Install manual pages
%{__make} -C man S=../man MANDIR=$RPM_BUILD_ROOT%{_mandir} install

# To avoid conflict with INN
mv -f $RPM_BUILD_ROOT%{_mandir}/man8/sm.8 $RPM_BUILD_ROOT%{_mandir}/man8/sm-zmailer.8

# Install Polish/English forms
cd forms*
cp -f forms/* $RPM_BUILD_ROOT%{_sysconfdir}/mail/forms/proto
cp vacation.msg $RPM_BUILD_ROOT%{_sysconfdir}/mail

# Install proto files
cd $RPM_BUILD_ROOT%{_sysconfdir}/mail/proto
for x in *; do cp $x ..; done
cd $RPM_BUILD_ROOT%{_sysconfdir}/mail/forms/proto
for x in *; do cp $x ..; done
cd $RPM_BUILD_ROOT%{_sysconfdir}/mail/db/proto
for x in *; do cp $x ..; done

# Aliases
touch $RPM_BUILD_ROOT%{_sysconfdir}/mail/aliases

# Remove unnecesary proto and bak files
rm -rf `find $RPM_BUILD_ROOT -name proto`
rm -rf `find $RPM_BUILD_ROOT -name bak`

# Install another files
cat  << EOF > $RPM_BUILD_ROOT/etc/cron.d/zmailer
# Resubmit deferred messages
28 */1 * * *		root	!%{_libdir}/zmailer/zmailer resubmit >/dev/null
# Cleanout public and postman directories
7 4 * * *		root	!%{_libdir}/zmailer/zmailer cleanup >/dev/null
# Check if services still work
11 6,12,18,0 * * *	root	!%{_libdir}/zmailer/zmailcheck
EOF

install %{SOURCE3} $RPM_BUILD_ROOT/etc/logrotate.d/zmailer

# Router configuration
cp -f $RPM_BUILD_ROOT%{_sysconfdir}/mail/cf/SMTP+UUCP.cf \
	$RPM_BUILD_ROOT%{_sysconfdir}/mail/router.cf

%post
umask 022
/sbin/chkconfig --add zmailer

if [ -x /bin/hostname ]; then
hostname --fqdn >/etc/mail/mailname
fi

# Gymnastics to convice zmailer to use /etc/mail/aliases
# or provide /etc/mail/aliases it if not found.
if [ ! -L /etc/mail/db/aliases ]; then
	if [ -f /etc/mail/aliases ]; then
		echo "Generating Symlink to use /etc/mail/aliases for aliasing"
		rm -f /etc/mail/db/aliases || echo "Dziwnie pusto w (Strange nothing at) /etc/mail/db/aliases. Ale nie martw siê ... (But dont worry..)"
	else
		echo "Installing new /etc/mail/aliases from zmailer sample"
		mv -f /etc/mail/db/aliases /etc/aliases
	fi
	ln -s ../aliases /etc/mail/db/aliases
fi

# Scan for Mandatory entries in /etc/aliases
# postoffice MAILER-DAEMON postmast nobody and other users
# otherwise bad things (tm) result.

if ! grep -q "^hostmaster:" /etc/mail/aliases; then
	echo "Adding Entry for hostmaster in /etc/mail/aliases"
	echo "hostmaster:	root" >>/etc/mail/aliases
fi
					
for i in postmaster postoffice MAILER-DAEMON postmast nobody webmaster administrator \
ftpmaster newsmaster w3cache squid news proxy abuse ircd; do
	if ! grep -q "^$i:" /etc/mail/aliases; then
		echo "Adding Entry for $i in /etc/mail/aliases"
		echo "$i:	hostmaster" >>/etc/mail/aliases
	fi
done

# localnames
for x in `hostname --fqdn` `hostname --domain` `hostname --yp`; do
	if [ -n $x ] && ! grep -q ^$x /etc/mail/db/localnames; then
		echo "$x		`hostname --fqdn`|"
	fi
done | tr -d '\n' | tr -s '|' '\n' | sort >> /etc/mail/db/localnames

# Rebuild databases
%{_libdir}/zmailer/zmailer newdb
%{_libdir}/zmailer/policy-builder.sh -n

%preun
if [ -e /var/lock/subsys/zmailer ]; then
	/etc/rc.d/init.d/zmailer stop || :
fi

rm -f /var/spool/postoffice/.pid.*
    
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del zmailer
	rm -f /var/log/mail/*
fi

%pre
#%{_sbindir}/groupadd -f -g 47 zmailer

if ! grep -q "^zmailer:" /etc/group; then
        echo "zmailer::47:root,petidomo,uucp,daemon,news" >>/etc/group
fi

%postun
if [ "$1" = "0" ]; then
	%{_sbindir}/groupdel zmailer 2> /dev/null
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_sysconfdir}/mail
%config %{_sysconfdir}/mail/cf
%config %{_sysconfdir}/mail/forms
%config %{_sysconfdir}/mail/fqlists

%defattr(644,root,root,3755)
%config %{_sysconfdir}/mail/db

%defattr(644,root,root,2755)
%config %{_sysconfdir}/mail/lists

%defattr(644,root,root,755)
%attr(644,root,root) %config %{_sysconfdir}/mail/*.*
%attr(644,root,root) %{_sysconfdir}/mail/mailname
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/mail/aliases

%attr(640,root,root) /etc/logrotate.d/zmailer
%attr(640,root,root) /etc/cron.d/zmailer

%attr(754,root,root) /etc/rc.d/init.d/zmailer

%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/sendmail
%attr(755,root,root) %{_libdir}/zmailer

%{_mandir}/man[158]/*
%attr(0755,root,root) %dir /var/spool/postoffice
%attr(0750,root,root) %dir /var/spool/postoffice/deferred
%attr(0750,root,root) %dir /var/spool/postoffice/freezer
%attr(0750,root,root) %dir /var/spool/postoffice/postman
%attr(0750,root,root) %dir /var/spool/postoffice/queue
%attr(1777,root,root) %dir /var/spool/postoffice/public
%attr(1777,root,root) %dir /var/spool/postoffice/router
%attr(0755,root,root) %dir /var/spool/postoffice/transport
%attr(0755,root,root) %dir /var/spool/postoffice/transport/*
%attr(0755,root,root) %dir /var/spool/postoffice/queue/*

%attr(750,root,root) %dir /var/log/mail
%attr(750,root,root) %dir /var/log/archiv/mail

%doc ChangeLog Overview README README.PERFORMANCE README.SPAM
%doc doc/guides doc/toplevel-domains doc/manual/FAQ utils/usenet/usenet.sh
%doc utils/mail2news utils/mailgateway doc/manual/zmanual.ps
%doc $RPM_SOURCE_DIR/zmailer-pl.txt

%files devel
%defattr(644,root,root,755)

%{_libdir}/libzmailer.a
%{_includedir}/zmailer.h

%{_mandir}/man3/*
