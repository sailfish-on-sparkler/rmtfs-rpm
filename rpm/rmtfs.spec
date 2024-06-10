Name:       rmtfs
Version:    1.0+git6
Release:    0
Summary:    Remote Filesystem Service for Qualcomm modems
License:    BSD-3-Clause
URL:        https://github.com/linux-msm/rmtfs
Source:     %{name}-%{version}.tar.gz

BuildRequires: qrtr-devel

%description
RMTFS implements the Remote Filesystem Service used by Qualcomm modems.

%prep
%setup -q -n %{name}-%{version}/rmtfs

%build
make clean
%make_build

%install
make DESTDIR=%{buildroot} prefix=/usr install
mkdir -p %{buildroot}%{_unitdir}/multi-user.target.wants
ln -s ../rmtfs.service %{buildroot}%{_unitdir}/multi-user.target.wants/rmtfs.service

%files
%defattr(-,root,root,-)
%license LICENSE
%{_bindir}/rmtfs
%{_unitdir}/rmtfs.service
%{_unitdir}/multi-user.target.wants/rmtfs.service
