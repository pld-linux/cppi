Summary:	GNU cppi - checks the indentation of C and C++ preprocessor directives
Summary(pl):	GNU cppi - narzêdzie sprawdzaj±ce wciêcia dyrektyw preprocesora C i C++
Name:		cppi
Version:	1.12
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.gnu.org/gnu/coreutils/%{name}-%{version}.tar.bz2
# Source0-md5:	3a9b8fa70cae2fb36b089a5f2ef4326f
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU `cppi' adjusts or checks the indentation of C and C++ preprocessor
directives in a file.

%description -l pl
GNU cppi sprawdza i poprawia wciêcia dyrektyw preprocesora C i C++.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
