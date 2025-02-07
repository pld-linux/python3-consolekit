%define		module	consolekit
Summary:	Additional utilities for click
Name:		python3-%{module}
Version:	1.7.2
Release:	0.1
License:	MIT
Group:		Libraries/Python
Source0:	https://pypi.debian.net/consolekit/%{module}-%{version}.tar.gz
# Source0-md5:	40252ac1089e0de3e7306109c30be76c
#URL:		https://pypi.org/project/MODULE/
URL:		https://pypi.org/project/consolekit/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Additional utilities for click.

%prep
%setup -q -n %{module}-%{version}

%build
%{__python3} -m build --wheel --no-isolation --outdir build-3

%install
rm -rf $RPM_BUILD_ROOT

%{__python3} -m installer --destdir=$RPM_BUILD_ROOT build-3/*.whl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}.dist-info
