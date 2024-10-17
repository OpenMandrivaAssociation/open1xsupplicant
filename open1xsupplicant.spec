Name:		open1xsupplicant
Summary:	Graphical interface to work with Xsupplicant
Version:	0.1
Release:	%mkrel 4
License:	GPL
Group:		Networking/Remote access
Url:		https://alumni.ipt.pt/~caceres/open1xsupplicant
Source0:	%{name}-%{version}.tar.gz
Source1:	network_traffic_wlan.png
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	desktop-file-utils
BuildRequires:	kdelibs-devel
BuildRequires:	libxml2-utils
BuildRequires:	perl imagemagick
Requires:	xsupplicant

%description
Open1xSupplicant is a graphical interface to work with xsupplicant to atempt
authenticate a user in a 802.1x protected network.

%prep
%setup -q

%build
%configure2_5x	--disable-rpath
%make

%install
rm -fr %{buildroot}
%makeinstall_std

sed -i 's:Icon=open1xsupplicant:Icon=network_traffic_wlan:g' %{buildroot}%{_datadir}/applnk/Utilities/%{name}.desktop
# Menu
desktop-file-install --vendor="" \
	--add-category="X-MandrivaLinux-Internet-RemoteAccess" \
	--add-category="Network" \
	--add-category="Dialup" \
	--dir %{buildroot}%{_datadir}/applnk/Utilities %{buildroot}%{_datadir}/applnk/Utilities/*

#icons
install -d %{buildroot}{%{_liconsdir},%{_iconsdir},%{_miconsdir}}
install -m644 %{SOURCE1} -D %{buildroot}%{_miconsdir}/network_traffic_wlan.png
convert %{SOURCE1} -size 32x32 %{buildroot}%{_iconsdir}/network_traffic_wlan.png
convert %{SOURCE1} -size 48x48 %{buildroot}%{_liconsdir}/network_traffic_wlan.png

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README TODO
%dir %{_docdir}/HTML/en/%{name}/
%{_docdir}/HTML/en/%{name}/*
%{_bindir}/%{name}
%{_datadir}/applnk/Utilities/%{name}.desktop
%dir %{_datadir}/apps/%{name}/
%{_datadir}/apps/%{name}/%{name}ui.rc
%{_miconsdir}/*.png
%{_iconsdir}/*.png
%{_liconsdir}/*.png

