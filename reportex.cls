%% 'reportex.cls'
%% A class for easily creating LaTeX reports
%% by Simon L. J. Robin
%% sljrobin@gmail.com
\LoadClass[a4paper,12pt]{report}
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{reportex}[2014/10/07 A class for easily creating LaTeX reports]


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  PROPERTIES  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Report properties
\newcommand{\reportTitle}{Title}  % Report title
\newcommand{\reportSubtitle}{Subitle}  % Report subtitle
\newcommand{\reportAuthor}{John Smith}  % Report author
\newcommand{\reportCompany}{Company}  % Report company
\newcommand{\reportDate}{dd/mm/yyyy}  % Report date

%% PDF properties
\newcommand{\pdfTitle}{\reportTitle}    % PDF title
\newcommand{\pdfAuthor}{\reportAuthor}  % PDF author
\newcommand{\pdfCreator}{}              % PDF creator
\newcommand{\pdfKeywords}{}             % PDF keywords


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  PACKAGES  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% PDF Information
\RequirePackage[% Add information and create hyperlinks within the document
  % PDF properties
  pdftitle={\pdfTitle},        % Title
  pdfauthor={\pdfAuthor},      % Author
  pdfcreator={\pdfCreator},    % Creator
  pdfkeywords={\pdfKeywords},  % Keywords
  % Links
  colorlinks=true,             % Colored links
  linkcolor=red,               % Internal links
  urlcolor=cyan,               % Web links
  citecolor=green,             % Bibliography links
  filecolor=magenta,           % File links
]{hyperref}

%% Colors
\RequirePackage[% Add colors
  svgnames,     % 150 colors
  table         % Add colors to tables
]{xcolor}

%% Miscellaneous
\RequirePackage[utf8]{inputenc}  % Special characters
\RequirePackage{graphicx}        % Images
\RequirePackage{mathtools}       % Maths
\RequirePackage{listings}        % Codes


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  PATHS  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\pathReport}{./report}                    % Report
\newcommand{\pathChapters}{\pathReport/chapters}      % Chapters
\newcommand{\pathComponents}{\pathReport/components}  % Components
\newcommand{\pathMaterials}{\pathReport/materials}    % Materials
\newcommand{\pathCodes}{\pathMaterials/codes}         % Codes
\newcommand{\pathImages}{\pathMaterials/images}       % Images


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  COMMANDS  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% code -- '\code[a_line_of_code]'; print a line of code with the \texttt command
\newcommand{\code}[1][]{\texttt{#1}}

%% img -- '\img[textwidth]{picture_name}'; print a picture
\newcommand{\img}[2][]{\includegraphics[width=#1\textwidth]{\pathImages/#2}}

%% sep -- '\sep'; horizontal rule
\newcommand{\sep}{\rule{\linewidth}{0.5mm}}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  STYLE  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Listings
\lstset{                  % Code style
  language=C,
  basicstyle=\footnotesize\ttfamily,
  numbers=left,
  numberstyle=\footnotesize,
  numbersep=5pt,
  backgroundcolor=\color{gray!05},
  frame=single,
  tabsize=2,
  captionpos=b,      % TODO to check!
  breaklines=true,
  morecomment=[l]{//}{/*}
}

%% Sections & Subsections
\setcounter{tocdepth}{2}  % Print subsection in Table of contents