Name:		nvme-cli
Version:	1.7
Release:	1
Source0:	https://github.com/linux-nvme/nvme-cli/archive/v%{version}.tar.gz
Group:		System/Hardware
Url:		http://nvmexpress.org/
License:	GPLv2
Summary:	Tools for working with NVMe storage

%description
Tools for working with NVMe storage

%prep
%autosetup -p1

%build
%make_build PREFIX=%{_prefix} CFLAGS="%{optflags} -I."

%install
%make_install PREFIX=%{_prefix}

%files
%{_sbindir}/*
%{_mandir}/*/*
%{_datadir}/bash-completion/completions/nvme
%{_datadir}/zsh/site-functions/_nvme
