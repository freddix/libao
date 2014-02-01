Summary:	Cross Platform Audio Output Library
Name:		libao
Version:	1.2.0
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Libraries
Source0:	http://downloads.xiph.org/releases/ao/%{name}-%{version}.tar.gz
# Source0-md5:	9f5dd20d7e95fd0dd72df5353829f097
URL:		http://www.xiph.org/ao/
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pulseaudio-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libao is a cross-platform audio library that allows programs to output
audio using a simple API on a wide variety of platforms. It currently
supports: Null output, WAV files, OSS (Open Sound System), ESD (ESounD
or Enlighten Sound Daemon), ALSA (Advanced Linux Sound Architecture),
Solaris (untested), IRIX (untested)

%package devel
Summary:	Cross Platform Audio Output Library Development
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
The libao-devel package contains the header files and documentation
needed to develop applications with libao.

%package plugins
Summary:	Plugins for AO Library
Group:		Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugins
Plugins for AO Library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-arts		\
	--disable-esd		\
	--disable-nas		\
	--disable-static	\
	--enable-alsa
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# dlopened by *.so
rm -f $RPM_BUILD_ROOT%{_libdir}/ao/plugins-4/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES README TODO
%attr(755,root,root) %ghost %{_libdir}/libao.so.?
%attr(755,root,root) %{_libdir}/libao.so.*.*.*
%dir %{_libdir}/ao
%dir %{_libdir}/ao/plugins-4
%attr(755,root,root) %{_libdir}/ao/plugins-4/libalsa.so

%files devel
%defattr(644,root,root,755)
%doc doc/*{html,css,c}
%attr(755,root,root) %{_libdir}/libao.so
%{_libdir}/libao.la
%{_includedir}/ao
%{_aclocaldir}/ao.m4
%{_pkgconfigdir}/*.pc

%files plugins
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ao/plugins-4/liboss.so
%attr(755,root,root) %{_libdir}/ao/plugins-4/libpulse.so
%{_mandir}/man5/*

