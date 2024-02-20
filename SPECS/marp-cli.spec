Name:           marp-cli
Version:        3.4.0
Release:        1%{?dist}
Summary:        Marp CLI - Markdown Presentation Ecosystem

License:        MIT
URL:            https://github.com/marp-team/marp-cli
Source0:        marp-cli-v3.4.0-linux.tar.gz

BuildArch:      x86_64

%description
Marp CLI is a tool that converts Markdown documents into HTML slideshows, PDFs, and images. It is part of the Marp Markdown Presentation Ecosystem, allowing developers and others to create presentation materials easily from Markdown files.

%prep
tar -xvf %{SOURCE0}

%build
# Nothing to build since it's a binary distribution

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 marp %{buildroot}%{_bindir}/marp

%files
%{_bindir}/marp

%changelog
* Sat Oct 28 2023 Thomas Mecattaf <thomasmecattaf@gmail.com> - 3.4.0-1
- Initial package


