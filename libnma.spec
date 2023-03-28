#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
Name     : libnma
Version  : 1.10.6
Release  : 19
URL      : https://download.gnome.org/sources/libnma/1.10/libnma-1.10.6.tar.xz
Source0  : https://download.gnome.org/sources/libnma/1.10/libnma-1.10.6.tar.xz
Summary  : NetworkManager UI utilities (libnm version)
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: libnma-data = %{version}-%{release}
Requires: libnma-lib = %{version}-%{release}
Requires: libnma-license = %{version}-%{release}
Requires: libnma-locales = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : buildreq-gnome
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gmodule-export-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(iso-codes)
BuildRequires : pkgconfig(libnm)
BuildRequires : pkgconfig(mobile-broadband-provider-info)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description


%package data
Summary: data components for the libnma package.
Group: Data

%description data
data components for the libnma package.


%package dev
Summary: dev components for the libnma package.
Group: Development
Requires: libnma-lib = %{version}-%{release}
Requires: libnma-data = %{version}-%{release}
Provides: libnma-devel = %{version}-%{release}
Requires: libnma = %{version}-%{release}

%description dev
dev components for the libnma package.


%package doc
Summary: doc components for the libnma package.
Group: Documentation

%description doc
doc components for the libnma package.


%package lib
Summary: lib components for the libnma package.
Group: Libraries
Requires: libnma-data = %{version}-%{release}
Requires: libnma-license = %{version}-%{release}

%description lib
lib components for the libnma package.


%package license
Summary: license components for the libnma package.
Group: Default

%description license
license components for the libnma package.


%package locales
Summary: locales components for the libnma package.
Group: Default

%description locales
locales components for the libnma package.


%prep
%setup -q -n libnma-1.10.6
cd %{_builddir}/libnma-1.10.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1680038744
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%configure --disable-static --with-libnma-gtk4
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1680038744
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libnma
cp %{_builddir}/libnma-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libnma/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/libnma-%{version}/COPYING.LGPL %{buildroot}/usr/share/package-licenses/libnma/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
%make_install
%find_lang libnma
## Remove excluded files
rm -f %{buildroot}*/usr/share/glib-2.0/schemas/org.gnome.nm-applet.gschema.xml

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/NMA-1.0.typelib
/usr/lib64/girepository-1.0/NMA4-1.0.typelib
/usr/share/gir-1.0/*.gir
/usr/share/glib-2.0/schemas/org.gnome.nm-applet.eap.gschema.xml
/usr/share/vala/vapi/libnma-gtk4.deps
/usr/share/vala/vapi/libnma-gtk4.vapi
/usr/share/vala/vapi/libnma.deps
/usr/share/vala/vapi/libnma.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/libnma/nma-bar-code-widget.h
/usr/include/libnma/nma-bar-code.h
/usr/include/libnma/nma-cert-chooser.h
/usr/include/libnma/nma-mobile-providers.h
/usr/include/libnma/nma-mobile-wizard.h
/usr/include/libnma/nma-ui-utils.h
/usr/include/libnma/nma-version.h
/usr/include/libnma/nma-vpn-password-dialog.h
/usr/include/libnma/nma-wifi-dialog.h
/usr/include/libnma/nma-ws-802-1x.h
/usr/include/libnma/nma-ws-dynamic-wep.h
/usr/include/libnma/nma-ws-leap.h
/usr/include/libnma/nma-ws-owe.h
/usr/include/libnma/nma-ws-sae.h
/usr/include/libnma/nma-ws-wep-key.h
/usr/include/libnma/nma-ws-wpa-eap.h
/usr/include/libnma/nma-ws-wpa-psk.h
/usr/include/libnma/nma-ws.h
/usr/lib64/libnma-gtk4.so
/usr/lib64/libnma.so
/usr/lib64/pkgconfig/libnma-gtk4.pc
/usr/lib64/pkgconfig/libnma.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/libnma/NMABarCode.html
/usr/share/gtk-doc/html/libnma/NMACertChooser.html
/usr/share/gtk-doc/html/libnma/NMAMobileProvidersDatabase.html
/usr/share/gtk-doc/html/libnma/NMAMobileWizard.html
/usr/share/gtk-doc/html/libnma/NMAVpnPasswordDialog.html
/usr/share/gtk-doc/html/libnma/NMAWifiDialog.html
/usr/share/gtk-doc/html/libnma/annotation-glossary.html
/usr/share/gtk-doc/html/libnma/api-index-1.8.0.html
/usr/share/gtk-doc/html/libnma/api-index-full.html
/usr/share/gtk-doc/html/libnma/api-reference.html
/usr/share/gtk-doc/html/libnma/home.png
/usr/share/gtk-doc/html/libnma/index.html
/usr/share/gtk-doc/html/libnma/left-insensitive.png
/usr/share/gtk-doc/html/libnma/left.png
/usr/share/gtk-doc/html/libnma/libnma-nma-ui-utils.html
/usr/share/gtk-doc/html/libnma/libnma.devhelp2
/usr/share/gtk-doc/html/libnma/object-tree.html
/usr/share/gtk-doc/html/libnma/right-insensitive.png
/usr/share/gtk-doc/html/libnma/right.png
/usr/share/gtk-doc/html/libnma/style.css
/usr/share/gtk-doc/html/libnma/up-insensitive.png
/usr/share/gtk-doc/html/libnma/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libnma-gtk4.so.0
/usr/lib64/libnma-gtk4.so.0.0.0
/usr/lib64/libnma.so.0
/usr/lib64/libnma.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libnma/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/libnma/4cc77b90af91e615a64ae04893fdffa7939db84c

%files locales -f libnma.lang
%defattr(-,root,root,-)

