#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-kubernetes
Version  : 24.2.0
Release  : 11
URL      : https://files.pythonhosted.org/packages/22/eb/6b2385fb2e2b8da2f329a2832cd29b3ca39e462f9719d550c7d55e502a73/kubernetes-24.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/22/eb/6b2385fb2e2b8da2f329a2832cd29b3ca39e462f9719d550c7d55e502a73/kubernetes-24.2.0.tar.gz
Summary  : Kubernetes python client
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-kubernetes-license = %{version}-%{release}
Requires: pypi-kubernetes-python = %{version}-%{release}
Requires: pypi-kubernetes-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(certifi)
BuildRequires : pypi(google_auth)
BuildRequires : pypi(ipaddress)
BuildRequires : pypi(py)
BuildRequires : pypi(python_dateutil)
BuildRequires : pypi(pyyaml)
BuildRequires : pypi(requests)
BuildRequires : pypi(requests_oauthlib)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(six)
BuildRequires : pypi(urllib3)
BuildRequires : pypi(websocket_client)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
# Kubernetes Python Client
[![Build Status](https://travis-ci.org/kubernetes-client/python.svg?branch=master)](https://travis-ci.org/kubernetes-client/python)
[![PyPI version](https://badge.fury.io/py/kubernetes.svg)](https://badge.fury.io/py/kubernetes)
[![codecov](https://codecov.io/gh/kubernetes-client/python/branch/master/graph/badge.svg)](https://codecov.io/gh/kubernetes-client/python "Non-generated packages only")
[![pypi supported versions](https://img.shields.io/pypi/pyversions/kubernetes.svg)](https://pypi.python.org/pypi/kubernetes)
[![Client Capabilities](https://img.shields.io/badge/Kubernetes%20client-Silver-blue.svg?style=flat&colorB=C0C0C0&colorA=306CE8)](http://bit.ly/kubernetes-client-capabilities-badge)
[![Client Support Level](https://img.shields.io/badge/kubernetes%20client-beta-green.svg?style=flat&colorA=306CE8)](http://bit.ly/kubernetes-client-support-badge)

%package license
Summary: license components for the pypi-kubernetes package.
Group: Default

%description license
license components for the pypi-kubernetes package.


%package python
Summary: python components for the pypi-kubernetes package.
Group: Default
Requires: pypi-kubernetes-python3 = %{version}-%{release}

%description python
python components for the pypi-kubernetes package.


%package python3
Summary: python3 components for the pypi-kubernetes package.
Group: Default
Requires: python3-core
Provides: pypi(kubernetes)
Requires: pypi(certifi)
Requires: pypi(google_auth)
Requires: pypi(ipaddress)
Requires: pypi(python_dateutil)
Requires: pypi(pyyaml)
Requires: pypi(requests)
Requires: pypi(requests_oauthlib)
Requires: pypi(setuptools)
Requires: pypi(six)
Requires: pypi(urllib3)
Requires: pypi(websocket_client)

%description python3
python3 components for the pypi-kubernetes package.


%prep
%setup -q -n kubernetes-24.2.0
cd %{_builddir}/kubernetes-24.2.0
pushd ..
cp -a kubernetes-24.2.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1655999342
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-kubernetes
cp %{_builddir}/kubernetes-24.2.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-kubernetes/8d27fd734630787bf68266a7f4fb6b4c55cd6853
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-kubernetes/8d27fd734630787bf68266a7f4fb6b4c55cd6853

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
