Summary:	GNOME base GUI library
Summary(pl):	Podstawowa biblioteka GUI GNOME
Name:		libgnomeui
Version:	2.3.3.1
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.3/%{name}-%{version}.tar.bz2
# Source0-md5:	0f02318a2b501f326cb79b7d16f3804e
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.3.0
BuildRequires:	ORBit2-devel >= 2.7.0
BuildRequires:	audiofile-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel >= 0.2.29
BuildRequires:	gnome-vfs2-devel >= 2.3.5
BuildRequires:	gtk-doc
BuildRequires:	libbonobo-devel >= 2.3.1-4
BuildRequires:	libbonoboui-devel >= 2.2.0
BuildRequires:	libglade2-devel >= 2.0.1-4
BuildRequires:	libgnome-devel >= 2.3.3.1
BuildRequires:	libgnomecanvas-devel >= 2.3.0
BuildRequires:	libjpeg-devel
BuildRequires:	libtool
BuildRequires:	pango-devel >= 1.2.0
BuildRequires:	rpm-build >= 4.1-10
Requires:	libbonobo >= 2.3.1-4
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
Requires:	%{name} = %{version}
Requires:	GConf2-devel
Requires:	esound-devel
Requires:	gnome-vfs2-devel
Requires:	gtk-doc-common
Requires:	libbonobo-devel
Requires:	libbonoboui-devel
Requires:	libglade2-devel
Requires:	libgnome-devel
Requires:	libgnomecanvas-devel
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
Requires:	%{name}-devel = %{version}

%description static
Static version of libgnomeui libraries.

%description static -l pl
Statyczna wersja bibliotek libgnomeui.

%prep
%setup -q

%build
rm -d missing
%{__libtoolize}
%{__aclocal} -I %{_aclocaldir}/gnome2-macros
%{__autoconf}
%{__automake}
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

# no static modules
rm -f $RPM_BUILD_ROOT%{_libdir}/libglade/2.0/*.a

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/gnome_segv2
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/libglade/2.0/*.so
%{_libdir}/libglade/2.0/*.la
%{_pixmapsdir}/*
# it seems that every package that uses %{_datadir}/gnome tree requires
# libgnomeui - so added these directories to this package
%dir %{_datadir}/gnome
%dir %{_datadir}/gnome/help

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_pkgconfigdir}/*.pc
%{_includedir}/libgnomeui-2.0
%{_gtkdocdir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
