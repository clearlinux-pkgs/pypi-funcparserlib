#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-funcparserlib
Version  : 1.0.0a1
Release  : 37
URL      : https://github.com/vlasovskikh/funcparserlib/archive/1.0.0a1/funcparserlib-1.0.0a1.tar.gz
Source0  : https://github.com/vlasovskikh/funcparserlib/archive/1.0.0a1/funcparserlib-1.0.0a1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: pypi-funcparserlib-license = %{version}-%{release}
Requires: pypi-funcparserlib-python = %{version}-%{release}
Requires: pypi-funcparserlib-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(poetry_core)
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
funcparserlib
=============
Recursive descent parsing library for Python based on functional combinators.

%package license
Summary: license components for the pypi-funcparserlib package.
Group: Default

%description license
license components for the pypi-funcparserlib package.


%package python
Summary: python components for the pypi-funcparserlib package.
Group: Default
Requires: pypi-funcparserlib-python3 = %{version}-%{release}

%description python
python components for the pypi-funcparserlib package.


%package python3
Summary: python3 components for the pypi-funcparserlib package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pypi-funcparserlib package.


%prep
%setup -q -n funcparserlib-1.0.0a1
cd %{_builddir}/funcparserlib-1.0.0a1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1650635667
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-funcparserlib
cp %{_builddir}/funcparserlib-1.0.0a1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-funcparserlib/9c43ed8af0243b23bbf87e137bfd753f4cc4b899
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-funcparserlib/9c43ed8af0243b23bbf87e137bfd753f4cc4b899

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
