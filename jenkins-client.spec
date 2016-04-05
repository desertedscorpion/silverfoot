Name:           jenkins-client
Version:        VERSION
Release:        RELEASE
Summary:        The jenkins client

Group:          Administrative
License:        GNU/GPL3
URL:            git@github.com:desertedscorpion/scatteredfinger.git
Source:         %{name}-%{version}.tar.gz
Prefix:         %{_prefix}
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  nodejs npm
Requires:       nodejs jenkins


%description
This program runs a jenkins-client.

%prep
%setup -q

%build
while ! npm install
do
    sleep 10s
    echo NETWORK PROBLEMS
done

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir --parents ${RPM_BUILD_ROOT}/opt/jenkins-client
cp --recursive node_modules server.express.js ${RPM_BUILD_ROOT}/opt/jenkins-client

%clean
rm -rf ${RPM_BUILD_ROOT}


%files
%attr(0500,root,root) /opt/jenkins-client/node_modules
%attr(0555,root,root) /opt/jenkins-client/server.express.js
