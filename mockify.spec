Name:           mockify
Version:        0.1
Release:        1%{?dist}
Summary:        Easy, configurable API mocking you can change on-the-fly
License:        ASL 2.0 
#Source0:        main.go
BuildRequires:  golang
BuildRequires:  tree

%description
Easy, configurable API mocking you can change on-the-fly

%build
whereis go
echo ''
export GOPATH=%{_builddir}/_build
echo ''
echo $GOPATH
echo ''
go get github.com/gorilla/mux
go get github.com/json-iterator/go
go get github.com/sirupsen/logrus
go get gopkg.in/yaml.v2
echo ''
mkdir -p $GOPATH/src/github.com/patsevanton
git clone https://github.com/patsevanton/mockify.git $GOPATH/src/github.com/patsevanton/mockify
echo ''
pwd
echo ''
go build -o mockify $GOPATH/src/github.com/patsevanton/mockify/app/cmd/mockify.go
echo ''
ls

#pushd _build/src/https://github.com/patsevanton/mockify
#go build -o ../../../../../mockify
#popd

#%install
#install -d %{buildroot}%{_bindir}
#install -p -m 0755 ./mockify %{buildroot}%{_bindir}/mockify

#%files
#%defattr(-,root,root,-)
#%{_bindir}/mockify
