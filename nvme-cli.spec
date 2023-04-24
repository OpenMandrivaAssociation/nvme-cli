Name:		nvme-cli
Version:	2.4
Release:	1
Source0:	https://github.com/linux-nvme/nvme-cli/archive/v%{version}/%{name}-%{version}.tar.gz
Group:		System/Hardware
Url:		http://nvmexpress.org/
License:	GPLv2
Summary:	Tools for working with NVMe storage

BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libnvme)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(zlib)
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
%config(noreplace) %{_sysconfdir}/nvme/discovery.conf
%{_datadir}/bash-completion/completions/nvme
%{_datadir}/zsh/site-functions/_nvme
%{_udevrulesdir}/70-nvmf-autoconnect.rules
%{_udevrulesdir}/71-nvmf-iopolicy-netapp.rules
%{_unitdir}/nvmefc-boot-connections.service
%{_unitdir}/nvmf-autoconnect.service
%{_unitdir}/nvmf-connect.target
%{_unitdir}/nvmf-connect@.service
%{_prefix}/lib/dracut/dracut.conf.d/70-nvmf-autoconnect.conf
