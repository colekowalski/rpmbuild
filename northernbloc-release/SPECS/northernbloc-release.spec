Name: northernbloc-release
Version: 7
Release: 1
Summary: Extra packages

Group: System Environment/Base
License: GPL
URL: http://rpm.northernbloc.org
Source0: RPM-GPG-KEY-NORTHERNBLOC
Source1: northernbloc.repo

BuildArch: noarch
Requires: redhat-release >= %{version}

%description


%prep
%setup -q -c -T
#install -pm 644 %{SOURCE0}
#install -pm 644 %{SOURCE1}


%build


%install
install -Dpm 644 %{SOURCE0} %{buildroot}/%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-NORTHERNBLOC
install -Dpm 644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/yum.repos.d/northernbloc.repo


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)

%config
%{_sysconfdir}/pki/rpm-gpg/*
%{_sysconfdir}/yum.repos.d/northernbloc.repo


%changelog
%changelog
* Fri Dec 29 2017 Cole Kowalski <cole@northernbloc.org> - 7-1
- Initial build.
