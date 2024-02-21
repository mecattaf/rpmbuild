Name:           iwgtk
Version:        0.9
Release:        0
Summary:        Wireless networking GUI for iwd
License:        GPL-3.0-or-later
URL:            https://github.com/J-Lentz/iwgtk
Source:         iwgtk-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  meson >= 0.60.0
BuildRequires:  pkgconfig
BuildRequires:  scdoc
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(gtk4) >= 4.6
BuildRequires:  pkgconfig(libqrencode)
%{?systemd_ordering}
Requires:       iwd >= 1.29

%description
iwgtk is a wireless networking GUI for Linux. It is a front-end for iwd (iNet Wireless Daemon),
with supported functionality similar to that of iwctl. Features include viewing and connecting
to available networks, managing known networks, provisioning new networks via WPS or Wi-Fi Easy
Connect, and an indicator (tray) icon displaying connection status and signal strength.

%prep
%autosetup -p1

%build
%meson \
  -Doptimization=2

%meson_build

%install
%meson_install

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%postun
%systemd_user_postun %{name}.service

%files
%license COPYING
%doc CHANGELOG README.md
%{_bindir}/iwgtk
%{_datadir}/applications/iwgtk.desktop
%{_datadir}/icons/hicolor/scalable/apps/iwgtk.svg
%{_mandir}/man1/iwgtk.1.*
%{_mandir}/man5/iwgtk.5.*
%config %{_sysconfdir}/iwgtk.conf
%config %{_sysconfdir}/xdg/autostart/iwgtk-indicator.desktop
%{_userunitdir}/iwgtk.service

%changelog
* Sat Oct 28 2023 Thomas Mecattaf <thomasmecattaf@gmail.com> - 0.9.0-1
- Initial RPM package for iwgtk
