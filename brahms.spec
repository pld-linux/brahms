%define kdeprefix /usr
%define qtdir /usr/lib/qt-1.44
%define version 0.97.2
%define kdename Brahms
%define kderelease 0

Name: %{kdename}
Summary: Brahms - a MIDI Program for KDE
Version: %{version}
Release: %{kderelease}
Source: http://lienhard.desy.de/mackag/homepages/jan/Brahms/Brahms-0.97.2.tar.gz
URL: http://lienhard.desy.de/mackag/homepages/jan/Brahms/
Group: Applications/Multimedia
BuildRoot: /var/tmp/%{kdename}-buildroot
Copyright: GPL
Requires: kdesupport
Prefix: %{kdeprefix}

%description
Brahms is a MIDI Program for the K Desktop Enviroment.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build
export KDEDIR=%{kdeprefix} QTDIR=%{qtdir}
./configure \
	--prefix=$KDEDIR \
	--with-install-root=$RPM_BUILD_ROOT

make CXXFLAGS="$RPM_OPT_FLAGS -DNO_DEBUG -DNDEBUG"

%install
make install-strip prefix=$RPM_BUILD_ROOT%{kdeprefix}

# remove conflicting mime types
rm -rf $RPM_BUILD_ROOT%{kdeprefix}/share/mimelnk

cd $RPM_BUILD_ROOT
find . -type d | sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > \
	$RPM_BUILD_DIR/file.list.%{kdename}

find . -type f | sed -e 's,^\.,\%attr(-\,root\,root) ,' \
	-e '/\/config\//s|^|%config|' >> \
	$RPM_BUILD_DIR/file.list.%{kdename}

find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> \
	$RPM_BUILD_DIR/file.list.%{kdename}

echo "%docdir /usr/doc/kde" >> $RPM_BUILD_DIR/file.list.%{kdename}

%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/file.list.%{kdename}

%files -f ../file.list.%{kdename}

%changelog
* Mon Nov 2 1999 Mattias Kunkel <mattias@kunkel.freeservers.com>
- made initial RPM
