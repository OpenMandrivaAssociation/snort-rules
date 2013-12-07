# (oe) undefining these makes the build _real_ quick.
# i timed this package and gained almost a minute(!).
%undefine __find_provides
%undefine __find_requires

Summary:	The GPL'ed Rulesets from snortrules-pr-%{version}
Name:		snort-rules
Version:	2.4
Release:	10
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


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 2.4-6mdv2011.0
+ Revision: 669995
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 2.4-5mdv2011.0
+ Revision: 607548
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 2.4-4mdv2010.1
+ Revision: 520227
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.4-3mdv2010.0
+ Revision: 427202
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 2.4-2mdv2009.0
+ Revision: 265728
- rebuild early 2009.0 package (before pixel changes)

* Wed May 07 2008 Oden Eriksson <oeriksson@mandriva.com> 2.4-1mdv2009.0
+ Revision: 202939
- use the latest possible gpl version after following the way debian does this.

* Thu Jan 03 2008 Oden Eriksson <oeriksson@mandriva.com> 2.3.3-4mdv2008.1
+ Revision: 141690
- added P0 to fix two borked rules

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Oct 22 2006 David Walluck <walluck@mandriva.org> 2.3.3-3mdv2007.0
+ Revision: 71644
+ Status: not released
- rebuild
- Import snort-rules

* Tue May 16 2006 Oden Eriksson <oeriksson@mandriva.com> 2.3.3-2mdk
- disable the auto provides and requires

* Sun Oct 30 2005 Oden Eriksson <oeriksson@mandriva.com> 2.3.3-1mdk
- initial Mandriva package

