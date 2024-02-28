Name:           chezmoi
Version:        2.47.0
Release:        0
Summary:        A multi-host manager for dotfiles
License:        MIT
Group:          Development/Tools/Version Control
URL:            https://chezmoi.io
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2: go1.21.7.linux-amd64.tar.gz
Recommends:     git
BuildRequires:  wget, tar, gcc

%global debug_package %{nil}

%description
chezmoi is a manager for personal preference configs and state files
("dotfiles") that programs such as editors might create. chezmoi
sources dotfiles from a GitHub repository and installs them onto new,
empty machines.

%package bash-completion
Summary:        Bash completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package fish-completion
Summary:        Fish completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Fish command line completion support for %{name}.

%prep
%autosetup -a 1

%build
# Extract the Go tarball
tar -xzf %{_sourcedir}/go1.21.7.linux-amd64.tar.gz -C %{_builddir}

# Set GOROOT to the extracted Go directory
export GOROOT=%{_builddir}/go
export PATH=$GOROOT/bin:$PATH

# Now, use the local Go to build chezmoi
go build \
        -mod=vendor \
        -buildmode=pie \
        -tags noupgrade \
        -ldflags "-X main.version=%version
                  -X main.builtBy=fedora"

%install
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"
install -D -m 0644 "completions/%{name}-completion.bash" "%{buildroot}/%{_datadir}/bash-completion/completions/%{name}"
install -D -m 0644 "completions/%{name}.fish" "%{buildroot}/%{_datadir}/fish/vendor_completions.d/%{name}.fish"

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%files fish-completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%changelog
* Sat Oct 28 2023 Thomas Mecattaf <thomasmecattaf@gmail.com> - 0.0.1
- Initial package version for chezmoi
