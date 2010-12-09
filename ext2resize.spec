Summary: Ext2 fs resizer
Name:	 ext2resize
Version: 1.1.19
Release: %mkrel 5
License: GPL
Group: System/Kernel and hardware
Url: http://ext2resize.sourceforge.net/
Source: http://ext2resize.sourceforge.net/%{name}-%{version}.tar.bz2
Patch0:	ext2resize-1.1.19-blkgetsize64.patch
Obsoletes: ext2fs
Provides: ext2fs
BuildRequires:	e2fsprogs-devel
BuildRequires:	autoconf2.5
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
ext2resize enable to enlarge or reduce a ext2 fs.

WARNING: this is BETA software.
You may lose data.
You have been warned
Save them before using ext2resize

WARNING: you should probably use resize2fs from e2fsprogs
         which is more robust.

%prep
%setup -q
%patch0 -p2 -b .blkgetsize64
# lib64 fixes, aka libuuid.a is in $(libdir) not /usr/lib
perl -pi -e "s@/usr/lib/(libuuid.a)@%{_libdir}/\1@g" \
	src/Makefile.am src/Makefile.in

%build
%configure2_5x
make

%install
rm -rf $RPM_BUILD_ROOT
chmod +r *
%makeinstall

install -d $RPM_BUILD_ROOT%{_mandir}/man8
install -m 644 doc/*.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL README
%{_sbindir}/*
%{_mandir}/*/*


