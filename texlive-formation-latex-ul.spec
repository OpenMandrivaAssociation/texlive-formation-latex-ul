Name:		texlive-formation-latex-ul
Version:	56714
Release:	2
Summary:	Introductory LaTeX course in French
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/formation-latex-ul
License:	cc-by-4
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/formation-latex-ul.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/formation-latex-ul.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/formation-latex-ul.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package contains the supporting documentation, slides,
exercise files, and templates for an introductory LaTeX course
(in French) prepared for Universite Laval, Quebec, Canada.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/formation-latex-ul
%doc %{_texmfdistdir}/doc/latex/formation-latex-ul

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
