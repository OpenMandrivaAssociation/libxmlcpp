%define major	1
%define api	5.0
%define libname	%mklibname xml++ %{api}
%define devname	%mklibname xml++ %{api} -d

Name: 		libxml++
Summary: 	C++ interface for working with XML files
Version:	5.4.0
Release: 	1
License:	LGPLv2+
Group:		System/Libraries
URL:		https://libxmlplusplus.sourceforge.net/
Source:		https://download.gnome.org/sources/libxml++/%{url_ver}/libxml++-%{version}.tar.xz
BuildRequires:	docbook5-style-xsl
#BuildRequires:	docbook5-schemas
BuildRequires:	xsltproc
BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	meson
BuildRequires:	pkgconfig(glibmm-2.4)
BuildRequires:	pkgconfig(libxml-2.0)

%description
libxml++ is a C++ interface for working with XML files, using libxml
(gnome-xml) to parse and write the actual XML files. It has a simple
but complete API.

%package	-n %{libname}
Summary: 	C++ interface for working with XML files
Group:		System/Libraries

%description	-n %{libname}
libxml++ is a C++ interface for working with XML files, using libxml
(gnome-xml) to parse and write the actual XML files. It has a simple
but complete API.

%package	-n %{devname}
Summary:	Headers for developing programs that will use %name
Group:		Development/C++
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{name}%{api}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}

%description	-n %{devname}
This package contains the headers that programmers will need to develop
applications which will use libraries from %name.

%prep
%autosetup -p1

%build
%meson \
	-Dbuild-documentation=false
%meson_build

%install
%meson_install

%files -n %{libname}
%license COPYING
%doc NEWS README.md
%{_libdir}/libxml++-%{api}.so.%{major}{,.*}

%files -n %{devname}
%doc ChangeLog NEWS README.md
%doc %{_datadir}/doc/libxml++-%{api}/
%{_datadir}/devhelp/books/libxml++-%{api}/libxml++-%{api}.devhelp2
%{_includedir}/libxml++-%{api}/
%{_libdir}/libxml++-%{api}/
%{_libdir}/pkgconfig/libxml++-%{api}.pc
%{_libdir}/libxml++-%{api}.so
