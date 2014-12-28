Summary:	GNU cppi - checks the indentation of C and C++ preprocessor directives
Summary(pl.UTF-8):	GNU cppi - narzędzie sprawdzające wcięcia dyrektyw preprocesora C i C++
Name:		cppi
Version:	1.18
Release:	1
License:	GPL v3+
Group:		Development/Tools
Source0:	http://ftp.gnu.org/gnu/cppi/%{name}-%{version}.tar.xz
# Source0-md5:	720f4e442287283a02979ba43a44366e
URL:		http://www.gnu.org/software/cppi/
BuildRequires:	gettext-tools >= 0.18.1
BuildRequires:	help2man
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU `cppi' adjusts or checks the indentation of C and C++ preprocessor
directives in a file.

%description -l pl.UTF-8
GNU cppi sprawdza i poprawia wcięcia dyrektyw preprocesora C i C++.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/cppi
%{_mandir}/man1/cppi.1*
