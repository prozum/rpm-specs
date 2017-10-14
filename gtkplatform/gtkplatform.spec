%global commit d16d14f8ada369d487b9d93363d05cc0290b87f0
%global shortcommit d16d14f

Name: gtkplatform
Version: 0.0.1
Release: git%{shortcommit}%{?dist}
Summary: Run Qt applications using gtk+ as a windowing system.

License: LGPL v3 or GPL 2+
URL: https://github.com/CrimsonAS/gtkplatform

Source0: https://github.com/CrimsonAS/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires: systemd-devel
BuildRequires: gtk3-devel
BuildRequires: libnotify-devel
BuildRequires: qt5-devel

%description
gtkplatform is a Qt Platform Abstraction plugin providing Qt applications with the capability to use gtk+ as a host toolkit, primarily intended for use on Linux desktops.

That is: it lets Qt applications render with native gtk+ menus, and use gtk+ for input (mouse, keyboard, touch), and getting window content on screen, the same as it uses e.g. cocoa on macOS for instance.

%prep
%setup -qn %{name}-%{commit}

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{qmake_qt5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install INSTALL_ROOT=%{buildroot} -C %{_target_platform}

%files
%license LICENSE
%doc README.md
%{_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_QGtkIntegrationPlugin.cmake
%{_qt5_libdir}/qt5/plugins/platforms/libqgtk.so

%changelog
* Sat Oct 14 2017 Niclas Moeslund Overby <noverby@prozum.dk> - 0.0.1-gitd16d14f8ada369d487b9d93363d05cc0290b87f0
- First version


