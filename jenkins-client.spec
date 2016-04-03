Name:           jenkins-client
Version:        VERSION
Release:        RELEASE
Summary:        The jenkins client

Group:          Administrative
License:        GNU/GPL3
URL:            git@github.com:desertedscorpion/whitevenus.git
Source:         %{name}-%{version}.tar.gz
Prefix:         %{_prefix}
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:       node
BuildRequires:  npm
%define debug_package %{nil}


%description
This program tests the phonetic program.

%prep


%build
npm install

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir --parents ${RPM_BUILD_ROOT}/opt/jenkins-client
cp --recursive node_modules server.express.js ${RPM_BUILD_ROOT}/opt/jenkins-client
mkdir --parents ${RPM_BUILD_ROOT}/usr/local/bin


%clean
rm -rf ${RPM_BUILD_ROOT}


%files
%attr(0500,root,root) /opt/jenkins-client/node_modules
%attr(0555,root,root) /opt/jenkins-client/server.express.js
