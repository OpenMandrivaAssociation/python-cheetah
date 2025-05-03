%define module cheetah
%define oname cheetah3

Name:		python-cheetah
Version:	3.4.0
Release:	1
License:	MIT
Summary:	Python-powered template engine and code-generator
Group:		Development/Python
URL:		https://www.CheetahTemplate.org/
Source0:	https://github.com/CheetahTemplate3/cheetah3/archive/%{version}/%{module}-%{version}.tar.gz

BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

Recommends:	python%{pyver}dist(markdown)
Suggests:		python%{pyver}dist(pygments)

%description
Python-cheetah:
* generates HTML, SGML, XML, SQL, Postscript, form email, LaTeX, or any other
  text-based format.
* cleanly separates content, graphic design, and program code. This leads to
  highly modular, flexible, and reusable site architectures; faster
  development time; and HTML and program code that is easier to understand and
  maintain. It is particularly well suited for team efforts.
* blends the power and flexibility of Python with a simple template language
  that non-programmers can understand.
* gives template writers full access to any Python data structure, module,
  function, object, or method in their templates.
* makes code reuse easy by providing an object-orientated interface to
  templates that is accessible from Python code or other Cheetah templates.
  One template can subclass another and selectively reimplement sections of it.
* provides a simple, yet powerful, caching mechanism that can dramatically
  improve the performance of a dynamic website.
* compiles templates into optimized, yet readable, Python code.

%prep
%autosetup -n %{oname}-%{version} -p1
# remove unnecessary shebang lines to silence rpmlint
find . -name \*.py -print0 |xargs -0 -t -l sed -i -e '1{\@^#!%{_bindir}/env python@d}'

%build
%py3_build

%install
%py3_install

%files
%{_bindir}/%{module}*
%{py3_platsitedir}/Cheetah
%{py3_platsitedir}/CT3-%{version}*.*-info
%doc ANNOUNCE.rst README.rst BUGS
%license LICENSE
