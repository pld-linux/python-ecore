Summary:	Python bindings for Ecore library
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki Ecore
Name:		python-ecore
Version:	0.7.3
Release:	1
License:	LGPL v2.1+
Group:		Development/Languages/Python
Source0:	http://download.enlightenment.org/releases/BINDINGS/python/%{name}-%{version}.tar.bz2
# Source0-md5:	a972aa785e708d9fac45ab52895a78e8
Patch0:		%{name}-cython.patch
Patch1:		%{name}-update.patch
URL:		http://trac.enlightenment.org/e/wiki/Python
BuildRequires:	ecore-devel >= 1.0.0
BuildRequires:	ecore-evas-devel >= 1.0.0
BuildRequires:	ecore-imf-devel >= 1.0.0
BuildRequires:	ecore-x-devel >= 1.0.0
BuildRequires:	epydoc
BuildRequires:	evas-devel >= 1.0.0
BuildRequires:	python-Cython >= 0.13
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-evas-devel >= 0.7.3
BuildRequires:	rpm-pythonprov
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	ecore >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for Ecore library.

%description -l pl.UTF-8
Wiązania Pythona do biblioteki Ecore.

%package devel
Summary:	Python bindings for Ecore library - development files
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki Ecore - pliki programistyczne
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ecore-devel >= 1.0.0

%description devel
Python bindings for Ecore library - development files.

%description devel -l pl.UTF-8
Wiązania Pythona do biblioteki Ecore - pliki programistyczne.

%package evas
Summary:	Python bindings for Ecore Evas library
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki Ecore Evas
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
Requires:	ecore-evas >= 1.0.0
Requires:	evas >= 1.0.0
Requires:	python-evas >= 0.7.3

%description evas
Python bindings for Ecore Evas library.

%description evas -l pl.UTF-8
Wiązania Pythona do biblioteki Ecore Evas.

%package evas-devel
Summary:	Python bindings for Ecore Evas library - development files
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki Ecore Evas - pliki programistyczne
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-evas = %{version}-%{release}
Requires:	ecore-evas-devel >= 1.0.0
Requires:	python-evas-devel >= 0.7.3

%description evas-devel
Python bindings for Ecore Evas library - development files.

%description evas-devel -l pl.UTF-8
Wiązania Pythona do biblioteki Ecore Evas - pliki programistyczne.

%package imf
Summary:	Python bindings for Ecore IMF library
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki Ecore IMF
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
Requires:	ecore-imf >= 1.0.0

%description imf
Python bindings for Ecore IMF library.

%description imf -l pl.UTF-8
Wiązania Pythona do biblioteki Ecore IMF.

%package imf-devel
Summary:	Python bindings for Ecore IMF library - development files
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki Ecore IMF - pliki programistyczne
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-imf = %{version}-%{release}
Requires:	ecore-imf-devel >= 1.0.0

%description imf-devel
Python bindings for Ecore IMF library - development files.

%description imf-devel -l pl.UTF-8
Wiązania Pythona do biblioteki Ecore IMF - pliki programistyczne.

%package x
Summary:	Python bindings for Ecore X library
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki Ecore X
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
Requires:	ecore-x >= 1.0.0

%description x
Python bindings for Ecore X library.

%description x -l pl.UTF-8
Wiązania Pythona do biblioteki Ecore X.

%package x-devel
Summary:	Python bindings for Ecore X library - development files
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki Ecore X - pliki programistyczne
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-x = %{version}-%{release}
Requires:	ecore-x-devel >= 1.0.0

%description x-devel
Python bindings for Ecore X library - development files.

%description x-devel -l pl.UTF-8
Wiązania Pythona do biblioteki Ecore X - pliki programistyczne.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/ecore/c_ecore.la
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/ecore/*/*.la

install -d $RPM_BUILD_ROOT%{_examplesdir}
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%dir %{py_sitedir}/ecore
%attr(755,root,root) %{py_sitedir}/ecore/c_ecore.so
%dir %{py_sitescriptdir}/ecore
%{py_sitescriptdir}/ecore/__init__.py[co]
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/*.py

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/python-ecore
%dir %{_includedir}/python-ecore/ecore
%{_includedir}/python-ecore/ecore/__init__.py
%{_includedir}/python-ecore/ecore/c_ecore.pxd
%{_includedir}/python-ecore/ecore/ecore.*.h
%{_pkgconfigdir}/python-ecore.pc

%files evas
%defattr(644,root,root,755)
%dir %{py_sitedir}/ecore/evas
%attr(755,root,root) %{py_sitedir}/ecore/evas/c_ecore_evas.so
%{py_sitescriptdir}/ecore/evas
%{_examplesdir}/%{name}-%{version}/ecore-evas

%files evas-devel
%defattr(644,root,root,755)
%{_includedir}/python-ecore/ecore/evas
%{_pkgconfigdir}/python-ecore-evas.pc

%files imf
%defattr(644,root,root,755)
%dir %{py_sitedir}/ecore/imf
%attr(755,root,root) %{py_sitedir}/ecore/imf/c_ecore_imf.so
%{py_sitescriptdir}/ecore/imf

%files imf-devel
%defattr(644,root,root,755)
%{_includedir}/python-ecore/ecore/imf
%{_pkgconfigdir}/python-ecore-imf.pc

%files x
%defattr(644,root,root,755)
%dir %{py_sitedir}/ecore/x
%attr(755,root,root) %{py_sitedir}/ecore/x/c_ecore_x.so
%{py_sitescriptdir}/ecore/x
%{_examplesdir}/%{name}-%{version}/x

%files x-devel
%defattr(644,root,root,755)
%{_includedir}/python-ecore/ecore/x
%{_pkgconfigdir}/python-ecore-x.pc
