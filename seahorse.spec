%define url_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	GNOME frontend to GnuPG
Name:		seahorse
Version:	3.8.1
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
#apply_patches

%build
%configure2_5x \
	--disable-static \
	--disable-scrollkeeper

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
%{_datadir}/seahorse/icons/hicolor/*
%{_mandir}/man1/*



%changelog
* Tue Oct 16 2012 Arkady L. Shane <ashejn@rosalab.ru> 3.6.1-1
- update to 3.6.1

* Mon Jul 16 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.4.1-1
+ Revision: 809909
- added compile patch
- disabled scrollkeeper

  + Alexander Khrukin <akhrukin@mandriva.org>
    - version update 3.4.1

* Sun May 22 2011 GÃ¶tz Waschk <waschk@mandriva.org> 3.0.2-1
+ Revision: 677309
- update to new version 3.0.2

* Sun May 22 2011 Funda Wang <fwang@mandriva.org> 3.0.1-2
+ Revision: 677122
- rebuild to add gconf2 as req

* Tue Apr 26 2011 Funda Wang <fwang@mandriva.org> 3.0.1-1
+ Revision: 659138
- build with gtk2
- update to new version 3.0.1

* Fri Apr 08 2011 Funda Wang <fwang@mandriva.org> 3.0.0-1
+ Revision: 651957
- add br
- new version 3.0.0

  + StÃ©phane TÃ©letchÃ©a <steletch@mandriva.org>
    - update to new version 2.91.91

* Tue Sep 28 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.32.0-1mdv2011.0
+ Revision: 581652
- update to new version 2.32.0

* Thu Sep 16 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.31.91-2mdv2011.0
+ Revision: 578944
- rebuild for new gobject-introspection

* Tue Aug 31 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.31.91-1mdv2011.0
+ Revision: 574627
- update to new version 2.31.91

* Sat Jul 31 2010 Funda Wang <fwang@mandriva.org> 2.30.1-2mdv2011.0
+ Revision: 563923
- rebuild for new gobject-introspection

* Tue Apr 27 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.30.1-1mdv2010.1
+ Revision: 539466
- update to new version 2.30.1

* Wed Mar 31 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.30.0-1mdv2010.1
+ Revision: 530224
- update to new version 2.30.0

* Mon Feb 22 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.91-1mdv2010.1
+ Revision: 509418
- update to new version 2.29.91

* Tue Feb 09 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.90-1mdv2010.1
+ Revision: 502602
- new version
- drop patch 1
- update file list

  + Christophe Fergeau <cfergeau@mandriva.com>
    - remove no longer needed CPPFLAGS

* Wed Jan 13 2010 Christophe Fergeau <cfergeau@mandriva.com> 2.29.4-3mdv2010.1
+ Revision: 490988
-add patch from gnome git to fix crash at startup

* Mon Dec 28 2009 Frederic Crozat <fcrozat@mandriva.com> 2.29.4-2mdv2010.1
+ Revision: 483003
- Obsoletes gnome-keyring-manager

* Thu Dec 24 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.4-1mdv2010.1
+ Revision: 482037
- new version
- update build deps
- add introspection files

* Wed Dec 09 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.3-1mdv2010.1
+ Revision: 475390
- update to new version 2.29.3

* Wed Oct 21 2009 Frederic Crozat <fcrozat@mandriva.com> 2.28.1-1mdv2010.0
+ Revision: 458598
- Release 2.28.1

* Mon Sep 21 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 446798
- update to new version 2.28.0

* Mon Sep 14 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.92-1mdv2010.0
+ Revision: 439073
- new version
- fix linking
- update file list

* Mon Sep 07 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.90-2mdv2010.0
+ Revision: 432559
- don't setuid the daemon

* Mon Aug 10 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.90-1mdv2010.0
+ Revision: 414392
- update to new version 2.27.90

* Tue Jul 28 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.5-2mdv2010.0
+ Revision: 401465
- release bump
- new version
- fix build
- update file list

* Mon May 11 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.1-1mdv2010.0
+ Revision: 374167
- new version

* Tue Apr 14 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.26.1-1mdv2009.1
+ Revision: 367000
- update to new version 2.26.1

* Sat Mar 14 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.26.0-1mdv2009.1
+ Revision: 355156
- update to new version 2.26.0

* Mon Mar 02 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.92-1mdv2009.1
+ Revision: 347295
- update to new version 2.25.92

* Sat Feb 14 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.91-1mdv2009.1
+ Revision: 340320
- update to new version 2.25.91

* Tue Feb 03 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.90-1mdv2009.1
+ Revision: 337020
- new version
- update file list

* Wed Jan 07 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.4-1mdv2009.1
+ Revision: 326689
- new version
- bump deps
- update file list

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Sun Nov 09 2008 Oden Eriksson <oeriksson@mandriva.com> 2.25.1-2mdv2009.1
+ Revision: 301586
- rebuilt against new libxcb

* Tue Nov 04 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.1-1mdv2009.1
+ Revision: 299881
- update to new version 2.25.1

* Sun Oct 19 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.1-1mdv2009.1
+ Revision: 295220
- update to new version 2.24.1

* Sun Sep 21 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 286291
- new version

* Mon Sep 08 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.92-1mdv2009.0
+ Revision: 282462
- new version

* Wed Sep 03 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.91-1mdv2009.0
+ Revision: 279800
- new version

* Tue Aug 19 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.90-1mdv2009.0
+ Revision: 273559
- new version
- remove extra icons

* Mon Aug 04 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.6-1mdv2009.0
+ Revision: 262950
- new version

* Tue Jul 22 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.5-1mdv2009.0
+ Revision: 240188
- new version
- update deps
- drop epiphany, nautilus and gedit plugins
- drop patches
- update file list

* Mon Jun 30 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.3-1mdv2009.0
+ Revision: 230368
- new version

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue May 27 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.2-1mdv2009.0
+ Revision: 211579
- new version

* Wed Apr 09 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.1-1mdv2009.0
+ Revision: 192454
- new version
- sync license tag with Fedora

* Mon Mar 10 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.0-2mdv2008.1
+ Revision: 183400
- build with epiphany 2.22

* Sun Mar 09 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.0-1mdv2008.1
+ Revision: 183051
- new version

* Mon Feb 25 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.92-1mdv2008.1
+ Revision: 174583
- new version

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 2.21.91-3mdv2008.1
+ Revision: 171105
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Tue Feb 12 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.91-2mdv2008.1
+ Revision: 166157
- libsoup rebuild

* Thu Jan 31 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.91-1mdv2008.1
+ Revision: 160630
- new version
- drop patch 2
- reenable epiphany extension

* Tue Jan 29 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.90-1mdv2008.1
+ Revision: 159683
- new version
- fix epiphany detection, but keep epi plugin build disabled

* Wed Jan 23 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.4-2mdv2008.1
+ Revision: 157091
- fix nautilus extension build
- new nautilus extensions directory

  + Funda Wang <fwang@mandriva.org>
    - rebuild against latest gnutls

  + Thierry Vignaud <tv@mandriva.org>
    - drop old menu
    - remove "no crypto" add from description

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 17 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.4-1mdv2008.1
+ Revision: 131124
- new version
- disable epiphany plugin for now

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - remove outdated data about en & ja translations from description

* Mon Dec 03 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.3-1mdv2008.1
+ Revision: 114546
- new version

* Mon Oct 15 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.20.1-1mdv2008.1
+ Revision: 98582
- new version
- drop patch 1

* Wed Sep 19 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.20.0-2mdv2008.0
+ Revision: 90815
- patch to support gedit 2.20
- build for new epiphany

* Wed Sep 19 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.20.0-1mdv2008.0
+ Revision: 90416
- new version
- new version

* Sun Aug 26 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.91-1mdv2008.0
+ Revision: 71580
- new version

* Tue Aug 14 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.90-1mdv2008.0
+ Revision: 62978
- new version
- new devel name

* Sun Jul 08 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.5-1mdv2008.0
+ Revision: 49771
- new version
- update file list

  + Andreas Hasenack <andreas@mandriva.com>
    - added buildrequires for libGConf2-devel
    - rebuild with new rpm-mandriva-setup (-fstack-protector)

* Mon Jun 18 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.4-1mdv2008.0
+ Revision: 41065
- new version
- drop patch 1

* Thu Jun 07 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.2-2mdv2008.0
+ Revision: 36498
- fix for epiphany 2.19
- new version
- update file list

* Tue Apr 17 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.0.1-1mdv2008.0
+ Revision: 13822
- new version
- drop patch


* Mon Mar 12 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1mdv2007.1
+ Revision: 142070
- patch for epiphany 2.18
- new version

* Fri Feb 23 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.9.92-1mdv2007.1
+ Revision: 125158
- new version

* Tue Feb 13 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.9.91-1mdv2007.1
+ Revision: 120272
- new version

* Fri Jan 05 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.9.10-1mdv2007.1
+ Revision: 104335
- new version

* Wed Dec 20 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.9.9-1mdv2007.1
+ Revision: 100371
- new version
- update file list

* Tue Dec 05 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.9.8-1mdv2007.1
+ Revision: 90718
- new version
- epiphany 2.17
- add omf files
- fix directory ownership

* Sun Nov 05 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.9.7-1mdv2007.1
+ Revision: 76766
- new version
- update file list

* Fri Oct 27 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.9.6-2mdv2007.1
+ Revision: 73247
- fix buildrequires
- Import seahorse

* Fri Oct 27 2006 Götz Waschk <waschk@mandriva.org> 0.9.6-1mdv2007.1
- unpack patch
- add epiphany plugin
- New version 0.9.6

* Wed Sep 13 2006 Götz Waschk <waschk@mandriva.org> 0.9.5-1mdv2007.0
- drop patch 1
- New version 0.9.5

* Tue Sep 12 2006 Götz Waschk <waschk@mandriva.org> 0.9.4-1mdv2007.0
- fix build
- patch for new gedit
- New version 0.9.4

* Sat Aug 26 2006 Götz Waschk <waschk@mandriva.org> 0.9.3-1mdv2007.0
- update file list
- drop merged patch 1
- New release 0.9.3

* Sat Aug 19 2006 Götz Waschk <waschk@mandriva.org> 0.9.2.1-3mdv2007.0
- patch 1: fix syntax error in schemas file

* Sat Aug 19 2006 Götz Waschk <waschk@mandriva.org> 0.9.2.1-2mdv2007.0
- add missing update-desktop-database call
- fix menu categories

* Fri Aug 18 2006 Götz Waschk <waschk@mandriva.org> 0.9.2.1-1mdv2007.0
- xdg menu
- new macros
- update file list
- New release 0.9.2.1

* Thu Apr 27 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.9.1-3mdk
- Fix BuildRequires

* Sun Apr 16 2006 Götz Waschk <waschk@mandriva.org> 0.9.1-2mdk
- fix buildrequires

* Sun Apr 16 2006 Götz Waschk <waschk@mandriva.org> 0.9.1-1mdk
- update file list
- handle scrollkeeper stuff
- New release 0.9.1

* Tue Mar 07 2006 Götz Waschk <waschk@mandriva.org> 0.9.0-1mdk
- update file list
- update deps
- rediff the patch
- New release 0.9.0

* Mon Mar 06 2006 Götz Waschk <waschk@mandriva.org> 0.8.1-1mdk
- rediff the patch
- New release 0.8.1

* Fri Oct 07 2005 GÃ¶tz Waschk <waschk@mandriva.org> 0.8-1mdk
- New release 0.8

* Thu Sep 08 2005 Michael Scherer <misc@mandriva.org> 0.7.9-3mdk
- Rebuild for libglitz
- mkrel

* Wed Aug 31 2005 Buchan Milne <bgmilne@linux-mandrake.com> 0.7.9-2mdk
- Rebuild for libldap2.3

* Fri Jul 29 2005 Götz Waschk <waschk@mandriva.org> 0.7.9-1mdk
- update file list
- New release 0.7.9

* Tue May 10 2005 Götz Waschk <waschk@mandriva.org> 0.7.8-1mdk
- add new nautilus extension
- drop bonobo parts
- New release 0.7.8

* Sat Apr 16 2005 Götz Waschk <waschk@linux-mandrake.com> 0.7.7-1mdk
- update file list
- fix build
- New release 0.7.7

* Tue Feb 22 2005 Götz Waschk <waschk@linux-mandrake.com> 0.7.6-2mdk
- fix buildrequires

* Sun Feb 20 2005 Götz Waschk <waschk@linux-mandrake.com> 0.7.6-1mdk
- update menu entry
- update file list
- rediff the patch
- New release 0.7.6

* Wed Nov 03 2004 Götz Waschk <waschk@linux-mandrake.com> 0.7.5-1mdk
- add library package
- New release 0.7.5

* Fri Oct 22 2004 Götz Waschk <waschk@linux-mandrake.com> 0.7.4-2mdk
- fix buildrequires

* Thu Oct 21 2004 Götz Waschk <waschk@linux-mandrake.com> 0.7.4-1mdk
- add gedit plugin and shared mime database package
- patch to fix installation
- requires new gpgme
- drop merged patch
- source URL
- New release 0.7.4

* Sat Aug 28 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.7.3-9mdk
- Fix menu

* Tue Apr 27 2004 Charles A Edwards <eslrahc@mandrake.org> 0.7.3-8mdk
- fix unneeded require by rm requires for gpgme 
- BuildRequires

