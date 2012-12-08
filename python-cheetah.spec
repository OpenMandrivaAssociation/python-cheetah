Summary: Python-powered template engine and code-generator
Name: python-cheetah
Version: 2.4.4
Release: %mkrel 4
URL: http://www.CheetahTemplate.org/
Source0: http://pypi.python.org/packages/source/C/Cheetah/Cheetah-%{version}.tar.gz
License: MIT like
Group: Development/Python
BuildRequires: python-devel
BuildRoot: %{_tmppath}/%{name}-buildroot
Provides: python-cheetah2
Obsoletes: python-cheetah2

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
%setup -q -n Cheetah-%version

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES LICENSE TODO
%_libdir/python*/site-packages/Cheetah
%_libdir/python*/site-packages/*.egg-info
%_bindir/*


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 2.4.4-3mdv2011.0
+ Revision: 667916
- mass rebuild

* Fri Mar 11 2011 Michael Scherer <misc@mandriva.org> 2.4.4-2
+ Revision: 643812
- rebuild for distepoch tag

* Mon Dec 13 2010 Lev Givon <lev@mandriva.org> 2.4.4-1mdv2011.0
+ Revision: 620646
- Update to 2.4.4.

* Fri Oct 29 2010 Funda Wang <fwang@mandriva.org> 2.4.3-2mdv2011.0
+ Revision: 589935
- rebuild for python 2.7

* Sat Oct 23 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.4.3-1mdv2011.0
+ Revision: 587724
- update to new version 2.4.3

* Sat Aug 14 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.4.2.1-1mdv2011.0
+ Revision: 569665
- update to new version 2.4.2.1

* Wed Jan 06 2010 Frederik Himpe <fhimpe@mandriva.org> 2.4.1-1mdv2010.1
+ Revision: 486905
- Update to new version 2.4.1
- Remove hashlib patch which is not needed anymore

* Fri Jan 16 2009 Bogdano Arendartchuk <bogdano@mandriva.com> 2.0.1-4mdv2009.1
+ Revision: 330226
- patched to use hashlib instead of md5 (deprecated in python-2.6)

* Fri Dec 26 2008 Adam Williamson <awilliamson@mandriva.org> 2.0.1-3mdv2009.1
+ Revision: 319199
- rebuild with python 2.6

* Thu Dec 25 2008 Funda Wang <fwang@mandriva.org> 2.0.1-2mdv2009.1
+ Revision: 318539
- rebuild for new python

* Tue Jan 29 2008 Funda Wang <fwang@mandriva.org> 2.0.1-1mdv2008.1
+ Revision: 159844
- update to new version 2.0.1

* Fri Dec 14 2007 Bogdano Arendartchuk <bogdano@mandriva.com> 2.0-1mdv2008.1
+ Revision: 119919
- merged python-cheetah2 into python-cheetah

* Sun Oct 21 2007 Jérôme Soyer <saispo@mandriva.org> 1.0-5mdv2008.1
+ Revision: 100793
- Add Conflicts and Obsoletes to allow cheetah2 and not to break Mandriva tools


* Tue Nov 28 2006 Andreas Hasenack <andreas@mandriva.com> 1.0-4mdv2007.0
+ Revision: 87982
- added patch for python-2.5 to get rid of this error:
  "SyntaxError: from __future__ imports must occur at the beginning of the file"

  + Oden Eriksson <oeriksson@mandriva.com>
    - add needed egg-info file
    - Import python-cheetah

* Mon May 08 2006 Michael Scherer <misc@mandriva.org> 1.0-1mdk
- New release 1.0

* Sun Nov 06 2005 Michael Scherer <misc@mandriva.org> 0.9.18-2mdk
- mkrel 
- remove prefix tag

* Mon Oct 24 2005 Jan Ciger <jan.ciger@gmail.com> 0.9.18-1mdk
- 0.9.18

* Sat Feb 05 2005 Frederic Lepied <flepied@mandrakesoft.com> 0.9.16-0.a2.2mdk
- merge the 2 spec files

* Sat Feb 05 2005 Frederic Lepied <flepied@mandrakesoft.com> 0.9.16-0.a2.1mdk
- 0.9.16a2

* Sat Dec 04 2004 Michael Scherer <misc@mandrake.org> 0.9.15-4mdk
- Rebuild for new python

* Tue Oct 26 2004 Michael Scherer <misc@mandrake.org> 0.9.15-3mdk
- Rebuild

