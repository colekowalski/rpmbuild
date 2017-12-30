Name: sshguard
Version: 2.1.0
Release: 1%{?dist}
Summary: Sshguard protects hosts from brute-force attacks against SSH and other services

Group: System Environment/Daemons
License: OpenBSD
URL: https://www.sshguard.net
Source0: https://sourceforge.net/projects/sshguard/files/sshguard/2.1.0/sshguard-%{version}.tar.gz
Source1: sshguard.conf
Source2: sshguard.service

BuildRequires: gcc make

%description
Sshguard can read log messages from standard input (suitable for piping from
syslog) or monitor one or more log files. Log messages are parsed,
line-by-line, for recognized patterns. If an attack, such as several login
failures within a few seconds, is detected, the offending IP is blocked.
Offenders are unblocked after a set interval, but can be semi-permanently
banned using the blacklist option.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
install -Dpm 644 examples/whitelistfile.example %{buildroot}/%{_datarootdir}/sshguard/whitelistfile.example
install -Dpm 644 examples/sshguard.conf.sample %{buildroot}/%{_datarootdir}/sshguard/sshguard.conf.sample
install -Dpm 644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/sshguard.conf
install -Dpm 644 %{SOURCE2} %{buildroot}/lib/systemd/system/sshguard.service


%files
%{_sbindir}/sshguard
%{_libexecdir}/sshg-*
/lib/systemd/system/sshguard.service

%config(noreplace)
%{_sysconfdir}/sshguard.conf

%config
%{_datarootdir}/sshguard/*

%doc
%{_mandir}/man7/sshguard-setup.7*
%{_mandir}/man8/sshguard.8*


%changelog
* Fri Dec 29 2017 Cole Kowalski <cole@northernbloc.org> - 2.1.0-1
- Initial build.
