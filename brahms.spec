Name:		brahms
Summary:	Brahms - a MIDI Program for KDE
Summary(pl):	Brahms - program MIDI dla KDE
Version:	1.01
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	http://brahms.sourceforge.net/download/%{name}-%{version}.tar.bz2
URL:		http://brahms.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	kdelibs-devel

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Brahms is a MIDI Program for the K Desktop Enviroment.

%description -l pl
Brahms jest programem MIDI dla ¶rodowiska KDE.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build
export KDEDIR=%{kdeprefix} QTDIR=%{qtdir}

./configure2_13 \
	--prefix=$KDEDIR \
	--with-install-root=$RPM_BUILD_ROOT

%{__make} CXXFLAGS="%{rpmcflags} %{!?debug:-DNO_DEBUG -DNDEBUG}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install prefix=$RPM_BUILD_ROOT%{kdeprefix}

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
