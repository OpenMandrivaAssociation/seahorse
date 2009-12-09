%define name seahorse
%define version 2.29.3
%define release %mkrel 1
%define major 0
%define libname %mklibname %name %major
%define libnamedev %mklibname -d %name

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
Patch: seahorse-2.27.92-fix-linking.patch
Requires:	gnupg
BuildRoot:	%{_tmppath}/%{name}-%{version}
BuildRequires:  gpgme-devel >= 1.0.0
BuildRequires:  openssh-clients
BuildRequires: avahi-client-devel avahi-glib-devel
BuildRequires: libGConf2-devel
BuildRequires: scrollkeeper
BuildRequires: libnotify-devel
BuildRequires: libldap-devel
BuildRequires: libsoup-devel
BuildRequires: gnome-keyring-devel >= 2.25.4
BuildRequires: gnome-doc-utils
BuildRequires: intltool
BuildRequires: automake
BuildRequires: imagemagick
BuildRequires: libxslt-proc
BuildRequires: desktop-file-utils
Obsoletes:	seahorse2
Provides:	seahorse2
Requires(post): rarian desktop-file-utils
Requires(postun): rarian desktop-file-utils

%description
Seahorse is a GNOME2 frontend for the GNU Privacy Guard ecryption tool. It can 
be used for file encryption and decryption and for digitally signing files and 
for verifying those signatures. Key management options are also included.

%package -n %libname
Group: System/Libraries
Summary: Seahorse libraries

%description -n %libname
Seahorse is a GNOME2 frontend for the GNU Privacy Guard ecryption tool. It can 
be used for file encryption and decryption and for digitally signing files and 
for verifying those signatures. Key management options are also included.
 
%package -n %libnamedev
Group: Development/C
Summary: Seahorse libraries
Requires: %libname = %version
Provides: lib%name-devel = %version-%release
Obsoletes: %mklibname -d %name 0

%description -n %libnamedev
Seahorse is a GNOME2 frontend for the GNU Privacy Guard ecryption tool. It can 
be used for file encryption and decryption and for digitally signing files and 
for verifying those signatures. Key management options are also included.


%prep

%setup -q
%patch -p1
autoreconf

%build
export CPPFLAGS="$CPPFLAGS -DLIBCRYPTUI_API_SUBJECT_TO_CHANGE -D_FILE_OFFSET_BITS=64 -DLARGEFILE_SOURCE=1"
%configure2_5x --enable-fast-install
make

%install
rm -rf $RPM_BUILD_ROOT %name.lang

GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std _ENABLE_SK=false
rm -f %buildroot%_libdir/libseahorse*{a,so}

# Menu
desktop-file-install --vendor="" \
  --remove-category="Advanced" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-System-FileTools" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/seahorse.desktop

%{find_lang} seahorse --with-gnome
%{find_lang} seahorse-applet --with-gnome
cat seahorse-applet.lang >> seahorse.lang
for omf in %buildroot%_datadir/omf/*/*-??*.omf;do 
echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed -e s!%buildroot!!)" >> %name.lang
done

 
%post
%if %mdkversion < 200900
%{update_menus}
%endif
%define schemas seahorse
%if %mdkversion < 200900
%post_install_gconf_schemas %schemas
%update_desktop_database
%update_icon_cache hicolor
%update_scrollkeeper
%endif

%preun
%preun_uninstall_gconf_schemas %schemas

%if %mdkversion < 200900
%postun
%{clean_menus} 
%clean_desktop_database
%clean_icon_cache hicolor
%clean_scrollkeeper
%endif

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %libname
%defattr(-,root,root,0755)
%_libdir/*.so.%{major}*

%files -n %libnamedev
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
%_sysconfdir/xdg/autostart/seahorse-daemon.desktop
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
