Name: twm
Version: 1.0.3
Release: %mkrel 1
Summary: Tab Window Manager for the X Window System
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Source1: system.twmrc
Source2: twm
Source3: twm.xpm
Source4: twm.xpm.large
Source5: twm.xpm.mini
License: MIT
Requires: desktop-common-data

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: libxmu-devel >= 1.0.0
BuildRequires: libxt-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
Twm is a window manager for the X Window System. It provides titlebars, shaped
windows, several forms of icon management, user-defined macro functions,
click-to-type and pointer-driven keyboard focus, and user-specified key and
pointer button bindings.

%prep
%setup -q -n %{name}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS -DSYSTEM_INIT_FILE='\"%{_sysconfdir}/X11/twm/system.twmrc\"'" %configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

mkdir -p %{buildroot}/%{_sysconfdir}/{menu.d,X11/twm}
install -m 644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/X11/twm/system.twmrc-menu
install -m 755 %{SOURCE2} %{buildroot}/%{_sysconfdir}/menu.d

#install icons
mkdir -p %{buildroot}%{_datadir}/icons/large
mkdir -p %{buildroot}%{_datadir}/icons/mini
install -m0644 %{SOURCE3} %{buildroot}%{_datadir}/icons/twm.xpm
install -m0644 %{SOURCE4} %{buildroot}%{_datadir}/icons/large/twm.xpm
install -m0644 %{SOURCE5} %{buildroot}%{_datadir}/icons/mini/twm.xpm

%clean
rm -rf %{buildroot}

%post
%update_menus

%postun
%clean_menus

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/X11/twm
%{_sysconfdir}/menu.d/twm
%{_bindir}/twm
%{_mandir}/man1/twm.*
%{_datadir}/icons/twm.xpm
%{_datadir}/icons/*/twm.xpm
%_datadir/X11/twm/system.twmrc


