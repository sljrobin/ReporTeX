%% 'reportex.cls'
%% A class for easily creating LaTeX reports
%% by Simon L. J. Robin
%% sljrobin@gmail.com
\LoadClass[a4paper,12pt]{report}
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{reportex}[2014/10/07 A class for easily creating LaTeX reports]


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  PACKAGES  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% PDF Information
\RequirePackage[% Add information and create hyperlinks within the document
  % PDF properties
  pdftitle={\pdfTitle},        % Title
  pdfauthor={\pdfAuthor},      % Author
  pdfcreator={\pdfCreator},    % Creator
  pdfkeywords={\pdfKeywords},  % Keywords
  % Links
  colorlinks=true,             % Colored links
  linkcolor=rptxBlue,          % Internal links
  urlcolor=cyan,               % Web links
  citecolor=green,             % Bibliography links
  filecolor=magenta,           % File links
]{hyperref}

%%% Colors
\RequirePackage[% Add colors
  svgnames,     % 150 colors
  table         % Add colors to tables
]{xcolor}

%%% Formatting
\RequirePackage[T1]{fontenc}         % T1 encoding
\RequirePackage{charter}             % Main font
\RequirePackage[expert]{mathdesign}  % Computer Modern font for maths
\RequirePackage{upgreek}             % Greek characters
\RequirePackage{titlesec}            % Style of headers
\RequirePackage{sectsty}             % Style of headers
\RequirePackage[                     % Style of Table of Contents
  subfigure  % Avoid conflict with '\setcounter'
]{tocloft}
\RequirePackage[                     % Text general appearance
  activate={     % Protrusion and Expansion
    true,
    nocompatibility},
  kerning=true,  % Kerning
  factor=1100,   % Add 10% to the protrusion amount
  final,         % Enable microtype
  spacing=true,  % Spacing
  shrink=10,     % Reduce shrinkability
  stretch=10,    % Reduce stretchability
  tracking=true  % Tracking
]{microtype}
\RequirePackage{subfigure}           % Figures and Tables inclusions

