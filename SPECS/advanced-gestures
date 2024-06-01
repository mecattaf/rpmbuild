%global commit0 e0cad229c3d799c7f72b1217ab2eb300ceecf3ac
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 483

%global __provides_exclude_from ^(%{_libdir}/hyprland/.*\\.so)$

Name:           hyprland-plugin-advanced-gestures
Version:        0.1.0
Release:        1%{?dist}
Summary:        Advanced gestures plugin for Hyprland

License:        BSD-3-Clause
URL:            https://github.com/mecattaf/advanced-gestures
Source:         %{url}/archive/%{commit0}/%{name}-%{commit0}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  hyprland-devel

Requires:       hyprland = %{_hyprland_version}

%description
This plugin provides advanced gesture support for Hyprland.

%prep
%autosetup -n %{name}-%{commit0} -p1

%build
%meson --libdir=%{_libdir}/hyprland
%meson_build

%install
%meson_install

%files
%license LICENSE
%{_libdir}/hyprland/libadvanced-gestures.so

%changelog
* Mon May 31 2024 Thomas Mecattaf <thomasmecattaf@gmail.com> - 0.1.0-1
- Initial RPM release
