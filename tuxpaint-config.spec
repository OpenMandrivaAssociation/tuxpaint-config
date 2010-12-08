Summary:	Pictures for use with the paint program Tuxpaint
Name: 		tuxpaint-config
Version:	0.0.12
Release:	%mkrel 3
License:	GPL
Source: 	%{name}-%{version}.tar.bz2

Group:		Graphics
URL:		http://sourceforge.net/projects/tuxpaint
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: 	tuxpaint
BuildRequires:  fltk-devel libpaper-devel


%description
Tux Paint is a simple paint program gear towards young children. 
It provides a simple but entertaining interface, allows drawing
with brushes, lines, shapes, and 'stamps,' and has a 'magic' 
tool, for special effects. Loading and saving is done via a 
graphical interface, and the underlying environment's 
filesystem isn't exposed (much like programs on PDAs).

This packages contains a lot of extra pictures (stamps) for tuxpaint.

%prep
%setup -q

%build
make OPTFLAGS="%{optflags}" PREFIX=%{_prefix} LIBDIR=%{_libdir}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot} %{buildroot}%{_bindir}  
make install BUILDPREFIX="%{buildroot}" PKG_ROOT="%{buildroot}" PREFIX="%{buildroot}%{_usr}" X11_ICON_PREFIX="%{buildroot}%{_includedir}/X11/pixmaps/" LIBDIR="%{buildroot}%{_libdir}"

install -m644 data/images/icon16x16.png -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 data/images/icon32x32.png -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 data/images/icon48x48.png -D %{buildroot}%{_liconsdir}/%{name}.png

#Fix perms:
chmod -R go+r docs/

%find_lang %{name}

# fix perms
chmod -R go=u-w $RPM_BUILD_ROOT/*

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(755,root,root,755)
%{_bindir}/%{name}
%doc docs/AUTHORS.txt docs/CHANGES.txt docs/COPYING.txt docs/README.txt docs/TODO.txt docs/html/README.html
%_mandir/man1/%{name}.*
%{_includedir}/X11/pixmaps/%{name}.*
%{_datadir}/pixmaps/*
%{_datadir}/%{name}/images/*
%{_miconsdir}/*.png
%{_iconsdir}/*.png
%{_liconsdir}/*.png
