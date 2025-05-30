Name: twm
Version: 1.0.13.1
Release: 1
Summary: Tab Window Manager for the X Window System
Group: Development/X11
Source0: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
Source1: system.twmrc
Source3: twm.xpm
Source4: twm.xpm.large
Source5: twm.xpm.mini
License: MIT
Requires: desktop-common-data
Requires: x11-font-misc

BuildRequires: pkgconfig(x11) >= 1.0.0
BuildRequires: pkgconfig(xext) >= 1.0.0
BuildRequires: pkgconfig(xmu) >= 1.0.0
BuildRequires: pkgconfig(xt) >= 1.0.0
BuildRequires: pkgconfig(xrandr)
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: flex
BuildRequires: byacc

%description
Twm is a window manager for the X Window System. It provides titlebars, shaped
windows, several forms of icon management, user-defined macro functions,
click-to-type and pointer-driven keyboard focus, and user-specified key and
pointer button bindings.

%prep
%autosetup -p1

%build

CFLAGS="$RPM_OPT_FLAGS -DSYSTEM_INIT_FILE='\"%{_sysconfdir}/X11/twm/system.twmrc\"'" \
%configure

%make_build

%install
%make_install

mkdir -p %{buildroot}/%{_sysconfdir}/X11/twm
install -m 644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/X11/twm/system.twmrc-menu

#install icons
mkdir -p %{buildroot}%{_datadir}/icons/large
mkdir -p %{buildroot}%{_datadir}/icons/mini
install -m0644 %{SOURCE3} %{buildroot}%{_datadir}/icons/twm.xpm
install -m0644 %{SOURCE4} %{buildroot}%{_datadir}/icons/large/twm.xpm
install -m0644 %{SOURCE5} %{buildroot}%{_datadir}/icons/mini/twm.xpm

%files
%config(noreplace) %{_sysconfdir}/X11/twm
%{_bindir}/twm
%doc %{_mandir}/man1/twm.*
%{_datadir}/icons/twm.xpm
%{_datadir}/icons/*/twm.xpm
%{_datadir}/X11/twm/system.twmrc
