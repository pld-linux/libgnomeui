Summary:	GNOME base GUI library
Summary(pl.UTF-8):	Podstawowa biblioteka GUI GNOME
Name:		libgnomeui
Version:	2.21.5
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgnomeui/2.21/%{name}-%{version}.tar.bz2
# Source0-md5:	63e36f083a865d92039b665593d793da
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.20.0
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 2.15.2
BuildRequires:	gnome-keyring-devel >= 2.20.0
BuildRequires:	gnome-vfs2-devel >= 2.20.0
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	intltool >= 0.36.2
BuildRequires:	libbonoboui-devel >= 2.20.0
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libgnome-devel >= 2.20.0
BuildRequires:	libgnomecanvas-devel >= 2.20.0
BuildRequires:	libjpeg-devel
BuildRequires:	libxml2-devel >= 2.6.30
BuildRequires:	libtool
BuildRequires:	pango-devel >= 1:1.18.2
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	popt-devel >= 1.5
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	xorg-lib-libSM-devel
Requires:	gtk+2 >= 2:2.12.0
Requires:	gnome-keyring-libs >= 2.20.0
Requires:	gnome-vfs2-libs >= 2.20.0
Requires:	libbonoboui >= 2.20.0
Requires:	pango >= 1:1.18.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME (GNU Network Object Model Environment) is a user-friendly set of
GUI applications and desktop tools to be used in conjunction with a
window manager for the X Window System. The libgnomeui package
includes GUI-related libraries that are needed to run GNOME. (The
libgnome package includes the library features that don't use the X
Window System.)

%description -l pl.UTF-8
GNOME (GNU Network Object Model Environment) jest przyjaznym dla
użytkownika zestawem aplikacji i narzędzi z graficznym interfejsem do
używania w połączeniu z zarządcą okien X Window System. Pakiet
libgnomeui zawiera biblioteki związane z graficznym interfejsem
użytkownika potrzebne do uruchomienia GNOME (pakiet libgnome zawiera
biblioteki nie używające X Window System).

%package devel
Summary:	Headers for libgnomeui
Summary(pl.UTF-8):	Pliki nagłówkowe libgnomeui
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	GConf2-devel >= 2.20.0
Requires:	gnome-keyring-devel >= 2.20.0
Requires:	gnome-vfs2-devel >= 2.20.0
Requires:	gtk+2-devel >= 2:2.12.0
Requires:	libbonoboui-devel >= 2.20.0
Requires:	libglade2-devel >= 1:2.6.2
Requires:	libjpeg-devel
Requires:	popt-devel >= 1.5
Requires:	xorg-lib-libSM-devel

%description devel
GNOME (GNU Network Object Model Environment) is a user-friendly set of
GUI applications and desktop tools to be used in conjunction with a
window manager for the X Window System. The libgnomeui-devel package
includes the libraries and include files that you will need to use
libgnomeui.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne do kompilacji programów
używających libgnomeui.

%package static
Summary:	Static libgnomeui libraries
Summary(pl.UTF-8):	Statyczne biblioteki libgnomeui
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of libgnomeui libraries.

%description static -l pl.UTF-8
Statyczna wersja bibliotek libgnomeui.

%package apidocs
Summary:	libgnomeui API documentation
Summary(pl.UTF-8):	Dokumentacja API libgnomeui
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libgnomeui API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libgnomeui.

%package examples
Summary:	libgnomeui - example programs
Summary(pl.UTF-8):	libgnomeui - przykładowe programy
Group:		X11/Development/Libraries

%description examples
libgnomeui - example programs.

%description examples
libgnomeui - przykładowe programy.

%prep
%setup -q

%build
%{__gtkdocize}
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/gnome/help,%{_examplesdir}/%{name}-%{version}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

cp demos/*.c $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# no static modules and *.la for libglade or vfs modules
rm -f $RPM_BUILD_ROOT%{_libdir}/libglade/2.0/*.{la,a}
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.*/filesystems/libgnome-vfs.{la,a}
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.*/filesystems/libgio.{la,a}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%attr(755,root,root) %{_libdir}/gtk-2.0/2.*/filesystems/libgnome-vfs.so
%attr(755,root,root) %{_libdir}/gtk-2.0/2.*/filesystems/libgio.so
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/libglade/2.0/*.so
%{_pixmapsdir}/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/libgnomeui-2.0
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
