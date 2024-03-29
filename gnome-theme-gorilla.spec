Summary:	Gorilla theme
Summary(pl.UTF-8):	Motyw gorilla
Name:		gnome-theme-gorilla
Version:	1.0
Release:	2
License:	Free
Group:		X11/Amusements
Source0:	http://www.lucidus.uklinux.net/metathemes/Gorilla.metatheme.tar.gz
# Source0-md5:	ae618bdeb8a6061aa1a6dbb3c87e20fa
URL:		http://sunshineinabag.co.uk/
BuildRequires:	bzip2
BuildRequires:	tar
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel
Requires:	gtk-theme-ThinIce
Requires:	nautilus-theme-gorilla
Requires:	sawfish-theme-gorilla
Requires:	xmms-skin-XimianSouth
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_xmmsskinsdir	%{xmms_datadir}/Skins

%description
Gorilla theme for GTK+ (ThinIce), Nautilus, Sawfish and XMMS (Ximian
South).

%description -l pl.UTF-8
Motyw gorilla dla GTK+ (ThinIce), Nautilusa, Sawfisza i XMMS-a (Ximian
South).

%package -n xmms-skin-XimianSouth
Summary:	Ximian South skin
Summary(pl.UTF-8):	Skórka Ximian South
Group:		X11/Amusements
Requires:	bzip2
Requires:	tar
Requires:	xmms

%description -n xmms-skin-XimianSouth
Ximian South skin. You may be interested in gnome-theme-gorilla
package.

%description -n xmms-skin-XimianSouth -l pl.UTF-8
Skórka Ximian South. Można też spróbować pakietu gnome-theme-gorilla.

%package -n nautilus-theme-gorilla
Summary:	Gorilla theme
Summary(pl.UTF-8):	Motyw gorilla
Group:		X11/Amusements
Requires:	nautilus

%description -n nautilus-theme-gorilla
Gorilla theme. You may be interested in gnome-theme-gorilla package.
Note: It is highly cpu intensive.

%description -n nautilus-theme-gorilla -l pl.UTF-8
Motyw gorilla. Można też spróbować pakietu gnome-theme-gorilla. Uwaga:
Wymaga szybkiego procesora.

%package -n sawfish-theme-gorilla
Summary:	Gorilla theme
Summary(pl.UTF-8):	Motyw gorilla
Group:		X11/Amusements
Requires:	sawfish

%description -n sawfish-theme-gorilla
Gorilla theme. You may be interested in gnome-theme-gorilla package.

%description -n sawfish-theme-gorilla -l pl.UTF-8
Motyw gorilla. Można też spróbować pakietu gnome-theme-gorilla.

%prep
%setup -q -n Gorilla

%build
# xmms section
cd xmms/ximian-south
tar cf - * | bzip2 -c > ../../XimianSouth.tar.bz2
cd -

# nautilus section
cd nautilus/ScalableGorilla
mv ../ScalableGorilla.xml .
cd -

# sawfish section
cd sawfish/gorilla
rm -rf CVS
cd -

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_xmmsskinsdir},%{_pixmapsdir}/nautilus,%{_datadir}/sawfish/themes}

install XimianSouth.tar.bz2 $RPM_BUILD_ROOT%{_xmmsskinsdir}
mv nautilus/ScalableGorilla $RPM_BUILD_ROOT%{_pixmapsdir}/nautilus
mv sawfish/gorilla $RPM_BUILD_ROOT%{_datadir}/sawfish/themes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# there is some tool for multi theme applying, but it requres gnome2, so
# this package is just to install all below packages

%files -n xmms-skin-XimianSouth
%defattr(644,root,root,755)
%{_xmmsskinsdir}/XimianSouth.tar.bz2

%files -n nautilus-theme-gorilla
%defattr(644,root,root,755)
%{_pixmapsdir}/nautilus/ScalableGorilla

%files -n sawfish-theme-gorilla
%defattr(644,root,root,755)
%{_datadir}/sawfish/themes/gorilla
