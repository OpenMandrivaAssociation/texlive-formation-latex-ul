%global tl_name formation-latex-ul
%global tl_revision 70507

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2024.03
Release:	%{tl_revision}.1
Summary:	Introductory LaTeX course in French
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/formation-latex-ul
License:	cc-by-4
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/formation-latex-ul.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/formation-latex-ul.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/formation-latex-ul.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package contains the supporting documentation, slides, exercise
files, and templates for an introductory LaTeX course (in French)
prepared for Universite Laval, Quebec, Canada.

