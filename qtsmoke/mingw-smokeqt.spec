%?mingw_package_header

%global name1 smokeqt

Name:    mingw-%{name1}
Version: 4.14.3
Release: 1%{?dist}
Summary: MinGW Windows bindings for Qt libraries

License: LGPLv2+
URL:     https://projects.kde.org/projects/kde/kdebindings/smoke
Source0: http://download.kde.org/%{stable}/%{version}/src/%{name1}-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-gcc-c++

BuildRequires:  mingw32-qt
BuildRequires:  mingw64-qt
BuildRequires:  mingw32-qwt
BuildRequires:  mingw64-qwt
BuildRequires:  mingw32-smokegen
BuildRequires:  mingw64-smokegen

BuildRequires:  wine


%description
This package includes MinGW Windows bindings for Qt libraries.

%package -n mingw32-%{name1}
Summary:        MinGW Windows Qwt library

%description -n mingw32-%{name1}
%{summary}.

%package -n mingw64-%{name1}
Summary:        MinGW Windows Qwt library

%description -n mingw64-%{name1}
%{summary}.


%prep
%setup -q -n %{name1}-%{version}

%build
%mingw_cmake -DWITH_Phonon=0 -DWITH_QImageBlitz=0 -DWITH_QScintilla=0 -Dqtdefines="QT_NO_ACCESSIBILITY" -Dqtdefines_run=1 -Dqtdefines_run__TRYRUN_OUTPUT=""
%mingw_make %{?_smp_mflags}


%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT


%files -n mingw32-%{name1}
%doc AUTHORS COPYING.LIB
%{mingw32_bindir}/*.dll

%files -n mingw64-%{name1}
%doc AUTHORS COPYING.LIB
%{mingw64_bindir}/*.dll
#%{_libdir}/libsmokephonon.so.3*
#%{_libdir}/libsmokeqimageblitz.so.3*
#%{_libdir}/libsmokeqsci.so.3*
#%{_libdir}/libsmokeqt3support.so.3*
#%{_libdir}/libsmokeqtcore.so.3*
#%{_libdir}/libsmokeqtdbus.so.3*
#%{_libdir}/libsmokeqtdeclarative.so.3*
#%{_libdir}/libsmokeqtgui.so.3*
#%{_libdir}/libsmokeqthelp.so.3*
#%{_libdir}/libsmokeqtmultimedia.so.3*
#%{_libdir}/libsmokeqtnetwork.so.3*
#%{_libdir}/libsmokeqtopengl.so.3*
#%{_libdir}/libsmokeqtscript.so.3*
#%{_libdir}/libsmokeqtsql.so.3*
#%{_libdir}/libsmokeqtsvg.so.3*
#%{_libdir}/libsmokeqttest.so.3*
#%{_libdir}/libsmokeqtuitools.so.3*
#%{_libdir}/libsmokeqtwebkit.so.3*
#%{_libdir}/libsmokeqtxml.so.3*
#%{_libdir}/libsmokeqtxmlpatterns.so.3*
#%{_libdir}/libsmokeqwt.so.3*

#%files devel
#%{_libdir}/libsmoke*.so
#%{_includedir}/smoke/*
#%{_datadir}/smokegen/*
#%{_datadir}/smoke/*


%changelog
* Fri Mar 27 2015 Niclas Moeslund Overby <nimoov@prozum.dk> - 4.14.3-1
- copied from native smokeqt
