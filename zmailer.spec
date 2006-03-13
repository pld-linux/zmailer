# TODO
# - missing service restart
# Conditional build:
%bcond_without	whoson	# build without WHOSON support
%bcond_without	ldap	# build without LDAP support
%bcond_without	gdbm	# build without GDBM support
#
Summary:	Secure Mailer for Extreme Performance Demands
Summary(pl):	Bezpieczny MTA dla Wymagaj±cych Ekstremalnej Wydajno¶ci
Name:		zmailer
Version:	2.99.56
Release:	6
License:	GPL
Group:		Networking/Daemons
Source0:	ftp://ftp.funet.fi/pub/unix/mail/zmailer/src/%{name}-%{version}.tar.gz
# Source0-md5:	c94cc0c2e2427a210a046a02ac4c2d50
Source1:	%{name}-pl.txt
Source2:	forms-pl-0.4.tar.gz
# Source2-md5:	c4ca963cd941e3ac533860d7d3d9f4b1
Source3:	%{name}.logrotate
Patch0:		%{name}-config.diff
Patch1:		%{name}-ldap-lmap.patch
Patch2:		%{name}-glibc.patch
Patch3:		%{name}-sleepycatdb.patch
URL:		http://www.zmailer.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	db-devel
BuildRequires:	ed
%{?with_gdbm:BuildRequires:	gdbm-devel}
BuildRequires:	libwrap-devel
%{?with_ldap:BuildRequires:	openldap-devel >= 2.3}
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pam-devel
BuildRequires:	perl-devel
BuildRequires:	rpmbuild(macros) >= 1.268
%{?with_whoson:BuildRequires:	whoson-devel}
Requires(post):	fileutils
Requires(post):	grep
Requires(post):	net-tools
Requires(post):	textutils
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/groupdel
Requires(pre):	grep
Requires:	/etc/cron.d
Requires:	logrotate >= 2.4
Requires:	rc-scripts
%{?with_whoson:Requires:	whoson >= 1.08}
Provides:	group(zmailer)
Provides:	smtpdaemon
Obsoletes:	courier
Obsoletes:	exim
Obsoletes:	masqmail
Obsoletes:	nullmailer
Obsoletes:	omta
Obsoletes:	postfix
Obsoletes:	qmail
Obsoletes:	sendmail
Obsoletes:	sendmail-cf
Obsoletes:	sendmail-doc
Obsoletes:	smail
Obsoletes:	smtpdaemon
Obsoletes:	ssmtp
Conflicts:	vacation
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Requires:	%{name} = %{version}

%description devel
This is ZMailer's development package. It includes static library and
header file.

%description devel -l pl
To jest pakiet dla developerów. Zawiera plik nag³ówkowy i bibliotekê
statyczn± ZMailera.

%prep
%setup -q -a2
%patch0 -p1
%patch1 -p0
%patch2 -p1
%patch3 -p1

%build
cp -f /usr/share/automake/config.* .
%{__autoconf}
%configure \
	--with-zconfig=%{_sysconfdir}/mail/zmailer.conf \
	--with-postoffice=/var/spool/postoffice \
	--with-rmailpath=%{_bindir}/rmail \
	--with-nntpserver=news \
	--with-system-malloc \
	--with-mailshare=%{_sysconfdir}/mail \
	--with-mailbin=%{_libdir}/zmailer \
	--with-mailvar=%{_sysconfdir}/mail \
	--with-ta-mmap \
	%{?with_whoson:--with-whoson} \
	%{?with_ldap:--with-ldap-prefix} \
	--with-openssl-prexix=%{_prefix} \
	--with-tcp-wrappers \
	--with-ipv6 \
	--with-mailbox=/var/mail
#	--with-yp \
#	--with-yp-lib='-lyp'
#	--prefix=%{_libdir}/zmailer \
#	--with-zconfig=no

%{__make} -j1 all \
	COPTS="%{rpmcflags} -w"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man{1,3,5,8} \
	$RPM_BUILD_ROOT%{_sysconfdir}/{cron.d,logrotate.d,rc.d/init.d} \
	$RPM_BUILD_ROOT{/var/mail,%{_sbindir}} \
	$RPM_BUILD_ROOT/var/log/archiv/mail

