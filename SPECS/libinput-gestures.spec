Name:           libinput-gestures
Version:        2.76
Release:        1%{?dist}
Summary:        Actions gestures on your touchpad using libinput

License:        GPLv3+
URL:            https://github.com/bulletmark/libinput-gestures
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc, make
BuildRequires:  python3-devel
BuildRequires:  systemd

Requires:       python3 >= 3.6
Requires:       libinput, libinput-utils
Requires:       hicolor-icon-theme
Requires:       wmctrl
Requires:       xdotool

%description
Libinput-gestures is a utility which reads libinput gestures from your touchpad
and maps them to gestures you configure in a configuration file. Each gesture
can be configured to activate a shell command which is typically an xdotool
command to action desktop/window/application keyboard combinations and commands.

%prep
%autosetup -n libinput-gestures-%{version}

%build
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_userunitdir}

install -m 0755 libinput-gestures-setup %{buildroot}%{_bindir}
install -m 0755 libinput-gestures %{buildroot}%{_bindir}
install -m 0644 libinput-gestures.conf %{buildroot}%{_sysconfdir}
install -Dm644 libinput-gestures.desktop %{buildroot}%{_datadir}/applications
install -Dm644 libinput-gestures.service %{buildroot}%{_userunitdir}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%postun
%systemd_user_postun_with_restart %{name}.service

%files
%doc README.md
%{_bindir}/libinput-gestures
%{_bindir}/libinput-gestures-setup
%{_datadir}/applications/libinput-gestures.desktop
%config(noreplace) %{_sysconfdir}/libinput-gestures.conf
%{_userunitdir}/libinput-gestures.service

%changelog
* Sun May 12 2024 Thomas Mecattaf <thomasmecattaf@gmail.com> - 2.76-1
- Updated package version to 2.76, aligning with the latest GitHub release tag.
