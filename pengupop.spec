Summary:	Clone of the game Bust a Move
Summary(pl):	Klon gry Bust a Move
Name:		pengupop
Version:	2.1.8
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://www.junoplay.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	9ee4366168973228d4790fd60e624f90
URL:		http://www.junoplay.com/
BuildRequires:	SDL-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The aim of this game is to shoot colored balls so they form similarily
colored groups, causing them to fall out of the screen. You can either
win by clearing your entire field, or lose if any balls attach below
the white line near the bottom.

%description -l pl
Celem tej gry jest strzelanie kolorowymi pi�kami tak, aby utworzy�y
one jednokolorowe grupy, kt�re znikaj� z ekranu. Aby wygra� nale�y
wyczy�ci� ca�e pole z pi�ek, natomiast gracz przegrywa, gdy jedna z
pi�ek przekroczy bia�� lini� na dole ekranu.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*