Summary:	GNOME base GUI library
Summary(pl):	Podstawowa biblioteka GUI GNOME
Name:		libgnomeui
Version:	2.0.6
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/2.0/%{name}-%{version}.tar.bz2
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libbonoboui-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_gtkdocdir	%{_defaultdocdir}/gtk-doc/html

%description
GNOME (GNU Network Object Model Environment) is a user-friendly set of
GUI applications and desktop tools to be used in conjunction with a
window manager for the X Window System. The libgnomeui package
includes GUI-related libraries that are needed to run GNOME. (The
libgnome package includes the library features that don't use the X
Window System.)

%description -l pl
GNOME (GNU Network Object Model Environment) jest przyjaznym dla
u�ytkownika zestawem aplikacji i narz�dzi z graficznym interfejsem do
u�ywania w po��czeniu z menad�erem okien X Window System. Pakiet
libgnomeui zawiera biblioteki zwi�zane z graficznym interfejsem
u�ytkownika potrzebne do uruchomienia GNOME (pakiet libgnome zawiera
biblioteki nie u�ywaj�ce X Window System).

%package devel
Summary:	Headers for libgnomeui
Summary(pl):	Pliki nag��wkowe libgnomeui
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	gtk-doc-common
Requires:	libbonoboui-devel

%description devel
GNOME (GNU Network Object Model Environment) is a user-friendly set of
GUI applications and desktop tools to be used in conjunction with a
window manager for the X Window System. The libgnomeui-devel package
includes the libraries and include files that you will need to use
libgnomeui.

You should install the libgnomeui-devel package if you would like to
compile GNOME applications. You do not need to install
libgnomeui-devel if you just want to use the GNOME desktop
environment.

%description devel -l pl
Ten pakiet zawiera pliki nag��wkowe potrzebne do kompilacji program�w
u�ywaj�cych libgnomeui.

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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
# AUTHORS, README - empty
# NEWS - outdated
%doc ChangeLog
%attr(755,root,root) %{_libdir}/gnome_segv2
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/libglade/2.0/*.so
%{_libdir}/libglade/2.0/*.la
%{_pixmapsdir}/*

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
%{_libdir}/libglade/2.0/*.a
