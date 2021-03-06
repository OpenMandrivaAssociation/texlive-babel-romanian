# revision 30285
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-babel-romanian
Version:	1.2l
Release:	2
Summary:	TeXLive babel-romanian package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-romanian.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-romanian.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-romanian.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive babel-romanian package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/babel-romanian/romanian.ldf
%doc %{_texmfdistdir}/doc/generic/babel-romanian/romanian.pdf
#- source
%doc %{_texmfdistdir}/source/generic/babel-romanian/romanian.dtx
%doc %{_texmfdistdir}/source/generic/babel-romanian/romanian.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
