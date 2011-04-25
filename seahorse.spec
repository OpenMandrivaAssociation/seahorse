%define name seahorse
%define version 3.0.1
%define release %mkrel 1
%define major 0
%define libname %mklibname cryptui %major
%define libnamedev %mklibname -d cryptui

Name:		%{name}
Summary:	GNOME2 frontend to GnuPG
Version:	%{version}
Release:	%{release}
# seahorse is GPLv2+
# libcryptui is LGPLv2+
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/GNOME
URL:		http://seahorse.sourceforge.net/
Source:		http://ftp.gnome.org/pub/GNOME/sources/seahorse/%{name}-%{version}.tar.bz2
Requires:	gnupg
BuildRoot:	%{_tmppath}/%{name}-%{version}
BuildRequires:  gpgme-devel >= 1.0.0
BuildRequires:  openssh-clients
BuildRequires: avahi-client-devel avahi-glib-devel
BuildRequires: libGConf2-devel GConf2
BuildRequires: scrollkeeper
BuildRequires: libnotify-devel
BuildRequires: libldap-devel
BuildRequires: libsoup-devel
BuildRequires: libgnome-keyring-devel >= 3.0.0
BuildRequires: libgcr-devel >= 3.0.0
BuildRequires: gobject-introspection-devel
BuildRequires: gtk+2-devel
BuildRequires: libsm-devel
BuildRequires: gnome-doc-utils
BuildRequires: intltool
BuildRequires: automake
BuildRequires: libxslt-proc
%rename seahorse2
%rename gnome-keyring-manager

%description
Seahorse is a GNOME2 frontend for the GNU Privacy Guard ecryption tool. It can 
be used for file encryption and decryption and for digitally signing files and 
for verifying those signatures. Key management options are also included.

%package -n %libname
Group: System/Libraries
Summary: Seahorse libraries
Obsoletes: %{_lib}seahorse0 < 3.0.0

%description -n %libname
Seahorse is a GNOME2 frontend for the GNU Privacy Guard ecryption tool. It can 
be used for file encryption and decryption and for digitally signing files and 
for verifying those signatures. Key management options are also included.
 
%package -n %libnamedev
Group: Development/C
Summary: Seahorse libraries
Requires: %libname = %version
Provides: %name-devel = %version-%release
Obsoletes: %mklibname -d %name 0
Obsoletes: %{_lib}seahorse-devel < 3.0.0

%description -n %libnamedev
Seahorse is a GNOME2 frontend for the GNU Privacy Guard ecryption tool. It can 
be used for file encryption and decryption and for digitally signing files and 
for verifying those signatures. Key management options are also included.


%prep
%setup -q

%build
%configure2_5x --disable-update-mime-database --disable-static --disable-schemas-install --with-gtk=2
%make

%install
rm -rf $RPM_BUILD_ROOT %name.lang
%makeinstall_std

%{find_lang} seahorse --with-gnome --all-name
for omf in %buildroot%_datadir/omf/*/*-??*.omf;do 
echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed -e s!%buildroot!!)" >> %name.lang
done
 
%clean
rm -rf $RPM_BUILD_ROOT

%preun
%preun_uninstall_gconf_schemas %name

%files -n %libname
%defattr(-,root,root,0755)
%_libdir/*.so.%{major}*
%_libdir/girepository-1.0/CryptUI-0.0.typelib

%files -n %libnamedev
%defattr(-,root,root,0755)
%_libdir/*.so
%_libdir/*.la
%_includedir/*
%_libdir/pkgconfig/*.pc
%_datadir/gir-1.0/CryptUI-0.0.gir

%files -f %{name}.lang
%defattr(-,root,root,0755)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_sysconfdir}/gconf/schemas/seahorse.schemas
%{_bindir}/seahorse
%{_bindir}/seahorse-daemon
%_mandir/man1/*
%{_libdir}/%name/
%{_datadir}/applications/seahorse.desktop
%_datadir/pixmaps/*
%dir %{_datadir}/omf/seahorse/
%dir %{_datadir}/seahorse/
%{_datadir}/seahorse/ui
%{_datadir}/omf/seahorse/seahorse-C.omf
%_datadir/dbus-1/services/*
%_datadir/icons/hicolor/*/apps/*
%_datadir/gtk-doc/html/libcryptui/
%_datadir/gtk-doc/html/libseahorse/
