Summary:	GNU cppi - checks the indentation of C and C++ preprocessor directives
Summary(pl):	GNU cppi - narz�dzie sprawdzajace wci�cia dyrektyw preprocesora C i C++
Name:		cppi
Version:	1.10
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	ftp://alpha.gnu.org/gnu/fetish/%{name}-%{version}.tar.bz2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU `cppi' adjusts or checks the indentation of C and C++ preprocessor
directives in a file.

%description -l pl
GNU cppi sprawdza i poprawia wci�cia dyrektyw preprocesora C i C++.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*