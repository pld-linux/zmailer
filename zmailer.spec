%define	oversion	2.99.51-pre1
Summary:	Secure Mailer for Extreme Performance Demands
Summary(pl):	Bezpieczny MTA dla Wymagaj±cych Ekstremalnej Wydajno¶ci
Name:		zmailer
Version:	2.99.51_pre1
Release:	1
Copyright:	GPL
Vendor:		Matti Aarnio <mea@nic.funet.fi>
Group:		Daemons
Group(pl):	Demony
Source0:	ftp://ftp.funet.fi/pub/unix/mail/zmailer/src/%{name}-%{oversion}.tar.gz
Source1:	zmailer-pl.txt
Source2:	forms-pl-0.4.tar.gz
Patch0:		zmailer-config.diff
Patch1:		zmailer-openssl.patch
Prereq:		/sbin/chkconfig
URL:		http://www.zmailer.org
Requires:	logrotate >= 2.4
Requires:	/etc/crontab.d
Requires:	whoson >= 1.08
Requires:	smtpdaemon
BuildPrereq:	openssl-devel
BuildPrereq:	whoson-devel
BuildPrereq:	openldap-devel
BuildPrereq:	glibc-devel >= 2.1
BuildRoot:	/tmp/%{name}-%{version}-root
Provides:	smtpdaemon
Conflicts:	sendmail
Conflicts:	qmail
Conflicts:	postfix
Conflicts:	exim
Conflicts:	smail

%description
This is a package that implements an internet message transfer agent called
ZMailer. It is intended for gateways or mail servers or other large site
environments that have extreme demands on the abilities of the mailer.  It
was motivated by the problems of the Sendmail design in such situations.
Zmailer is one of the mailers able to deal with huge quantities of mail and
is more efficient any other mailer, qmail included. It supports IPv6,
WHOSON, SSL and TLS protocol.

%description -l pl
Ten pakiet zawiera implementacjê agenta transportu wiadomo¶ci internetowych
o nazwie ZMailer. ZMailer przeznaczony jest dla bramek, serwerów poczty
lub innych ¶rodowisk wymagaj±cych niezwyk³ych mo¿liwo¶ci od mailera.
Motywacj± dla ZMailera by³y problemy z Sendmailem w trudnych sytuacjach.
ZMailer jest jednym z tych mailerów, które potrafi± daæ sobie radê z ogromn±
ilo¶ci± poczty. Ponadto ZMailer jest bardziej wydajny od innych mailerów
w³±czaj±c w to qmaila. Kolejn± zalet± jest wsparcie dla protoko³u IPv6, WHOSON,
SSL oraz TLS.

%package devel
Summary:	Static library and header file for zmailer
Summary(pl):	Plik nag³ówkowy i biblioteka statyczna dla zmailera
Group:		Development/Libraries
Group(pl):	Programowanie/biblioteki
Requires:	%{name} = %{version}

%description devel
This is ZMailer's development package.
It includes static library and header file.

%description -l pl devel
To jest pakiet dla developerów.
Zawiera plik nag³ówkowy i bibliotekê statyczn± ZMailera.

%prep
%setup -q -n %{name}-%{oversion}
%patch0 -p1
%patch1 -p1
%setup -q -a 2 -D -T -n %{name}-%{oversion}

%build
ZCONFIG=/etc/mail/zmailer.conf \
./configure %{_target_platform} \
	--mandir=%{_mandir} \
	--libdir=%{_libdir} \
	--prefix=%{_libdir}/zmailer \
	--with-postoffice=/var/spool/postoffice \
	--with-rmailpath=%{_bindir}/rmail \
	--with-nntpserver=news \
	--with-system-malloc \
	--with-mailshare=/etc/mail \
	--with-zconfig=no \
	--with-mailbin=%{_libdir}/zmailer \
	--with-mailvar=/etc/mail \
	--with-ta-mmap \
	--includedir=%{_includedir} \
	--with-whoson \
	--with-ldap-prefix \
	--with-ipv6 \
	--with-mailbox=/var/mail

make COPTS="$RPM_OPT_FLAGS -w" all

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/man{1,3,5,8}
install -d $RPM_BUILD_ROOT/etc/{crontab.d,logrotate.d,rc.d/init.d}
install -d $RPM_BUILD_ROOT/{var/mail,usr/sbin}

# Install main files
make install \
	prefix=$RPM_BUILD_ROOT \
	MAILVAR=$RPM_BUILD_ROOT/etc/mail \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	includedir=$RPM_BUILD_ROOT%{_includedir}

