%define url_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	GNOME frontend to GnuPG
Name:		seahorse
Version:	 3.15.92
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		http://seahorse.sourceforge.net/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

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

Requires:	gnupg
%rename		gnome-keyring-manager

%description
Seahorse is a GNOME frontend for the GNU Privacy Guard ecryption tool. It can
be used for file encryption and decryption and for digitally signing files and
for verifying those signatures. Key management options are also included.

%prep
%setup -q
%apply_patches

%build
%configure

%make

%install
%makeinstall_std

# Menu
desktop-file-install --vendor="" \
	--remove-category="Advanced" \
	--remove-category="Application" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name} --all-name --with-gnome

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/seahorse
%{_libdir}/%{name}/
%{_datadir}/applications/seahorse.desktop
%{_datadir}/GConf/gsettings/*.convert
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/seahorse
%{_mandir}/man1/*
%{_datadir}/appdata/seahorse.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.seahorse.Application.service
%{_datadir}/gnome-shell/search-providers/seahorse-search-provider.ini


