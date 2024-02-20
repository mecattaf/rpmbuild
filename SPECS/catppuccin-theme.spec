Name:           catppuccin-theme
Version:        1.0.0
Release:        1%{?dist}
Summary:        OpenSource Theme and Icon pack following Catppuccin

License:        GNU General Public License v3.0
URL:            https://github.com/Fausto-Korpsvart/Catppuccin-GTK-Theme
Source0:        catppuccin-theme.tar.gz

BuildArch:      noarch

%description
OpenSource theme and icon pack following Catppuccin, offering a cozy and warm color scheme for GTK environments and icon themes compatible with various desktop environments. Some GTK themes were also copied from: https://github.com/catppuccin/gtk

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}

# Extract the tar.gz file directly into the buildroot.
tar -xzf %{SOURCE0} -C %{buildroot}%{_datadir}

# Move the icons and themes to the expected locations.
mv %{buildroot}%{_datadir}/catppuccin-theme/icons %{buildroot}%{_datadir}
mv %{buildroot}%{_datadir}/catppuccin-theme/themes %{buildroot}%{_datadir}

%clean
rm -rf %{buildroot}

%files
%{_datadir}/icons/*
%{_datadir}/themes/*

%changelog
* Sat Oct 28 2023 Thomas Mecattaf <thomasmecattaf@gmail.com> - 1.0.0-1
- Initial package version for Catppuccin theme and icons.

