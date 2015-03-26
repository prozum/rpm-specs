%if 0%{?fedora} > 16 || 0%{?rhel} > 6
%global monodir /usr/lib/mono
%else
%global monodir %{_libdir}/mono
%endif

Name:    qyoto 
Summary: .NET/Mono bindings for the Qt libraries 
Version: 4.14.3
Release: 2%{?dist}

# libqyoto LGPLv2+, mono bindings GPLv2+
License: LGPLv2+ and GPLv2+
URL:     http://techbase.kde.org/Development/Languages/Qyoto
#URL:     https://projects.kde.org/projects/kde/kdebindings/csharp/qyoto
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: cmake
BuildRequires: pkgconfig(mono)
BuildRequires: pkgconfig(phonon)
BuildRequires: pkgconfig(qimageblitz)
BuildRequires: pkgconfig(QtCore) pkgconfig(QtScript) pkgconfig(QtTest) pkgconfig(QtUiTools)
BuildRequires: pkgconfig(QtWebKit) 
BuildRequires: qscintilla-devel
BuildRequires: qwt-devel
BuildRequires: smokeqt-devel >= %{version}
BuildRequires: pkgconfig(sqlite3)

# common name some other distros use
Provides: mono-qt = %{version}-%{release} 

%{?_qt4:Requires: qt4%{?_isa} >= %{_qt4_version}}
Requires: smokeqt%{?_isa} >= %{version}

%{?mono_arches:ExclusiveArch: %{mono_arches}}

%description
%{summary}.

%package devel
Summary: Development libraries for %{name} 
Provides: mono-qt-devel = %{version}-%{release}
Requires: %{name}%{_isa} = %{version}-%{release}
%description devel
This package contains development files for the .NET/Mono bindings 
for the Qt libraries.


%prep
%setup -q


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files 
%doc AUTHORS COPYING README
# LGPLv2+
%{_libdir}/libqyoto.so.2*
# bindings GPLv2+
%{_libdir}/libqtscript-sharp.so
%{_libdir}/libphonon-sharp.so
%{_libdir}/libqttest-sharp.so
%{_libdir}/libqtuitools-sharp.so
%{_libdir}/libqtwebkit-sharp.so
%{_libdir}/libqscintilla-sharp.so
%{monodir}/gac/qt-dotnet/
%{monodir}/gac/qtscript/
%{monodir}/gac/qttest/
%{monodir}/gac/qtuitools/
%{monodir}/gac/qtwebkit/
%{monodir}/gac/phonon/
%{monodir}/gac/qscintilla/
%{monodir}/qyoto/
%dir %{_datadir}/qyoto/
%{_datadir}/qyoto/key.snk

%files devel
%{_bindir}/csrcc
%{_bindir}/uics
%{_includedir}/qyoto/
%{_libdir}/pkgconfig/qyoto.pc
%{_libdir}/pkgconfig/qtwebkit-sharp.pc
%{_libdir}/pkgconfig/qttest-sharp.pc
%{_libdir}/pkgconfig/qtuitools-sharp.pc
%{_libdir}/pkgconfig/qtscript-sharp.pc
%{_libdir}/libqyoto.so
%{_datadir}/qyoto/cmake/


%changelog
* Thu Jan 08 2015 Rex Dieter <rdieter@fedoraproject.org> 4.14.3-2
- drop el6/cmake28 hack

* Sat Nov 08 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.14.3-1
- 4.14.3

* Sat Oct 11 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.14.2-1
- 4.14.2

* Mon Sep 15 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.14.1-1
- 4.14.1

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Aug 14 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.14.0-1
- 4.14.0

* Tue Aug 05 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.97-1
- 4.13.97

* Sun Jul 13 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.3-1
- 4.13.3

* Mon Jun 09 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.2-1
- 4.13.2

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 11 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.1-1
- 4.13.1

* Fri Apr 11 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.0-1
- 4.13.0

* Thu Apr 03 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.97-1
- 4.12.97

* Sat Mar 22 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.95-1
- 4.12.95

* Tue Mar 18 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.90-1
- 4.12.90

* Sat Mar 01 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.3-1
- 4.12.3

* Fri Jan 31 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.2-1
- 4.12.2

* Fri Jan 10 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.1-1
- 4.12.1

* Thu Dec 19 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.12.0-1
- 4.12.0

* Sun Dec 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.97-1
- 4.11.97

* Thu Nov 21 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.95-1
- 4.11.95

* Fri Nov 15 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.90-1
- 4.11.90

* Fri Nov 08 2013 Rex Dieter <rdieter@fedoraproject.org> 4.11.3-2
- rebuild (qscintilla)

* Fri Nov 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.3-1
- 4.11.3

* Sat Sep 28 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.2-1
- 4.11.2

* Tue Sep 03 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.1-1
- 4.11.1

* Thu Aug 08 2013 Than Ngo <than@redhat.com> - 4.11.0-1
- 4.11.0

* Thu Jul 25 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.97-1
- 4.10.97

* Tue Jul 23 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.95-1
- 4.10.95

* Thu Jun 27 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.90-1
- 4.10.90

* Sat Jun 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.4-1
- 4.10.4

* Mon May 06 2013 Than Ngo <than@redhat.com> - 4.10.3-1
- 4.10.3

* Sun Mar 31 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.2-1
- 4.10.2

* Sat Mar 02 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.1-1
- 4.10.1

* Fri Feb 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.0-1
- 4.10.0

* Sun Jan 20 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.9.98-1
- 4.9.98

* Fri Jan 04 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.9.97-1
- 4.9.97

* Thu Dec 20 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.95-1
- 4.9.95

* Mon Dec 17 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.90-2
- rebuild (qcsintilla)

* Tue Dec 04 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.90-1
- 4.9.90

* Mon Dec 03 2012 Than Ngo <than@redhat.com> - 4.9.4-1
- 4.9.4

* Tue Nov 06 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.3-2
- fix build against cmake-2.8.10 (#872829)

* Sat Nov 03 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.3-1
- 4.9.3

* Fri Sep 28 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.2-1
- 4.9.2

* Mon Sep 03 2012 Than Ngo <than@redhat.com> - 4.9.1-1
- 4.9.1

* Thu Jul 26 2012 Lukas Tinkl <ltinkl@redhat.com> - 4.9.0-1
- 4.9.0

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.97-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.97-1
- 4.8.97

* Wed Jun 27 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.95-1
- 4.8.95

* Sat Jun 09 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.90-1
- 4.8.90

* Tue May 29 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.80-1
- 4.8.80

* Mon Apr 30 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.3-1
- 4.8.3

* Fri Mar 30 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.2-1
- 4.8.2

* Mon Mar 05 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.1-1
- 4.8.1

* Wed Feb 08 2012 Dan Horák <dan[at]danny.cz> - 4.8.0-2
- set EclusiveArchs

* Sun Jan 22 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.0-1
- 4.8.0

* Tue Jan 10 2012 Rex Dieter <rdieter@fedoraproject.org> 4.7.97-3
- set %%{monodir} for f17+ differences

* Wed Jan 04 2012 Rex Dieter <rdieter@fedoraproject.org> 4.7.97-2
- move lib*-sharp.so to main pkg

* Wed Jan 04 2012 Rex Dieter <rdieter@fedoraproject.org> 4.7.97-1
- 4.7.97
- devel: make %%description shorter
- update URL

* Fri Dec 23 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.95-1
- 4.7.95

* Fri Dec 09 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.90-1
- first try

