## don't replace ltmain.sh
%define __libtoolize echo


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

Summary: GNOME base GUI library
Name: libgnomeui
Version: 1.110.0
Release: 1
URL: ftp://ftp.gnome.org
Source0: %{name}-%{version}.tar.gz
Source2: gnomeui-fixed-ltmain.sh
License: LGPL
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-root

Requires: ORBit2 >= %{orbit2_version}
Requires: glib2 >= %{glib2_version}
Requires: gtk2 >= %{gtk2_version}
Requires: GConf2 >= %{gconf2_version} 
Requires: gnome-vfs2 >= %{gnome_vfs2_version}
Requires: libgnomecanvas >= %{libgnomecanvas_version}
Requires: bonobo-activation >= %{bonobo_activation_version}
Requires: libbonobo >= %{libbonobo_version}
Requires: libbonoboui >= %{libbonoboui_version}
Requires: libxml2 >= %{libxml2_version}
Requires: libgnome >= %{libgnome_version}
Requires: libart_lgpl >= %{libart_lgpl_version}
Requires: libglade2 >= %{libglade2_version}

BuildRequires:	zlib-devel
BuildRequires:	esound-devel
BuildRequires:	ORBit2-devel >= %{orbit2_version}
BuildRequires:	glib2-devel >= %{glib2_version}
BuildRequires:	gtk2-devel >= %{gtk2_version}
BuildRequires:  GConf2-devel >= %{gconf2_version} 
BuildRequires:  gnome-vfs2-devel >= %{gnome_vfs2_version}
BuildRequires:  libgnomecanvas-devel >= %{libgnomecanvas_version}
BuildRequires:  bonobo-activation-devel >= %{bonobo_activation_version}
BuildRequires:  libbonobo-devel >= %{libbonobo_version}
BuildRequires:  libbonoboui-devel >= %{libbonoboui_version}
BuildRequires:  libxml2-devel >= %{libxml2_version}
BuildRequires:  libgnome-devel >= %{libgnome_version}
BuildRequires:  libart_lgpl-devel >= %{libart_lgpl_version}
BuildRequires:  libglade2-devel >= %{libglade2_version}

%description

GNOME (GNU Network Object Model Environment) is a user-friendly set of
GUI applications and desktop tools to be used in conjunction with a
window manager for the X Window System. The libgnomeui package
includes GUI-related libraries that are needed to run GNOME. (The
libgnome package includes the library features that don't use the X
Window System.)

%package devel
Summary: Libraries and headers for libgnome
Group: Development/Libraries
Requires:	%name = %{version}

Requires: zlib-devel
Requires: esound-devel
Requires: ORBit2-devel >= %{orbit2_version}
Requires: glib2-devel >= %{glib2_version}
Requires: gtk2-devel >= %{gtk2_version}
Requires: GConf2-devel >= %{gconf2_version} 
Requires: gnome-vfs2-devel >= %{gnome_vfs2_version}
Requires: libgnomecanvas-devel >= %{libgnomecanvas_version}
Requires: bonobo-activation-devel >= %{bonobo_activation_version}
Requires: libbonobo-devel >= %{libbonobo_version}
Requires: libbonoboui-devel >= %{libbonoboui_version}
Requires: libxml2-devel >= %{libxml2_version}
Requires: libgnome-devel >= %{libgnome_version}
Requires: libart_lgpl-devel >= %{libart_lgpl_version}
Requires: libglade2-devel >= %{libglade2_version}

Conflicts: gnome-libs-devel < 1.4.1.2
Conflicts: gdk-pixbuf-devel <= 0.11

%description devel

GNOME (GNU Network Object Model Environment) is a user-friendly set of
GUI applications and desktop tools to be used in conjunction with a
window manager for the X Window System. The libgnomeui-devel package
includes the libraries and include files that you will need to
use libgnomeui.

You should install the libgnomeui-devel package if you would like to
compile GNOME applications. You do not need to install
libgnomeui-devel if you just want to use the GNOME desktop
environment.

%prep
%setup -q

## bad hack for a broken CVS snap that didn't dist this file
touch libgnomeui/pixmaps/copyright.txt

%build

rm ltmain.sh && cp %{SOURCE2} ltmain.sh
for i in config.guess config.sub ; do
	test -f /usr/share/libtool/$i && cp /usr/share/libtool/$i .
done

%configure --disable-gtk-doc
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post

%files -f %{name}.lang
%defattr(-,root,root)

%doc AUTHORS COPYING ChangeLog NEWS README

%{_libdir}/lib*.so.*
%{_bindir}/*
## FIXME questionable that libgnomeui still contains these
%{_datadir}/pixmaps/*
%{_libdir}/libglade/2.0/*

%files devel
%defattr(-,root,root)

%{_libdir}/lib*.a
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/gtk-doc

%changelog
* Wed Jan 30 2002 Owen Taylor <otaylor@redhat.com>
- Version 1.110.0

* Mon Jan 28 2002 Havoc Pennington <hp@redhat.com>
- rebuild in rawhide
- --disable-gtk-doc

* Mon Jan  7 2002 Havoc Pennington <hp@redhat.com>
- 1.108.0.90 snap, remove gconf stuff moved to libgnome

* Tue Nov 27 2001 Havoc Pennington <hp@redhat.com>
- 1.106.0.90 snap, glib 1.3.11
- add explicit-versioned requires on dependency libs
- do gconftool stuff, put schemas in file list
- use makeinstall instead of destdir to avoid broken makefiles

* Mon Oct 29 2001 Havoc Pennington <hp@redhat.com>
- grumble, we require libglade 2 not libglade 1

* Mon Oct 29 2001 Havoc Pennington <hp@redhat.com>
- add libglade module to file list
- add libglade dependency

* Sun Oct 28 2001 Havoc Pennington <hp@redhat.com>
- new snap, rebuild for glib 1.3.10

* Fri Oct  5 2001 Havoc Pennington <hp@redhat.com>
- new tarball, rebuild for new glib, remove db1 dependency

* Mon Sep 24 2001 Havoc Pennington <hp@redhat.com>
- new cvs snap

* Tue Sep 18 2001 Havoc Pennington <hp@redhat.com>
- Initial build.