# Install main files
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	MAILVAR=$RPM_BUILD_ROOT%{_sysconfdir}/mail \
	MAILSHARE=$RPM_BUILD_ROOT%{_sysconfdir}/mail \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	includedir=$RPM_BUILD_ROOT%{_includedir}

install	contrib/zmailcheck	$RPM_BUILD_ROOT%{_libdir}/zmailer/zmailcheck
install	utils/zmailer.init.sh	$RPM_BUILD_ROOT/etc/rc.d/init.d/zmailer

> $RPM_BUILD_ROOT%{_sysconfdir}/mail/mailname

# Few symlinks
ln -fs zmailer/sendmail			$RPM_BUILD_ROOT%{_libdir}/sendmail
ln -fs ../lib/zmailer/vacation.sh	$RPM_BUILD_ROOT%{_bindir}/vacation
ln -fs ../lib/zmailer/mailq		$RPM_BUILD_ROOT%{_bindir}/mailq
ln -fs ../lib/zmailer/rmail		$RPM_BUILD_ROOT%{_bindir}/rmail
ln -fs ../lib/zmailer/newaliases	$RPM_BUILD_ROOT%{_bindir}/newaliases
ln -fs ../lib/zmailer/zmailer		$RPM_BUILD_ROOT%{_sbindir}/zmailer
ln -fs ../lib/zmailer/sendmail		$RPM_BUILD_ROOT%{_sbindir}/sendmail

# Install manual pages
%{__make} -C man install \
	S=../man \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}

# To avoid conflict with INN
mv -f $RPM_BUILD_ROOT%{_mandir}/man8/sm.8zm $RPM_BUILD_ROOT%{_mandir}/man8/sm-zmailer.8zm

