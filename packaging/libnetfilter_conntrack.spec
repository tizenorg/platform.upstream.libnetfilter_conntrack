Name:           libnetfilter_conntrack
Version:        1.0.2
Release:        0
Url:            http://netfilter.org/projects/libnetfilter_conntrack/
Summary:        Userspace library for the in-kernel connection tracking state table
License:        GPL-2.0+
Group:          Productivity/Networking/Security

#Git-Clone:	git://git.netfilter.org/libnetfilter_conntrack
#DL-URL:	http://netfilter.org/projects/libnetfilter_conntrack/files/
Source:         http://netfilter.org/projects/libnetfilter_conntrack/files/%name-%version.tar.bz2
Source2:        baselibs.conf
Source1001: 	libnetfilter_conntrack.manifest
BuildRequires:  pkgconfig >= 0.21
BuildRequires:  pkgconfig(libmnl) >= 1.0.3
BuildRequires:  pkgconfig(libnfnetlink) >= 1.0.0

%description
libnetfilter_conntrack is a userspace library providing a programming
interface (API) to the in-kernel connection tracking state table. The
library libnetfilter_conntrack has been previously known as
libnfnetlink_conntrack and libctnetlink. This library is currently
used by conntrack-tools among many other applications.

%package devel
Requires:       %name = %version
Summary:        Userspace library for the in-kernel connection tracking state table
Group:          Development/Libraries/C and C++

%description devel
libnetfilter_conntrack is a userspace library providing a programming
interface (API) to the in-kernel connection tracking state table. The
library libnetfilter_conntrack has been previously known as
libnfnetlink_conntrack and libctnetlink. This library is currently
used by conntrack-tools among many other applications.

%prep
%setup -q
cp %{SOURCE1001} .

%build
if [ "%git_snapshot" -ne 0 ] || [ ! -e configure ]; then
	autoreconf -fi;
fi;
%configure --disable-static --includedir="%_includedir/%name-%version"
make %{?_smp_mflags}

%install
%make_install

%post  -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files 
%manifest %{name}.manifest
%defattr(-,root,root)
%_libdir/libnetfilter_conntrack.so.3*

%files devel
%manifest %{name}.manifest
%defattr(-,root,root)
%_includedir/%name-%version
%_libdir/libnetfilter_conntrack.so
%_libdir/pkgconfig/libnetfilter_conntrack.pc

%changelog
