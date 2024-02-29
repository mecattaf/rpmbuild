Name:           marp-cli
Version:        3.4.0
Release:        1%{?dist}
Summary:        Marp CLI is a tool that converts Markdown documents into HTML slideshows, PDFs, and images.
License:        MIT
URL:            https://github.com/marp-team/marp-cli
Source0:        marp-cli-v%{version}-linux.tar.gz

BuildArch:      x86_64
Requires:       nodejs
BuildRequires:  patchelf

%description
Marp CLI is part of the Marp Markdown Presentation Ecosystem, allowing developers and others to create presentation materials easily from Markdown files.

%prep
%setup -q -n marp-cli-v%{version}-linux

%build
# Nothing to build since it's a binary distribution

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 marp %{buildroot}%{_bindir}/marp-cli

# Assuming dynamic linking adjustment is necessary for the binary
# Replace /usr/lib64/libc.so.6 with the actual dynamic linker path if different
patchelf --set-interpreter /usr/lib64/libc.so.6 %{buildroot}%{_bindir}/marp-cli

# Set RPATH if there are specific directories where the binary should look for shared libraries
# patchelf --set-rpath /usr/lib64:%{buildroot}/lib %{buildroot}%{_bindir}/marp-cli

%files
%{_bindir}/marp-cli

%license LICENSE
%doc README.md

%changelog
* Sat Oct 28 2023 Thomas Mecattaf <thomasmecattaf@gmail.com> - 3.4.0-1
