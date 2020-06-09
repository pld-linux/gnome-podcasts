Summary:	Podcasts player for GNOME
Summary(pl.UTF-8):	Odtwarzacz podcastów dla GNOME
Name:		gnome-podcasts
Version:	0.4.7
Release:	1
License:	GPL v3
Group:		X11/Applications/Multimedia
Source0:	https://gitlab.gnome.org/World/podcasts/uploads/90c4f40f529ff91dabac5d7cbbc0f5ed/%{name}-%{version}.tar.xz
# Source0-md5:	a29a9b348e5538f9fdd3c3b8892b69ae
URL:		http://wiki.gnome.org/Apps/Podcasts
BuildRequires:	gstreamer-devel >= 1.12
BuildRequires:	gtk+3-devel >= 3.22
BuildRequires:	libhandy-devel
BuildRequires:	meson
BuildRequires:	ninja
BuildRequires:	rust >= 1.27
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.26.0
Requires(post,postun):	gtk-update-icon-cache
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Podcasts is a podcasts player for GNOME.

%description -l pl.UTF-8
GNOME Podcasts to odtwarzacz podcastów dla GNOME.

%prep
%setup -q

%build
%meson build
%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang org.gnome.Podcasts --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f org.gnome.Podcasts.lang
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/gnome-podcasts
%{_datadir}/metainfo/org.gnome.Podcasts.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.Podcasts.gschema.xml
%{_desktopdir}/org.gnome.Podcasts.desktop
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Podcasts-symbolic.svg
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Podcasts.svg
%{_datadir}/dbus-1/services/org.gnome.Podcasts.service
