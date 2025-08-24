Summary:	Purple Plugin Pack
Summary(pl.UTF-8):	Zestaw wtyczek do komunikatorów opartych na Purple
Name:		libpurple-plugin-pack
Version:	2.8.0
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	https://downloads.sourceforge.net/pidgin/purple-plugin-pack-%{version}.tar.xz
# Source0-md5:	6db3f96379c9e5f3f8a7fc06bbdbffe1
URL:		https://keep.imfreedom.org/pidgin/purple-plugin-pack
BuildRequires:	cairo-devel
BuildRequires:	enchant2-devel
BuildRequires:	finch-devel
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	gtkspell-devel >= 2.0.2
BuildRequires:	json-glib-devel
BuildRequires:	libgnt-devel
BuildRequires:	libpurple-devel >= 2
BuildRequires:	meson
BuildRequires:	ninja >= 1.5
BuildRequires:	pango-devel
BuildRequires:	pidgin-devel >= 2
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A collection of plugins for purple-based clients such as Pidgin.

%description -l pl.UTF-8
Zbiór wtyczek dla opartych na purple klientów komunikatorów, takich
jak Pidgin.

%package -n pidgin-plugin-pack
Summary:	Pidgin Plugin Pack
Summary(pl.UTF-8):	Zestaw wtyczek dla komunikatora Pidgin
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	pidgin >= 2

%description -n pidgin-plugin-pack
A collection of plugins for Pidgin.

%description -n pidgin-plugin-pack -l pl.UTF-8
Zbiór wtyczek dla komunikatora Pidgin.

%prep
%setup -q -n purple-plugin-pack-%{version}

%build
%meson \
	-Dtypes=all

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%{__mv} $RPM_BUILD_ROOT%{_localedir}/{es_ES,es}

%find_lang plugin_pack

%clean
rm -rf $RPM_BUILD_ROOT

%files -f plugin_pack.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.md
%attr(755,root,root) %{_libdir}/purple-2/autoreply.so
%attr(755,root,root) %{_libdir}/purple-2/bash.so
%attr(755,root,root) %{_libdir}/purple-2/capsnot.so
%attr(755,root,root) %{_libdir}/purple-2/colorize.so
%attr(755,root,root) %{_libdir}/purple-2/dewysiwygification.so
%attr(755,root,root) %{_libdir}/purple-2/dice.so
%attr(755,root,root) %{_libdir}/purple-2/eight_ball.so
%attr(755,root,root) %{_libdir}/purple-2/flip.so
%attr(755,root,root) %{_libdir}/purple-2/google.so
%attr(755,root,root) %{_libdir}/purple-2/groupmsg.so
%attr(755,root,root) %{_libdir}/purple-2/highlight.so
%attr(755,root,root) %{_libdir}/purple-2/ignore.so
%attr(755,root,root) %{_libdir}/purple-2/irc-more.so
%attr(755,root,root) %{_libdir}/purple-2/irchelper.so
%attr(755,root,root) %{_libdir}/purple-2/listhandler.so
%attr(755,root,root) %{_libdir}/purple-2/ning.so
%attr(755,root,root) %{_libdir}/purple-2/okcupid.so
%attr(755,root,root) %{_libdir}/purple-2/oldlogger.so
%attr(755,root,root) %{_libdir}/purple-2/omegle.so
%attr(755,root,root) %{_libdir}/purple-2/showoffline.so
%attr(755,root,root) %{_libdir}/purple-2/simfix.so
%attr(755,root,root) %{_libdir}/purple-2/slashexec.so
%attr(755,root,root) %{_libdir}/purple-2/snpp.so
%attr(755,root,root) %{_libdir}/purple-2/splitter.so
%attr(755,root,root) %{_libdir}/purple-2/sslinfo.so
%attr(755,root,root) %{_libdir}/purple-2/translate.so
%attr(755,root,root) %{_libdir}/purple-2/xmppprio.so
%{_datadir}/metainfo/purple-plugin-pack.metainfo.xml

%files -n pidgin-plugin-pack
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pidgin/album.so
%attr(755,root,root) %{_libdir}/pidgin/blistops.so
%attr(755,root,root) %{_libdir}/pidgin/convbadger.so
%attr(755,root,root) %{_libdir}/pidgin/difftopic.so
%attr(755,root,root) %{_libdir}/pidgin/enhancedhist.so
%attr(755,root,root) %{_libdir}/pidgin/gRIM.so
%attr(755,root,root) %{_libdir}/pidgin/icon-override.so
%attr(755,root,root) %{_libdir}/pidgin/irssi.so
%attr(755,root,root) %{_libdir}/pidgin/lastseen.so
%attr(755,root,root) %{_libdir}/pidgin/listlog.so
%attr(755,root,root) %{_libdir}/pidgin/mystatusbox.so
%attr(755,root,root) %{_libdir}/pidgin/nicksaid.so
%attr(755,root,root) %{_libdir}/pidgin/plonkers.so
%attr(755,root,root) %{_libdir}/pidgin/schedule.so
%attr(755,root,root) %{_libdir}/pidgin/sepandtab.so
%attr(755,root,root) %{_libdir}/pidgin/switchspell.so
%attr(755,root,root) %{_libdir}/pidgin/timelog.so
%{_pixmapsdir}/pidgin/protocols/*/okcupid.png
