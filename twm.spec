Name: twm
Version: 1.0.6
Release: %mkrel 2
Summary: Tab Window Manager for the X Window System
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Source1: system.twmrc
Source3: twm.xpm
Source4: twm.xpm.large
Source5: twm.xpm.mini
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
Requires: desktop-common-data
Requires: x11-font-misc

BuildRequires: pkgconfig(x11) >= 1.0.0
BuildRequires: pkgconfig(xext) >= 1.0.0
BuildRequires: pkgconfig(xmu) >= 1.0.0
BuildRequires: pkgconfig(xt) >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: flex
BuildRequires: byacc

%description
Twm is a window manager for the X Window System. It provides titlebars, shaped
windows, several forms of icon management, user-defined macro functions,
click-to-type and pointer-driven keyboard focus, and user-specified key and
pointer button bindings.

%prep
%setup -q -n %{name}-%{version}

%build

CFLAGS="$RPM_OPT_FLAGS -DSYSTEM_INIT_FILE='\"%{_sysconfdir}/X11/twm/system.twmrc\"'" \
%configure2_5x

%make

%install
rm -rf %{buildroot}
%makeinstall_std

mkdir -p %{buildroot}/%{_sysconfdir}/X11/twm
install -m 644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/X11/twm/system.twmrc-menu

#install icons
mkdir -p %{buildroot}%{_datadir}/icons/large
mkdir -p %{buildroot}%{_datadir}/icons/mini
install -m0644 %{SOURCE3} %{buildroot}%{_datadir}/icons/twm.xpm
install -m0644 %{SOURCE4} %{buildroot}%{_datadir}/icons/large/twm.xpm
install -m0644 %{SOURCE5} %{buildroot}%{_datadir}/icons/mini/twm.xpm

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/X11/twm
%{_bindir}/twm
%{_mandir}/man1/twm.*
%{_datadir}/icons/twm.xpm
%{_datadir}/icons/*/twm.xpm
%_datadir/X11/twm/system.twmrc




%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.6-2mdv2011.0
+ Revision: 670735
- mass rebuild

* Tue Jan 18 2011 Thierry Vignaud <tv@mandriva.org> 1.0.6-1
+ Revision: 631509
- new release

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-6mdv2011.0
+ Revision: 608046
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-5mdv2010.1
+ Revision: 524268
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.4-4mdv2010.0
+ Revision: 427437
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.0.4-3mdv2009.0
+ Revision: 266442
- drop old style menu entry
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu May 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.4-2mdv2009.0
+ Revision: 207698
- If a locale other than POSIX or C is used (i.e. en_US), twm will use
  the internationalization code on Xlib.
  An alternative option would be to force twm to only use ascii characters,
  or import some non official patches, like the one described in:
  http://lists.freedesktop.org/archives/xorg/2008-January/031838.html
  "[vtwm-hackers] TWM: truetype support (now for VTWM -- finished!)"

* Mon Apr 14 2008 Thierry Vignaud <tv@mandriva.org> 1.0.4-1mdv2009.0
+ Revision: 192991
- new release

* Wed Feb 13 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.3-3mdv2008.1
+ Revision: 167169
- Fix menu location.
- Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Tue Jan 22 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.3-2mdv2008.1
+ Revision: 156428
- Updated BuildRequires and resubmit package.

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Feb 16 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.0.3-1mdv2007.0
+ Revision: 121723
- fix file list
- new release

  + Gustavo Pichorim Boiko <boiko@mandriva.com>
    - adding missing icons

* Tue Jul 18 2006 Frederic Crozat <fcrozat@mandriva.com> 1.0.1-5mdv2007.0
+ Revision: 41457
- Fix incorrect path for xdg_menu
- Fix path for xdg_menu

* Tue Jul 18 2006 Frederic Crozat <fcrozat@mandriva.com> 1.0.1-4mdv2007.0
+ Revision: 41451
- update menu on (un)install
- Fix incorrect include
- Add new XDG script

  + Gustavo Pichorim Boiko <boiko@mandriva.com>
    - rebuild to fix cooker uploading
    - increment release
    - Adding X.org 7.0 to the repository

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

