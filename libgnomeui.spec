#
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc
%bcond_without	static_libs	# static library

Summary:	GNOME base GUI library
Summary(pl.UTF-8):	Podstawowa biblioteka GUI GNOME
Name:		libgnomeui
Version:	2.24.5
Release:	5
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgnomeui/2.24/%{name}-%{version}.tar.bz2
# Source0-md5:	d4bb506b1916015323928faab5aa708b
Patch0:		format-security.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.24.0
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.9
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gdk-pixbuf2-devel >= 2.12.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.18.0
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gnome-vfs2-devel >= 2.24.0
BuildRequires:	gtk+2-devel >= 2:2.12.8
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.8}
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libbonoboui-devel >= 2.24.0
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libgnome-devel >= 2.24.0
BuildRequires:	libgnome-keyring-devel >= 2.24.0
BuildRequires:	libgnomecanvas-devel >= 2.20.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	pango-devel >= 1:1.1.2
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	popt-devel >= 1.5
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
Requires:	GConf2-libs >= 2.24.0
Requires:	gdk-pixbuf2 >= 2.12.0
Requires:	glib2 >= 1:2.18.0
Requires:	gnome-vfs2-libs >= 2.24.0
Requires:	gtk+2 >= 2:2.12.8
Requires:	libbonoboui >= 2.24.0
Requires:	libgnome-keyring >= 2.24.0
Requires:	libgnome-libs >= 2.24.0
Requires:	libxml2 >= 1:2.6.31
Requires:	popt >= 1.5
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
Requires:	GConf2-devel >= 2.24.0
Requires:	gdk-pixbuf2-devel >= 2.12.0
Requires:	glib2-devel >= 1:2.18.0
Requires:	gnome-vfs2-devel >= 2.24.0
Requires:	gtk+2-devel >= 2:2.12.8
Requires:	libbonoboui-devel >= 2.24.0
Requires:	libglade2-devel >= 1:2.6.2
Requires:	libgnome-keyring-devel >= 2.24.0
Requires:	libgnomecanvas-devel >= 2.20.0
Requires:	popt-devel >= 1.5
Requires:	xorg-lib-libSM-devel

%description devel
This package includes the header files that you will need for
libgnomeui applications development.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne do kompilacji programów
używających libgnomeui.

%package static
Summary:	Static libgnomeui library
Summary(pl.UTF-8):	Statyczna biblioteka libgnomeui
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of libgnomeui library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki libgnomeui.

%package apidocs
Summary:	libgnomeui API documentation
Summary(pl.UTF-8):	Dokumentacja API libgnomeui
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
libgnomeui API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libgnomeui.

%package examples
Summary:	libgnomeui - example programs
Summary(pl.UTF-8):	libgnomeui - przykładowe programy
Group:		X11/Development/Libraries
BuildArch:	noarch

%description examples
libgnomeui - example programs.

%description examples -l pl.UTF-8
libgnomeui - przykładowe programy.

%prep
%setup -q
%patch0 -p1

%build
%{?with_apidocs:%{__gtkdocize}}
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static} \
	--enable-gtk-doc%{!?with_apidocs:=no} \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/gnome/help,%{_examplesdir}/%{name}-%{version}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

cp demos/*.c $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# no static modules and *.la for libglade
# libraries .la obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la \
	$RPM_BUILD_ROOT%{_libdir}/libglade/2.0/*.la
%if %{with static_libs}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libglade/2.0/*.a
%endif

%if %{without apidocs}
rm -rf $RPM_BUILD_ROOT%{_gtkdocdir}/libgnomeui
%endif

%{__mv} $RPM_BUILD_ROOT%{_localedir}/{sr@ije,sr@ijekavian}

%find_lang %{name}-2.0

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}-2.0.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%attr(755,root,root) %{_libdir}/libgnomeui-2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnomeui-2.so.0
%attr(755,root,root) %{_libdir}/libglade/2.0/libgnome.so
%{_pixmapsdir}/gnome-about-logo.png

%files devel
%defattr(644,root,root,755)
%{_includedir}/libgnomeui-2.0
%attr(755,root,root) %{_libdir}/libgnomeui-2.so
%{_pkgconfigdir}/libgnomeui-2.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgnomeui-2.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}
%endif

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