(
# Install Polish/English forms
cd forms*
cp -f forms/* $RPM_BUILD_ROOT%{_sysconfdir}/mail/forms/proto
install vacation.msg $RPM_BUILD_ROOT%{_sysconfdir}/mail

# Install proto files
cd $RPM_BUILD_ROOT%{_sysconfdir}/mail/proto
for x in *; do cp -f $x ..; done
cd $RPM_BUILD_ROOT%{_sysconfdir}/mail/forms/proto
for x in *; do cp -f $x ..; done
cd $RPM_BUILD_ROOT%{_sysconfdir}/mail/db/proto
for x in *; do cp -f $x ..; done
cd $RPM_BUILD_ROOT%{_sysconfdir}/mail/cf/proto
for x in *; do cp -f $x ..; done
cd $RPM_BUILD_ROOT%{_sysconfdir}/mail
cp -f ./cf/SMTP+UUCP.cf router.cf
)

# Aliases
> $RPM_BUILD_ROOT%{_sysconfdir}/mail/aliases

# Remove unnecesary proto and bak files
rm -rf `find $RPM_BUILD_ROOT -name proto`
rm -rf `find $RPM_BUILD_ROOT -name bak`

# Install another files
cat << EOF > $RPM_BUILD_ROOT/etc/cron.d/zmailer
# Resubmit deferred messages
28 */1 * * *		root	! %{_libdir}/zmailer/zmailer resubmit >/dev/null
# Cleanout public and postman directories
7 4 * * *		root	! %{_libdir}/zmailer/zmailer cleanup >/dev/null
# Check if services still work
11 6,12,18,0 * * *	root	! %{_libdir}/zmailer/zmailcheck
EOF

install %{SOURCE3} $RPM_BUILD_ROOT/etc/logrotate.d/zmailer

# postoffice tree (as created by proto/post-install.sh):
install -d $RPM_BUILD_ROOT/var/spool/postoffice/{deferred,freezer,postman,public}
for f1 in A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ; do
	install -d $RPM_BUILD_ROOT/var/spool/postoffice/{TLSsrvrcache,TLSclntcache,router}/$f1
	for f2 in A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ; do
		install -d $RPM_BUILD_ROOT/var/spool/postoffice/{queue,transport}/$f1/$f2
	done
done

cp -f %{SOURCE1} .

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
/sbin/chkconfig --add zmailer

if [ "$1" = 1 -a -x /bin/hostname ]; then
	hostname --fqdn > /etc/mail/mailname
fi

if [ -f /etc/mail/router.fc ]; then
	rm -f /etc/mail/router.fc
fi

# Gymnastics to convice zmailer to use /etc/mail/aliases
# or provide /etc/mail/aliases it if not found.
if [ ! -L /etc/mail/db/aliases ]; then
	if [ -f /etc/mail/aliases ]; then
		echo "Generating Symlink to use /etc/mail/aliases for aliasing"
		rm -f /etc/mail/db/aliases || echo "Strange nothing at (Dziwnie puste) /etc/mail/db/aliases. Don't worry (Nie martw siê)."
	else
		echo "Installing new /etc/mail/aliases from zmailer sample"
		mv -f /etc/mail/db/aliases /etc/aliases
	fi
	ln -sf ../aliases /etc/mail/db/aliases
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
if [ "$1" = "0" ]; then
	%service zmailer stop
	/sbin/chkconfig --del zmailer
	rm -f /var/spool/postoffice/.pid.*
fi

%pre
%groupadd -g 47 zmailer
for u in root petidomo uucp daemon news; do
	if [ -z "`/bin/id -u $u 2>/dev/null`" ]; then
		continue
	fi
	GROUPS=`/bin/id -n -G $u | sed 's/ /,/g'`
	if [ -z "`echo $GROUPS | grep '\(^\|,\)zmailer\($\|,\)'`" ]; then
		/usr/sbin/usermod -G "${GROUPS},zmailer" $u 1>&2 || :
	fi
done

%postun
if [ "$1" = "0" ]; then
	%groupremove zmailer
fi

%files
%defattr(644,root,root,755)
%doc ChangeLog Overview README* TODO doc/toplevel-domains
%doc doc/manual/FAQ doc/design/zmog.ps zmailer-pl.txt doc/guides
%doc utils/usenet/usenet.sh utils/mail2news utils/mailgateway
%dir %{_sysconfdir}/mail
%config(noreplace) %{_sysconfdir}/mail/cf
%config(noreplace) %{_sysconfdir}/mail/forms
%config(noreplace) %{_sysconfdir}/mail/fqlists

%defattr(644,root,root,3755)
%config(noreplace) %{_sysconfdir}/mail/db

%defattr(644,root,root,2755)
%config(noreplace) %{_sysconfdir}/mail/lists

%defattr(644,root,root,755)
%attr(644,root,root) %config %{_sysconfdir}/mail/*.*
%attr(644,root,root) %{_sysconfdir}/mail/mailname
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/mail/aliases

%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/zmailer
%attr(640,root,root) /etc/cron.d/zmailer

%attr(754,root,root) /etc/rc.d/init.d/zmailer

%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/sendmail
%attr(755,root,root) %{_libdir}/zmailer

%{_mandir}/man[158]/*
%attr(755,root,root) %dir /var/spool/postoffice
%attr(750,root,root) %dir /var/spool/postoffice/deferred
%attr(750,root,root) %dir /var/spool/postoffice/freezer
%attr(750,root,root) %dir /var/spool/postoffice/postman
%attr(750,root,root) %dir /var/spool/postoffice/queue
%attr(1777,root,root) %dir /var/spool/postoffice/public
%attr(1777,root,root) %dir /var/spool/postoffice/router
%attr(755,root,root) %dir /var/spool/postoffice/transport
%attr(755,root,root) %dir /var/spool/postoffice/transport/*
%attr(755,root,root) %dir /var/spool/postoffice/transport/*/*
%attr(755,root,root) %dir /var/spool/postoffice/queue/*
%attr(755,root,root) %dir /var/spool/postoffice/queue/*/*
%attr(700,root,root) %dir /var/spool/postoffice/TLSsrvrcache
%attr(700,root,root) %dir /var/spool/postoffice/TLSsrvrcache/*
%attr(700,root,root) %dir /var/spool/postoffice/TLSclntcache
%attr(700,root,root) %dir /var/spool/postoffice/TLSclntcache/*
%attr(750,root,root) %dir /var/log/mail
%attr(750,root,root) %dir /var/log/archiv/mail

%files devel
%defattr(644,root,root,755)

%{_libdir}/libzmailer.a
%{_includedir}/zmailer.h

%{_mandir}/man3/*
