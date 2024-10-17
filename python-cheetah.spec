Summary:	Python-powered template engine and code-generator
Name:		python-cheetah
Version:	3.1.0
Release:	4
License:	MIT
Group:		Development/Python
Url:		https://www.CheetahTemplate.org/
Source0:	https://pypi.python.org/packages/54/86/ea50bb5baf1daa8ca1a56774d48150a69376679d27c4130848702efc378c/Cheetah3-%{version}.tar.gz
BuildRequires:	pkgconfig(python)
BuildRequires:	python3egg(setuptools)

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

#----------------------------------------------------------------------------

%files
%doc ANNOUNCE.rst README.rst TODO BUGS LICENSE
%{_bindir}/*
%{py3_platsitedir}/

#----------------------------------------------------------------------------

%prep
%setup -q -n Cheetah3-%{version}
# remove unnecessary shebang lines to silence rpmlint
sed -i -e '/^#!/,1d' Cheetah/Tests/* \
         Cheetah/DirectiveAnalyzer.py Cheetah/Utils/Misc.py

%build
%py3_build

%install
%py3_install