install	contrib/zmailcheck	$RPM_BUILD_ROOT%{_libdir}/zmailer/zmailcheck
install	utils/zmailer.init.sh	$RPM_BUILD_ROOT/etc/rc.d/init.d/zmailer

touch $RPM_BUILD_ROOT/etc/mail/mailname

# Few symlinks
ln -fs zmailer/sendmail			$RPM_BUILD_ROOT%{_libdir}/sendmail
ln -fs ../lib/zmailer/vacation.sh	$RPM_BUILD_ROOT%{_bindir}/vacation
ln -fs ../lib/zmailer/mailq		$RPM_BUILD_ROOT%{_bindir}/mailq
ln -fs ../lib/zmailer/rmail             $RPM_BUILD_ROOT%{_bindir}/rmail
ln -fs ../lib/zmailer/newaliases	$RPM_BUILD_ROOT%{_bindir}/newaliases
ln -fs ../lib/zmailer/zmailer		$RPM_BUILD_ROOT%{_sbindir}/zmailer
ln -fs ../lib/zmailer/sendmail		$RPM_BUILD_ROOT%{_sbindir}/sendmail

# Install manual pages
make -C man S=../man MANDIR=$RPM_BUILD_ROOT%{_mandir} install

# To avoid conflict with INN
mv $RPM_BUILD_ROOT%{_mandir}/man8/sm.8 $RPM_BUILD_ROOT%{_mandir}/man8/sm-zmailer.8

# Install Polish/English forms
cd forms*
cp -f forms/*   $RPM_BUILD_ROOT/etc/mail/forms/proto
cp vacation.msg $RPM_BUILD_ROOT/etc/mail

# Install proto files
cd $RPM_BUILD_ROOT/etc/mail/proto
for x in *; do cp $x ..; done
cd $RPM_BUILD_ROOT/etc/mail/forms/proto
for x in *; do cp $x ..; done
cd $RPM_BUILD_ROOT/etc/mail/db/proto
for x in *; do cp $x ..; done

# Aliases
touch $RPM_BUILD_ROOT/etc/mail/aliases

# Remove unnecesary proto and bak files
rm -r `find $RPM_BUILD_ROOT -name proto`
rm -r `find $RPM_BUILD_ROOT -name bak`

# Install another files
cat  << EOF > $RPM_BUILD_ROOT/etc/crontab.d/zmailer
# Resubmit deferred messages
28 */1 * * *		root	!%{_libdir}/zmailer/zmailer resubmit >/dev/null
# Cleanout public and postman directories
7 4 * * *		root	!%{_libdir}/zmailer/zmailer cleanup >/dev/null
# Check if services still work
11 6,12,18,0 * * *	root	!%{_libdir}/zmailer/zmailcheck
EOF

cat  << EOF > $RPM_BUILD_ROOT/etc/logrotate.d/zmailer
errors root
compress
monthly

