Name:		classloader-leak-test-framework
Version:	1.1.1
Release:	5%{?dist}
Summary:	Detection and verification of Java ClassLoader leaks
License:	ASL 2.0
URL:		https://github.com/mjiderhamn/classloader-leak-prevention/tree/master/%{name}
Source0:	https://github.com/mjiderhamn/classloader-leak-prevention/archive/%{name}-%{version}.tar.gz

BuildArch:	noarch

# build
BuildRequires:	maven-local
BuildRequires:	mvn(junit:junit)
BuildRequires:	mvn(org.apache.bcel:bcel)
# test dependencies
%if ! 0%{?centos}
BuildRequires:	mvn(javax.el:el-api)
BuildRequires:	mvn(com.sun.faces:jsf-api)
BuildRequires:	mvn(com.sun.faces:jsf-impl)
%endif

%description
Stand-alone test framework for detecting and/or verifying the existence or
non-existence of Java ClassLoader leaks. It is also possible to test leak
prevention mechanisms to confirm that the leak really is avoided. The framework
is an built upon JUnit.

%package javadoc
Summary:	Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n classloader-leak-prevention-%{name}-%{version}
rm -r classloader-leak-prevention
cp -r %{name}/* .

%build
%if 0%{?centos}
%mvn_build -f
%else
%mvn_build
%endif

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Mon May 28 2018 Sandro Bonazzola <sbonazzo@redhat.com> - 1.1.1-5
- Skip tests and drop tests deps on CentOS for CentOS Virt SIG since we have
  no man power for maintaining all the test dependency tree

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 03 2016 Tomas Repik <trepik@redhat.com> - 1.1.1-1
- initial package

