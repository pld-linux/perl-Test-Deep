#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	Deep
Summary:	Test::Deep - Extremely flexible deep comparison
Summary(pl):	Test::Deep - bardzo elastyczne g³êbokie porównania
Name:		perl-Test-Deep
Version:	0.092
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2b08c439013db230dc153cf52553fd7a
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

%description -l pl
Test::Deep udostêpnia bardzo elastyczne sposoby sprawdzania, czy
otrzymany wynik jest tym, który by³ oczekiwany. W najprostszym
przypadku porównuje dwie struktury przechodz±c po ka¿dym poziomie,
sprawdzaj±c czy warto¶ci siê zgadzaj±, czy tablice i hasze maj± te
same elementy i czy referencje s± pob³ogos³awione do w³a¶ciwych klas.
Obs³uguje tak¿e zapêtlone struktury danych bez wpadania w nieskoñczon±
pêtlê.

Bardziej interesuj±ce jest to, ¿e pozwala na robienie czego¶ wiêcej
ni¿ proste przyrównania. Dla ³añcuchów znaków operator eq sprawdza,
czy 2 ³añcuchy s± dok³adnie takie same, ale czasem nie jest to tym,
co chcemy. Je¶li nie wiemy dok³adnie, jaki powinien byæ ³añcuch, ale
wiemy co¶ o tym, jak powinien wygl±daæ - Test::Deep pozwala na
dopasowywanie wzorców dla z³o¿onych struktur danych.

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
