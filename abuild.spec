Summary:	Script to build Alpine Linux Packages
Name:		abuild
Version:	3.3.1
Release:	1
License:	GPL v2
Group:		Development/Building
Source0:	https://dev.alpinelinux.org/archive/abuild/%{name}-%{version}.tar.xz
# Source0-md5:	29043340e251eb5677f176af0a98ce2d
URL:		https://git.alpinelinux.org/abuild/
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	apk-tools >= 2.0.7-r1
Requires:	attr
Requires:	curl
Requires:	fakeroot
Requires:	lzip
Requires:	openssl
Requires:	patch
Requires:	pax-utils
Requires:	pkgconf
Requires:	sudo
Requires:	tar
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Build scripts to build Alpine Linux packages.

%prep
%setup -q

%build
%{__make} \
	VERSION="%{version}-%{release}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	VERSION="%{version}-%{release}" \
	DESTDIR=$RPM_BUILD_ROOT

chmod u+rw $RPM_BUILD_ROOT%{_bindir}/abuild-sudo

install -d $RPM_BUILD_ROOT/var/cache/distfiles

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/abuild.conf
%attr(4111,root,root) %{_bindir}/abuild-sudo
%attr(755,root,root) %{_bindir}/abuild
%attr(755,root,root) %{_bindir}/abuild-addgroup
%attr(755,root,root) %{_bindir}/abuild-adduser
%attr(755,root,root) %{_bindir}/abuild-apk
%attr(755,root,root) %{_bindir}/abuild-fetch
%attr(755,root,root) %{_bindir}/abuild-gzsplit
%attr(755,root,root) %{_bindir}/abuild-keygen
%attr(755,root,root) %{_bindir}/abuild-rmtemp
%attr(755,root,root) %{_bindir}/abuild-sign
%attr(755,root,root) %{_bindir}/abuild-tar
%attr(755,root,root) %{_bindir}/abump
%attr(755,root,root) %{_bindir}/apkbuild-cpan
%attr(755,root,root) %{_bindir}/apkbuild-gem-resolver
%attr(755,root,root) %{_bindir}/apkgrel
%attr(755,root,root) %{_bindir}/buildlab
%attr(755,root,root) %{_bindir}/checkapk
%attr(755,root,root) %{_bindir}/newapkbuild
%{_mandir}/man1/newapkbuild.1*
%{_mandir}/man5/APKBUILD.5*
%{_datadir}/%{name}
%dir /var/cache/distfiles
