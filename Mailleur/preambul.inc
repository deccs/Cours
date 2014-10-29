% sortie ECRAN PDF
\usepackage{ifpdf}
\usepackage{graphics}
%
\ifpdf
  \usepackage[pdftex,designiii,french,navibar,tight]{web}
  \DeclareGraphicsExtensions{.png,.jpg,.mps,.pdf}
  % couleur du fond et couleur du texte (rouge)
  \definecolor{red}{rgb}{0.0,0.0,0.0}
\else
  \DeclareGraphicsExtensions{.eps,.ps,.pst}
  %\usepackage{html}
  % pas utilisation de hyperref
  %\def\href#1#2{\htmladdnormallink{#2}{#1}}
  \usepackage{hyperref}
  %\definecolor{mycolorfond}{rgb}{1.0,1.0,1.0}
  %\definecolor{red}{rgb}{1.0,1.0,1.0}
  % entete
  \usepackage{fancyhdr}
  \pagestyle{fancyplain}
  %\fancyhead{}
  \fancyhead[RE,LO]{\bf\large\thepage} 
  %\fancyhead[LE,RO]{\it Chapitre \thechapter}
  \fancyfoot{}
  \fancyfoot[LE,LO]{\small\it Marc BUFFAT, UFR Mécanique, UCBLyon}
\fi
% package
\usepackage{color}
\usepackage{fancybox}
% Macro couleur
\def\B#1{\color {blue}#1 \color {black}} 
\def\V#1{\color {green}#1 \color {black}}
\def\R#1{\color {red}#1 \color {black}}
% Index
\usepackage{makeidx}
\makeindex
% Paragraphe en couleur
\usepackage{color,calc}
% Macros
\newenvironment{tscreen}%
 {\begin{quote}\bgroup\small\tt}%
 {\egroup\end{quote}} 
\newcommand{\cparam}[1]{{\rm \lbr{\sl #1}\rbr}}  
\newcommand{\st}{\small\tt}             % Small typewriter -- comes in handy.
\newcommand{\lb}{{\tt\char '173}}       % Left Brace '{'
\newcommand{\rb}{{\tt\char '175}}       % Right Brace '}'
\newcommand{\lbr}{$\langle$}            % Left Bracket '<'
\newcommand{\rbr}{$\rangle$}            % Right Bracket '>'
\newcommand{\bs}{{\tt\char '134}}       % BackSlash '\'
% Listing
% package listing version 1.0 !!!!
\usepackage{listings}

