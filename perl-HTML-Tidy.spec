#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	HTML
%define		pnam	Tidy
%include	/usr/lib/rpm/macros.perl
Summary:	HTML::Tidy - (X)HTML validation in a Perl object
Summary(pl.UTF-8):	HTML::Tidy - sprawdzanie poprawności (X)HTML-a w obiekcie Perla
Name:		perl-HTML-Tidy
Version:	1.54
Release:	5
License:	Artistic v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTML/HTML-Tidy-%{version}.tar.gz
# Source0-md5:	3025e63d5a85d2abfa793dc1353f8752
URL:		http://search.cpan.org/dist/HTML-Tidy/
BuildRequires:	libtidyp-devel
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Pod
BuildRequires:	perl-Test-Pod-Coverage
BuildRequires:	perl-Test-Simple
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::Tidy is an HTML checker in a handy dandy object. It's meant as a
replacement for HTML::Lint. If you're currently an HTML::Lint user
looking to migrate, see the section /Converting from HTML::Lint.

%description -l pl.UTF-8
HTML::Tidy to narzędzie do sprawdzania poprawności HTML-a postaci
poręcznego obiektu. Jest pomyślany jako zamiennik HTML::Lint.
Użytkownikom modułu HTML::Lint, chcącym się przenieść, przyda się
lektura sekcji /Converting from HTML::Lint.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%attr(755,root,root) %{_bindir}/webtidy
%{perl_vendorarch}/HTML/Tidy.pm
%dir %{perl_vendorarch}/HTML/Tidy
%{perl_vendorarch}/HTML/Tidy/Message.pm
%dir %{perl_vendorarch}/auto/HTML/Tidy
%attr(755,root,root) %{perl_vendorarch}/auto/HTML/Tidy/Tidy.so
%{_mandir}/man3/HTML::Tidy*
