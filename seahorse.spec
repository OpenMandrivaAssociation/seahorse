%define url_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	GNOME frontend to GnuPG
Name:		seahorse
Version:	3.4.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		http://seahorse.sourceforge.net/
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	gnome-doc-utils
BuildRequires:	gnupg
BuildRequires:	imagemagick
BuildRequires:	intltool
BuildRequires:	xsltproc
BuildRequires:	desktop-file-utils
BuildRequires:	gpgme-devel >= 1.0.0
BuildRequires:	libldap-devel
BuildRequires:	pkgconfig(avahi-client)
BuildRequires:	pkgconfig(avahi-glib) >= 0.6
BuildRequires:	pkgconfig(gck-1) >= 3.1.2
BuildRequires:	pkgconfig(gcr-3) >= 3.1.5
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gmodule-2.0)
BuildRequires:	pkgconfig(gnome-keyring-1) >= 2.25.5
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk+-3.0) >= 2.90.0
BuildRequires:	pkgconfig(libsoup-2.4)

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
%configure2_5x \
	--disable-static
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
%dir %{_datadir}/seahorse/
%{_datadir}/seahorse/ui
%{_datadir}/seahorse/icons/hicolor/*/*/*
%{_mandir}/man1/*

