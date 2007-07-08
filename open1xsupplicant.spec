
Name:		open1xsupplicant
Summary:	Graphical interface to work with Xsupplicant.
Version:	0.1
Release:	%mkrel 1
License:	GPL
Group:		Networking/Remote access
Url:		http://alumni.ipt.pt/~caceres/open1xsupplicant
Source:		%name-%version.tar.gz
Source1:	network_traffic_wlan.png
BuildRoot:	%{_tmppath}/%name-%version-%release-buildroot
BuildRequires:	desktop-file-utils
BuildRequires:	kdelibs-devel
BuildRequires:	libxml2-utils
BuildRequires:	perl
Requires:	xsupplicant

%files
%defattr(-,root,root)
%doc README INSTALL COPYING TODO
%dir %_docdir/HTML/en/%name/
%_docdir/HTML/en/%name/*
%_bindir/%name
%_datadir/applnk/Utilities/%name.desktop
%dir %_datadir/apps/%name/
%_datadir/apps/%name/%{name}ui.rc
%_liconsdir/*.png
%_miconsdir/*.png
%_iconsdir/*.png

%description
Open1xSupplicant is a graphical interface to work with xsupplicant to atempt authenticate a user in a 802.1x protected network.

%prep
%setup -q

%build
CFLAGS="%optflags"
CXXFLAGS="%optflags"

%configure2_5x

%make

%install
rm -fr %buildroot
%makeinstall_std

sed -i 's:Icon=open1xsupplicant:Icon=network_traffic_wlan:g' %buildroot%_datadir/applnk/Utilities/%name.desktop
# Menu
desktop-file-install --vendor="" \
	--add-category="MandrivaLinux-Internet-RemoteAccess" \
	--add-category="Network" \
	--add-category="Dialup" \
	--dir %buildroot%_datadir/applnk/Utilities %buildroot%_datadir/applnk/Utilities/*

#icons
install -d -m755 %buildroot{%_liconsdir,%_miconsdir}
install -m644 %SOURCE1 %buildroot%_miconsdir/network_traffic_wlan.png
convert %SOURCE1 -size 32x32 %buildroot%_iconsdir/network_traffic_wlan.png
convert %SOURCE1 -size 48x48 %buildroot%_liconsdir/network_traffic_wlan.png

%clean
rm -rf %buildroot