/var/log/mail/* {
	create 640 root root
        postrotate
        %{_libdir}/zmailer/zmailer synclog
        endscript
}
EOF

# Router configuration
cp -f $RPM_BUILD_ROOT/etc/mail/cf/SMTP+UUCP.cf \
      $RPM_BUILD_ROOT/etc/mail/router.cf

strip     $RPM_BUILD_ROOT%{_libdir}/zmailer/{*,ta}	2>/dev/null || :
gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/*

%post
/sbin/chkconfig --add zmailer

if [ -x /bin/hostname ]; then
hostname --fqdn >/etc/mail/mailname
#echo "System skonfigurowany do odbioru poczty dla `hostname --fqdn` (w /etc/mail/mailname)."
#echo "System configured to receive mail for `hostname --fqdn` (in /etc/mail/mailname)."
fi

# Gymnastics to convice zmailer to use /etc/mail/aliases
# or provide /etc/mail/aliases it if not found.
if [ ! -L /etc/mail/db/aliases ]; then
	if [ -f /etc/mail/aliases ]; then
#		echo "Generujê dowi±zanie symboliczne tak by u¿ywaæ /etc/mail/aliases w aliasach"
#		echo "Generating Symlink to use /etc/mail/aliases for aliasing"
		rm /etc/mail/db/aliases || echo "Dziwnie pusto w (Strange nothing at) /etc/mail/db/aliases. Ale nie martw siê ... (But dont worry..)"
	else
#		echo "Instalujê nowe /etc/mail/aliases z przyk³adowego pliku"
#		echo "Installing new /etc/mail/aliases from zmailer sample"
		mv /etc/mail/db/aliases /etc/aliases
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
    
if [ "$1" = 0 ]; then
    /sbin/chkconfig --del zmailer
    rm -f /var/log/mail/*
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(644,root,root) %config /etc/mail/cf
%defattr(644,root,root,3755)
%attr(644,root,root) %config /etc/mail/db
%defattr(644,root,root,755)
%attr(644,root,root) %config /etc/mail/forms
%attr(644,root,root) %config /etc/mail/fqlists
%defattr(644,root,root,2755)
%attr(644,root,root) %config /etc/mail/lists

%defattr(644,root,root,755)
%attr(644,root,root) %config /etc/mail/*.*
%attr(644,root,root) /etc/mail/mailname
%attr(644,root,root) %config(noreplace) /etc/mail/aliases

%attr(640,root,root) /etc/logrotate.d/zmailer
%attr(640,root,root) /etc/crontab.d/zmailer

%attr(700,root,root) /etc/rc.d/init.d/zmailer

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
%attr(1777,root,mail) %dir /var/mail

%attr(750,root,root) %dir /var/log/mail

%doc ChangeLog Overview README README.PERFORMANCE README.SPAM
%doc doc/guides doc/toplevel-domains doc/manual/FAQ utils/usenet/usenet.sh
%doc utils/mail2news utils/mailgateway $RPM_SOURCE_DIR/zmailer-pl.txt
%doc doc/manual/zmanual.ps

%files devel
%defattr(644,root,root,755)

%{_libdir}/libzmailer.a
%{_includedir}/zmailer.h

%{_mandir}/man3/*

%changelog
* Mon Jul 05 1999 Arkadiusz Mi¶kiewicz <misiek@pld.org.pl>
- new logging style

$Log: zmailer.spec,v $
Revision 1.8  1999-07-10 15:57:14  misiek
auto zmailer.spec actualization

Revision 1.13  1999/07/09 16:22:28  kloczek

- added line on top spec file with cvs tags ($Revision: 1.8 $ and $Date: 1999-07-10 15:57:14 $).

Revision 1.12  1999/07/05 12:20:11  misiek
*** empty log message ***

Revision 1.11  1999/07/05 12:18:40  misiek
update to 2.99.51-pre1


* Thu May 20 1999 Arkadiusz Mi¶kiewicz <misiek@pld.org.pl>
  [2.99.50s18-1d]
- new version
- corrected spec file (ready for rpm 3.x)

* Thu Feb 10 1999 Micha³ Kuratczyk <kurkens@polbox.com>
  [2.99.50s11-4d]
- sloted BuildRoot into PLD standard
- "Conflicts: smtpdaemon" instead a lot of conflicts
- cosmetic changes

* Tue Jan 19 1999 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
[2.99.50s11-3d]
- compile with WHOSON support
- now it's using fsync()

* Sat Jan 16 1999 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
[2.99.50s11-2d]
- moved /etc/zmailer to /etc/mail
- moved /etc/{aliases,mailname} to /etc/mail/{aliases,mailname}
- spec completly rewrited

* Fri Nov 27 1998 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
[2.99.50-s11-1d]
- new forms-pl-0.3,
- still as 1d,
- changed Requires hc-cron to /etc/crontab.d (few cron daemons
  support it).
By Wojtek Slusarczyk <wojtek@shadow.eu.org>
- compressed mail pages.

* Thu Nov 26 1998 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
[2.99.50-s11-1d]
- added forms-pl-0.2 (Polish/English forms).

* Wed Nov 25 1998 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
- now using modified router.cf

* Tue Nov 24 1998 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
- updated to s11
- few changes

* Wed Nov 11 1998 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
- merged %SOURCE1 and %SOURCE2 into one file
- corrected mode on /var/spool/mail
- added few pl translations
- obsoletes replaced by conflicts
- added Group(pl)
- added smail and vmailer to conflicts
- changed mode to 600 on /etc/crontab.d/zmailer

* Mon Oct 12 1998 Arkadiusz Mi¶kiewicz <misiek@zsz2.starachowice.pl>
[2.99.50s10-1d]
- new upstream release
- compiled with ipv6 support
- added /etc/crontab.d entry
- added hc-cron to requires
- added Polish documentation
- added alfa-glibc patch
- modified logrotate config

* Sun Sep 27 1998 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
- added -p to cp crontab file
- modified times in crontab file
- some fixes to manual.sgml
- added vacation to %{_bindir}
- added more restrictive files and directories modes
- added logorotate rules
- added striping
- modified Summary
- added auto stopping ZMailer before removing package
- added auto removing pid files
- added development package (but what for ? ;)

* Sat Sep 26 1998 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
- added automatic removing Zmailer's cron jobs
- added $RPM_OPT_FLAGS to make

* Fri Sep 25 1998 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
- Initial rpm release
