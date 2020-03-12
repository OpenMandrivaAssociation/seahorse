%define url_ver	%(echo %{version}|cut -d. -f1,2)
%define _disable_rebuild_configure 1

Summary:	GNOME frontend to GnuPG
Name:		seahorse
Version:	3.36
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		http://seahorse.sourceforge.net/
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	desktop-file-utils
BuildRequires:	gnupg
BuildRequires:	imagemagick
BuildRequires:	intltool itstool
BuildRequires:	xsltproc
BuildRequires:	gpgme-devel >= 1.0.0
BuildRequires:	openldap-devel
BuildRequires:	pkgconfig(avahi-client)
BuildRequires:	pkgconfig(avahi-glib)
BuildRequires:	pkgconfig(gck-1)
BuildRequires:	pkgconfig(gcr-3)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gmodule-2.0)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(libsecret-1)
BuildRequires:	pkgconfig(pwquality)
BuildRequires:	vala
BuildRequires:	openssh-clients
BuildRequires:	meson

Requires:	gnupg
%rename		gnome-keyring-manager

%description
Seahorse is a GNOME frontend for the GNU Privacy Guard ecryption tool. It can
be used for file encryption and decryption and for digitally signing files and
for verifying those signatures. Key management options are also included.

%prep
%setup -q
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install

# Menu
#desktop-file-install --vendor="" \
#	--remove-category="Advanced" \
#	--remove-category="Application" \
#	--dir %{buildroot}%{_datadir}/applications \
#	%{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name} --all-name --with-gnome

%files -f %{name}.lang
%doc AUTHORS NEWS README.md
%{_bindir}/seahorse
%{_datadir}/applications/org.gnome.seahorse.Application.desktop
#{_datadir}/GConf/gsettings/*.convert
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/seahorse
#{_mandir}/man1/*
%{_datadir}/metainfo/org.gnome.seahorse.Application.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.seahorse.Application.service
%{_datadir}/gnome-shell/search-providers/seahorse-search-provider.ini
%{_libexecdir}/seahorse/ssh-askpass
%{_libexecdir}/seahorse/xloadimage
