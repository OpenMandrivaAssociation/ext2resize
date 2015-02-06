Summary: Ext2 fs resizer
Name:	 ext2resize
Version: 1.1.19
Release: 6
License: GPL
Group: System/Kernel and hardware
Url: http://ext2resize.sourceforge.net/
Source0: http://ext2resize.sourceforge.net/%{name}-%{version}.tar.bz2
Patch0:	ext2resize-1.1.19-blkgetsize64.patch
Obsoletes: ext2fs
Provides: ext2fs
BuildRequires:	pkgconfig(ext2fs)
#BuildRequires:	autoconf2.5

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
chmod +r *
%makeinstall

install -d %{buildroot}%{_mandir}/man8
install -m 644 doc/*.8 %{buildroot}%{_mandir}/man8

%files
%doc AUTHORS COPYING ChangeLog INSTALL README
%{_sbindir}/*
%{_mandir}/*/*
