Name:		Brahms
Summary:	Brahms - a MIDI Program for KDE
Version:	0.97.2
Release:	0
License:	GPL
Group:		Applications/Multimedia
Group(pl):	Aplikacje/Multimedia
Source0:	http://lienhard.desy.de/mackag/homepages/jan/Brahms/%{name}-%{version}.tar.gz
URL:		http://lienhard.desy.de/mackag/homepages/jan/Brahms/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	kdesupport

%description
Brahms is a MIDI Program for the K Desktop Enviroment.

%description -l pl
Brahms jest programem MIDI dla ¶rodowiska KDE.

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

echo "%docdir %{_prefix}/doc/kde" >> $RPM_BUILD_DIR/file.list.%{kdename}

%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/file.list.%{kdename}

%files -f ../file.list.%{kdename}
%defattr(644,root,root,755)
