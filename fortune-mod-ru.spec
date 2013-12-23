Summary:	Russian fortune messages
Name:		fortune-mod-ru
Version:	1.52
Release:	1
License:	GPLv2+
Group:		Toys
Url:		http://jack.kiev.ua/fortune-mod-ru/
Source0:	http://jack.kiev.ua/filez/%{name}-%{version}.tar.bz2
Requires:	fortune-mod
BuildArch:	noarch

%description
Russian fortune messages from Acid Jack.

%files
%doc ChangeLog README
%{_gamesdatadir}/fortunes/ru/

#----------------------------------------------------------------------------

%prep
%setup -q

%build

%install
%makeinstall_std INSTALL=install

