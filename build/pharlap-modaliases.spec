Name:           pharlap-modaliases
Version:        1.1.1
Release:        1%{?dist}
Summary:        Driver modalias map for Pharlap and Jockey

License:        GPLv2+
URL:            http://kororaproject.org
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Provides:       jockey-modaliases
Obsoletes:      jockey-modaliases

%description
This package provides modaliases for kernel modules which are not installed
by default. This is used by Pharlap and Jockey to detect required modules
for system's hardware.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_datadir}/pharlap
mkdir -p %{buildroot}%{_datadir}/jockey/{modaliases,modaliases-PAE,modaliases-akmods}/
install -m 644 pharlap-modalias.map %{buildroot}%{_datadir}/pharlap/
install -m 644 rpmfusion-modules.aliases %{buildroot}%{_datadir}/jockey/modaliases/
install -m 644 rpmfusion-modules-PAE.aliases %{buildroot}%{_datadir}/jockey/modaliases-PAE/
install -m 644 rpmfusion-modules-akmods.aliases %{buildroot}%{_datadir}/jockey/modaliases-akmods/

%files
%{_datadir}/pharlap/pharlap-modalias.map
%{_datadir}/jockey/modaliases*

%changelog
* Tue Dec 24 2013 Chris Smart <csmart@kororaproject.org> - 1.1.1-1
- Update modalias map for RPMFusion 20 repos

* Sat Nov 23 2013 Chris Smart <csmart@kororaproject.org> - 1.1.0-1
- Rename package to pharlap-modaliases to provide and obsolete jockey-modaliases

* Sun Jun 30 2013 Chris Smart <csmart@kororaproject.org> - 1.0.6-1
- Updated to Korora 19 release.

* Fri Jun 29 2012 Chris Smart <chris@kororaa.org> - 1.0.5-1
- Updated to support proprietary ATI driver.

* Sat Jun 02 2012 Chris Smart <chris@kororaa.org> - 1.0.4-1
- Update for Fedora 17

* Tue Dec 06 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 1.0.3-1
- Rename to jockey-modaliases
- Update for Fedora 16
- Add a script to generate modalias files

* Mon Dec 05 2011 Chris Smart <chris@kororaa.org> - 1.0.2-1
- Add akmod based modaliases file.

* Sun Oct 16 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 1.0.1-1
- Add PAE modaliases

* Thu Jul 28 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 1.0.0-1
- Initial version

