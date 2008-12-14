#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	Deep
Summary:	Test::Deep - Extremely flexible deep comparison
Summary(pl.UTF-8):	Test::Deep - bardzo elastyczne głębokie porównania
Name:		perl-Test-Deep
Version:	0.103
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2fc92524553a3077475ea9589f02d4ee
URL:		http://search.cpan.org/dist/Test-Deep/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-NoWarnings >= 0.02
BuildRequires:	perl-Test-Tester >= 0.04
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Test::Deep gives you very flexible ways to check that the result you
got is the result you were expecting. At it's simplest it compares two
structures by going through each level, ensuring that the values
match, that arrays and hashes have the same elements and that
references are blessed into the correct class. It also handles
circular data structures without getting caught in an infinite loop.

Where it becomes more interesting is in allowing you to do something
besides simple exact comparisons. With strings, the eq operator checks
that 2 strings are exactly equal but sometimes that's not what you
want. When you don't know exactly what the string should be but you do
know some things about how it should look, eq is no good and you must
use pattern matching instead. Test::Deep provides pattern matching for
complex data structures.

%description -l pl.UTF-8
Test::Deep udostępnia bardzo elastyczne sposoby sprawdzania, czy
otrzymany wynik jest tym, który był oczekiwany. W najprostszym
przypadku porównuje dwie struktury przechodząc po każdym poziomie,
sprawdzając czy wartości się zgadzają, czy tablice i hasze mają te
same elementy i czy referencje są pobłogosławione do właściwych klas.
Obsługuje także zapętlone struktury danych bez wpadania w nieskończoną
pętlę.

Bardziej interesujące jest to, że pozwala na robienie czegoś więcej
niż proste przyrównania. Dla łańcuchów znaków operator eq sprawdza,
czy 2 łańcuchy są dokładnie takie same, ale czasem nie jest to tym,
co chcemy. Jeśli nie wiemy dokładnie, jaki powinien być łańcuch, ale
wiemy coś o tym, jak powinien wyglądać - Test::Deep pozwala na
dopasowywanie wzorców dla złożonych struktur danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO
%{perl_vendorlib}/Test/*.pm
%{perl_vendorlib}/Test/Deep
%{_mandir}/man3/*