%%% Miscellaneous
\RequirePackage[utf8]{inputenc}      % Special characters
\RequirePackage{graphicx}            % Images
\RequirePackage{mathtools}           % Maths
\RequirePackage{listings}            % Source codes


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  PATHS  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\pathReport}{./report}                    % Report
\newcommand{\pathChapters}{\pathReport/chapters}      % Chapters
\newcommand{\pathComponents}{\pathReport/components}  % Components
\newcommand{\pathMaterials}{\pathReport/materials}    % Materials
\newcommand{\pathCodes}{\pathMaterials/codes}         % Codes
\newcommand{\pathImages}{\pathMaterials/images}       % Images


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  COMMANDS  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% code -- '\code[a_line_of_code]'; print a line of code with the \texttt command
\newcommand{\code}[1][]{\texttt{#1}}

%%% img -- '\img[textwidth]{picture_name}'; print a picture
\newcommand{\img}[2][]{\includegraphics[width=#1\textwidth]{\pathImages/#2}}

%%% sep -- '\sep'; horizontal rule
\newcommand{\sep}{\rule{\linewidth}{0.5mm}}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  STYLE  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% Colors
\definecolor{rptxBlue}{HTML}{08087B}

%%% Listings
%% C
\lstset{                                         % Code style
  belowcaptionskip=1\baselineskip,               % Space after caption
  backgroundcolor=\color{white},                 % Background color
  basicstyle=\footnotesize\ttfamily,             % Font size
  breaklines=true,                               % Automatic line breaking
  captionpos=b,                                  % Caption-position to bottom
  commentstyle=\itshape\color{purple!40!black},  % Comment style
  extendedchars=true,                            % Use non-ASCII characters
  frame=L,                                       % Frame around the code
  identifierstyle=\color{red},                   % Identifiers
  keepspaces=true,                               % Keeps spaces in text
  keywordstyle=\bfseries\color{green!40!black},  % Keywords style
  language=C,                                    % Language
  literate=*{0}{{\textcolor{blue}{0}}}{1}%       % Coloring numbers
            {1}{{\textcolor{blue}{1}}}{1}%
            {2}{{\textcolor{blue}{2}}}{1}%
            {3}{{\textcolor{blue}{3}}}{1}%
            {4}{{\textcolor{blue}{4}}}{1}%
            {5}{{\textcolor{blue}{5}}}{1}%
            {6}{{\textcolor{blue}{6}}}{1}%
            {7}{{\textcolor{blue}{7}}}{1}%
            {8}{{\textcolor{blue}{8}}}{1}%
            {9}{{\textcolor{blue}{9}}}{1}%
            {.0}{{\textcolor{blue}{.0}}}{1}%
            {.1}{{\textcolor{blue}{.1}}}{1}%
            {.2}{{\textcolor{blue}{.2}}}{1}%
            {.3}{{\textcolor{blue}{.3}}}{1}%
            {.4}{{\textcolor{blue}{.4}}}{1}%
            {.5}{{\textcolor{blue}{.5}}}{1}%
            {.6}{{\textcolor{blue}{.6}}}{1}%
            {.7}{{\textcolor{blue}{.7}}}{1}%
            {.8}{{\textcolor{blue}{.8}}}{1}%
            {.9}{{\textcolor{blue}{.9}}}{1}%
            {\ }{{ }}{1},% Handle the space
  morekeywords={},                               % Additional keywords
  numbers=left,                                  % Line-numbers
  numbersep=10pt,                                % Distance between line-numbers and the code
  numberstyle=\scriptsize\color{gray},           % Line-numbers style
  rulecolor=\color{black},                       % Rule color
  showstringspaces=false,                        % Underline spaces within strings only
  showtabs=false,                                % Show tab characters
  stepnumber=1,                                  % Step between two line-numbers
  stringstyle=\color{orange},                    % String literal style
  xleftmargin=\parindent,                        % Left margin
  xrightmargin=\parindent,                       % Right margin
  tabsize=2,                                     % Default tabsize
  title=\lstname                                 % Print name if caption field empty
}

%%% Headers
%% Title style
\chapterfont{
  \usefont{T1}  % Type1 encoding
          {qhv} % qhv font family
          {b}   % Bold
          {n}   % Shape
          \selectfont\huge
}

%% Section style
\titleformat{\section}[hang]{
  \usefont{T1}  % Type1 encoding
          {qhv} % qhv font family
          {b}   % Bold
          {n}   % Shape
          \selectfont
}
{}              % Label
{0em}           % Space between label and title body
{\hspace{-0.4pt}\Large \thesection\hspace{0.6em}}  % Code preceding the title

%% Table of Contents
% ToC title
\renewcommand{\cfttoctitlefont}{
  \usefont{T1}  % Type1 encoding
          {qhv} % qhv font family
          {b}   % Bold
          {n}   % Shape
          \selectfont\huge
}
% ToC Chapter titles
\renewcommand{\cftchapfont}{
  \usefont{T1}  % Type1 encoding
          {qhv} % qhv font family
          {b}   % Bold
          {n}   % Shape
          \selectfont
}          
% ToC Section titles
\renewcommand{\cftsecfont}{
  \usefont{T1}  % Type1 encoding
          {bch} % bch font family
          {m}   % Medium
          {n}   % Shape
          \selectfont
}
% Toc Subsection titles
\renewcommand{\cftsubsecfont}{
  \usefont{T1}  % Type1 encoding
          {bch} % bch font family
          {m}   % Medium
          {n}   % Shape
          \selectfont
}
% Chapter page numbers
\renewcommand{\cftchappagefont}{
  \usefont{T1}  % Type1 encoding
          {bch} % bch font family
          {b}   % Bold
          {n}   % Shape
          \selectfont
}
% Section page numbers
\renewcommand{\cftsecpagefont}{\cftsecfont}
% Subsection page numbers
\renewcommand{\cftsubsecpagefont}{\cftsubsecfont}
             
%% Section & Subsection
\setcounter{tocdepth}{2}  % Print subsection in Table of contents

%% List of Figures
\renewcommand{\cftloftitlefont}{
  \usefont{T1}  % Type1 encoding
          {qhv} % qhv font family
          {b}   % Bold
          {n}   % Shape
          \selectfont\huge
}

%%% Typography
%% Protusion
\SetProtrusion{
  encoding={*},
  family={bch},
  series={*},
  size={6,7}
}
{1={ ,750},
 2={ ,500},
 3={ ,500},
 4={ ,500},
 5={ ,500},
 6={ ,500},
 7={ ,600},
 8={ ,500},
 9={ ,500},
 0={ ,500}
}

%% Kerning
% Titles
\SetExtraKerning[unit=space]{
  encoding={*},
  family={qhv},
  series={b},
  size={
    large,
    Large}
}
{1={-200,-200}, 
 \textendash={400,400}
}

% Miscellaneous
\SetExtraKerning[unit=space]{
  encoding={*},
  family={bch},
  series={*},
  size={
    footnotesize,
    small,
    normalsize
  }
}
{\textendash={400,400},       % En-dash, add more space around it
 "28={ ,150},                 % Left bracket, add space from right
 "29={150, },                 % Right bracket, add space from left
 \textquotedblleft={ ,150},   % Left quotation mark, space from right
 \textquotedblright={150, }   % Right quotation mark, space from left
}

%% Tracking
\SetTracking{                 % Space for small capitals%
  encoding={*},
  shape=sc
}{40}