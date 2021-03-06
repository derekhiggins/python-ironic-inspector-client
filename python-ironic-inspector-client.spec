%global pypi_name python-ironic-inspector-client

Name:           python-ironic-inspector-client
Version:        XXX
Release:        XXX
Summary:        Python client and CLI tool for Ironic Inspector

License:        ASL 2.0
URL:            https://launchpad.net/python-ironic-inspector-client
Source0:        https://pypi.python.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-pbr

Requires:  python-cliff
Requires:  python-oslo-i18n
Requires:  python-oslo-utils
Requires:  python-openstackclient
Requires:  python-requests
Requires:  python-six

# Conflict due to ironic-discoverd also providing a CLI tool
Conflicts: python-ironic-discoverd

%description
Ironic Inspector is an auxiliary service for discovering hardware properties
for a node managed by OpenStack Ironic. Hardware introspection or hardware
properties discovery is a process of getting hardware parameters required for
scheduling from a bare metal node, given it’s power management credentials
(e.g. IPMI address, user name and password).

This package contains Python client and command line tool for Ironic Inspector.

%prep
%setup -q -n %{pypi_name}-%{upstream_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Let RPM handle the dependencies
rm -f {test-,}requirements.txt

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files
%doc README.rst LICENSE
%{python2_sitelib}/ironic_inspector_client*
%{python2_sitelib}/python_ironic_inspector_client*egg-info

%changelog
* Tue Jul 14 2015 Dmitry Tantsur <divius.inside@gmail.com> - 1.0.1-1
- Initial package.
