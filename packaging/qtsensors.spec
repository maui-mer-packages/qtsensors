# Package prefix
%define pkgname qt5-qtsensors

Name:       qtsensors
Summary:    Qt Sensors module
Version:    5.3.2
Release:    1
Group:      Qt/Qt
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.io
Source0:    %{name}-%{version}.tar.xz
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtopengl-devel
BuildRequires:  qt5-qtnetwork-devel
BuildRequires:  qt5-qtdeclarative-qtquick-devel
BuildRequires:  qt5-qmake
BuildRequires:  fdupes
BuildRequires:  pkgconfig(sensord-qt5)

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.

This package contains the Qt sensors module.

%package -n %{pkgname}
Summary:    Qt Sensors module
Group:      Qt/Qt

%description -n %{pkgname}
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.

This package contains the Qt sensors module.


%package -n %{pkgname}-devel
Summary:    Qt Sensors - development files
Group:      Qt/Qt
Requires:   %{pkgname} = %{version}-%{release}

%description -n %{pkgname}-devel
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.

This package contains the Qt sensors module development files.


%package -n qt5-qtdeclarative-import-sensors
Summary:    QtQml sensors import
Group:      Qt/Qt
Requires:   %{pkgname} = %{version}-%{release}
Requires:   qt5-qtdeclarative

%description -n qt5-qtdeclarative-import-sensors
This package contains the Sensors import for Qtml


%package -n %{pkgname}-plugin-sensorfw
Summary:    sensorfw sensors plugin
Group:      Qt/Qt
Requires:   %{pkgname} = %{version}-%{release}

%description -n %{pkgname}-plugin-sensorfw
This package contains the sensorfw plugin for sensors


%package -n %{pkgname}-plugin-generic
Summary:    Generic sensors plugin
Group:      Qt/Qt
Requires:   %{pkgname} = %{version}-%{release}

%description -n %{pkgname}-plugin-generic
This package contains the generic plugin for sensors


%package -n %{pkgname}-plugin-gestures-shake
Summary:    Shake gesture plugin
Group:      Qt/Qt
Requires:   %{pkgname} = %{version}-%{release}

%description -n %{pkgname}-plugin-gestures-shake
This package contains the shake gesture plugin for sensors


%package -n %{pkgname}-plugin-gestures-sensor
Summary:    Sensor gesture plugin
Group:      Qt/Qt
Requires:   %{pkgname} = %{version}-%{release}

%description -n %{pkgname}-plugin-gestures-sensor
This package contains the gesture plugin for sensors


%prep
%setup -q -n %{name}-%{version}


%build
export QTDIR=/usr/share/qt5
touch .git
%qmake5 CONFIG+=sensorfw
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%qmake5_install
# Remove unneeded .la files
rm -f %{buildroot}/%{_libdir}/*.la
%fdupes %{buildroot}/%{_includedir}


%post -n %{pkgname}
/sbin/ldconfig
%postun -n %{pkgname}
/sbin/ldconfig


%files -n %{pkgname}
%defattr(-,root,root,-)
%{_libdir}/libQt5Sensors.so.5
%{_libdir}/libQt5Sensors.so.5.*

%files -n %{pkgname}-devel
%defattr(-,root,root,-)
%{_libdir}/libQt5Sensors.so
%{_libdir}/libQt5Sensors.prl
%{_libdir}/pkgconfig/*
%{_includedir}/qt5/*
%{_datadir}/qt5/mkspecs/
%{_libdir}/cmake/

%files -n qt5-qtdeclarative-import-sensors
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/QtSensors/

%files -n %{pkgname}-plugin-sensorfw
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/sensors/libqtsensors_sensorfw.so
%{_sysconfdir}/xdg/QtProject/Sensors.conf

%files -n %{pkgname}-plugin-generic
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/sensors/libqtsensors_generic.so

%files -n %{pkgname}-plugin-gestures-shake
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/sensorgestures/libqtsensorgestures_shakeplugin.so

%files -n %{pkgname}-plugin-gestures-sensor
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/sensorgestures/libqtsensorgestures_plugin.so
