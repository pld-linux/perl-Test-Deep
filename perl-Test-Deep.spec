#
# Conditional build:
%bcond_without	tests	# unit tests

%define		pdir	Test
%define		pnam	Deep
Summary:	Test::Deep - Extremely flexible deep comparison
Summary(pl.UTF-8):	Test::Deep - bardzo elastyczne głębokie porównania
Name:		perl-Test-Deep
Version:	1.204
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fcff296434cd92538ae9de9d1744705f
URL:		https://metacpan.org/dist/Test-Deep
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.78
BuildRequires:	perl-devel >= 1:5.12.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Scalar-List-Utils >= 1.09
BuildRequires:	perl-Test-Simple >= 0.96
BuildRequires:	perl-Test-Tester >= 0.107
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
czy 2 łańcuchy są dokładnie takie same, ale czasem nie jest to tym, co
chcemy. Jeśli nie wiemy dokładnie, jaki powinien być łańcuch, ale
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
%doc Changes README TODO
%{perl_vendorlib}/Test/Deep.pm
%{perl_vendorlib}/Test/Deep
%{_mandir}/man3/Test::Deep*.3pm*
