Summary:	Brahms - a MIDI Program for KDE
Summary(pl):	Brahms - program MIDI dla KDE
Name:		brahms
Version:	1.02
Release:	3
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://brahms.sourceforge.net/download/%{name}-%{version}-kde2.tar.bz2
URL:		http://brahms.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRequires:	kdemultimedia-devel
BuildRequires:	libtool
BuildRequires:	perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_htmldir	/usr/share/doc/kde/HTML

%description
Brahms is a MIDI Program for the K Desktop Enviroment.

%description -l pl
Brahms jest programem MIDI dla ¶rodowiska KDE.

%prep
%setup -q -n Brahms

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
%configure2_13

%{__make} CXXFLAGS="%{rpmcflags} -fno-exceptions -fno-rtti %{!?debug:-DNO_DEBUG -DNDEBUG}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

# remove conflicting mime types
rm -rf $RPM_BUILD_ROOT%{_datadir}/mimelnk

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_libdir}/mcop/*
%{_pixmapsdir}/*/*/apps/*
%{_datadir}/apps/brahms
%{_applnkdir}/Multimedia/*
