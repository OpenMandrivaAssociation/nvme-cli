Name:		nvme-cli
Version:	2.2.1
Release:	1
Source0:	https://github.com/linux-nvme/nvme-cli/archive/v%{version}.tar.gz
Group:		System/Hardware
Url:		http://nvmexpress.org/
License:	GPLv2
Summary:	Tools for working with NVMe storage

BuildRequires:  meson
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libnvme)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  python3dist(autopep8)
BuildRequires:  python3dist(flake8)
BuildRequires:  python3dist(isort)
BuildRequires:  python3dist(mypy)

%description
Tools for working with NVMe storage

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%{_sbindir}/*
%{_mandir}/*/*
%{_datadir}/bash-completion/completions/nvme
%{_datadir}/zsh/site-functions/_nvme
