%global debug_package %{nil}

Name: python-more-itertools
Epoch: 100
Version: 8.12.0
Release: 1%{?dist}
BuildArch: noarch
Summary: More routines for operating on iterables, beyond itertools
License: MIT
URL: https://github.com/more-itertools/more-itertools/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Python's itertools library is a gem - you can compose elegant solutions
for a variety of problems with the functions it provides. In
more-itertools we collect additional building blocks, recipes, and
routines for working with Python iterables.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-more-itertools
Summary: More routines for operating on iterables, beyond itertools
Requires: python3
Provides: python3-more-itertools = %{epoch}:%{version}-%{release}
Provides: python3dist(more-itertools) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-more-itertools = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(more-itertools) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-more-itertools = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(more-itertools) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-more-itertools
Python's itertools library is a gem - you can compose elegant solutions
for a variety of problems with the functions it provides. In
more-itertools we collect additional building blocks, recipes, and
routines for working with Python iterables.

%files -n python%{python3_version_nodots}-more-itertools
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-more-itertools
Summary: More routines for operating on iterables, beyond itertools
Requires: python3
Provides: python3-more-itertools = %{epoch}:%{version}-%{release}
Provides: python3dist(more-itertools) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-more-itertools = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(more-itertools) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-more-itertools = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(more-itertools) = %{epoch}:%{version}-%{release}

%description -n python3-more-itertools
Python's itertools library is a gem - you can compose elegant solutions
for a variety of problems with the functions it provides. In
more-itertools we collect additional building blocks, recipes, and
routines for working with Python iterables.

%files -n python3-more-itertools
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
