%?mingw_package_header

%global name1 smokegen

Name:    mingw-%{name1}
Version: 4.14.3
Release: 1%{?dist}
Summary: Smoke Generator

License: LGPLv2 and GPLv2+
URL: https://projects.kde.org/projects/kde/kdebindings/smoke 

Source0: http://download.kde.org/stable/%{version}/src/%{name1}-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-gcc-c++

BuildRequires:  mingw32-qt
BuildRequires:  mingw64-qt
BuildRequires:  mingw32-qwt
BuildRequires:  mingw64-qwt


%description
Smoke Generator for MinGW Windows

%package -n mingw32-%{name1}
Summary:        Smoke Generator for MinGW Windows
%description -n mingw32-%{name1}
%{summary}.

%package -n mingw64-%{name1}
Summary:        Smoke Generator for MinGW Windows
%description -n mingw64-%{name1}
%{summary}.

#%?mingw_debug_package


%prep
%setup -q -n %{name1}-%{version}


%build
%mingw_cmake
%mingw_make %{?_smp_mflags}


%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT


%files -n mingw32-%{name1}
%doc COPYING
%doc README
%{mingw32_bindir}/smokebase.dll

%{mingw32_bindir}/smokeapi.exe
%{mingw32_bindir}/smokegen.exe
%{mingw32_bindir}/cppparser.dll
%{mingw32_libdir}/cppparser.dll.a
%{mingw32_libdir}/smokebase.dll.a
%{mingw32_libdir}/smokegen.dll.a
%{mingw32_libdir}/smokegen/
%{mingw32_includedir}/smoke.h
%{mingw32_includedir}/smokegen/
%{mingw32_datadir}/smoke/
%{mingw32_datadir}/smokegen/

%files -n mingw64-%{name1}
%doc COPYING
%doc README
%{mingw64_bindir}/smokebase.dll

%{mingw64_bindir}/smokeapi.exe
%{mingw64_bindir}/smokegen.exe
%{mingw64_bindir}/cppparser.dll
%{mingw64_libdir}/cppparser.dll.a
%{mingw64_libdir}/smokebase.dll.a
%{mingw64_libdir}/smokegen.dll.a
%{mingw64_libdir}/smokegen/
%{mingw64_includedir}/smoke.h
%{mingw64_includedir}/smokegen/
%{mingw64_datadir}/smoke/
%{mingw64_datadir}/smokegen/


%changelog
* Fri Mar 27 2015 Niclas Moeslund Overby <nimoov@prozum.dk> - 4.14.3-1
- copied from native smokegen
