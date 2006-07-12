Summary:	GNOME base GUI library
Summary(pl):	Podstawowa biblioteka GUI GNOME
Name:		libgnomeui
Version:	2.15.2
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/libgnomeui/2.15/%{name}-%{version}.tar.bz2
# Source0-md5:	ec5841c2c01d79e97bc363414e446240
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.14.0
BuildRequires:	audiofile-devel >= 1:0.2.3
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	esound-devel >= 1:0.2.31
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	gnome-keyring-devel >= 0.5.1
BuildRequires:	gnome-vfs2-devel >= 2.15.3
BuildRequires:	gtk-doc >= 1.6
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	libbonoboui-devel >= 2.14.0
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgnome-devel >= 2.15.1
BuildRequires:	libgnomecanvas-devel >= 2.14.0
BuildRequires:	libjpeg-devel
BuildRequires:	libtool
BuildRequires:	pango-devel >= 1:1.13.3
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	popt-devel >= 1.5
BuildRequires:	rpmbuild(macros) >= 1.197
Requires:	gtk+2 >= 2:2.10.0
Requires:	gnome-keyring-libs >= 0.5.1
Requires:	gnome-vfs2-libs >= 2.15.3
Requires:	libbonoboui >= 2.14.0
Requires:	pango >= 1:1.13.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME (GNU Network Object Model Environment) is a user-friendly set of
GUI applications and desktop tools to be used in conjunction with a
window manager for the X Window System. The libgnomeui package
includes GUI-related libraries that are needed to run GNOME. (The
libgnome package includes the library features that don't use the X
Window System.)

%description -l pl
GNOME (GNU Network Object Model Environment) jest przyjaznym dla
u¿ytkownika zestawem aplikacji i narzêdzi z graficznym interfejsem do
u¿ywania w po³±czeniu z zarz±dc± okien X Window System. Pakiet
libgnomeui zawiera biblioteki zwi±zane z graficznym interfejsem
u¿ytkownika potrzebne do uruchomienia GNOME (pakiet libgnome zawiera
biblioteki nie u¿ywaj±ce X Window System).

%package devel
Summary:	Headers for libgnomeui
Summary(pl):	Pliki nag³ówkowe libgnomeui
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	GConf2-devel >= 2.14.0
Requires:	esound-devel >= 1:0.2.31
Requires:	gnome-vfs2-devel >= 2.15.3
Requires:	gnome-keyring-devel >= 0.5.1
Requires:	gtk-doc-common
Requires:	gtk+2-devel >= 2:2.10.0
Requires:	libbonoboui-devel >= 2.14.0
Requires:	libglade2-devel >= 1:2.6.0
Requires:	libjpeg-devel

%description devel
GNOME (GNU Network Object Model Environment) is a user-friendly set of
GUI applications and desktop tools to be used in conjunction with a
window manager for the X Window System. The libgnomeui-devel package
includes the libraries and include files that you will need to use
libgnomeui.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe potrzebne do kompilacji programów
u¿ywaj±cych libgnomeui.

%package static
Summary:	Static libgnomeui libraries
Summary(pl):	Statyczne biblioteki libgnomeui
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of libgnomeui libraries.

%description static -l pl
Statyczna wersja bibliotek libgnomeui.

%prep
%setup -q

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
LDFLAGS="%{rpmldflags} -Wl,--as-needed"
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/gnome/help

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

# no static modules and *.la for libglade or vfs modules
rm -f $RPM_BUILD_ROOT%{_libdir}/libglade/2.0/*.{la,a}
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.*/filesystems/libgnome-vfs.{la,a}

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/tk

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
# it seems that every package that uses %{_datadir}/gnome tree requires
# libgnomeui - so added these directories to this package
%dir %{_datadir}/gnome
%dir %{_datadir}/gnome/help
%attr(755,root,root) %{_libdir}/gnome_segv2
%attr(755,root,root) %{_libdir}/gtk-2.0/2.*/filesystems/libgnome-vfs.so
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/libglade/2.0/*.so
%{_pixmapsdir}/*

%files devel
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}
%{_includedir}/libgnomeui-2.0
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
