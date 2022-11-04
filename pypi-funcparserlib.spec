#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-funcparserlib
Version  : 1.0.1
Release  : 50
URL      : https://github.com/vlasovskikh/funcparserlib/archive/1.0.1/funcparserlib-1.0.1.tar.gz
Source0  : https://github.com/vlasovskikh/funcparserlib/archive/1.0.1/funcparserlib-1.0.1.tar.gz
Summary  : Recursive descent parsing library based on functional combinators
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
Funcparserlib
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
Provides: pypi(funcparserlib)

%description python3
python3 components for the pypi-funcparserlib package.


%prep
%setup -q -n funcparserlib-1.0.1
cd %{_builddir}/funcparserlib-1.0.1
pushd ..
cp -a funcparserlib-1.0.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1667576303
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-funcparserlib
cp %{_builddir}/funcparserlib-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-funcparserlib/9c43ed8af0243b23bbf87e137bfd753f4cc4b899 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
