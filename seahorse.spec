%define name seahorse
%define version 2.19.4
%define release %mkrel 2
%define major 0
%define libname %mklibname %name %major

%define epiphany 2.19

Name:		%{name}
Summary:	Seahorse is a GNOME2 frontend to GnuPG
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Graphical desktop/GNOME
URL:		http://seahorse.sourceforge.net/
Source:		http://ftp.gnome.org/pub/GNOME/sources/seahorse/%{name}-%{version}.tar.bz2
Patch:		seahorse-0.9.0-makefile.patch
Requires:	gnupg
BuildRoot:	%{_tmppath}/%{name}-%{version}
BuildRequires:  gpgme-devel >= 1.0.0
BuildRequires:  openssh-clients
BuildRequires:  gedit-devel
BuildRequires:  epiphany-devel >= %epiphany mozilla-firefox-devel
BuildRequires: libnautilus-devel
BuildRequires: scrollkeeper
BuildRequires: libnotify-devel
BuildRequires: libldap-devel
BuildRequires: libsoup-devel
BuildRequires: gnome-panel-devel
BuildRequires: gnome-doc-utils
BuildRequires: intltool
BuildRequires: automake1.9
BuildRequires: ImageMagick
BuildRequires: libxslt-proc
BuildRequires: desktop-file-utils
Obsoletes:	seahorse2
Provides:	seahorse2
Requires(post): scrollkeeper,shared-mime-info,desktop-file-utils
Requires(postun):scrollkeeper,shared-mime-info,desktop-file-utils

%description
Seahorse is a GNOME2 frontend for the GNU Privacy Guard ecryption tool. It can 
be used for file encryption and decryption and for digitally signing files and 
for verifying those signatures. Key management options are also included. Both 
English and Japanese is support is provided. 
NOTE: NO CRYPTO STUFF IN THIS PACKAGE

%package -n %libname
Group: System/Libraries
Summary: Seahorse libraries

%description -n %libname
Seahorse is a GNOME2 frontend for the GNU Privacy Guard ecryption tool. It can 
be used for file encryption and decryption and for digitally signing files and 
for verifying those signatures. Key management options are also included. Both 
English and Japanese is support is provided. 
NOTE: NO CRYPTO STUFF IN THIS PACKAGE

%package -n %libname-devel
Group: Development/C
Summary: Seahorse libraries
Requires: %libname = %version
Provides: lib%name-devel = %version-%release

%description -n %libname-devel
Seahorse is a GNOME2 frontend for the GNU Privacy Guard ecryption tool. It can 
be used for file encryption and decryption and for digitally signing files and 
for verifying those signatures. Key management options are also included. Both 
English and Japanese is support is provided. 
NOTE: NO CRYPTO STUFF IN THIS PACKAGE

%package epiphany
Group: Networking/WWW
Summary: Seahorse GnuPG plugin for Epiphany 
Requires: %name = %version
Requires: epiphany >= %epiphany

%description epiphany
Seahorse is a GNOME2 frontend for the GNU Privacy Guard ecryption tool. It can 
be used for file encryption and decryption and for digitally signing files and 
for verifying those signatures.

This package integrates Seahorse with the Epiphany web browser.

%prep

%setup -q

%patch -p1 -b .makefile
aclocal -I m4
automake -a -c
autoconf

%build
export CPPFLAGS="$CPPFLAGS -DLIBCRYPTUI_API_SUBJECT_TO_CHANGE"
%configure2_5x --enable-fast-install

make

%install
rm -rf $RPM_BUILD_ROOT

GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std _ENABLE_SK=false
rm -f %buildroot%_libdir/libseahorse*{a,so}

# Menu
mkdir -p %buildroot/%_menudir
cat > %buildroot/%_menudir/%name  <<EOF
?package(%name): command="%_bindir/seahorse" needs="X11" \
icon="seahorse.png" section="System/File Tools" \
title="GPG Keys Manager" longtitle="Manage your GPG keys" xdg="true"
?package(%name): command="%_bindir/seahorse-preferences" needs="gnome" \
icon="seahorse.png" section="Configuration/GNOME/Advanced" \
title="PGP Preferences" longtitle="Configure PGP" xdg="true"
EOF
desktop-file-install --vendor="" \
  --remove-category="Advanced" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-System-FileTools" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/seahorse.desktop
