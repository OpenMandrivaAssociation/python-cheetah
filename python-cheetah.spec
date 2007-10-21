Summary: Python-powered template engine and code-generator
Name: python-cheetah
Version: 1.0
Release: %mkrel 5
URL: http://www.CheetahTemplate.org/
Source0: http://prdownloads.sourceforge.net/cheetahtemplate/Cheetah-%{version}.tar.bz2
Patch: python-cheetah-1.0-future.patch
License: MIT like
Group: Development/Python
BuildRequires: python-devel
BuildRoot: %{_tmppath}/%{name}-buildroot
Conflicts: python-cheetah2
Obsoletes: python-cheetah2

%description
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
%setup -q -n Cheetah-%version
%patch -p1 -b .future

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README CHANGES LICENSE TODO
%_libdir/python*/site-packages/Cheetah
%_libdir/python*/site-packages/*.egg-info
%_bindir/*

