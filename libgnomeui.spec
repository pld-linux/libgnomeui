%define libxml2_version 2.4.12
%define orbit2_version 2.3.103
%define bonobo_activation_version 0.9.3.91
%define libbonobo_version 1.110.0
%define libgnomecanvas_version 1.110.0
%define libgnome_version 1.110.0
%define libart_lgpl_version 2.3.8
%define libbonoboui_version 1.110.0
%define glib2_version 1.3.13
%define gtk2_version 1.3.13
%define gconf2_version 1.1.6
%define gnome_vfs2_version 1.9.4.91
%define libglade2_version 1.99.5.90

Summary:	GNOME base GUI library
Name:		libgnomeui
Version:	1.110.0
Release:	1
License:	LGPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/Библиотеки
Group(uk):	X11/Б╕бл╕отеки
Source0:	ftp://ftp.gnome.org/pub/gnome/pre-gnome2/sources/libgnomeui/%{name}-%{version}.tar.bz2
URL:		http://www.gnome.org/
Requires:	ORBit2 >= %{orbit2_version}
Requires:	glib2 >= %{glib2_version}
Requires:	gtk2 >= %{gtk2_version}
Requires:	GConf2 >= %{gconf2_version} 
Requires:	gnome-vfs2 >= %{gnome_vfs2_version}
Requires:	libgnomecanvas >= %{libgnomecanvas_version}
Requires:	bonobo-activation >= %{bonobo_activation_version}
Requires:	libbonobo >= %{libbonobo_version}
Requires:	libbonoboui >= %{libbonoboui_version}
Requires:	libxml2 >= %{libxml2_version}
Requires:	libgnome >= %{libgnome_version}
Requires:	libart_lgpl >= %{libart_lgpl_version}
Requires:	libglade2 >= %{libglade2_version}
BuildRequires:	zlib-devel
BuildRequires:	esound-devel
BuildRequires:	ORBit2-devel >= %{orbit2_version}
BuildRequires:	glib2-devel >= %{glib2_version}
BuildRequires:	gtk2-devel >= %{gtk2_version}
BuildRequires:	GConf2-devel >= %{gconf2_version} 
BuildRequires:	gnome-vfs2-devel >= %{gnome_vfs2_version}
BuildRequires:	libgnomecanvas-devel >= %{libgnomecanvas_version}
BuildRequires:	bonobo-activation-devel >= %{bonobo_activation_version}
BuildRequires:	libbonobo-devel >= %{libbonobo_version}
BuildRequires:	libbonoboui-devel >= %{libbonoboui_version}
BuildRequires:	libxml2-devel >= %{libxml2_version}
BuildRequires:	libgnome-devel >= %{libgnome_version}
BuildRequires:	libart_lgpl-devel >= %{libart_lgpl_version}
BuildRequires:	libglade2-devel >= %{libglade2_version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
GNOME (GNU Network Object Model Environment) is a user-friendly set of
GUI applications and desktop tools to be used in conjunction with a
window manager for the X Window System. The libgnomeui package
includes GUI-related libraries that are needed to run GNOME. (The
libgnome package includes the library features that don't use the X
Window System.)

%package devel
Summary:	Libraries and headers for libgnome
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Разработка/Библиотеки
Group(uk):	X11/Розробка/Б╕бл╕отеки
Requires:	%name = %{version}
Requires:	zlib-devel
Requires:	esound-devel
Requires:	ORBit2-devel >= %{orbit2_version}
Requires:	glib2-devel >= %{glib2_version}
Requires:	gtk2-devel >= %{gtk2_version}
Requires:	GConf2-devel >= %{gconf2_version} 
Requires:	gnome-vfs2-devel >= %{gnome_vfs2_version}
Requires:	libgnomecanvas-devel >= %{libgnomecanvas_version}
Requires:	bonobo-activation-devel >= %{bonobo_activation_version}
Requires:	libbonobo-devel >= %{libbonobo_version}
Requires:	libbonoboui-devel >= %{libbonoboui_version}
Requires:	libxml2-devel >= %{libxml2_version}
Requires:	libgnome-devel >= %{libgnome_version}
Requires:	libart_lgpl-devel >= %{libart_lgpl_version}
Requires:	libglade2-devel >= %{libglade2_version}

Conflicts:	gnome-libs-devel < 1.4.1.2
Conflicts:	gdk-pixbuf-devel <= 0.11

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

%prep
%setup -q

%build
%configure \
	--disable-gtk-doc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)

%doc AUTHORS COPYING ChangeLog NEWS README

%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_libdir}/libglade/2.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la

%{_libdir}/lib*.a
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/gtk-doc
