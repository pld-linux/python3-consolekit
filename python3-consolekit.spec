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
BuildRequires:	python3-flit_core < 4
BuildRequires:	python3-flit_core >= 3.2
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Additional utilities for click.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}.dist-info
