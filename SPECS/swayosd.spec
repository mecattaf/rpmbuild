Name:           swayosd
Version:        0.0.1
Release:        1%{?dist}
Summary:        An OSD window for common actions like volume and caps lock in SwayWM.

License:        MIT
URL:            https://github.com/ErikReider/swayosd
Source0:        swayosd-0.0.1.tar.gz

BuildRequires:  rust, cargo, meson, ninja-build, libinput-devel, gtk3-devel, sassc, pulseaudio-libs-devel
Requires:       swaywm, libinput, gtk3, pulseaudio

%description
SwayOSD is an on-screen display (OSD) window for SwayWM, supporting common actions such as volume and caps lock indication, brightness control, and more. This project is written in Rust and uses libinput for backend input detection.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install
# The service file installation command assumes the service file is included within the source archive.
# Ensure the path to the service file is correct relative to the root of the source directory after extraction.
install -Dm 644 %{name}-libinput-backend.service %{buildroot}%{_unitdir}/%{name}-libinput-backend.service

%files
%license LICENSE
%doc README.md
%{_bindir}/swayosd-server
%{_bindir}/swayosd-client
%{_bindir}/swayosd-libinput-backend
%{_unitdir}/swayosd-libinput-backend.service

%changelog
* Sat Oct 28 2023 Thomas Mecattaf <thomasmecattaf@gmail.com> - 0.0.1-1
- Initial RPM package for SwayOSD.