desktop-file-install --vendor="" \
  --remove-category="Advanced" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-System-Configuration-Other" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/seahorse-pgp-preferences.desktop


mkdir -p %buildroot{%_liconsdir,%_miconsdir,%_iconsdir}
ln -s %_datadir/pixmaps/%name.png %buildroot%_liconsdir/
convert -scale 32 pixmaps/48x48/%name.png %buildroot%_iconsdir/%name.png
convert -scale 16 pixmaps/48x48/%name.png %buildroot%_miconsdir/%name.png

%{find_lang} seahorse --with-gnome
%{find_lang} seahorse-applet --with-gnome
cat seahorse-applet.lang >> seahorse.lang
for omf in %buildroot%_datadir/omf/%name/%name-??*.omf;do 
echo "%lang($(basename $omf|sed -e s/%name-// -e s/.omf//)) $(echo $omf|sed -e s!%buildroot!!)" >> %name.lang
done


#remove unpackaged files
rm -f $RPM_BUILD_ROOT%{_libdir}/{epiphany/*/extensions/,nautilus/extensions-1.0,gedit-2/plugins}/*.{la,a}
 
%post
%{update_menus}
%define schemas seahorse-gedit seahorse
%post_install_gconf_schemas %schemas
%update_mime_database
%update_desktop_database
%update_icon_cache hicolor
%update_scrollkeeper

%preun
%preun_uninstall_gconf_schemas %schemas

%postun
%{clean_menus} 
%clean_mime_database
%clean_desktop_database
%clean_icon_cache hicolor
%clean_scrollkeeper

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %libname
%defattr(-,root,root,0755)
%_libdir/*.so.%{major}*

%files -n %libname-devel
%defattr(-,root,root,0755)
%_libdir/*.so
%_libdir/*.a
%attr(644,root,root) %_libdir/*.la
%_includedir/*
%_libdir/pkgconfig/*.pc

%files -f %{name}.lang
%defattr(-,root,root,0755)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_sysconfdir}/gconf/schemas/seahorse.schemas
%{_sysconfdir}/gconf/schemas/seahorse-gedit.schemas
%{_bindir}/seahorse
%{_bindir}/seahorse-agent
%{_bindir}/seahorse-preferences
%{_bindir}/seahorse-tool
%attr(4755,root,root) %{_bindir}/seahorse-daemon
%_mandir/man1/*
%{_libdir}/%name/
%{_libdir}/gedit-2/plugins/*
%_libdir/nautilus/extensions-1.0/libnautilus-seahorse.so
%_datadir/mime/packages/%name.xml
%{_datadir}/applications/seahorse.desktop
%{_datadir}/applications/seahorse-pgp-encrypted.desktop
%{_datadir}/applications/seahorse-pgp-keys.desktop
%{_datadir}/applications/seahorse-pgp-signature.desktop
%{_datadir}/applications/seahorse-pgp-preferences.desktop
%dir %{_datadir}/omf/seahorse/
%_datadir/pixmaps/*
%{_datadir}/omf/seahorse/seahorse-C.omf
%dir %{_datadir}/seahorse/
%dir %{_datadir}/seahorse/glade/
%{_datadir}/seahorse/glade/*
%_datadir/dbus-1/services/*
#%_libexecdir/seahorse-applet
%_libdir/bonobo/servers/*
%_datadir/gnome-2.0/ui/*.xml
%_datadir/icons/hicolor/*/apps/*
%dir %_datadir/omf/seahorse-applet/
%_datadir/omf/seahorse-applet/*-C.omf
%{_menudir}/*
%_liconsdir/%name.png
%_iconsdir/%name.png
%_miconsdir/%name.png

%files epiphany
%defattr(-,root,root,0755)
%_libdir/epiphany/%epiphany/extensions/*
