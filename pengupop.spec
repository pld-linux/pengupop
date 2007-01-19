Summary:	Clone of the game Bust a Move
Summary(pl):	Klon gry Bust a Move
Name:		pengupop
Version:	2.2.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://www.junoplay.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	afcf595c8450be3e25b6775e4013f454
Patch0:		%{name}-desktop.patch
URL:		http://www.junoplay.com/
BuildRequires:	SDL-devel >= 1.2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The aim of this game is to shoot colored balls so they form similarily
colored groups, causing them to fall out of the screen. You can either
win by clearing your entire field, or lose if any balls attach below
the white line near the bottom.

%description -l pl
Celem tej gry jest strzelanie kolorowymi pi³kami tak, aby utworzy³y
one jednokolorowe grupy, które znikaj± z ekranu. Aby wygraæ nale¿y
wyczy¶ciæ ca³e pole z pi³ek, natomiast gracz przegrywa, gdy jedna z
pi³ek przekroczy bia³± liniê na dole ekranu.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}
install %{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
