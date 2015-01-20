Summary: Linux Standard Base tools
Name: lsb-release
Version: 2.0
Release: 37
License: GPL
Source: lsb-release-%{version}.tar.bz2
Patch0: lsb-release-%{version}-no-support.patch
Group: System/Base
URL: http://bzr.linuxfoundation.org/loggerhead/lsb/devel/si/files/head:/lsb_release/ 
BuildRoot: %{_tmppath}/%{name}-root

%define debug_package %{nil}

%description
LSB version query program

This program forms part of the required functionality of
the LSB (Linux Standard Base) specification.

The program queries the installed state of the distribution
to display certain properties such as the version of the
LSB against which the distribution claims compliance as 
well. It can also attempt to display the name and release
of the distribution along with an identifier of who produces
the distribution.

%prep

%setup -q
%patch0 -p1 -b .no-support

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=%buildroot mandir=%buildroot/%{_mandir} install 
mkdir -p %buildroot/%{_sysconfdir}/%{name}.d
mkdir -p %buildroot/%{_sysconfdir}

# set codename accordingly to https://wiki.openmandriva.org/en/Codename
cat > %buildroot/%{_sysconfdir}/lsb-release << EOF
LSB_VERSION=
DISTRIB_ID=OpenMandrivaLinux
DISTRIB_RELEASE=%{product_version}
DISTRIB_CODENAME=Einsteinium
DISTRIB_DESCRIPTION="%{distribution} %{product_version} alpha"
EOF

mkdir -p %buildroot/usr/bin
pushd %buildroot/usr/bin
ln -sf /bin/lsb_release lsb_release
popd


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
/bin/lsb_release
%_bindir/lsb_release
%{_mandir}/man1/lsb_release.1*
%config(noreplace) %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}.d


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.0-34mdv2011.0
+ Revision: 666098
- mass rebuild

* Fri Apr 01 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.0-33
+ Revision: 649746
- from Stew Benedict:
  	o remove lsb support level from this package, handle in lsb
  	o leave LSB_VERSION empty, quote DISTRIB_ID

* Fri Jan 07 2011 Antoine Ginies <aginies@mandriva.com> 2.0-30mdv2011.0
+ Revision: 629592
- need a codename

* Thu Jan 06 2011 Leonardo Coelho <leonardoc@mandriva.com> 2.0-29mdv2011.0
+ Revision: 629080
- Fix old binary path but keeping both.

* Sat Oct 02 2010 Anssi Hannula <anssi@mandriva.org> 2.0-28mdv2011.0
+ Revision: 582621
- replace hardcoded distribution version with a build-time one
- clear codename for now (lsb-release will guess 'Cooker' from
  /etc/release until it is refilled)

* Tue May 25 2010 Antoine Ginies <aginies@mandriva.com> 2.0-27mdv2010.1
+ Revision: 545911
- update codename

* Tue May 18 2010 Antoine Ginies <aginies@mandriva.com> 2.0-26mdv2010.1
+ Revision: 545113
- back to 2.0, because this is the version of the script, not the version of the LSB
- new codename, LSB 4 no more 2.X

* Wed Apr 28 2010 Antoine Ginies <aginies@mandriva.com> 2.0-25mdv2010.1
+ Revision: 540448
- new codename

* Wed Mar 31 2010 Antoine Ginies <aginies@mandriva.com> 2.0-24mdv2010.1
+ Revision: 530345
- beta1

* Fri Feb 26 2010 Antoine Ginies <aginies@mandriva.com> 2.0-23mdv2010.1
+ Revision: 511505
- new lsb-release (2010 spring)

* Thu Oct 29 2009 Anne Nicolas <ennael@mandriva.org> 2.0-22mdv2010.0
+ Revision: 460076
- change release name, lsb version

* Tue Aug 11 2009 Antoine Ginies <aginies@mandriva.com> 2.0-21mdv2010.0
+ Revision: 414796
- release 2010.0

* Thu Apr 23 2009 Antoine Ginies <aginies@mandriva.com> 2.0-20mdv2009.1
+ Revision: 368782
- final release name

* Thu Apr 02 2009 Antoine Ginies <aginies@mandriva.com> 2.0-19mdv2009.1
+ Revision: 363481
- change release name

* Mon Mar 09 2009 Antoine Ginies <aginies@mandriva.com> 2.0-18mdv2009.1
+ Revision: 353073
- update codename

* Fri Feb 06 2009 Antoine Ginies <aginies@mandriva.com> 2.0-17mdv2009.1
+ Revision: 338155
- 2009.1 release

* Wed Oct 01 2008 Antoine Ginies <aginies@mandriva.com> 2.0-16mdv2009.0
+ Revision: 290346
- codename zarapha

* Mon Sep 22 2008 Antoine Ginies <aginies@mandriva.com> 2.0-15mdv2009.0
+ Revision: 286964
- sophie release

* Mon Sep 01 2008 Antoine Ginies <aginies@mandriva.com> 2.0-14mdv2009.0
+ Revision: 278114
- prepare rc1

* Tue Aug 19 2008 Antoine Ginies <aginies@mandriva.com> 2.0-13mdv2009.0
+ Revision: 273682
- change codename to okapi (beta2)

* Thu Jul 24 2008 Frederic Crozat <fcrozat@mandriva.com> 2.0-12mdv2009.0
+ Revision: 245612
- Rebuild for 2009.0

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.0-11mdv2009.0
+ Revision: 223130
- rebuild

* Wed Apr 02 2008 Antoine Ginies <aginies@mandriva.com> 2.0-10mdv2008.1
+ Revision: 191719
- final name

* Wed Mar 05 2008 Antoine Ginies <aginies@mandriva.com> 2.0-9mdv2008.1
+ Revision: 180086
- update DISTRIBNAME

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 2.0-8mdv2008.1
+ Revision: 152874
- rebuild
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Sep 07 2007 Antoine Ginies <aginies@mandriva.com> 2.0-6mdv2008.0
+ Revision: 81439
- fill empty field in /etc/lsb-release


* Thu Jan 18 2007 Frederic Crozat <fcrozat@mandriva.com> 2.0-5mdv2007.0
+ Revision: 110311
-Use mkrel
-fix url
- Import lsb-release

* Sat Apr 01 2006 Stew Benedict <sbenedict@mandriva.com> 2.0-4mdk
- change the ident standard - now lsb-version-arch/noarch

* Tue Feb 21 2006 Stew Benedict <sbenedict@mandriva.com> 2.0-3mdk
- move graphics ident files to lsb-graphics

* Wed Jan 18 2006 Stew Benedict <sbenedict@mandriva.com> 2.0-2mdk
- leave DISTRIB_CODENAME blank, lsb_release can find it

* Wed Jun 01 2005 Stew Benedict <sbenedict@mandriva.com> 2.0-1mdk
- 2.0 - cvs snapshot
- conform to the new requirements for lsb-release format

* Sat Apr 23 2005 Stew Benedict <sbenedict@mandriva.com> 1.4-8mdk
- LSB3.0, use variables to populate lsb-release
- leave DISTRIB_RELEASE blank, lsb_release can find it

* Fri Mar 11 2005 Stew Benedict <sbenedict@mandrakesoft.com> 1.4-7mdk
- 10.2 (Bugzilla #14491)

* Tue Jun 22 2004 Stew Benedict <sbenedict@mandrakesoft.com> 1.4-6mdk
- LSB2.0

* Mon Apr 05 2004 Stew Benedict <sbenedict@mandrakesoft.com> 1.4-5mdk
- Mandrakelinux 10.1, codename Cooker

