Name:           mockify
Version:        0.1
Release:        1%{?dist}
Summary:        Easy, configurable API mocking you can change on-the-fly
License:        ASL 2.0 
Source0:        main.go
BuildRequires:  golang
BuildRequires:  tree

%description
Easy, configurable API mocking you can change on-the-fly

%build
whereis go
echo $GOPATH
echo $GOROOT
# mkdir -p _build/src/https://github.com/patsevanton/mockify
cp ../SOURCES/main.go _build/src/https://github.com/patsevanton/mockify
export GOPATH=$(pwd)/_build
export PATH=$PATH:$(pwd)/_build/bin

pushd _build/src/https://github.com/patsevanton/mockify
go build -o ../../../../../mockify
popd

%install
install -d %{buildroot}%{_bindir}
install -p -m 0755 ./mockify %{buildroot}%{_bindir}/mockify

%files
%defattr(-,root,root,-)
%{_bindir}/mockify
