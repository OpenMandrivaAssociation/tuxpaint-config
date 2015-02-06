Summary:	Pictures for use with the paint program Tuxpaint
Name: 		tuxpaint-config
Version:	0.0.12
Release:	6
License:	GPL
Group:		Graphics
URL:		http://sourceforge.net/projects/tuxpaint
Source:		%{name}-%{version}.tar.bz2
Patch0:		tuxpaint-config-0.0.12-locale.patch
BuildRequires:	desktop-file-utils
BuildRequires:	fltk-devel
BuildRequires:	libpaper-devel
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(pixman-1)
Requires:	tuxpaint

%description
Tux Paint Config is a graphical configuration tool for "Tux Paint."
It provides a point-and-click interface that allows parents and teachers
to alter Tux Paint's behavior -- disable sound effects, run in
full-screen mode, etc. - without needing to manipulate a text-based
configuration file.

%prep
%setup -q
%patch0 -p1

%build
make OPTFLAGS="%{optflags}" PREFIX=%{_prefix} LIBDIR=%{_libdir}

%install
mkdir -p %{buildroot} %{buildroot}%{_bindir}
make install BUILDPREFIX="%{buildroot}" PKG_ROOT="%{buildroot}" PREFIX="%{buildroot}%{_usr}" X11_ICON_PREFIX="%{buildroot}%{_includedir}/X11/pixmaps/" LIBDIR="%{buildroot}%{_libdir}"

install -m644 data/images/icon16x16.png -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 data/images/icon32x32.png -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 data/images/icon48x48.png -D %{buildroot}%{_liconsdir}/%{name}.png

#Fix perms:
chmod -R go+r docs/

%find_lang %{name}

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install	--vendor="" \
			--dir %{buildroot}%{_datadir}/applications \
			--remove-category="Settings" \
			--add-category="Education" \
			src/tuxpaint-config.desktop

# fix perms
chmod -R go=u-w %{buildroot}/*

%files -f %{name}.lang
%defattr(755,root,root,755)
%{_bindir}/%{name}
%doc docs/AUTHORS.txt docs/CHANGES.txt docs/COPYING.txt docs/README.txt docs/TODO.txt docs/html/README.html
%{_mandir}/man1/%{name}.*
%{_includedir}/X11/pixmaps/%{name}.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*
%{_datadir}/%{name}/images/*
%{_miconsdir}/*.png
%{_iconsdir}/*.png
%{_liconsdir}/*.png


%changelog
* Thu Mar 17 2011 Angelo Naselli <anaselli@mandriva.org> 0.0.12-4mdv2011.0
+ Revision: 646254
- Added missing icon

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0.12-3mdv2011.0
+ Revision: 615277
- the mass rebuild of 2010.1 packages

* Tue Jan 12 2010 Angelo Naselli <anaselli@mandriva.org> 0.0.12-2mdv2010.1
+ Revision: 490252
- fixed requirements for X86_64
- fixed url
- import tuxpaint-config


