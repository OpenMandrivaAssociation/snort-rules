# (oe) undefining these makes the build _real_ quick.
# i timed this package and gained almost a minute(!).
%undefine __find_provides
%undefine __find_requires

Summary:	The GPL'ed Rulesets from snort-2.3.3
Name:		snort-rules
Version:	2.3.3
Release:	%mkrel 4
License:	GPL
Group:		Networking/Other
URL:		http://www.snort.org
Source0:	http://www.snort.org/dl/snort-2.3.3.tar.gz
Source1:	http://www.snort.org/dl/snort-2.3.3.tar.gz.asc
Patch0:		snort-rawbytes.diff
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
These rules were taken from snort-2.3.3 which was released under 
the GPL license. Recent snort rules has a more strict licensing 
scheme and are not distributed along with snort-2.4.x+.

%prep
%setup -q -n snort-%{version}
%patch0 -p0

%build

%install
%{__rm} -rf %{buildroot} 

%{__mkdir_p} %{buildroot}%{_sysconfdir}/snort/rules
%{__cp} -a rules/*.rules %{buildroot}%{_sysconfdir}/snort/rules/

%clean
%{__rm} -rf %{buildroot} 

%files
%defattr(0644,root,root,0755)
%doc doc/signatures COPYING LICENSE
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/snort/rules/*.rules
