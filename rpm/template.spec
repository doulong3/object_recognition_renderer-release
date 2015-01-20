Name:           ros-hydro-object-recognition-renderer
Version:        0.2.2
Release:        0%{?dist}
Summary:        ROS object_recognition_renderer package

Group:          Development/Libraries
License:        BSD>
URL:            http://ecto.willowgarage.com/recognition
Source0:        %{name}-%{version}.tar.gz

Requires:       DevIL-devel
Requires:       SDL-devel
Requires:       assimp
Requires:       boost-devel
Requires:       freeglut-devel
Requires:       freeimage-devel
Requires:       libXi-devel
Requires:       libXmu-devel
Requires:       mesa-libOSMesa-devel
Requires:       ros-hydro-cv-bridge
BuildRequires:  DevIL-devel
BuildRequires:  SDL-devel
BuildRequires:  assimp-devel
BuildRequires:  boost-devel
BuildRequires:  freeglut-devel
BuildRequires:  freeimage-devel
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  mesa-libOSMesa-devel
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-cv-bridge

%description
Code that generates random views of an object

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Tue Jan 20 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.2.2-0
- Autogenerated by Bloom

* Sun Jan 18 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.2.1-0
- Autogenerated by Bloom

