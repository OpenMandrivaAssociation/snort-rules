# (oe) undefining these makes the build _real_ quick.
# i timed this package and gained almost a minute(!).
%undefine __find_provides
%undefine __find_requires

Summary:	The GPL'ed Rulesets from snortrules-pr-%{version}
Name:		snort-rules
Version:	2.4
Release:	%mkrel 5
License:	GPL
Group:		Networking/Other
URL:		http://www.snort.org
Source0:	snortrules-pr-%{version}.tar.bz2
Source1:	purge-non-gpl.sh
Source2:	remove-non-gpl.pl
Source3:	changelog
BuildArch:	noarch
Suggests:	oinkmaster
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
These rules were taken from the snortrules-pr-2.4.tar.gz tar ball and all non
GPL rules were removed, then the tar ball was repackaged. Please read the
relevant changelog entry from debian that explains this.

%prep

%setup -q -c -n snortrules-pr-%{version}

cp %{SOURCE1} purge-non-gpl.sh
cp %{SOURCE2} remove-non-gpl.pl
cp %{SOURCE3} changelog

%build

%install
rm -rf %{buildroot} 

install -d %{buildroot}%{_sysconfdir}/snort/rules
install -m0644 rules/* %{buildroot}%{_sysconfdir}/snort/rules/

cat > README << EOF
These rules were taken from the snortrules-pr-2.4.tar.gz tar ball and all non
GPL rules were removed, then the tar ball was repackaged. Please read the
relevant changelog entry from debian that explains this.
EOF

# cleanup
rm -f %{buildroot}%{_sysconfdir}/snort/rules/VRT-License.txt
rm -f %{buildroot}%{_sysconfdir}/snort/rules/snort.conf

%clean
rm -rf %{buildroot} 

%files
%defattr(0644,root,root,0755)
%doc doc/signatures README changelog purge-non-gpl.sh remove-non-gpl.pl rules/VRT-License.txt rules/snort.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/snort/rules/*.rules
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/snort/rules/*.conf*
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/snort/rules/*.map
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/snort/rules/cgi-bin.list
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/snort/rules/generators
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/snort/rules/sid
