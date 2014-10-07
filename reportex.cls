\LoadClass[a4paper,12pt]{report}
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{reportex}[2014/10/07 A template for LaTeX reports]


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  PACKAGES  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
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


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  COMMANDS  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% code
% '\code[a_line_of_code]'; print a line of code with the \texttt command
\newcommand{\code}[1][]{\texttt{#1}}

%% img
% '\img[textwidth]{picture_name}'; print a picture
\newcommand{\img}[2][]{\includegraphics[width=#1\textwidth]{\pathImages/#2}}

%% sep
% '\sep'; horizontal rule
\newcommand{\sep}{\rule{\linewidth}{0.5mm}}