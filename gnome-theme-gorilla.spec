Summary:	Gorilla theme
Summary(pl):	Temat gorilla
Name:		gnome-theme-gorilla
Version:	1.0
Release:	1
License:	Free
Group:		X11/Amusements
Source0:	http://www.lucidus.uklinux.net/metathemes/Gorilla.metatheme.tar.gz
URL:		http://sunshineinabag.co.uk/
BuildRequires:	tar
BuildRequires:	bzip2
BuildRequires:	xmms-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	xmms-skin-XimianSouth
Requires:	gtk-theme-ThinIce
Requires:	nautilus-theme-gorilla
Requires:	sawfish-theme-gorilla

%define		_prefix		/usr/X11R6
%define		_xmmsskinsdir	%(xmms-config --data-dir)/Skins

%description
Gorilla theme for GTK (ThinIce), Nautilus, Sawfish and XMMS (Ximian
South).

%description -l pl
Temat gorilla dla GTK (ThinIce), Nautilusa, Sawfisza i XMMS-a (Ximian
South).

%package -n xmms-skin-XimianSouth
Summary:	Ximian South skin
Summary(pl):	Skórka Ximian South
Group:		X11/Amusements
Requires:	tar
Requires:	bzip2
Requires:	xmms

%description -n xmms-skin-XimianSouth
Ximian South skin. You may be interested in gnome-theme-gorilla
package.

%description -n xmms-skin-XimianSouth -l pl
Skórka Ximian South. Mo¿na te¿ spróbowaæ pakietu gnome-theme-gorilla.

%package -n nautilus-theme-gorilla
Summary:	Gorilla theme
Summary(pl):	Temat gorilla
Group:		X11/Amusements
Requires:	nautilus

%description -n nautilus-theme-gorilla
Gorilla theme. You may be interested in gnome-theme-gorilla package.
Note: It is highly cpu intensive.

%description -n nautilus-theme-gorilla -l pl
Temat gorilla. Mo¿na te¿ spróbowaæ pakietu gnome-theme-gorilla. Uwaga:
Wymaga szybkiego procesora.

%package -n sawfish-theme-gorilla
Summary:	Gorilla theme
Summary(pl):	Temat gorilla
Group:		X11/Amusements
Requires:	sawfish

%description -n sawfish-theme-gorilla
Gorilla theme. You may be interested in gnome-theme-gorilla package.

%description -n sawfish-theme-gorilla -l pl
Temat gorilla. Mo¿na te¿ spróbowaæ pakietu gnome-theme-gorilla.

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
