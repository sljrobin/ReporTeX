%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% `reportex.cls`

%    1. LAYOUT
%    2. TYPOGRAPHY
%    3. GRAPHICS
%    4. TABLES
%    5. ELEMENTS
%    6. REPORTEX
%        - Paths
%        - Commands


\LoadClass[
  a4paper,  % A4 paper
  oneside   % Side
]{report}
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{reportex}[2014/10/07 A class for easily creating LaTeX reports]

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%-----------------------------------------------------------------------------------------------------------------------
%    1. LAYOUT
%-----------------------------------------------------------------------------------------------------------------------
%%% Margins
\RequirePackage[
  DIV=14,            % Type area dimensions (in mm; width: 165.00, height: 233.36, top: 21.21, inner: 15.00)
  BCOR=2mm,          % Binding correction
  headinclude=true,  % Include the header line to compute the type area
  footinclude=false  % Not include the footer line to compute the type area
]{typearea}

\RequirePackage[% Dimensions for page layout
    a4paper,
    width=150mm,
    top=25mm,
    bottom=25mm,
]{geometry}

\RequirePackage{emptypage} % Suppress page numbers and headings on empty pages

%%% Header and Footer
\RequirePackage{fancyhdr}                                                          % Style of headers/footers
% Header
\pagestyle{fancy}                                                                  % Use the "fancy" page style to implement a new header
\renewcommand{\chaptermark}[1]{                                                    % Chapter model: `Chapter X. Title`
  \markboth{\usefont{T1}{qhv}{m}{n}\selectfont \chaptername\ \thechapter.\ #1}{}} 
\renewcommand{\sectionmark}[1]{                                                    % Section model: `X.Y Title`
  \markright{\usefont{T1}{qhv}{m}{n}\selectfont \thesection\ #1}{}}
\renewcommand{\headrulewidth}{0.5pt}                                               % Width of the head rule
\fancyhead{}                                                                       % Header reinitialization
\fancyhead[L]{\leftmark}                                                           % Chapter
\fancyhead[R]{\thepage}                                                            % Page number
% Footer
\fancyfoot{}                                                                       % Empty footer


%-----------------------------------------------------------------------------------------------------------------------
%    2. TYPOGRAPHY
%-----------------------------------------------------------------------------------------------------------------------
%%% Encoding
\RequirePackage[T1]{fontenc}                                               % Encoding
\RequirePackage[utf8]{inputenc}                                            % Encoding
\RequirePackage[english]{babel}                                            % Language
\RequirePackage[none]{hyphenat}                                            % Hyphenation

%%% Fonts
\RequirePackage{charter}                                                   % Main font: `Charter BT`
\RequirePackage[expert]{mathdesign}                                        % Maths font: `Computer Modern`
\RequirePackage{inconsolata}                                               % Code font: `Inconsolata`
\newcommand*\justify{                                                      % `\justify` command: justify text with `\texttt{}`
    \fontdimen2\font=0.4em % Interword space
    \fontdimen3\font=0.2em % Interword search
    \fontdimen4\font=0.1em % Interword shrink
    \fontdimen7\font=0.1em % Extra space
    \hyphenchar\font=`\-   % Allowing hyphenation
}
\newcommand{\rptxTt}[1]{\texttt{\justify #1}}                              % `rptxTt`: create a justified line of code

%%% Maths
\RequirePackage[version=3]{mhchem}                                         % Write chemistry equations
\RequirePackage{xfrac}                                                     % Write slanted fractions

%%% Titles
\RequirePackage{sectsty}                                                   % Use different font for header titles
\RequirePackage{titlesec}                                                  % Alternative header titles

% Part
% Part
\def\hrulePart{\leavevmode\leaders\hrule height 2pt\hfill\kern\z@}         % New \hrule for Part
\partfont{\usefont{T1}{qhv}{b}{n}\selectfont\Huge}                         % Use a different font
\newcommand{\rptxPart}[3]{                                                 % `rptxPart`: add a Part with a text
  \part[#1]{\begin{center}#2\end{center}                                   %   [1] : Title in ToC     
    \begin{minipage}[l]{1\textwidth}                                       %   [2] : Title in Body
      \hrulePart\newline\vspace{1ex}\newline                               %   [3] : Text after the Part title
      \normalsize{\textnormal{#3}}
    \end{minipage}
  }
}

% Chapter
\titleformat{\chapter}[display]{
    \usefont{T1}{qhv}{b}{n}\selectfont\huge}
    {\chaptertitlename\ \thechapter}{20pt}{\huge}
    [\vspace{1ex}{\titlerule[2pt]}]

% Section
\titleformat{\section}[hang]{
    \usefont{T1}{qhv}{b}{n}\selectfont}
    {}{0em}{\hspace{-0.4pt}\Large \thesection\hspace{0.6em}}[]
    
% Subsection
\titleformat{\subsection}[hang]{
    \usefont{T1}{qhv}{b}{n}\selectfont}
    {}{0em}{\hspace{-0.4pt}\large \thesubsection\hspace{0.6em}}[]

% Subsubsection
\titleformat{\subsubsection}[hang]{
    \usefont{T1}{qhv}{b}{n}\selectfont}
    {}{0em}{\hspace{-0.4pt}\normalsize \thesubsubsection\hspace{0.6em}}[]

% Paragraph
\newcommand{\rptxParagraph}[1]{\paragraph{#1}\mbox{}\vspace*{3pt}\newline}


\RequirePackage[                     % Text general appearance
  activate={true, nocompatibility},      % Protrusion and Expansion
  kerning=true,  % Kerning
  factor=1100,   % Add 10% to the protrusion amount
  final,         % Enable microtype
  spacing=true,  % Spacing
  shrink=10,     % Reduce shrinkability
  stretch=10,    % Reduce stretchability
  tracking=true  % Tracking
]{microtype}

%% Tracking
\SetTracking{encoding=*, shape=sc}{40}

%% Protusion
\SetProtrusion{
  encoding={*},
  family={bch},
  series={*},
  size={6,7}
}{1={ ,750}, 2={ ,500}, 3={ ,500}, 4={ ,500}, 5={ ,500},
  6={ ,500}, 7={ ,600}, 8={ ,500}, 9={ ,500}, 0={ ,500}}
  
% Miscellaneous
\SetExtraKerning[unit=space]{
  encoding={*},
  family={bch},
  series={*},
  size={footnotesize, small, normalsize}
}{\textendash={400,400},       % En-dash, add more space around it
  "28={ ,150},                 % Left bracket, add space from right
  "29={150, },                 % Right bracket, add space from left
  \textquotedblleft={ ,150},   % Left quotation mark, space from right
  \textquotedblright={150, }   % Right quotation mark, space from left
}



\RequirePackage{lipsum} % Lorem Ipsum dummy text



%-----------------------------------------------------------------------------------------------------------------------
%    3. GRAPHICS
%-----------------------------------------------------------------------------------------------------------------------
%%% Floats
\RequirePackage{graphicx}                % Import images
\RequirePackage{float}		              % Control of float positions
\RequirePackage{wrapfig}                 % Wrap text around figures

%%% Captions
\RequirePackage[                         % Enable Captions
  labelfont=bf,                            % Bold font for Captions
  singlelinecheck=false                    % Not automatically center a Caption
]{caption}        
\RequirePackage{subcaption}              % Enable Subcaptions

% French traductions
\addto\captionsfrancais{\def\figurename{Figure}}
\addto\captionsfrancais{\def\tablename{Tableau}}

\def\seplineCap{\leavevmode\leaders\hrule height 0.8pt\hfill\kern\z@} % New \hrulefill for Captions
\def\seplineSubcap{\leavevmode\leaders\hrule height 0.6pt\hfill\kern\z@} % New \hrulefill for Captions

\DeclareCaptionFormat{rptxCapCaption}{\color{rptxClrBlack3}\seplineCap\newline\color{rptxClrBlack2}#1#2#3}                     % Define a new style for Captions
\DeclareCaptionFormat{rptxCapSubcaption}{\color{rptxClrBlack2}\centering #1#2#3}                                               % Define a new style for Subcaptions
\DeclareCaptionFormat{rptxCapTable}{\color{rptxClrBlack2}#1#2#3\vspace*{-.5em}\color{rptxClrBlack3}\seplineCap}                % Define a new style for Tables
\DeclareCaptionFormat{rptxCapSubtable}{\color{rptxClrBlack2}#1#2#3\vspace*{-.5em}\color{rptxClrBlack3}\seplineSubcap}          % Define a new style for Subtables
\DeclareCaptionFormat{rptxCapCode}{\color{rptxClrBlack2}#1#2#3\vspace*{-.5em}\color{rptxClrBlack3}\seplineCap\vspace*{-.8em}}  % Define a new style for Listings
\captionsetup[figure]{format=rptxCapCaption}                                                                                   % Use new style for Captions
\captionsetup[subfigure]{format=rptxCapSubcaption}                                                                             % Use new style for Subcaptions
\captionsetup[table]{format=rptxCapTable}                       % Use new style for Tables
\captionsetup[subtable]{format=rptxCapSubtable}                 % Use new style for Subtables
\captionsetup[lstlisting]{format=rptxCapCode}                   % Use new style for Listings

%%% Colors
\RequirePackage[svgnames, table]{xcolor} % Add colors

%%% TikZ
\RequirePackage{pgf, tikz} % Draw schemas
\usetikzlibrary{
  arrows,
  backgrounds,
  calc,
  chains,
  decorations.pathmorphing,
  decorations.pathreplacing,
  decorations.text,
  matrix,
  positioning,
  shapes,
  shapes.geometric,
  shapes.symbols,
  trees
}
  
%%% Links
\RequirePackage[% Add information and create hyperlinks within the document
  % PDF properties
%  pdftitle={\pdfTitle},        % Title
%  pdfauthor={\pdfAuthor},      % Author
%  pdfcreator={\pdfCreator},    % Creator
%  pdfkeywords={\pdfKeywords},  % Keywords
  % Links
  colorlinks=true,              % Colored links
  linkcolor=rptxClrBlue1,       % Internal links
  urlcolor=rptxClrGray1,        % Web links
  citecolor=rptxClrBlue2,       % Bibliography links
  filecolor=rptxClrBlack3,      % File links
]{hyperref}
\urlstyle{sf}                   % URL style

%%% Footnotes
\RequirePackage[bottom]{footmisc}   % Footnotes always stick to bottom of page
\RequirePackage{chngcntr}           % Resetting of counters
\counterwithout{footnote}{chapter}  % Continuous footnote numbering

%% Palette
% Main
\definecolor{rptxClrBlack1}{HTML}{111111}
\definecolor{rptxClrBlack2}{HTML}{222222}
\definecolor{rptxClrBlack3}{HTML}{333333}
\definecolor{rptxClrBlack4}{HTML}{30723D}
\definecolor{rptxClrBlue1}{HTML}{08087B}
\definecolor{rptxClrBlue2}{HTML}{030350}
\definecolor{rptxClrGray1}{HTML}{505360}
\definecolor{rptxClrGreen}{HTML}{30723D}

% Code
\definecolor{rptxClrCodeBlack}{HTML}{111111}
\definecolor{rptxClrCodeBlue1}{HTML}{6983A8}
\definecolor{rptxClrCodeBlue2}{HTML}{29A1A0}
\definecolor{rptxClrCodeGray1}{HTML}{505360}
\definecolor{rptxClrCodeGray2}{HTML}{93A1AA}
\definecolor{rptxClrCodeGray3}{HTML}{949698}
\definecolor{rptxClrCodeGray4}{HTML}{EAEAEA}
\definecolor{rptxClrCodeGray5}{HTML}{F8F8F8}
\definecolor{rptxClrCodeGreen}{HTML}{869901}
\definecolor{rptxClrCodeOrange}{HTML}{CB4B15}
\definecolor{rptxClrCodeRed}{HTML}{DC3431}
\definecolor{rptxClrCodeWhite}{HTML}{FFFFFF}
\definecolor{rptxClrCodeYellow}{HTML}{B59002}

%% Boxes
\NewDocumentCommand{\framecolorbox}{oommm}
 {% #1 = width (optional)
  % #2 = inner alignment (optional)
  % #3 = frame color
  % #4 = background color
  % #5 = text
  \IfValueTF{#1}
   {%
    \IfValueTF{#2}
     {\fcolorbox{#3}{#4}{\makebox[#1][#2]{#5}}}
     {\fcolorbox{#3}{#4}{\makebox[#1]{#5}}}%
   }
   {\fcolorbox{#3}{#4}{#5}}%
 }

\newcommand{\fboxresized}[1]{
%  \setlength{\fboxsep}{2\fboxrule}\framebox{\raisebox{1pt}[6pt][1.2pt]{\hspace{1.2pt}\strut\texttt{\scriptsize #1}}\hspace{1.2pt}}
  \setlength{\fboxsep}{0\fboxrule}\framecolorbox{rptxClrCodeGray3}{rptxClrCodeGray4}{\raisebox{1pt}[6.7pt][1.2pt]{\hspace{1.2pt}\strut\texttt{\scriptsize #1}}\hspace{1.2pt}}
}


%-----------------------------------------------------------------------------------------------------------------------
%    4. TABLES
%-----------------------------------------------------------------------------------------------------------------------
\RequirePackage{tocloft}                                                   % Tables design
\setcounter{secnumdepth}{3}                                                % Add numbering for Subsubsections

%%% Title Font
% Table of Contents
\renewcommand{\cfttoctitlefont}{\usefont{T1}{qhv}{b}{n}\selectfont\huge}              % Table of Contents title
\renewcommand{\cftpartfont}{\usefont{T1}{qhv}{b}{n}\fontsize{12}{15}\selectfont}      % Part titles
\renewcommand{\cftchapfont}{\usefont{T1}{qhv}{b}{n}\selectfont}                       % Chapter titles
\renewcommand{\cftsecfont}{\usefont{T1}{bch}{m}{n}\selectfont}                        % Section titles
\renewcommand{\cftsubsecfont}{\usefont{T1}{bch}{m}{n}\selectfont}                     % Subsection titles
\renewcommand{\cftpartpagefont}{\usefont{T1}{bch}{b}{n}\fontsize{12}{15}\selectfont}  % Part page numbers
\renewcommand{\cftchappagefont}{\usefont{T1}{bch}{b}{n}\selectfont}                   % Chapter page numbers
\renewcommand{\cftsecpagefont}{\cftsecfont}                                           % Section page numbers
\renewcommand{\cftsubsecpagefont}{\cftsubsecfont}                                     % Subsection page numbers

% List of Figures
\renewcommand{\cftloftitlefont}{\usefont{T1}{qhv}{b}{n}\selectfont\huge}   % List of Figures title
\renewcommand{\cftfigfont}{\usefont{T1}{bch}{m}{n}\selectfont}             % Figure titles
\renewcommand{\cftfigpagefont}{\cftsecfont}                                % Figure page numbers

% List of Tables
\renewcommand{\cftlottitlefont}{\usefont{T1}{qhv}{b}{n}\selectfont\huge}   % List of Tables title
\renewcommand{\cfttabfont}{\usefont{T1}{bch}{m}{n}\selectfont}             % Table titles
\renewcommand{\cfttabpagefont}{\cftsecfont}                                % Table page numbers

%%% Spaces
% Table of Contents
\setlength{\cftbeforetoctitleskip}{5.88em}                                 % Align Table of Contents title with the previous Front Matter title
\renewcommand{\cftbeforechapskip}{1em}                                     % Space before Chapter title
\renewcommand{\cftchapaftersnumb}{\hskip -0.4em}                           % Space between Chapter number and Chapter title
\renewcommand{\cftchapafterpnum}{\vskip 0.2em}                             % Space after Chapter title
\renewcommand{\cftsecindent}{1.2em}                                        % Space between Margin and Section number
\renewcommand{\cftbeforesecskip}{0.2em}                                    % Space before Section title
\renewcommand{\cftsecaftersnumb}{\hskip -0.4em}                            % Space between Section number and Section title
\renewcommand{\cftsecafterpnum}{\vskip 0.1em}                              % Space after Section title
\renewcommand{\cftsubsecindent}{3.1em}                                     % Space between Margin and Subsection number
\renewcommand{\cftbeforesubsecskip}{0.2em}                                 % Space before Subection title
\renewcommand{\cftsubsecaftersnumb}{\hskip -0.4em}                         % Space between Subection number and Subsection title
\renewcommand{\cftsubsecafterpnum}{\vskip 0em}                             % Space after Subection title

% List of Figures
\renewcommand{\cftfigindent}{1.2em}                                        % Space between Margin and Figure number
\renewcommand{\cftfigaftersnumb}{\hskip -0.4em}                            % Space between Figure number and Figure title

% List of Tables
\renewcommand{\cfttabindent}{1.2em}                                        % Space between Margin and Table number
\renewcommand{\cfttabaftersnumb}{\hskip -0.4em}                            % Space between Table number and Table title

%%% Title rules
\renewcommand{\cftaftertoctitle}{\vskip 1.88em\titlerule[2pt]}             % Title rule for Table of Contents
\renewcommand{\cftafterloftitle}{\vskip 1.43em\titlerule[2pt]}             % Title rule for List of Figures
\renewcommand{\cftafterlottitle}{\vskip 1.88em\titlerule[2pt]}             % Title rule for List of Tables


%-----------------------------------------------------------------------------------------------------------------------
%    5. ELEMENTS
%-----------------------------------------------------------------------------------------------------------------------
%% Bibliography
\RequirePackage[
  backend=bibtex,      % Backend to generate Bibliography
  backref=true,        % Enable back references (number of page)
  block=none,          % Space between blocks
  doi=false,           % Disable DOI
  hyperref=true,       % Clickable hyperlinks
  isbn=false,          % Disable ISBN
  maxbibnames=100,     % Maximum number of citations in the document body
  maxcitenames=3,      % Maximum number of authors in the bibliography 
  url=true,            % Enable URLs
  style=numeric-comp   % Citation style
]{biblatex}

% Formatting
\DefineBibliographyStrings{english}{backrefpage = {\lowercase{s}ee p.}, backrefpages = {\lowercase{s}ee pp.}} % Back References
\DeclareFieldFormat{url}{\newline\space\small{\url{#1}}} % URL
\DeclareFieldFormat{edition}{\ifinteger{#1}{\mkbibordedition{#1}\addthinspace{}ed.}{#1\isdot}} % Edition
\DeclareFieldFormat{journaltitle}{\mkbibemph{#1,}} % Journal title
\renewbibmacro{in:}{} % Remove `In:`

% Print names in small caps
\renewcommand{\mkbibnamefirst}[1]{\textsc{#1}}
\renewcommand{\mkbibnamelast}[1]{\textsc{#1}}
\renewcommand{\mkbibnameprefix}[1]{\textsc{#1}}
\renewcommand{\mkbibnameaffix}[1]{\textsc{#1}}


%% Glossary
\RequirePackage[
  acronym,     % Use acronyms
  nopostdot,   % Remove the dot at the end of descriptions
  toc          % Add to Table of Contents
]{glossaries}


%% Lists
\RequirePackage{enumitem}
% Bullets for lists and diamond and circles
%\renewcommand{\labelitemi}{$\bullet$}
%\renewcommand{\labelitemii}{$\diamond$}
%\renewcommand{\labelitemiii}{$\circ$}
\newlist{rptxitemize}{itemize}{4}
\setlist[rptxitemize, 1]{label=\textbullet, topsep=1.3pt, leftmargin=2.5em, parsep=1.5pt}
\setlist[rptxitemize, 2]{label=$\diamond$, topsep=1.7pt, leftmargin=2em}
\setlist[rptxitemize, 3]{label=$\circ$, parsep=1.7pt}
\setlist[rptxitemize, 4]{label=$\cdot$, topsep=1.9pt, parsep=1.5pt}

%% Tables
\RequirePackage[none]{hyphenat}		% No word wrapping in a table
\RequirePackage{array}				    % Extends the options for column formats
\RequirePackage{multirow}              % Enable multirows
\RequirePackage{booktabs}              % Nice tables
\RequirePackage{tabularx}
\newcolumntype{$}{>{\global\let\currentrowstyle\relax}}                        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcolumntype{^}{>{\currentrowstyle}}
\newcommand{\rowstyle}[1]{\gdef\currentrowstyle{#1}#1\ignorespaces}

%% Epigraph
\RequirePackage{epigraph}                                                  % Enable Epigraphs
\renewcommand{\textflush}{flushepinormal}                                  % Justified text
\renewcommand{\epigraphrule}{.1pt}                                         % Width of the Epigraph rule

%% Codes
\RequirePackage{listings}                                                  % Add source code
\renewcommand{\lstlistingname}{Source Code}                                % Change `Listing` by `Source Code`
\renewcommand{\lstlistlistingname}{List of Source Code}                    % Change `Listings` by `List of Source Code`

% C (Style)
\lstdefinestyle{CodeStyleC}{                     % Code style
  belowcaptionskip=1\baselineskip,               % Space after caption
  backgroundcolor=\color{rptxClrCodeWhite},      % Background color
  basicstyle=\footnotesize\ttfamily\color{rptxClrCodeGray1},          % Font style
  breaklines=true,                               % Automatic line breaking
  captionpos=t,                                  % Caption-position to the top
  columns=fullflexible,                          % Render a better typography
  commentstyle=\itshape\color{rptxClrCodeGray2}, % Comment style
  emph=[1]{},                                    % List n°1 of additional coloured words (separate words with `,`)
  emph=[2]{},                                    % List n°2 of additional coloured words (separate words with `,`)
  emphstyle=[1]{\color{rptxClrCodeOrange}},      % List n°1 style
  emphstyle=[2]{\color{rptxClrCodeGreen}}        % List n°2 style
  extendedchars=true,                            % Use non-ASCII characters
  firstline=1,                                   % First line begins at '1'
  frame=l,                                       % Frame at the left of the code
  framerule=0.7pt,                               % Height of the frame rule
  framesep=5pt,                                  % Separation width of the frame
  identifierstyle=\color{rptxClrCodeBlue1},      % Identifiers
  keepspaces=true,                               % Keeps spaces in text
  keywordstyle=\bfseries\color{rptxClrCodeRed},  % Keywords style
  language=C,                                    % Language
  literate=*{0}{{\textcolor{rptxClrCodeYellow}{0}}}{1}%       % Coloring numbers
            {1}{{\textcolor{rptxClrCodeYellow}{1}}}{1}%
            {2}{{\textcolor{rptxClrCodeYellow}{2}}}{1}%
            {3}{{\textcolor{rptxClrCodeYellow}{3}}}{1}%
            {4}{{\textcolor{rptxClrCodeYellow}{4}}}{1}%
            {5}{{\textcolor{rptxClrCodeYellow}{5}}}{1}%
            {6}{{\textcolor{rptxClrCodeYellow}{6}}}{1}%
            {7}{{\textcolor{rptxClrCodeYellow}{7}}}{1}%
            {8}{{\textcolor{rptxClrCodeYellow}{8}}}{1}%
            {9}{{\textcolor{rptxClrCodeYellow}{9}}}{1}%
            {.0}{{\textcolor{rptxClrCodeYellow}{.0}}}{1}%
            {.1}{{\textcolor{rptxClrCodeYellow}{.1}}}{1}%
            {.2}{{\textcolor{rptxClrCodeYellow}{.2}}}{1}%
            {.3}{{\textcolor{rptxClrCodeYellow}{.3}}}{1}%
            {.4}{{\textcolor{rptxClrCodeYellow}{.4}}}{1}%
            {.5}{{\textcolor{rptxClrCodeYellow}{.5}}}{1}%
            {.6}{{\textcolor{rptxClrCodeYellow}{.6}}}{1}%
            {.7}{{\textcolor{rptxClrCodeYellow}{.7}}}{1}%
            {.8}{{\textcolor{rptxClrCodeYellow}{.8}}}{1}%
            {.9}{{\textcolor{rptxClrCodeYellow}{.9}}}{1}%
            {\ }{{ }}{1},% Handle the space
  morekeywords={},                               % Additional keywords (separate words with `,`)
  numbers=left,                                  % Line-numbers
  numbersep=8pt,                                 % Distance between line-numbers and the code
  numberstyle=\tt\scriptsize\color{rptxClrCodeGray3},  % Line-numbers style
  rulecolor=\color{rptxClrBlack2},               % Rule color
  showstringspaces=false,                        % Underline spaces within strings only
  showtabs=false,                                % Show tab characters
  stepnumber=1,                                  % Step between two line-numbers
  stringstyle=\color{rptxClrCodeBlue2},          % String literal style
  xleftmargin=\parindent,                        % Left margin
  xrightmargin=\parindent,                       % Right margin
  tabsize=4,                                     % Default tabsize
  title=\lstname                                 % Print name if caption field empty
}

% C (Environment)
\lstnewenvironment{CodeEnvC}{\lstset{style=CodeStyleC}}{}

% DOS (Style)
\lstdefinestyle{CodeStyleDOS}{                   % Code style
  belowcaptionskip=1\baselineskip,               % Space after caption
  backgroundcolor=\color{rptxClrCodeBlack},      % Background color
  basicstyle=\footnotesize\ttfamily\color{rptxClrCodeWhite},             % Font style
  breaklines=true,                               % Automatic line breaking
  captionpos=t,                                  % Caption-position to the top
  columns=fullflexible,                          % Render a better typography
  frame=single,                                  % Frame around the code
  framerule=0.5pt,                               % Frame rule
  keepspaces=true,                               % Keeps spaces in text
  rulecolor=\color{rptxClrCodeGray1},            % Frame color
  showstringspaces=false,                        % Underline spaces within strings only
  showtabs=false,                                % Show tab characters
  xleftmargin=.45em,                             % Left margin
  xrightmargin=.45em,                            % Right margin
  tabsize=4,                                     % Default tabsize
  title=\lstname                                 % Print name if caption field empty
}

% DOS (Environment)
\lstnewenvironment{CodeEnvDOS}{\lstset{style=CodeStyleDOS}}{}

% XML (Style)
\lstdefinestyle{CodeStyleXML}{                   % Code style
  belowcaptionskip=1\baselineskip,               % Space after caption
  backgroundcolor=\color{rptxClrCodeWhite},      % Background color
  basicstyle=\footnotesize\ttfamily\color{rptxClrCodeGray1},          % Font style
  breaklines=true,                               % Automatic line breaking
  captionpos=t,                                  % Caption-position to the top
  columns=fullflexible,                          % Render a better typography
  commentstyle=\itshape\color{rptxClrCodeGray2}, % Comment style
  extendedchars=true,                            % Use non-ASCII characters
  firstline=1,                                   % First line begins at '1'
  frame=l,                                       % Frame at the left of the code
  framerule=0.7pt,                               % Height of the frame rule
  framesep=5pt,                                  % Separation width of the frame
  identifierstyle=\color{rptxClrCodeBlue1},      % Identifiers
  keepspaces=true,                               % Keeps spaces in text
  keywordstyle=\bfseries\color{rptxClrCodeRed},  % Keywords style
  language=XML,                                  % Language
  literate=*{0}{{\textcolor{rptxClrCodeYellow}{0}}}{1}%       % Coloring numbers
            {1}{{\textcolor{rptxClrCodeYellow}{1}}}{1}%
            {2}{{\textcolor{rptxClrCodeYellow}{2}}}{1}%
            {3}{{\textcolor{rptxClrCodeYellow}{3}}}{1}%
            {4}{{\textcolor{rptxClrCodeYellow}{4}}}{1}%
            {5}{{\textcolor{rptxClrCodeYellow}{5}}}{1}%
            {6}{{\textcolor{rptxClrCodeYellow}{6}}}{1}%
            {7}{{\textcolor{rptxClrCodeYellow}{7}}}{1}%
            {8}{{\textcolor{rptxClrCodeYellow}{8}}}{1}%
            {9}{{\textcolor{rptxClrCodeYellow}{9}}}{1}%
            {.0}{{\textcolor{rptxClrCodeYellow}{.0}}}{1}%
            {.1}{{\textcolor{rptxClrCodeYellow}{.1}}}{1}%
            {.2}{{\textcolor{rptxClrCodeYellow}{.2}}}{1}%
            {.3}{{\textcolor{rptxClrCodeYellow}{.3}}}{1}%
            {.4}{{\textcolor{rptxClrCodeYellow}{.4}}}{1}%
            {.5}{{\textcolor{rptxClrCodeYellow}{.5}}}{1}%
            {.6}{{\textcolor{rptxClrCodeYellow}{.6}}}{1}%
            {.7}{{\textcolor{rptxClrCodeYellow}{.7}}}{1}%
            {.8}{{\textcolor{rptxClrCodeYellow}{.8}}}{1}%
            {.9}{{\textcolor{rptxClrCodeYellow}{.9}}}{1}%
            {\ }{{ }}{1},% Handle the space
  morekeywords={},                               % Additional keywords (separate words with `,`)
  numbers=left,                                  % Line-numbers
  numbersep=8pt,                                 % Distance between line-numbers and the code
  numberstyle=\tt\scriptsize\color{rptxClrCodeGray3},  % Line-numbers style
  rulecolor=\color{rptxClrBlack2},               % Rule color
  showstringspaces=false,                        % Underline spaces within strings only
  showtabs=false,                                % Show tab characters
  stepnumber=1,                                  % Step between two line-numbers
  stringstyle=\color{rptxClrCodeBlue2},          % String literal style
  xleftmargin=\parindent,                        % Left margin
  xrightmargin=\parindent,                       % Right margin
  tabsize=4,                                     % Default tabsize
  title=\lstname                                 % Print name if caption field empty
}

% XML (Environment)
\lstnewenvironment{CodeEnvXML}{\lstset{style=CodeStyleXML}}{}


%-----------------------------------------------------------------------------------------------------------------------
%    6. REPORTEX
%-----------------------------------------------------------------------------------------------------------------------
%% Paths
\newcommand{\pathReport}{./report}                                         % Main path
\newcommand{\pathBack}{\pathReport/back}                                   % Back matter path
\newcommand{\pathChapters}{\pathReport/chapters}                           % Chapters path
\newcommand{\pathPrelims}{\pathReport/prelims}                             % Front matter path
\newcommand{\pathAssets}{\pathReport/assets}                               % Assets path
\newcommand{\pathCodes}{\pathAssets/codes}                                 % Code path
\newcommand{\pathImages}{\pathAssets/images}                               % Images path
\newcommand{\pathGraphics}{\pathAssets/graphics}                           % Graphics path
\newcommand{\pathTables}{\pathAssets/tables}                               % Tables path
\graphicspath{{\pathImages/}}                                              % Images path (LaTeX command)

%% Commands
%\newcommand{\includecode}[3][c]{\lstinputlisting[language=#1,caption=#2]{\pathCodes/#3}}
\newcommand{\img}[2][]{\includegraphics[width=#1\textwidth]{\pathImages/#2}}
\newcommand{\rptxEpigraph}[2]{\epigraph{\textit{\Large{``}\hspace*{3pt}\normalsize{#1}\hspace*{3pt}\Large{''}}}{\textemdash{} \textup{#2}}}
%\newcommand{\rptxCodeBox}[1]{\framecolorbox{rptxClrCodeGray3}{rptxClrCodeGray4}{\texttt{\scriptsize{#1}}}}
\newcommand{\rptxCodeBox}[1]{\hspace{-1.2pt}\fboxresized{#1}\hspace{-2pt}}