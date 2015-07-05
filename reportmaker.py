#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Title          :reportmaker.py
# Description    :A tool to create LaTeX reports
# Author         :Simon L. J. Robin
# Created        :2015-01-22 15:53:39
# Modified       :2015-07-05 18:25:45
########################################################################################## 

import argparse
import os
import re
import sys
import urllib

try:
    from colorama import init
    from termcolor import colored
    from time import strptime
    init()
except ImportError:
    print "Make sure you have installed 'colorama', 'termcolor' packages."

########################################################################################## 
## About
RPTX_AUTHOR_NAME = "Simon L. J. Robin"
RPTX_AUTHOR_WEBSITE = "http://work.sljrobin.com/reportex"
RPTX_CLASS = "reportex"
RPTX_DESCRIPTION = "A helper and a class for quickly making LaTeX reports"
RPTX_LICENSE = "GPL license"
RPTX_NAME = "ReporTeX"
RPTX_REPO = "http://github.com/sljrobin/ReporTeX/"

#####################################################################################
## Arguments
ARG_D_DOWNLOAD = "download the ReporTeX class"
ARG_M_MAKEFILE = "generate the makefile"
ARG_N_NEW = "create a new report"

#####################################################################################
## Checker
# Answers
CKR_ANS_N = "n"
CKR_ANS_NO = "no"
CKR_ANS_Y = "y"
CKR_ANS_YES = "yes"

# Selectors
CKR_SEL_NO = "[y/N]"
CKR_SEL_NONE = "[y/n]"
CKR_SEL_YES = "[Y/n]"

#####################################################################################
## Extensions
EXT_BIB = ".bib"
EXT_CLS = ".cls"
EXT_PDF = ".pdf"
EXT_TAR = ".tar.gz"
EXT_TEX = ".tex"
EXT_ZIP = ".zip"

#####################################################################################
## Files
RPTX_CLASS_FILE = "reportex" + EXT_CLS
RPTX_MAIN_FILE = "report" + EXT_TEX
RPTX_MAKE_FILE = "makefile"
RPTX_TITLEPAGE_FILE = "title" + EXT_TEX

#####################################################################################
## Folders
FLDR_ASSETS = "assets/"
FLDR_BACK = "back/"
FLDR_CHAPTERS = "chapters/"
FLDR_CODES = "codes/"
FLDR_GRAPHICS = "graphics/"
FLDR_IMAGES = "images/"
FLDR_PRELIMS = "prelims/"
FLDR_REPORT = "report/"
FLDR_TABLES = "tables/"

#####################################################################################
## Headers
# Dictionary
HDR_DICT_AUTHOR_NAME_FIRST = "Author's first name"
HDR_DICT_AUTHOR_NAME_LAST = "Author's last name"
HDR_DICT_COMPANY = "Company"
HDR_DICT_DATE = "Date"
HDR_DICT_SUBTITLE = "Subtitle"
HDR_DICT_SUPERVISOR_NAME_FIRST = "Supervisor's first name"
HDR_DICT_SUPERVISOR_NAME_LAST = "Supervisor's last name"
HDR_DICT_TITLE = "Title"

# Properties
HDR_PROP_AUTHOR_NAME_FIRST = "Author's first name"
HDR_PROP_AUTHOR_NAME_LAST = "Author's last name"
HDR_PROP_COMPANY = "Company"
HDR_PROP_DATE = "Date"
HDR_PROP_SUBTITLE = "Subtitle"
HDR_PROP_SUPERVISOR_NAME_FIRST = "Supervisor's first name"
HDR_PROP_SUPERVISOR_NAME_LAST = "Supervisor's last name"
HDR_PROP_TITLE = "Title"

#####################################################################################
## Bash
# Commands
BSH_CMD_ARCHIVE = "archive"
BSH_CMD_CLASS = "class"
BSH_CMD_MAKEFILE = "makefile"
BSH_CMD_REPORT = "report"
BSH_CMD_REPORTMAKER = "reportmaker"
BSH_CMD_RM = "rm -f"
BSH_CMD_TAR = "tar -cvzf"
BSH_CMD_ZIP = "zip -r"

# Comments
BSH_CMT_MAKEFILE_HEADER = "ReporTeX: Makefile"
BSH_CMT_RULE_ARCHIVETAR = "'archive-tar': Compress the files in a `.tar.gz` archive"
BSH_CMT_RULE_ARCHIVEZIP = "'archive-zip': Compress the files in a `.zip` archive"
BSH_CMT_RULE_BUILDFULL = "'build-full': Clean, and compile"
BSH_CMT_RULE_BUILDSIMPLE = "'build-simple': Compile only the main file"
BSH_CMT_RULE_CLEAN = "'clean': Remove the odd files"
BSH_CMT_RULE_VIEW = "'view': Read the PDF"
BSH_CMT_VAR_APPLICATIONS = "Applications"
BSH_CMT_VAR_VARIABLES = "Variables"

# Rules
BSH_RULE_ARCHIVETAR = "archive-tar: clean"
BSH_RULE_ARCHIVEZIP = "archive-zip: clean"
BSH_RULE_BUILDFULL = "build-full:"
BSH_RULE_BUILDSIMPLE = "build-simple:"
BSH_RULE_CLEAN = "clean:"
BSH_RULE_VIEW = "view:"

# Variables
BSH_VAR_ARCHIVE_NME = "archive"
BSH_VAR_ARCHIVE_VLE = "=${report}_$(shell date +'%Y-%m-%d_%H-%M-%S')"
BSH_VAR_BIB_NME = "BIB"
BSH_VAR_BIB_VLE = "=bibtex"
BSH_VAR_CLASS_NME = "class"
BSH_VAR_CLASS_VLE = "=reportex.cls"
BSH_VAR_GLO_NME = "GLO"
BSH_VAR_GLO_VLE = "=makeglossaries"
BSH_VAR_MAKEFILE_NME = "makefile"
BSH_VAR_MAKEFILE_VLE = "=makefile"
BSH_VAR_REPORT_NME = "report"
BSH_VAR_REPORT_VLE = "=report"
BSH_VAR_REPORTMAKER_NME = "reportmaker"
BSH_VAR_REPORTMAKER_VLE = "=reportmaker.py"
BSH_VAR_PDF_NME = "PDF"
BSH_VAR_PDF_VLE = "=evince"
BSH_VAR_TEX_NME = "TEX"
BSH_VAR_TEX_VLE = "=pdflatex"

#####################################################################################
## LaTeX
# Commands
LTX_CMD_ADD_CONTENTS_LINE = "addcontentsline{toc}{chapter}"
LTX_CMD_ADD_LENGTH = "addtolength"
LTX_CMD_ACRONYM_TYPE = "acronymtype"
LTX_CMD_ARABIC = "arabic"
LTX_CMD_BEGIN = "begin"
LTX_CMD_BIBLIOGRAPHY = "bibliography"
LTX_CMD_CENTER = "center"
LTX_CMD_CENTERING = "centering"
LTX_CMD_CHAPTER = "chapter"
LTX_CMD_CHAPTER_UNNAMED = "chapter*"
LTX_CMD_CLEARDOUBLEPAGE = "cleardoublepage"
LTX_CMD_DOC = "document"
LTX_CMD_DOCCLASS = "documentclass"
LTX_CMD_END = "end"
LTX_CMD_EVENSIDEMARGIN = "evensidemargin"
LTX_CMD_FANCYHEAD = "fancyhead"
LTX_CMD_FI = "fi"
LTX_CMD_GLOSSARY_TYPE = "main"
LTX_CMD_HOFFSET = "hoffset"
LTX_CMD_HSPACE = "hspace*"
LTX_CMD_HUGE = "huge"
LTX_CMD_IFTWOSIDE = "if@twoside"
LTX_CMD_INPUT = "input"
LTX_CMD_IMG = "img"
LTX_CMD_LARGE = "Large"
LTX_CMD_LEFTMARK = "leftmark"
LTX_CMD_LET = "let"
LTX_CMD_LINEWIDTH = "linewidth"
LTX_CMD_LOAD_GLOSSARY = "loadglsentries"
LTX_CMD_MAKEATLETTER = "makeatletter"
LTX_CMD_MAKEATOTHER = "makeatother"
LTX_CMD_MAKEGLOSSARIES = "makeglossaries"
LTX_CMD_MICROTYPESETUP = "microtypesetup"
LTX_CMD_NEW_CMD = "newcommand"
LTX_CMD_NEW_ENV = "newenvironment"
LTX_CMD_NEW_LENGTH = "newlength"
LTX_CMD_NEWLINE = "\\"
LTX_CMD_NUMBERLINE = "numberline"
LTX_CMD_PAGE = "page"
LTX_CMD_PAGENUMBERING = "pagenumbering"
LTX_CMD_PDF_AUTHOR = "pdfAuthor"
LTX_CMD_PDF_CREATOR = "pdfCreator"
LTX_CMD_PDF_KEYWORDS = "pdfKeywords"
LTX_CMD_PDF_TITLE = "pdfTitle"
LTX_CMD_PRINTBIBLIOGRAPHY = "printbibliography"
LTX_CMD_PRINTGLOSSARY = "printglossary"
LTX_CMD_PROTUSION = "protusion"
LTX_CMD_RIGHTMARK = "rightmark"
LTX_CMD_RPTX_AUTHOR = "reportAuthor"
LTX_CMD_RPTX_COMPANY = "reportCompany"
LTX_CMD_RPTX_DATE = "reportDate"
LTX_CMD_RPTX_SUBTITLE = "reportSubtitle"
LTX_CMD_RPTX_SUPERVISOR = "reportSupervisor"
LTX_CMD_RPTX_TITLE = "reportTitle"
LTX_CMD_ROMAN = "roman"
LTX_CMD_RULE = "rule"
LTX_CMD_SECTION = "section"
LTX_CMD_SELECTFONT = "selectfont"
LTX_CMD_SET_COUNTER = "setcounter"
LTX_CMD_SET_LENGTH = "setlength"
LTX_CMD_SUBSECTION = "subsection"
LTX_CMD_TABLE = "table"
LTX_CMD_TABLE_CONTENTS = "tableofcontents"
LTX_CMD_TABLE_FIGURES = "listoffigures"
LTX_CMD_TABLE_LISTINGS = "lstlistoflistings"
LTX_CMD_TABLE_TABLES = "listoftables"
LTX_CMD_TABULAR = "tabular"
LTX_CMD_TEXTIT = "textit"
LTX_CMD_TEXTSC = "textsc"
LTX_CMD_TEXTBLOCKOFFSET = "textblockoffset"
LTX_CMD_THEPAGE = "thepage"
LTX_CMD_THISPAGESTYLE = "thispagestyle"
LTX_CMD_TITLEPAGE = "titlepage"
LTX_CMD_USEFONT = "usefont"
LTX_CMD_VFILL = "vfill"
LTX_CMD_VSPACE = "vspace*"

# Comments
LTX_CMT_BACK_BIBLIOGRAPHY = "Bibliography"
LTX_CMT_BODY_TWOSIDE_ENABLE = "Only executed if the `twoside` option is enabled"
LTX_CMT_BODY_TWOSIDE_HEADER = "Change the Header"
LTX_CMT_BODY_TWOSIDE_HEADER_CHAPTER = "Chapter"
LTX_CMT_BODY_TWOSIDE_HEADER_PAGENUMBER = "Page number"
LTX_CMT_BODY_TWOSIDE_HEADER_REINITIALIZATION = "Header reinitialization"
LTX_CMT_BODY_TWOSIDE_HEADER_SECTION = "Section"
LTX_CMT_BODY_TWOSIDE_OFFSET = "Change the offset of the textblock"
LTX_CMT_HDR_BACK = "BACK"
LTX_CMT_HDR_BODY = "BODY"
LTX_CMT_HDR_PRELIMS = "PRELIMS"
LTX_CMT_HDR_TABLES = "TABLES"
LTX_CMT_PAGENUMBERING = "Page numbering"
LTX_CMT_PROPERTIES = "Properties"
LTX_CMT_TABLES_ACRONYMS = "Acronyms"
LTX_CMT_TABLES_GLOSSARY = "Glossary"
LTX_CMT_TABLES_LOF = "List of Figures"
LTX_CMT_TABLES_LOL = "List of Listings"
LTX_CMT_TABLES_LOT = "List of Tables"
LTX_CMT_TABLES_TOC = "Table of Contents"
LTX_CMT_TITLE_AUTHOR = RPTX_NAME + " has been developed by " + RPTX_AUTHOR_NAME
LTX_CMT_TITLE_CREATED = "Created by using " + RPTX_NAME
LTX_CMT_TITLE_LICENSE = RPTX_NAME + " is licensed under the " + RPTX_LICENSE
LTX_CMT_TITLE_WEBSITES = RPTX_AUTHOR_WEBSITE + " | " + RPTX_REPO
LTX_CMT_TITLEPAGE = "Title Page"
LTX_CMT_TITLEPAGE_DATE = "Date"
LTX_CMT_TITLEPAGE_LOGO = "Logo"
LTX_CMT_TITLEPAGE_MAINTITLE = "Main Title"
LTX_CMT_TITLEPAGE_NAMES = "Names"
LTX_CMT_TITLEPAGE_SUBTITLE = "Subtitle"

# Paths
LTX_PATH_BACK = "pathBack/"
LTX_PATH_CHAPTERS = "pathChapters/"
LTX_PATH_PRELIMS = "pathPrelims/"

# Starting characters
LTX_START_CHAR_CMD = "\\"
LTX_START_CHAR_CMT = "%"


#####################################################################################
## Limits
LMT_AUTHOR_NAME_FIRST = 25
LMT_AUTHOR_NAME_LAST = 25
LMT_COMPANY = 20
LMT_INDENTATION = 4
LMT_SUBTITLE = 150
LMT_SUPERVISOR_NAME_FIRST = 25
LMT_SUPERVISOR_NAME_LAST = 25
LMT_TITLE = 150


#####################################################################################
## Messages
# Errors
MSG_TEXT_ERROR_CHECKING_ANSWER_VALUE = "Incorrect checking answer!"
MSG_TEXT_ERROR_CLASS_FILE_FAILED_DOWNLOAD = "The download of the main class file ('" + RPTX_CLASS_FILE + "') has failed!"
MSG_TEXT_ERROR_DATE_FORMAT = "Incorrect date format (dd/mm/yyyy)"
MSG_TEXT_ERROR_EXIT_SCRIPT = "Exiting the ReportMaker..."
MSG_TEXT_ERROR_FILE_ALREADY_EXISTS = "The file already exists!"
MSG_TEXT_ERROR_FOLDER_ALREADY_EXISTS = "The folder already exists!"
MSG_TEXT_ERROR_INCORRECT_ANSWER_CHECKER = "Incorrect answer. Answer by 'yes'/'y' or 'no'/'n'!"
MSG_TEXT_ERROR_INCORRECT_FORMAT_PLAN_ELEMENT = "Incorrect format for the current plan's element."
MSG_TEXT_ERROR_INVALID_DEFAULT_ANSWER = "Invalid default answer."
MSG_TEXT_ERROR_KEYBOARD_INTERRUPT = "Keyboard Interrupt. Make sure to delete all the files that have been created before launching the ReportMaker again."
MSG_TEXT_ERROR_NO_ARGS = "Select an argument! Use the '-h'/'--help' parameter to print help."
MSG_TEXT_ERROR_NO_MATCHES = "There are no matches!"

# Info
MSG_TEXT_INFO_CLASS_FILE_SUCCESSFULLY_DOWNLOADED = "The download of the main class file ('" + RPTX_CLASS_FILE + "') has been successful!"
MSG_TEXT_INFO_PROCESS_SUCCESSFULLY_ENDED = "The files and folders were successfully created. The report is now ready to be edited."
MSG_TEXT_INFO_DONT_FORGET_CLASS = "Do not forget to download the ReporTeX class. Use the `-d` parameter with the ReportMaker."
MSG_TEXT_INFOID_COLLECTING_PROPERTIES = "Collecting properties"
MSG_TEXT_INFOID_DOWNLOAD_CLASS = "Downloading ReporTeX class"
MSG_TEXT_INFOID_WRITING_PLAN = "Writing plan"

# Kinds
MSG_KIND_ERROR = "ERROR"
MSG_KIND_INFO = "INFO"
MSG_KIND_INFO_ID = "INFO_ID"
MSG_KIND_INPUT = "INPUT"

# Prefixes
MSG_PREFIX_ERROR = "Error!"
MSG_PREFIX_INFO = "Info:"

# Questions
MSG_TEXT_ANSWERS_CHECKING = "Do you agree with these values?"

# Total Info
MSG_INFO_TOTAL = 5


#####################################################################################
## Paths
PATH_RPTX_CLASS_FILE = "./"
PATH_RPTX_MAIN = "./"
PATH_RPTX_MAIN_FILE = "./"
PATH_RPTX_REPORT = PATH_RPTX_MAIN + FLDR_REPORT


#####################################################################################
## Plan
PLAN_DELIMITER_SIMPLE = "-"
PLAN_DELIMITER_DOUBLE = "--"
PLAN_ESCAPE_BODY_LEVEL_LESS = "<"
PLAN_ESCAPE_BODY_LEVEL_MORE = ">"
PLAN_ESCAPE_MISC_BACK = "b"
PLAN_ESCAPE_MISC_LEVEL_LESS = "-"
PLAN_ESCAPE_MISC_LEVEL_MORE = "+"
PLAN_ESCAPE_MISC_PRELIMS = "p"

PLAN_ESCAPE_REPORT = "_end_"


PLAN_HEADER_MISC_ABSTRACT = "Abstract"
PLAN_HEADER_MISC_ABSTRACT_L = "abstract"
PLAN_HEADER_MISC_ABSTRACT_S = "abs"

PLAN_HEADER_MISC_ACKNOWLEDGMENTS = "Acknowledgments"
PLAN_HEADER_MISC_ACKNOWLEDGMENTS_L = "acknowledgments"
PLAN_HEADER_MISC_ACKNOWLEDGMENTS_S = "ack"

PLAN_HEADER_MISC_ACRONYMS = "Acronyms"
PLAN_HEADER_MISC_ACRONYMS_L = "acronyms"
PLAN_HEADER_MISC_ACRONYMS_S = "acr"

PLAN_HEADER_MISC_BIBLIOGRAPHY = "Bibliography"
PLAN_HEADER_MISC_BIBLIOGRAPHY_L = "bibliography"
PLAN_HEADER_MISC_BIBLIOGRAPHY_S = "bib"

PLAN_HEADER_MISC_GLOSSARY = "Glossary"
PLAN_HEADER_MISC_GLOSSARY_L = "glossary"
PLAN_HEADER_MISC_GLOSSARY_S = "glo"

PLAN_ID_MISC = "#"
PLAN_ID_MISC_BACK = PLAN_ID_MISC + "B"
PLAN_ID_MISC_PRELIMS = PLAN_ID_MISC + "P"

PLAN_NUMBER_WIDTH = 2
PLAN_NUMBER_CHAPTER_WIDTH = PLAN_NUMBER_WIDTH
PLAN_NUMBER_MISC_WIDTH = PLAN_NUMBER_WIDTH
PLAN_NUMBER_SECTION_WIDTH = PLAN_NUMBER_WIDTH + 1 + PLAN_NUMBER_WIDTH
PLAN_NUMBER_SUBSECTION_WIDTH = PLAN_NUMBER_WIDTH + 1 + PLAN_NUMBER_WIDTH + 1 + PLAN_NUMBER_WIDTH

PLAN_TABLES_ACRONYMS = "Acronyms"
PLAN_TABLES_GLOSSARY = "Glossary"
PLAN_TABLES_LOF = "List of Figures"
PLAN_TABLES_LOL = "List of Listings"
PLAN_TABLES_LOT = "List of Tables"
PLAN_TABLES_TOC = "Table of Contents"

PLAN_BACK_BIBLIOGRAPHY = "Bibliography"


#####################################################################################
## Steps

# Maximums
STEP_MAX_DOCUMENT = "7"
STEP_MAX_MAIN = "3"
STEP_MAX_FOLDERS = "6"
STEP_MAX_GENERATION = "2"
STEP_MAX_WRITING = "7"

# Info
STEP_INFO_DBACK = "Writing the Back"
STEP_INFO_DBODY = "Writing the Body"
STEP_INFO_DDOCBEGIN = "Beginning of the Document"
STEP_INFO_DDOCEND = "Ending of the Document"
STEP_INFO_DHEADER = "Writing the Header"
STEP_INFO_DPRELIMS = "Writing the Prelims"
STEP_INFO_DTABLES = "Writing the Tables"
STEP_INFO_FASSETS = "Creating '" + FLDR_ASSETS + "'"
STEP_INFO_FBACK = "Creating '" + FLDR_BACK + "'"
STEP_INFO_FCHAPTERS = "Creating '" + FLDR_CHAPTERS + "'"
STEP_INFO_FPRELIMS = "Creating '" + FLDR_PRELIMS + "'"
STEP_INFO_FREPORT = "Creating '" + FLDR_REPORT + "'"
STEP_INFO_REPORT = "Creating '" + RPTX_MAIN_FILE + "'"


# Titles
STEP_TITLE_MAIN_1 = "Properties"
STEP_TITLE_MAIN_2 = "Plan"
STEP_TITLE_MAIN_3 = "Generation"

## URL
URL_REPORTEX_CLASS = "https://raw.githubusercontent.com/sljrobin/ReporTeX/master/reportex.cls"


##########################################################################################
class Component:
    r"""A class for Components (Files/Folders)
    """
    def __init__(self, name, path):
        r"""Component initialization

        name: Component's name
        path: Component's path

        """
        self._name = name
        self._path = path
        self._path_full = self._path + self._name

    def get_name(self):
        r"""Return the Component's name
        """
        return self._name

    def get_path(self):
        r"""Return the Component's path
        """
        return self._path

    def get_path_full(self):
        r"""Return the Component's path and the Component's name
        """
        return self._path_full


#####################################################################################
class File(Component):
    r"""A class for Files
    """
    def close(self):
        r"""Close a file
        """
        path = self._path_full
        component = open(path, "w")
        component.close()

    def make(self):
        r"""Create a file

        If the file already exists and is a file, print an error message
        Else, create the file

        """
        path = self._path_full
        if os.path.exists(path):
            err_file_already_exists = Messager(MSG_KIND_ERROR, "", MSG_TEXT_ERROR_FILE_ALREADY_EXISTS + " '" + path  + "'")
            err_file_already_exists.show()
        else:
            self.open()
            self.close()

    def open(self):
        r"""Open a file
        """
        path = self._path_full
        component = open(path, "w")


#####################################################################################
class Folder(Component):
    r"""A class for Folders
    """
    def make(self):
        r"""Create a folder

        If the folder already exists, print an error message
        Else, create the folder

        """
        path = self._path + self._name
        if os.path.exists(path):
            err_folder_already_exists = Messager(MSG_KIND_ERROR, "", MSG_TEXT_ERROR_FOLDER_ALREADY_EXISTS + " '" + path  + "'")
            err_folder_already_exists.show()
        else:
            os.makedirs(path, 0755);


########################################################################################## 
class Helper:
    r"""A class for Helps
    """
    def show_last_info(self):
        r"""Print the final message for the main report creating process
        """
        print
        print(colored(MSG_TEXT_INFO_PROCESS_SUCCESSFULLY_ENDED, "green", attrs = ["bold"]))
        print(colored(MSG_TEXT_INFO_DONT_FORGET_CLASS, "green", attrs = ["bold"]))

    def show_plan_help(self):
        r"""Print help for plan inputs
        """
        ## Normal User Input
        print(colored("* General", "cyan", attrs = ["bold"]))
        print(colored(" " * 4 + ">", "cyan", attrs = ["bold"])),
        print "Selection / Normal input"
        print " " * 4 + "Type `_end_` when the plan redaction is finished"
        ## Prelims
        print(colored("* Prelims", "cyan", attrs = ["bold"]))
        print " " * 4 + "Type `+p` or `<` to switch or quit Prelims elements"
        print(colored(" " * 4 + "+p", "blue", attrs = []) + \
              colored(">", "cyan", attrs = ["bold"])),
        print "Prelim"
        ## Body
        print(colored("* Body", "cyan", attrs = ["bold"]))
        print " " * 4 + "Type `>` or `<` to switch between Body elements"
        # Chapter
        print(colored(" " * 4 + ">", "blue", attrs = []) + \
              colored(">", "cyan", attrs = ["bold"])),
        print "Chapter"
        # Section
        print(colored(" " * 4 + ">>", "blue", attrs = []) + \
              colored(">", "cyan", attrs = ["bold"])),
        print "Section"
        # Subsection
        print(colored(" " * 4 + ">>>", "blue", attrs = []) + \
              colored(">", "cyan", attrs = ["bold"])),
        print "Subsection"
        ## Back
        print(colored("* Back", "cyan", attrs = ["bold"]))
        print " " * 4 + "Type `+b` or `<` to switch or quit Back elements"
        print(colored(" " * 4 + "+b", "blue", attrs = []) + \
              colored(">", "cyan", attrs = ["bold"])),
        print "Back"
        ## Predefined elements
        print(colored("* Predefined", "cyan", attrs = ["bold"]))
        print " " * 4 + "Type `++` or `<` to switch or quit Predefined elements"
        print " " * 4 + "Predefined elements:"
        # Abstract
        print " " * 8 + " * " + PLAN_HEADER_MISC_ABSTRACT + "        ->",
        print(colored(PLAN_HEADER_MISC_ABSTRACT_S, "magenta", attrs = [])),
        print "|",
        print(colored(PLAN_HEADER_MISC_ABSTRACT_L, "magenta", attrs = []))
        # Acknowledgments
        print " " * 8 + " * " + PLAN_HEADER_MISC_ACKNOWLEDGMENTS + " ->",
        print(colored(PLAN_HEADER_MISC_ACKNOWLEDGMENTS_S, "magenta", attrs = [])),
        print "|",
        print(colored(PLAN_HEADER_MISC_ACKNOWLEDGMENTS_L, "magenta", attrs = []))
        # Acronyms
        print " " * 8 + " * " + PLAN_HEADER_MISC_ACRONYMS + "        ->",
        print(colored(PLAN_HEADER_MISC_ACRONYMS_S, "magenta", attrs = [])),
        print "|",
        print(colored(PLAN_HEADER_MISC_ACRONYMS_L, "magenta", attrs = []))
        # Bibliography
        print " " * 8 + " * " + PLAN_HEADER_MISC_BIBLIOGRAPHY + "    ->",
        print(colored(PLAN_HEADER_MISC_BIBLIOGRAPHY_S, "magenta", attrs = [])),
        print "|",
        print(colored(PLAN_HEADER_MISC_BIBLIOGRAPHY_L, "magenta", attrs = []))
        # Glossary
        print " " * 8 + " * " + PLAN_HEADER_MISC_GLOSSARY + "        ->",
        print(colored(PLAN_HEADER_MISC_GLOSSARY_S, "magenta", attrs = [])),
        print "|",
        print(colored(PLAN_HEADER_MISC_GLOSSARY_L, "magenta", attrs = []))
        print(colored("-" * 64 + "\n", "blue", attrs = ["bold"]))

    def show_process_step(self, nstep, text):
        r"""Show a header of the main report creating process

        nstep: step number of the main report creating process
        text: the text to print

        """
        print(colored("[" + str(nstep) + "/" + STEP_MAX_MAIN + "] " + text, "blue", attrs = ["bold"]))
        print(colored("-" * 64 + "\n", "blue", attrs = ["bold"]))

    def show_reportex_header(self):
        r"""Print the ReporTeX header
        """
        print(colored("~" * 64, "white", attrs = ["bold"]))
        print(colored(RPTX_NAME, "white", attrs = ["bold"])),
        print(colored("- " + RPTX_DESCRIPTION, "white", attrs = []))
        print(colored("~" * 64, "white", attrs = ["bold"]))
        print(colored("For help or information, visit:", "white", attrs = []))
        print(colored(" " * 4 + "* " + RPTX_AUTHOR_WEBSITE, "white", attrs = []))
        print(colored(" " * 4 + "* " + RPTX_REPO, "white", attrs = []))
        print(colored(RPTX_NAME + " is under the " + RPTX_LICENSE, "white", attrs = []))
        print(colored("~" * 64, "white", attrs = ["bold"]))
        print

    def show_step_generation(self, ngeneration, nsub, submax, text):
        r"""Show an information of the current step during the generation of folders and document writing

        ngeneration: step number of the generation process
        nsub: substep number of the generation process
        submax: max of substeps of the generation process
        text: the text to print

        """
        print(colored("[3/" + STEP_MAX_MAIN + "]", "blue", attrs = ["bold"]) + \
              colored("[" + str(ngeneration) + "/" + STEP_MAX_GENERATION + "]", "cyan", attrs = ["bold"]) + \
              colored("[" + str(nsub) + "/" + submax + "] ", "yellow", attrs = ["bold"]) + \
              colored(text, "yellow", attrs = []))


########################################################################################## 
class Report:
    r"""A class for a Report
    """

    def make(self):
        r"""Make a report

        Main function which creates a report
        Process:
            * Collect the properties (author, date, etc.)
            * Collect the plan (chapters, sections, etc.)
            * Create the files and folders
            * Set the values for specific elements (Bibliography, Glossary, etc.)
            * Write the different parts in the main file (Header, Prelims, Tables, etc.)

        """
        builder = Builder()
        helper = Helper()
        setter = Setter()
        writer = Writer()
        ## [1/3] Collect properties
        panf, panl, pdate, pcomp, psnf, psnl, pttl, psttl = builder.collect_properties()
        ## [2/3] Collect plan
        plan = builder.collect_plan()
        ## [3/3] Create main file and folders
        # Show header
        helper.show_reportex_header()
        helper.show_process_step(3, STEP_TITLE_MAIN_3)
        # Create folders
        report = builder.create_report()
        freport = builder.create_freport()
        fchapters = builder.create_fchapters()
        fprelims = builder.create_fprelims()
        fback = builder.create_fback()
        fassets = builder.create_fassets()
        # Setting values for specific elements
        sacr, sbib, sglo = setter.set_references(plan)
        # Writing the different parts
        builder.write_header(report, freport, fchapters, fprelims, fback, plan, sacr, sbib, sglo, panf, panl, pdate, pcomp, psnf, psnl, pttl, psttl)
        helper.show_step_generation(2, 2, STEP_MAX_DOCUMENT, STEP_INFO_DDOCBEGIN)
        writer.latex_command(report, LTX_CMD_BEGIN, LTX_CMD_DOC, "\n")
        builder.write_prelims(report, freport, fchapters, fprelims, fback, plan, sacr, sbib, sglo, panf, panl, pdate, pcomp, psnf, psnl, pttl, psttl)
        builder.write_tables(report, freport, fchapters, fprelims, fback, plan, sacr, sbib, sglo, panf, panl, pdate, pcomp, psnf, psnl, pttl, psttl)
        builder.write_body(report, freport, fchapters, fprelims, fback, plan, sacr, sbib, sglo, panf, panl, pdate, pcomp, psnf, psnl, pttl, psttl)
        builder.write_back(report, freport, fchapters, fprelims, fback, plan, sacr, sbib, sglo, panf, panl, pdate, pcomp, psnf, psnl, pttl, psttl)
        helper.show_step_generation(2, 7, STEP_MAX_DOCUMENT, STEP_INFO_DDOCEND)
        writer.latex_command(report, LTX_CMD_END, LTX_CMD_DOC, "\n")
        # Last info
        helper.show_last_info()


#####################################################################################
class Builder(Report):
    def collect_properties(self):
        r"""Collect properties

        Collect and assemble properties
        Give an overview
        Ask user for validation
        Return the following values:
            * author_name_first: the value for the Author first name
            * author_name_last: the value for the Author last name
            * date: the value for the Date
            * company: the value for the Company
            * supervisor_name_first: the value for the Supervisor first name
            * supervisor_name_last: the value for the Supervisor last name
            * title: the value for the Title
            * subtitle: the value for the Subtitle

        """
        assembler = Assembler()
        checker = Checker()
        cleaner = Cleaner()
        dicochecker = Dicochecker()
        helper = Helper()
        overviewer = Overviewer()
        # Print headers
        helper.show_reportex_header()
        helper.show_process_step(1, STEP_TITLE_MAIN_1)
        # Collect properties
        rptx_properties = assembler.assemble_properties()
        # Overview properties
        print
        overviewer.show_properties(rptx_properties)
        # Valid properties
        while True:
            checking_answer_value = checker.ask(MSG_TEXT_ANSWERS_CHECKING, CKR_ANS_YES)
            # Answer 'y'
            if checking_answer_value == True:
                break
            # Answer 'n'
            elif checking_answer_value == False:
                # Clean the screen
                cleaner.clean()
                # Print headers
                helper.show_reportex_header()
                helper.show_process_step(1, STEP_TITLE_MAIN_1)
                # Collect properties
                rptx_properties = assembler.assemble_properties()
                # Overview properties
                print
                overviewer.show_properties(rptx_properties)
            # Answer 'misc'
            else:
                err_checking_answer_value = Messager(MSG_KIND_ERROR, "", MSG_TEXT_ERROR_CHECKING_ANSWER_VALUE)
                err_checking_answer_value.show()
        # Clean the screen
        cleaner.clean()
        # Assigning properties
        author_name_first = dicochecker.value(rptx_properties, HDR_DICT_AUTHOR_NAME_FIRST)
        author_name_last = dicochecker.value(rptx_properties, HDR_DICT_AUTHOR_NAME_LAST)
        date = dicochecker.value(rptx_properties, HDR_DICT_DATE)
        company = dicochecker.value(rptx_properties, HDR_DICT_COMPANY)
        supervisor_name_first = dicochecker.value(rptx_properties, HDR_DICT_SUPERVISOR_NAME_FIRST)
        supervisor_name_last = dicochecker.value(rptx_properties, HDR_DICT_SUPERVISOR_NAME_LAST)
        title = dicochecker.value(rptx_properties, HDR_DICT_TITLE)
        subtitle = dicochecker.value(rptx_properties, HDR_DICT_SUBTITLE)
        return (author_name_first, author_name_last, date, company, supervisor_name_first, supervisor_name_last, title, subtitle)

    def collect_plan(self):
        r"""Collect plan

        Print help for plan inputs
        Collect and assemble plan
        Give an overview
        Ask user for validation

        """
        assembler = Assembler()
        checker = Checker()
        cleaner = Cleaner()
        helper = Helper()
        overviewer = Overviewer()
        # Print headers and help
        helper.show_reportex_header()
        helper.show_process_step(2, STEP_TITLE_MAIN_2)
        helper.show_plan_help()
        # Collect plan
        rptx_plan = assembler.assemble_plan()
        # Overview plan
        print
        overviewer.show_plan(rptx_plan)
        # Valid plan
        while True:
            checking_answer_value = checker.ask(MSG_TEXT_ANSWERS_CHECKING, CKR_ANS_YES)
            # Answer 'y'
            if checking_answer_value == True:
                break
            # Answer 'n'
            elif checking_answer_value == False:
                # Clean the screen
                cleaner.clean()
                # Print headers and help
                helper.show_reportex_header()
                helper.show_process_step(2, STEP_TITLE_MAIN_2)
                helper.show_plan_help()
                # Collect plan
                rptx_plan = assembler.assemble_plan()
                # Overview plan
                print
                overviewer.show_plan(rptx_plan)
            # Answer 'misc'
            else:
                err_checking_answer_value = Messager(MSG_KIND_ERROR, "", MSG_TEXT_ERROR_CHECKING_ANSWER_VALUE)
                err_checking_answer_value.show()
        # Clean the screen
        cleaner.clean()
        return rptx_plan

    def create_fassets(self):
        """Create the assets folder, return its full path, and create the subfolders

        Subfolders created
            * codes/
            * graphics/
            * images/
            * tables/

        """
        helper = Helper()
        helper.show_step_generation(1, 6, STEP_MAX_FOLDERS, STEP_INFO_FASSETS)
        assets_folder = Folder(FLDR_ASSETS, PATH_RPTX_REPORT)
        assets_folder.make()
        assets_folder_name = assets_folder.get_path_full()
        # Subfolder 'codes/'
        codes_folder = Folder(FLDR_CODES, PATH_RPTX_REPORT + FLDR_ASSETS)
        codes_folder.make()
        # Subfolder 'graphics/'
        graphics_folder = Folder(FLDR_GRAPHICS, PATH_RPTX_REPORT + FLDR_ASSETS)
        graphics_folder.make()
        # Subfolder 'images/
        images_folder = Folder(FLDR_IMAGES, PATH_RPTX_REPORT + FLDR_ASSETS)
        images_folder.make()
        # Subfolder 'tables/'
        tables_folder = Folder(FLDR_TABLES, PATH_RPTX_REPORT + FLDR_ASSETS)
        tables_folder.make()
        return assets_folder_name

    def create_fback(self):
        r"""Create the back folder and return its full path
        """
        helper = Helper()
        helper.show_step_generation(1, 5, STEP_MAX_FOLDERS, STEP_INFO_FBACK)
        back_folder = Folder(FLDR_BACK, PATH_RPTX_REPORT)
        back_folder.make()
        back_folder_name = back_folder.get_path_full()
        return back_folder_name

    def create_fchapters(self):
        r"""Create the chapters folder and return its full path
        """
        helper = Helper()
        helper.show_step_generation(1, 3, STEP_MAX_FOLDERS, STEP_INFO_FCHAPTERS)
        chapters_folder = Folder(FLDR_CHAPTERS, PATH_RPTX_REPORT)
        chapters_folder.make()
        chapters_folder_name = chapters_folder.get_path_full()
        return chapters_folder_name

    def create_fprelims(self):
        r"""Create the prelims folder and return its full path
        """
        helper = Helper()
        helper.show_step_generation(1, 4, STEP_MAX_FOLDERS, STEP_INFO_FPRELIMS)
        prelims_folder = Folder(FLDR_PRELIMS, PATH_RPTX_REPORT)
        prelims_folder.make()
        prelims_folder_name = prelims_folder.get_path_full()
        return prelims_folder_name

    def create_freport(self):
        r"""Create the main folder
        """
        helper = Helper()
        helper.show_step_generation(1, 2, STEP_MAX_FOLDERS, STEP_INFO_FREPORT)
        report_folder = Folder(FLDR_REPORT, PATH_RPTX_MAIN)
        report_folder.make()

    def create_report(self):
        r"""Create the report main file and return it opened
        """
        helper = Helper()
        helper.show_step_generation(1, 1, STEP_MAX_FOLDERS, STEP_INFO_REPORT)
        report_main_file = File(RPTX_MAIN_FILE, PATH_RPTX_MAIN_FILE)
        report_main_file.make()
        report_main_file_name = report_main_file.get_path_full()
        report_main_file = open(report_main_file_name, "w")
        return report_main_file

    def download_class(self):
        r"""Download the ReporTeX class
        """
        downloader = Downloader(RPTX_CLASS_FILE, PATH_RPTX_CLASS_FILE)
        downloader.download(URL_REPORTEX_CLASS)

    def write_back(self, report, freport, fchapters, fprelims, fback, plan, sacr, sbib, sglo, panf, panl, pdate, pcomp, psnf, psnl, pttl, psttl):
        r"""Write the Back

        report: the main file where header will be written
        freport: the report main folder
        fchapters: the chapters folder
        fprelims: the prelims folder
        fback: the back folder
        plan: the plan containing the order of chapters
        sacr: the setting for the acronyms
        sbib: the setting for the bibliography
        sglo: the setting for the glossary
        panf: the property for the author first name
        panl: the property for the author last name
        pdate: the property for the date
        pcomp: the property for the company
        psnf: the property for the supervisor first name
        psnl: the property for the supervisor last name
        pttl: the property for the title
        psttl: the property for the subtitle

        """
        helper = Helper()
        helper.show_step_generation(2, 6, STEP_MAX_DOCUMENT, STEP_INFO_DBACK)
        back = Back(report, freport, fchapters, fprelims, fback, plan, sacr, sbib, sglo, panf, panl, pdate, pcomp, psnf, psnl, pttl, psttl)
        back.build()

    def write_body(self, report, freport, fchapters, fprelims, fback, plan, sacr, sbib, sglo, panf, panl, pdate, pcomp, psnf, psnl, pttl, psttl):
        r"""Write the Body

        report: the main file where header will be written
        freport: the report main folder
        fchapters: the chapters folder
        fprelims: the prelims folder
        fback: the back folder
        plan: the plan containing the order of chapters
        sacr: the setting for the acronyms
        sbib: the setting for the bibliography
        sglo: the setting for the glossary
        panf: the property for the author first name
        panl: the property for the author last name
        pdate: the property for the date
        pcomp: the property for the company
        psnf: the property for the supervisor first name
        psnl: the property for the supervisor last name
        pttl: the property for the title
        psttl: the property for the subtitle

        """
        helper = Helper()
        helper.show_step_generation(2, 5, STEP_MAX_DOCUMENT, STEP_INFO_DBODY)
        body = Body(report, freport, fchapters, fprelims, fback, plan, sacr, sbib, sglo, panf, panl, pdate, pcomp, psnf, psnl, pttl, psttl)
        body.build()

    def write_header(self, report, freport, fchapters, fprelims, fback, plan, sacr, sbib, sglo, panf, panl, pdate, pcomp, psnf, psnl, pttl, psttl):
        r"""Write the Header

        report: the main file where header will be written
        freport: the report main folder
        fchapters: the chapters folder
        fprelims: the prelims folder
        fback: the back folder
        plan: the plan containing the order of chapters
        sacr: the setting for the acronyms
        sbib: the setting for the bibliography
        sglo: the setting for the glossary
        panf: the property for the author first name
        panl: the property for the author last name
        pdate: the property for the date
        pcomp: the property for the company
        psnf: the property for the supervisor first name
        psnl: the property for the supervisor last name
        pttl: the property for the title
        psttl: the property for the subtitle

        """
        helper = Helper()
        helper.show_step_generation(2, 1, STEP_MAX_DOCUMENT, STEP_INFO_DHEADER)
        header = Header(report, freport, fchapters, fprelims, fback, plan, sacr, sbib, sglo, panf, panl, pdate, pcomp, psnf, psnl, pttl, psttl)
        header.build()

    def write_prelims(self, report, freport, fchapters, fprelims, fback, plan, sacr, sbib, sglo, panf, panl, pdate, pcomp, psnf, psnl, pttl, psttl):
        r"""Write the Prelims

        report: the main file where header will be written
        freport: the report main folder
        fchapters: the chapters folder
        fprelims: the prelims folder
        fback: the back folder
        plan: the plan containing the order of chapters
        sacr: the setting for the acronyms
        sbib: the setting for the bibliography
        sglo: the setting for the glossary
        panf: the property for the author first name
        panl: the property for the author last name
        pdate: the property for the date
        pcomp: the property for the company
        psnf: the property for the supervisor first name
        psnl: the property for the supervisor last name
        pttl: the property for the title
        psttl: the property for the subtitle

        """
        helper = Helper()
        helper.show_step_generation(2, 3, STEP_MAX_DOCUMENT, STEP_INFO_DPRELIMS)
        prelims = Prelims(report, freport, fchapters, fprelims, fback, plan, sacr, sbib, sglo, panf, panl, pdate, pcomp, psnf, psnl, pttl, psttl)
        prelims.build()

    def write_tables(self, report, freport, fchapters, fprelims, fback, plan, sacr, sbib, sglo, panf, panl, pdate, pcomp, psnf, psnl, pttl, psttl):
        r"""Write the Tables

        report: the main file where header will be written
        freport: the report main folder
        fchapters: the chapters folder
        fprelims: the prelims folder
        fback: the back folder
        plan: the plan containing the order of chapters
        sacr: the setting for the acronyms
        sbib: the setting for the bibliography
        sglo: the setting for the glossary
        panf: the property for the author first name
        panl: the property for the author last name
        pdate: the property for the date
        pcomp: the property for the company
        psnf: the property for the supervisor first name
        psnl: the property for the supervisor last name
        pttl: the property for the title
        psttl: the property for the subtitle

        """
        helper = Helper()
        helper.show_step_generation(2, 4, STEP_MAX_DOCUMENT, STEP_INFO_DTABLES)
        tables = Tables(report, freport, fchapters, fprelims, fback, plan, sacr, sbib, sglo, panf, panl, pdate, pcomp, psnf, psnl, pttl, psttl)
        tables.build()


#####################################################################################
class Collector(Report):
    r"""Collector: A class for Properties and Date
    """


################################################################################
class Assembler(Collector):
    r"""Assembler: assemble informtion
    """
    def assemble_plan(self):
        r"""Collect and assemble the plan and return it

        Count automatically the numbers of chapters/sections/subsections
        If selected, add automatically:
            * Acknowledgments
            * Abstract
            * List of Figures
            * List of Tables
            * Glossary
            * Bibliography
            * Appendixes
        Remove empty elements
        Add prelims or back elements
        Order the final plan (prelims, body, back)
        For adding a chapter/section/subsection:
            * Zero fill the counter
            * Select only the title
                * If the title is empty; pass
                * Else, add the chapter/section/subsection and increase the counter
        """
        plan = []
        plan_sorted = []
        list_prelims = []
        list_body = []
        list_back = []
        spellchecker = Spellchecker()
        cnt_chapter = 1
        cnt_section = 1
        cnt_subsection = 1
        exit_status = False
        while True:
            new_element = raw_input(colored("> ", "blue", attrs = ["bold"]))
            new_element_corrected_1 = spellchecker.remove_space_duplicated(new_element)
            new_element_corrected_2 = spellchecker.remove_space_leadend(new_element_corrected_1)
            first_char = new_element_corrected_2[:1]
            second_char = new_element_corrected_2[1:2]

            # Chapters
            if first_char == PLAN_ESCAPE_BODY_LEVEL_MORE:
                # Typing error
                if second_char:
                    pass
                else:
                    while True:
                        new_chapter = raw_input(colored(">", "blue", attrs = []) + colored("> ", "blue", attrs = ["bold"]))
                        new_chapter_corrected_1 = spellchecker.remove_space_duplicated(new_chapter)
                        new_chapter_corrected_2 = spellchecker.remove_space_leadend(new_chapter_corrected_1)
                        first_char = new_chapter_corrected_2[:1]
                        second_char = new_chapter_corrected_2[1:2]
                        # Exit plan definition
                        if new_chapter_corrected_2 == PLAN_ESCAPE_REPORT:
                            exit_status = True
                            break
                        # Exit the current level
                        if first_char == PLAN_ESCAPE_BODY_LEVEL_LESS:
                            break

                        # Sections
                        elif first_char == PLAN_ESCAPE_BODY_LEVEL_MORE:
                            # Typing error
                            if second_char:
                                pass
                            else:
                                cnt_chapter -= 1
                                while True:
                                    new_section = raw_input(colored(">>", "blue", attrs = []) + colored("> ", "blue", attrs = ["bold"]))
                                    new_section_corrected_1 = spellchecker.remove_space_duplicated(new_section)
                                    new_section_corrected_2 = spellchecker.remove_space_leadend(new_section_corrected_1)
                                    first_char = new_section_corrected_2[:1]
                                    second_char = new_section_corrected_2[1:2]
                                    # Exit plan definition
                                    if new_section_corrected_2 == PLAN_ESCAPE_REPORT:
                                        exit_status = True
                                        break
                                    # Exit the current level
                                    if first_char == PLAN_ESCAPE_BODY_LEVEL_LESS:
                                        cnt_chapter += 1
                                        break

                                    # Subsections
                                    elif first_char == PLAN_ESCAPE_BODY_LEVEL_MORE:
                                        # Typing error
                                        if second_char:
                                            pass
                                        else:
                                            cnt_section -= 1
                                            while True:
                                                new_subsection = raw_input(colored(">>>", "blue", attrs = []) + colored("> ", "blue", attrs = ["bold"]))
                                                new_subsection_corrected_1 = spellchecker.remove_space_duplicated(new_subsection)
                                                new_subsection_corrected_2 = spellchecker.remove_space_leadend(new_subsection_corrected_1)
                                                first_char = new_subsection_corrected_2[:1]
                                                second_char = new_subsection_corrected_2[1:2]
                                                # Exit plan definition
                                                if new_subsection_corrected_2 == PLAN_ESCAPE_REPORT:
                                                    exit_status = True
                                                    break
                                                # Exit the current level
                                                if first_char == PLAN_ESCAPE_BODY_LEVEL_LESS:
                                                    cnt_section += 1
                                                    break
                                                # Add Subsections
                                                else:
                                                    line_subsection = str(cnt_chapter).zfill(PLAN_NUMBER_WIDTH) + PLAN_DELIMITER_SIMPLE + \
                                                                    str(cnt_section).zfill(PLAN_NUMBER_WIDTH) + PLAN_DELIMITER_SIMPLE + \
                                                                    str(cnt_subsection).zfill(PLAN_NUMBER_WIDTH) + PLAN_DELIMITER_DOUBLE + \
                                                                    new_subsection_corrected_2
                                                    matcher_subsection = Matcher(r'(.*)' + PLAN_DELIMITER_DOUBLE + '(.*)', line_subsection)
                                                    subsection_title = matcher_subsection.get_last_group()
                                                    if not subsection_title:
                                                        pass
                                                    else:
                                                        plan.append(line_subsection)
                                                        cnt_subsection += 1
                                        # Exit plan definition
                                        if exit_status:
                                            break

                                    # Add Sections
                                    else:
                                        line_section = str(cnt_chapter).zfill(PLAN_NUMBER_WIDTH) + PLAN_DELIMITER_SIMPLE + \
                                                    str(cnt_section).zfill(PLAN_NUMBER_WIDTH) + PLAN_DELIMITER_DOUBLE + \
                                                    new_section_corrected_2
                                        matcher_section = Matcher(r'(.*)' + PLAN_DELIMITER_DOUBLE + '(.*)', line_section)
                                        section_title = matcher_section.get_last_group()
                                        if not section_title:
                                            pass
                                        else:
                                            plan.append(line_section)
                                            cnt_section += 1
                            # Exit plan definition
                            if exit_status:
                                break
                        # Add Chapters
                        else:
                            line_chapter = str(cnt_chapter).zfill(PLAN_NUMBER_WIDTH) + PLAN_DELIMITER_DOUBLE + \
                                        new_chapter_corrected_2
                            matcher_chapter = Matcher(r'(.*)' + PLAN_DELIMITER_DOUBLE + '(.*)', line_chapter)
                            chapter_title = matcher_chapter.get_last_group()
                            if not chapter_title:
                                pass
                            else:
                                plan.append(line_chapter)
                                cnt_chapter += 1

            # Miscellaneous elements
            if first_char == PLAN_ESCAPE_MISC_LEVEL_MORE:
                # Typing error

                # Prelims
                if second_char == PLAN_ESCAPE_MISC_PRELIMS:
                    while True:
                        new_misc_prelims = raw_input(colored("+p", "blue", attrs = []) + colored("> ", "blue", attrs = ["bold"]))
                        new_misc_prelims_corrected_1 = spellchecker.remove_space_duplicated(new_misc_prelims)
                        new_misc_prelims_corrected_2 = spellchecker.remove_space_leadend(new_misc_prelims_corrected_1)
                        first_char = new_misc_prelims_corrected_2[:1]
                        # Exit plan definition
                        if new_misc_prelims_corrected_2 == PLAN_ESCAPE_REPORT:
                            exit_status = True
                            break
                        # Exit the current level
                        if first_char == PLAN_ESCAPE_MISC_LEVEL_LESS:
                            break
                        # Avoid faults typing (`<`: exit the current level)
                        elif first_char == PLAN_ESCAPE_BODY_LEVEL_LESS:
                            break
                        # Avoid faults typing (`>`: do nothing)
                        elif first_char == PLAN_ESCAPE_BODY_LEVEL_MORE:
                            pass
                        # Add prelims elements
                        else:
                            line_misc_prelims = PLAN_ID_MISC_PRELIMS + PLAN_DELIMITER_DOUBLE + \
                                                new_misc_prelims_corrected_2
                            matcher_misc_prelims =  Matcher(r'(.*)' + PLAN_DELIMITER_DOUBLE + '(.*)', line_misc_prelims)
                            misc_prelims_title = matcher_misc_prelims.get_last_group()
                            if not misc_prelims_title:
                                pass
                            else:
                                plan.append(line_misc_prelims)

                # Back
                elif second_char == PLAN_ESCAPE_MISC_BACK:
                    while True:
                        new_misc_back = raw_input(colored("+b", "blue", attrs = []) + colored("> ", "blue", attrs = ["bold"]))
                        new_misc_back_corrected_1 = spellchecker.remove_space_duplicated(new_misc_back)
                        new_misc_back_corrected_2 = spellchecker.remove_space_leadend(new_misc_back_corrected_1)
                        first_char = new_misc_back_corrected_2[:1]
                        # Exit plan definition
                        if new_misc_back_corrected_2 == PLAN_ESCAPE_REPORT:
                            exit_status = True
                            break
                        # Exit the current level
                        if first_char == PLAN_ESCAPE_MISC_LEVEL_LESS:
                            break
                        # Avoid faults typing (`<`: exit the current level)
                        elif first_char == PLAN_ESCAPE_BODY_LEVEL_LESS:
                            break
                        # Avoid faults typing (`>`: do nothing)
                        elif first_char == PLAN_ESCAPE_BODY_LEVEL_MORE:
                            pass
                        # Add back elements
                        else:
                            line_misc_back = PLAN_ID_MISC_BACK + PLAN_DELIMITER_DOUBLE + \
                                             new_misc_back_corrected_2
                            matcher_misc_back =  Matcher(r'(.*)' + PLAN_DELIMITER_DOUBLE + '(.*)', line_misc_back)
                            misc_back_title = matcher_misc_back.get_last_group()
                            if not misc_back_title:
                                pass
                            else:
                                plan.append(line_misc_back)

                # Already defined
                elif second_char == PLAN_ESCAPE_MISC_LEVEL_MORE:
                    while True:
                        new_misc = raw_input(colored("+", "blue", attrs = []) + colored("> ", "blue", attrs = ["bold"]))
                        new_misc_corrected_1 = spellchecker.remove_space_duplicated(new_misc)
                        new_misc_corrected_2 = spellchecker.remove_space_leadend(new_misc_corrected_1)
                        first_char = new_misc_corrected_2[:1]
                        # Exit plan definition
                        if new_misc_corrected_2 == PLAN_ESCAPE_REPORT:
                            exit_status = True
                            break
                        # Exit the current level
                        if first_char == PLAN_ESCAPE_MISC_LEVEL_LESS:
                            break
                        # Avoid faults typing (`<`: exit the current level)
                        elif first_char == PLAN_ESCAPE_BODY_LEVEL_LESS:
                            break
                        # Avoid faults typing (`>`: do nothing)
                        elif first_char == PLAN_ESCAPE_BODY_LEVEL_MORE:
                            pass
                        # Add miscellaneous elements
                        else:
                            # Abstract
                            if new_misc_corrected_2 == PLAN_HEADER_MISC_ABSTRACT_S or new_misc_corrected_2 == PLAN_HEADER_MISC_ABSTRACT_L:
                                line_misc_abstract = PLAN_ID_MISC_PRELIMS + PLAN_DELIMITER_DOUBLE + \
                                                     PLAN_HEADER_MISC_ABSTRACT
                                plan.append(line_misc_abstract)
                            # Acknowledgments
                            elif new_misc_corrected_2 == PLAN_HEADER_MISC_ACKNOWLEDGMENTS_S or new_misc_corrected_2 == PLAN_HEADER_MISC_ACKNOWLEDGMENTS_L:
                                line_misc_acknowledgments = PLAN_ID_MISC_PRELIMS + PLAN_DELIMITER_DOUBLE + \
                                                            PLAN_HEADER_MISC_ACKNOWLEDGMENTS
                                plan.append(line_misc_acknowledgments)
                            # Acronyms
                            elif new_misc_corrected_2 == PLAN_HEADER_MISC_ACRONYMS_S or new_misc_corrected_2 == PLAN_HEADER_MISC_ACRONYMS_L:
                                line_misc_acronyms = PLAN_ID_MISC_PRELIMS + PLAN_DELIMITER_DOUBLE + \
                                                         PLAN_HEADER_MISC_ACRONYMS
                                plan.append(line_misc_acronyms)
                            # Glossary
                            elif new_misc_corrected_2 == PLAN_HEADER_MISC_GLOSSARY_S or new_misc_corrected_2 == PLAN_HEADER_MISC_GLOSSARY_L:
                                line_misc_glossary = PLAN_ID_MISC_PRELIMS + PLAN_DELIMITER_DOUBLE + \
                                                         PLAN_HEADER_MISC_GLOSSARY
                                plan.append(line_misc_glossary)
                            # Bibliography
                            elif new_misc_corrected_2 == PLAN_HEADER_MISC_BIBLIOGRAPHY_S or new_misc_corrected_2 == PLAN_HEADER_MISC_BIBLIOGRAPHY_L:
                                line_misc_bibliography = PLAN_ID_MISC_BACK + PLAN_DELIMITER_DOUBLE + \
                                                         PLAN_HEADER_MISC_BIBLIOGRAPHY
                                plan.append(line_misc_bibliography)
                # Typing fault
                else:
                    pass

            # Exit plan definition
            if new_element_corrected_2 == PLAN_ESCAPE_REPORT:
                break
            elif exit_status:
                break
            else:
                pass

        # Remove empty elements
        listerchecker = Listchecker()
        plan_no_empty_elements = listerchecker.remove_empty_elements(plan)

        # Put elements in a specific list
        for item in plan:
            if item[:2] == PLAN_ID_MISC_PRELIMS:
                list_prelims.append(item)
            elif item[:2] == PLAN_ID_MISC_BACK:
                list_back.append(item)
            else:
                list_body.append(item)
        # Order the final plan
        for item in list_prelims:
            plan_sorted.append(item)
        for item in list_body:
            plan_sorted.append(item)
        for item in list_back:
            plan_sorted.append(item)
        return plan_sorted

    def assemble_properties(self):
        r"""Collect, assemble all the properties, and gathering it into a dictionary
        
        Author (First name / Last name)
        Date
        Company
        Supervisor (First name / Last name)
        Titles

        Return the dictionary 'rptx_properties'
        """
        getter = Getter()
        # Collecting
        rptx_author_name_first = getter.get_details(HDR_PROP_AUTHOR_NAME_FIRST, LMT_AUTHOR_NAME_FIRST)
        rptx_author_name_last = getter.get_details(HDR_PROP_AUTHOR_NAME_LAST, LMT_AUTHOR_NAME_LAST)
        rptx_date = getter.get_date()
        rptx_company = getter.get_details(HDR_PROP_COMPANY, LMT_COMPANY)
        rptx_supervisor_name_first = getter.get_details(HDR_PROP_SUPERVISOR_NAME_FIRST, LMT_SUPERVISOR_NAME_FIRST)
        rptx_supervisor_name_last = getter.get_details(HDR_PROP_SUPERVISOR_NAME_LAST, LMT_SUPERVISOR_NAME_LAST)
        rptx_title = getter.get_details(HDR_PROP_TITLE, LMT_TITLE)
        rptx_subtitle = getter.get_details(HDR_PROP_SUBTITLE, LMT_SUBTITLE)
        # Gathering
        rptx_properties = {}
        rptx_properties[HDR_DICT_AUTHOR_NAME_FIRST] = rptx_author_name_first
        rptx_properties[HDR_DICT_AUTHOR_NAME_LAST] = rptx_author_name_last
        rptx_properties[HDR_DICT_DATE] = rptx_date
        rptx_properties[HDR_DICT_COMPANY] = rptx_company
        rptx_properties[HDR_DICT_SUPERVISOR_NAME_FIRST] = rptx_supervisor_name_first
        rptx_properties[HDR_DICT_SUPERVISOR_NAME_LAST] = rptx_supervisor_name_last
        rptx_properties[HDR_DICT_TITLE] = rptx_title
        rptx_properties[HDR_DICT_SUBTITLE] = rptx_subtitle
        return rptx_properties


################################################################################
class Getter(Collector):
    def get_date(self):
        r"""Get the date and check for the format for creating the report
        """
        while True:
            date = raw_input(colored("%s: " %(HDR_PROP_DATE), "blue", attrs = ["bold"]))
            try:
                date_parsed = strptime(date, "%d/%m/%Y")
            except ValueError as e:
                err_date_format = Messager(MSG_KIND_ERROR, "", MSG_TEXT_ERROR_DATE_FORMAT)
                err_date_format.show()
            else:
                # Select only year, month, day
                date_year = date_parsed[:1]
                date_month = date_parsed[1:2]
                date_day = date_parsed[2:3]
                # Convert to string
                date_year_formatted = str(date_year)
                date_month_formatted = str(date_month)
                date_day_formatted = str(date_day)
                # Delete characters from strptime ('(', ')', ',')
                # Pad the month and the day with '0' to fill width
                date_year_corrected = date_year_formatted[1:-2]
                date_month_corrected = date_month_formatted[1:-2].zfill(2)
                date_day_corrected = date_day_formatted[1:-2].zfill(2)
                # Format 'dd/mm/yyyy'
                date_corrected = date_day_corrected + "/" + date_month_corrected + "/" + date_year_corrected
                return date_corrected

    def get_details(self, header, limit):
        r"""Get details about the author, the company, titles, etc.

        header: the text before user input
        limit: maximum number of characters for an entry

        """
        info = raw_input(colored("%s: " %(header), "cyan", attrs = ["bold"]))
        info_truncated = info[:limit]
        spellchecker = Spellchecker()
        info_corrected_1 = spellchecker.remove_space_duplicated(info_truncated)
        info_corrected_2 = spellchecker.remove_space_leadend(info_corrected_1)
        return info_corrected_2


################################################################################
class Setter(Collector):
    r""""""
    def set_references(self, plan):
        r"""Set a on/off value to an element

        plan: entries typed by the user

        Return the following values:
            * acr_value: the value for the Acronyms
            * bib_value: the value for the Bibliography
            * glo_value: the value for the Glossary

        """
        acr_value = False
        bib_value = False
        glo_value = False
        for element in plan:
            matcher = Matcher(r'(.*)' + PLAN_DELIMITER_DOUBLE + '(.*)', element)
            element_id = matcher.get_first_group()
            element_id_length = len(element_id)
            element_title = matcher.get_last_group()
            first_char = element_id[:1]
            second_char = element_id[1:2]
            
            if first_char == PLAN_ID_MISC:
                # Prelims
                if second_char == PLAN_ID_MISC_PRELIMS[1:2]:
                    # ON Acronyms
                    if element_title == PLAN_HEADER_MISC_ACRONYMS:
                        acr_value = True
                    # ON Glossary
                    elif element_title == PLAN_HEADER_MISC_GLOSSARY:
                        glo_value = True
                # Back
                elif second_char == PLAN_ID_MISC_BACK[1:2]:
                    # ON Bibliography
                    if element_title == PLAN_HEADER_MISC_BIBLIOGRAPHY:
                        bib_value = True
                # OFF Values
                else:
                    acr_value = False
                    bib_value = False
                    glo_value = False
        return (acr_value, bib_value, glo_value)


#####################################################################################
class Matter(Report):
    r"""A class for the report's matter
    """
    def __init__(self, report, freport, fchapters, fprelims, fback, plan, sacr, sbib, sglo, panf, panl, pdate, pcomp, psnf, psnl, pttl, psttl):
        r"""Matter initialization

        report: the report main file
        freport: the report main folder
        fchapters: the chapters folder
        fprelims: the prelims folder
        fback: the back folder
        plan: the plan containing the order of chapters
        sacr: the setting for the acronyms
        sbib: the setting for the bibliography
        sglo: the setting for the glossary
        panf: the property for the author first name
        panl: the property for the author last name
        pdate: the property for the date
        pcomp: the property for the company
        psnf: the property for the supervisor first name
        psnl: the property for the supervisor last name
        pttl: the property for the title
        psttl: the property for the subtitle

        """
        self._report = report
        self._freport = freport
        self._fchapters = fchapters
        self._fprelims = fprelims
        self._fback = fback
        self._plan = plan
        self._sacr = sacr
        self._sbib = sbib
        self._sglo = sglo
        self._panf = panf
        self._panl = panl
        self._pdate = pdate
        self._pcomp = pcomp
        self._psnf = psnf
        self._psnl = psnl
        self._pttl = pttl
        self._psttl = psttl


################################################################################
class Back(Matter):
    r"""A class for the Back of the report
    """
    def build(self):
        r"""Build the Back
        """
        # Write the comment header
        writer = Writer()
        writer.blank_line(self._report, 1)
        writer.latex_comment_header(self._report, LTX_CMT_HDR_BACK)
        # Write the entries
        self._write_entries()
        # Write the Bibliography if chosen
        if self._sbib:
            self._create_bibliography()
        else:
            pass

    def _create_bibliography(self):
        r"""Create an entry for the Bibliography in Back
        """
        writer = Writer()
        writer.latex_comment(self._report, 2, LTX_CMT_BACK_BIBLIOGRAPHY)
        writer.latex_command_simple(self._report, LTX_CMD_PRINTBIBLIOGRAPHY, "\n")
        writer.latex_command(self._report, LTX_CMD_ADD_CONTENTS_LINE, LTX_START_CHAR_CMD + LTX_CMD_NUMBERLINE + "{}" + LTX_CMD_HSPACE + "{-1.5em}" + PLAN_BACK_BIBLIOGRAPHY, "\n")
        writer.latex_command_simple(self._report, LTX_CMD_CLEARDOUBLEPAGE, "\n\n")

    def _create_entry(self, item):
        r"""Create an entry in Back

        item: the item of the plan

        """
        spellchecker = Spellchecker()
        writer = Writer()
        element_title = item[PLAN_NUMBER_MISC_WIDTH + 2:]
        element_name = spellchecker.replace_space_underscore(element_title) + EXT_TEX
        element_file = File(element_name.lower(), self._fback)
        element_file.make()
        element_file_name = element_file.get_path_full()
        element_file = open(element_file_name, 'w')
        writer.latex_comment(self._report, 2, element_title)
        writer.latex_command(self._report, LTX_CMD_INPUT, LTX_START_CHAR_CMD + LTX_PATH_BACK + element_name.lower(), "\n")
        writer.latex_command(self._report, LTX_CMD_ADD_CONTENTS_LINE, LTX_START_CHAR_CMD + LTX_CMD_NUMBERLINE + "{}" + LTX_CMD_HSPACE + "{-1.5em}" + element_title, "\n")
        writer.latex_command_simple(self._report, LTX_CMD_CLEARDOUBLEPAGE, "\n\n")
        writer.latex_command(element_file, LTX_CMD_CHAPTER_UNNAMED, element_title, "\n")
        element_file.close()

    def _write_entries(self):
        r"""Write entries in Back

        Element format:
            '#B' = Back elements

        """
        err_incorrect_format_plan_element = Messager(MSG_KIND_ERROR, "", MSG_TEXT_ERROR_INCORRECT_FORMAT_PLAN_ELEMENT)
        for element in self._plan:
            matcher = Matcher(r'(.*)' + PLAN_DELIMITER_DOUBLE + '(.*)', element)
            element_id = matcher.get_first_group()
            element_id_length = len(element_id)
            element_title = matcher.get_last_group()
            first_char = element_id[:1]
            second_char = element_id[1:2]

            if first_char == PLAN_ID_MISC:
                # Prelims
                if second_char == PLAN_ID_MISC_PRELIMS[1:2]:
                    pass
                # Back
                elif second_char == PLAN_ID_MISC_BACK[1:2]:
                    # Bibliography; pass
                    if element_title == PLAN_HEADER_MISC_BIBLIOGRAPHY:
                        pass
                    # Create an entry
                    else:
                        self._create_entry(element)
                # Incorrect format
                else: 
                    err_incorrect_format_plan_element.show()


################################################################################
class Body(Matter):
    r"""A class for the Body of the report
    """
    def build(self):
        r"""Build the Body
        """
        # Write the comment header
        writer = Writer()
        writer.blank_line(self._report, 1)
        writer.latex_comment_header(self._report, LTX_CMT_HDR_BODY)
        # Set Page numbering
        self._set_pagenumbering()
        # Write the entries
        self._write_entries()
    
    def _create_entry(self, item, key, width, command):
        r"""Create a file with the matching entry in Body

        item: the item of the plan
        key: the body's element ID
        width: the item's ID width
        command: the command which will be written on the header of the created file

        """
        writer = Writer()
        element_title = item[width + 2:]
        element_name = key + EXT_TEX
        element_file = File(element_name, self._fchapters)
        element_file.make()
        element_file_name = element_file.get_path_full()
        element_file = open(element_file_name, 'w')
        writer.latex_command(self._report, LTX_CMD_INPUT, LTX_START_CHAR_CMD + LTX_PATH_CHAPTERS + element_name, "\n")
        writer.latex_command(element_file, command, element_title, "\n")
        element_file.close()

    def _set_pagenumbering(self):
        r"""Set Page numbering in Body
        """
        writer = Writer()
        writer.latex_comment(self._report, 2, LTX_CMT_PAGENUMBERING)
        writer.latex_command(self._report, LTX_CMD_PAGENUMBERING, LTX_CMD_ARABIC, "\n")
        writer.latex_command(self._report, LTX_CMD_SET_COUNTER, LTX_CMD_PAGE, "{1}" + "\n")
        writer.blank_line(self._report, 1)

    def _write_entries(self):
        r"""Write entries in the Body

        Element format:
            'X--' = '\chapter'
            'X-Y--' = '\section'
            'X-Y-Z--' = '\subsection'

        """
        err_incorrect_format_plan_element = Messager(MSG_KIND_ERROR, "", MSG_TEXT_ERROR_INCORRECT_FORMAT_PLAN_ELEMENT)
        for element in self._plan:
            matcher = Matcher(r'(.*)' + PLAN_DELIMITER_DOUBLE + '(.*)', element)
            element_id = matcher.get_first_group()
            element_id_length = len(element_id)
            element_title = matcher.get_last_group()
            first_char = element_id[:1]
            second_char = element_id[1:2]

            # Skip Miscellaneous elements
            if first_char == PLAN_ID_MISC:
                pass
            # Body
            else:
                # Create a Chapter
                if element_id_length == PLAN_NUMBER_CHAPTER_WIDTH:
                    self._create_entry(element, element_id, PLAN_NUMBER_CHAPTER_WIDTH, LTX_CMD_CHAPTER)
                # Create a Section
                elif element_id_length == PLAN_NUMBER_SECTION_WIDTH:
                    self._create_entry(element, element_id, PLAN_NUMBER_SECTION_WIDTH, LTX_CMD_SECTION)
                # Create a Subsection
                elif element_id_length == PLAN_NUMBER_SUBSECTION_WIDTH:
                    self._create_entry(element, element_id, PLAN_NUMBER_SUBSECTION_WIDTH, LTX_CMD_SUBSECTION)
                # Incorrect format
                else:
                    err_incorrect_format_plan_element.show()


################################################################################
class Header(Matter):
    r"""A class for the Header of the report
    """
    def build(self):
        r"""Build the Header
        """
        # Write the class
        self._write_class()
        # Write the macro
        macro = Macro(self._report, self._freport, self._fchapters, self._fprelims, self._fback, self._plan, self._sacr, self._sbib, self._sglo, self._panf, self._panl, self._pdate, self._pcomp, self._psnf, self._psnl, self._pttl, self._psttl)
        macro.build()
        # Write Acronyms | Glossary if chosen
        if self._sacr or self._sglo:
            self._write_acronyms_glossary()
        else:
            pass
        # Write Bibliography if chosen
        if self._sbib:
            self._write_bibliography()
        else:
            pass
        # Write the Properties
        self._write_properties()

    def _create_acronyms_glossary(self):
        r"""Create the file for the Acronyms/Glossary
        """
        writer = Writer()
        glossary_name = PLAN_HEADER_MISC_GLOSSARY_L + EXT_TEX
        glossary_file = File(glossary_name, self._fprelims)
        glossary_file.make()
        glossary_file_name = glossary_file.get_path_full()
        glossary_file = open(glossary_file_name, 'w')
        writer.latex_comment(glossary_file, 2, PLAN_HEADER_MISC_GLOSSARY)

    def _create_bibliography(self):
        r"""Create the file for the Bibliography
        """
        writer = Writer()
        bibliography_name = PLAN_HEADER_MISC_BIBLIOGRAPHY_L + EXT_BIB
        bibliography_file = File(bibliography_name, self._fback)
        bibliography_file.make()
        bibliography_file_name = bibliography_file.get_path_full()
        bibliography_file = open(bibliography_file_name, 'w')
        writer.latex_comment(bibliography_file, 2, PLAN_HEADER_MISC_BIBLIOGRAPHY)

    def _write_acronyms_glossary(self):
        r"""Write the Acronyms/Glossary entry
        """
        writer = Writer()
        glossary_name = PLAN_HEADER_MISC_GLOSSARY_L
        writer.latex_command_simple(self._report, LTX_CMD_MAKEGLOSSARIES, "\n")
        writer.latex_command(self._report, LTX_CMD_LOAD_GLOSSARY, LTX_START_CHAR_CMD + LTX_PATH_PRELIMS + glossary_name, "\n")
        self._create_acronyms_glossary()

    def _write_bibliography(self):
        r"""Write the Bibliography entry
        """
        writer = Writer()
        bibliography_name = PLAN_HEADER_MISC_BIBLIOGRAPHY_L + EXT_BIB
        writer.latex_command(self._report, LTX_CMD_BIBLIOGRAPHY, LTX_START_CHAR_CMD + LTX_PATH_BACK + bibliography_name, "\n")
        self._create_bibliography()

    def _write_class(self):
        r"""Include the ReporTeX class
        """
        writer = Writer()
        writer.line(self._report, "%" * 119 + "\n")
        writer.latex_command(self._report, LTX_CMD_DOCCLASS, RPTX_CLASS, "\n\n")

    def _write_properties(self):
        r"""Write the Properties
        """
        writer = Writer()
        writer.blank_line(self._report, 1)
        writer.latex_comment(self._report, 2, LTX_CMT_PROPERTIES)
        # Title
        writer.latex_command(self._report, LTX_CMD_NEW_CMD, LTX_START_CHAR_CMD + LTX_CMD_RPTX_TITLE, "{" + self._pttl + "}" + "\n")
        # Subtitle
        writer.latex_command(self._report, LTX_CMD_NEW_CMD, LTX_START_CHAR_CMD + LTX_CMD_RPTX_SUBTITLE, "{" + self._psttl + "}" + "\n")
        # Company
        writer.latex_command(self._report, LTX_CMD_NEW_CMD, LTX_START_CHAR_CMD + LTX_CMD_RPTX_COMPANY, "{" + self._pcomp + "}" + "\n")
        # Date
        writer.latex_command(self._report, LTX_CMD_NEW_CMD, LTX_START_CHAR_CMD + LTX_CMD_RPTX_DATE, "{" + self._pdate + "}" + "\n")
        # Author
        writer.latex_command(self._report, LTX_CMD_NEW_CMD, LTX_START_CHAR_CMD + LTX_CMD_RPTX_AUTHOR, "{" + self._panf + " " + \
                LTX_START_CHAR_CMD + LTX_CMD_TEXTSC + "{" + self._panl + "}" + "}" + "\n")
        # Supervisor
        writer.latex_command(self._report, LTX_CMD_NEW_CMD, LTX_START_CHAR_CMD + LTX_CMD_RPTX_SUPERVISOR, "{" + self._psnf + " " + \
                LTX_START_CHAR_CMD + LTX_CMD_TEXTSC + "{" + self._psnl + "}" + "}" + "\n")
        writer.blank_line(self._report, 1)


###########################################################################
class Macro(Header):
    r"""A class for the Macro inside the Header of the report
    """
    def build(self):
        r"""Build the Macro
        """
        writer = Writer()
        writer.latex_comment(self._report, 2, LTX_CMT_BODY_TWOSIDE_ENABLE)
        writer.latex_command_simple(self._report, LTX_CMD_MAKEATLETTER, "\n")
        self._write_twoside()
        self._write_keeppage()
        writer.blank_line(self._report, 1)

    def _write_keeppage(self):
        r"""Create the 'keeppage' environment
        """
        writer = Writer()
        writer.latex_command(self._report, LTX_CMD_NEW_ENV, "keeppage", writer.brackets(LTX_START_CHAR_CMD + LTX_CMD_LET + LTX_START_CHAR_CMD + LTX_CMD_THISPAGESTYLE + "=" + LTX_START_CHAR_CMD + "@gobble") + writer.brackets("") + "\n")

    def _write_twoside(self):
        r"""Create the `twoside` condition
        """
        writer = Writer()
        writer.latex_command_simple(self._report, LTX_CMD_IFTWOSIDE, "\n")
        writer.line(self._report, " " * LMT_INDENTATION)
        writer.latex_comment(self._report, 1, LTX_CMT_BODY_TWOSIDE_OFFSET)
        writer.line(self._report, " " * LMT_INDENTATION)
        writer.latex_command(self._report, LTX_CMD_NEW_LENGTH, LTX_START_CHAR_CMD + LTX_CMD_TEXTBLOCKOFFSET, "\n")
        writer.line(self._report, " " * LMT_INDENTATION)
        writer.latex_command(self._report, LTX_CMD_SET_LENGTH, LTX_START_CHAR_CMD + LTX_CMD_TEXTBLOCKOFFSET, writer.brackets("12mm") +"\n")
        writer.line(self._report, " " * LMT_INDENTATION)
        writer.latex_command(self._report, LTX_CMD_ADD_LENGTH, LTX_START_CHAR_CMD + LTX_CMD_HOFFSET, writer.brackets(LTX_START_CHAR_CMD + LTX_CMD_TEXTBLOCKOFFSET) + "\n")
        writer.line(self._report, " " * LMT_INDENTATION)
        writer.latex_command(self._report, LTX_CMD_ADD_LENGTH, LTX_START_CHAR_CMD + LTX_CMD_EVENSIDEMARGIN, writer.brackets("-2.0" + LTX_START_CHAR_CMD + LTX_CMD_TEXTBLOCKOFFSET) + "\n")
        writer.line(self._report, " " * LMT_INDENTATION)
        writer.latex_comment(self._report, 1, LTX_CMT_BODY_TWOSIDE_HEADER)
        writer.line(self._report, " " * LMT_INDENTATION)
        writer.latex_command(self._report, LTX_CMD_FANCYHEAD, "", " " * 16 + LTX_START_CHAR_CMT + " " + LTX_CMT_BODY_TWOSIDE_HEADER_REINITIALIZATION + "\n")
        writer.line(self._report, " " * LMT_INDENTATION)
        writer.latex_command(self._report, LTX_CMD_FANCYHEAD + "[LO,RE]", LTX_START_CHAR_CMD + LTX_CMD_THEPAGE, " " + LTX_START_CHAR_CMT + " " + LTX_CMT_BODY_TWOSIDE_HEADER_PAGENUMBER + "\n")
        writer.line(self._report, " " * LMT_INDENTATION)
        writer.latex_command(self._report, LTX_CMD_FANCYHEAD + "[CE]", LTX_START_CHAR_CMD + LTX_CMD_LEFTMARK, " " * 3 + LTX_START_CHAR_CMT + " " + LTX_CMT_BODY_TWOSIDE_HEADER_CHAPTER + "\n")
        writer.line(self._report, " " * LMT_INDENTATION)
        writer.latex_command(self._report, LTX_CMD_FANCYHEAD + "[CO]", LTX_START_CHAR_CMD + LTX_CMD_RIGHTMARK, " " * 2 + LTX_START_CHAR_CMT + " " + LTX_CMT_BODY_TWOSIDE_HEADER_SECTION + "\n")
        writer.latex_command_simple(self._report, LTX_CMD_FI, "\n")


################################################################################
class Prelims(Matter):
    r"""A class for the Prelims of the report
    """
    def build(self):
        r"""Build the Prelims
        """
        # Write the comment header
        writer = Writer()
        writer.blank_line(self._report, 1)
        writer.latex_comment_header(self._report, LTX_CMT_HDR_PRELIMS)
        # Write the title page
        self._write_titlepage()
        # Set Page numbering
        self._set_pagenumbering()
        # Write the entries
        self._write_entries()

    def _create_entry(self, item):
        r"""Create an entry in Prelims

        item: the item of the plan

        """
        spellchecker = Spellchecker()
        writer = Writer()
        element_title = item[PLAN_NUMBER_MISC_WIDTH + 2:]
        element_name = spellchecker.replace_space_underscore(element_title) + EXT_TEX
        element_file = File(element_name.lower(), self._fprelims)
        element_file.make()
        element_file_name = element_file.get_path_full()
        element_file = open(element_file_name, 'w')
        writer.latex_comment(self._report, 2, element_title)
        writer.latex_command(self._report, LTX_CMD_INPUT, LTX_START_CHAR_CMD + LTX_PATH_PRELIMS + element_name.lower(), "\n")
        writer.latex_command(self._report, LTX_CMD_ADD_CONTENTS_LINE, LTX_START_CHAR_CMD + LTX_CMD_NUMBERLINE + "{}" + LTX_CMD_HSPACE + "{-1.5em}" + element_title, "\n")
        writer.latex_command_simple(self._report, LTX_CMD_CLEARDOUBLEPAGE, "\n\n")
        writer.latex_command(element_file, LTX_CMD_CHAPTER_UNNAMED, element_title, "\n")
        element_file.close()

    def _create_titlepage(self):
        r"""Create the title page
        """
        writer = Writer()
        titlepage_file = File(RPTX_TITLEPAGE_FILE, PATH_RPTX_REPORT + FLDR_PRELIMS)
        titlepage_file.make()
        titlepage_file_name = titlepage_file.get_path_full()
        titlepage_file = open(titlepage_file_name, "w")
        # Begin Title Page
        writer.latex_command(titlepage_file, LTX_CMD_BEGIN, LTX_CMD_TITLEPAGE, "\n")
        writer.blank_line(titlepage_file, 1)
        # Logo
        writer.latex_comment(titlepage_file, 2, LTX_CMT_TITLEPAGE_LOGO)
        writer.latex_command(titlepage_file, LTX_CMD_VSPACE, "4em", "\n")
        writer.latex_command(titlepage_file, LTX_CMD_BEGIN, LTX_CMD_CENTER, "\n" + "    ")
        writer.latex_command_simple(titlepage_file, LTX_CMD_IMG + "[0.5]" + "{logo}", "\n" + "    ") 
        writer.latex_command_simple(titlepage_file, LTX_CMD_NEWLINE + "[2cm]", "\n") 
        writer.latex_command(titlepage_file, LTX_CMD_END, LTX_CMD_CENTER, "\n")
        writer.blank_line(titlepage_file, 1)
        # Subtitle
        writer.latex_comment(titlepage_file, 2, LTX_CMT_TITLEPAGE_SUBTITLE)
        writer.latex_command(titlepage_file, LTX_CMD_BEGIN, LTX_CMD_CENTER, "\n" + "    ")
        writer.latex_command_simple(titlepage_file, LTX_CMD_USEFONT, "{T1}{qhv}{m}{n}" + \
                LTX_START_CHAR_CMD + LTX_CMD_SELECTFONT + \
                LTX_START_CHAR_CMD + LTX_CMD_LARGE + \
                "{" + LTX_START_CHAR_CMD + LTX_CMD_RPTX_SUBTITLE + "}" + "\n")
        writer.latex_command(titlepage_file, LTX_CMD_END, LTX_CMD_CENTER, "\n")
        writer.blank_line(titlepage_file, 1)
        # Main Title
        writer.latex_comment(titlepage_file, 2, LTX_CMT_TITLEPAGE_MAINTITLE)
        writer.latex_command(titlepage_file, LTX_CMD_BEGIN, LTX_CMD_CENTER, "\n" + "    ")
        writer.latex_command(titlepage_file, LTX_CMD_RULE, LTX_START_CHAR_CMD + LTX_CMD_LINEWIDTH, "{1pt}" + "\n    ")
        writer.latex_command_simple(titlepage_file, LTX_CMD_NEWLINE + "[0.4cm]", "\n" + "    ") 
        writer.latex_command_simple(titlepage_file, LTX_CMD_USEFONT, "{T1}{qhv}{m}{n}" + \
                LTX_START_CHAR_CMD + LTX_CMD_SELECTFONT + \
                LTX_START_CHAR_CMD + LTX_CMD_HUGE + \
                "{" + LTX_START_CHAR_CMD + LTX_CMD_RPTX_TITLE + "}" + "\n" + "    ")
        writer.latex_command(titlepage_file, LTX_CMD_RULE, LTX_START_CHAR_CMD + LTX_CMD_LINEWIDTH, "{1pt}" + "\n")
        writer.latex_command(titlepage_file, LTX_CMD_END, LTX_CMD_CENTER, "\n")
        writer.blank_line(titlepage_file, 1)
        # Names
        writer.latex_comment(titlepage_file, 2, LTX_CMT_TITLEPAGE_NAMES)
        writer.latex_command(titlepage_file, LTX_CMD_BEGIN, LTX_CMD_TABLE, "\n" + "    ")
        writer.latex_command_simple(titlepage_file, LTX_CMD_CENTERING, "\n" + "    ")
        writer.latex_command(titlepage_file, LTX_CMD_BEGIN, LTX_CMD_TABULAR, "{l@{\hskip 7cm}r}" + "\n" + "        ")
        writer.latex_command(titlepage_file, LTX_CMD_TEXTIT, "Author", " & ")
        writer.latex_command(titlepage_file, LTX_CMD_TEXTIT, "Supervisor", "\\\\\n" + "        ")
        writer.latex_command(titlepage_file, LTX_CMD_RULE, "0pt", "{1.2em}" + LTX_START_CHAR_CMD + LTX_CMD_RPTX_AUTHOR + " & ")
        writer.latex_command(titlepage_file, LTX_CMD_RULE, "0pt", "{1.2em}" + LTX_START_CHAR_CMD + LTX_CMD_RPTX_SUPERVISOR + "\n" + "    ")
        writer.latex_command(titlepage_file, LTX_CMD_END, LTX_CMD_TABULAR, "\n")
        writer.latex_command(titlepage_file, LTX_CMD_END, LTX_CMD_TABLE, "\n")
        writer.blank_line(titlepage_file, 1)
        # Date
        writer.latex_comment(titlepage_file, 2, LTX_CMT_TITLEPAGE_DATE)
        writer.latex_command_simple(titlepage_file, LTX_CMD_VFILL, "\n")
        writer.latex_command(titlepage_file, LTX_CMD_BEGIN, LTX_CMD_CENTER, "\n" + "    ")
        writer.latex_command_simple(titlepage_file, LTX_CMD_RPTX_DATE, "\n")
        writer.latex_command(titlepage_file, LTX_CMD_END, LTX_CMD_CENTER, "\n")
        # End Title Page
        writer.latex_command(titlepage_file, LTX_CMD_END, LTX_CMD_TITLEPAGE, "\n")

    def _set_pagenumbering(self):
        r"""Set Page numbering in Prelims
        """
        writer = Writer()
        writer.latex_comment(self._report, 2, LTX_CMT_PAGENUMBERING)
        writer.latex_command(self._report, LTX_CMD_PAGENUMBERING, LTX_CMD_ROMAN, "\n")
        writer.blank_line(self._report, 1)

    def _write_entries(self):
        r"""Write entries in Prelims

        Element format:
            '#P' = Prelims elements

        """
        err_incorrect_format_plan_element = Messager(MSG_KIND_ERROR, "", MSG_TEXT_ERROR_INCORRECT_FORMAT_PLAN_ELEMENT)
        for element in self._plan:
            matcher = Matcher(r'(.*)' + PLAN_DELIMITER_DOUBLE + '(.*)', element)
            element_id = matcher.get_first_group()
            element_id_length = len(element_id)
            element_title = matcher.get_last_group()
            first_char = element_id[:1]
            second_char = element_id[1:2]

            if first_char == PLAN_ID_MISC:
                # Prelims
                if second_char == PLAN_ID_MISC_PRELIMS[1:2]:
                    # Acronyms; pass
                    if element_title == PLAN_HEADER_MISC_ACRONYMS:
                        pass
                    # Glossary; pass
                    elif element_title == PLAN_HEADER_MISC_GLOSSARY:
                        pass
                    # Create an entry
                    else:
                        self._create_entry(element)
                # Back
                elif second_char == PLAN_ID_MISC_BACK[1:2]:
                    pass
                # Incorrect format
                else: 
                    err_incorrect_format_plan_element.show()

    def _write_titlepage(self):
        r"""Write the Title page entry in Prelims
        """
        writer = Writer()
        titlepage_name = RPTX_TITLEPAGE_FILE 
        writer.latex_comment(self._report, 2, LTX_CMT_TITLEPAGE)
        writer.latex_command(self._report, LTX_CMD_INPUT, LTX_START_CHAR_CMD + LTX_PATH_PRELIMS + titlepage_name, "\n")
        writer.latex_command_simple(self._report, LTX_CMD_CLEARDOUBLEPAGE, "\n")
        writer.blank_line(self._report, 1)
        self._create_titlepage()


################################################################################
class Tables(Matter):
    r"""A class for the Tables of the report
    """
    def build(self):
        r"""Build the Tables
        """
        # Write the comment header
        writer = Writer()
        writer.blank_line(self._report, 1)
        writer.latex_comment_header(self._report, LTX_CMT_HDR_TABLES)
        # Disable microtypesetup
        self._set_microtypesetup("false")
        # Write the Table of Contents
        self._write_toc()
        # Write the List of Figures
        self._write_lof()
        # Write the List of Tables
        self._write_lot()
        # Write the List of Listings
        self._write_lol()
        # Enable microtypesetup
        self._set_microtypesetup("true")
        # Write the Glossary if chosen
        if self._sglo:
            self._write_glossary()
        else:
            pass
        # Write the Acronyms if chosen
        if self._sacr:
            self._write_acronyms()
        else:
            pass

    def _set_microtypesetup(self, protusion):
        r"""Set the microtypesetup option

        protusion: 'true' or 'false'

        """
        writer = Writer()
        writer.latex_command(self._report, LTX_CMD_MICROTYPESETUP, LTX_CMD_PROTUSION + "=" + protusion, "\n")

    def _write_acronyms(self):
        r"""Write the Acronyms in the Tables
        """
        writer = Writer()
        writer.latex_comment(self._report, 2, LTX_CMT_TABLES_ACRONYMS)
        writer.latex_command_simple(self._report, LTX_CMD_PRINTGLOSSARY, "[type=" + LTX_START_CHAR_CMD + LTX_CMD_ACRONYM_TYPE + ", title=" + PLAN_TABLES_ACRONYMS + "]" + "\n")
        writer.latex_command_simple(self._report, LTX_CMD_CLEARDOUBLEPAGE, "\n\n")

    def _write_glossary(self):
        r"""Write the Glossary in the Tables
        """
        writer = Writer()
        writer.latex_comment(self._report, 2, LTX_CMT_TABLES_GLOSSARY)
        writer.latex_command_simple(self._report, LTX_CMD_PRINTGLOSSARY, "[type=" + LTX_START_CHAR_CMD + LTX_CMD_GLOSSARY_TYPE + ", title=" + PLAN_TABLES_GLOSSARY + "]" + "\n")
        writer.latex_command_simple(self._report, LTX_CMD_CLEARDOUBLEPAGE, "\n\n")

    def _write_lof(self):
        r"""Write the List of Figures in the Tables
        """
        writer = Writer()
        writer.latex_comment(self._report, 2, LTX_CMT_TABLES_LOF)
        writer.latex_command_simple(self._report, LTX_CMD_TABLE_FIGURES, "\n")
        writer.latex_command(self._report, LTX_CMD_ADD_CONTENTS_LINE, LTX_START_CHAR_CMD + LTX_CMD_NUMBERLINE + "{}" + LTX_CMD_HSPACE + "{-1.5em}" + PLAN_TABLES_LOF, "\n")
        writer.latex_command_simple(self._report, LTX_CMD_CLEARDOUBLEPAGE, "\n\n")

    def _write_lol(self):
        r"""Write the List of Listings in the Tables
        """
        writer = Writer()
        writer.latex_comment(self._report, 2, LTX_CMT_TABLES_LOL)
        writer.latex_command_simple(self._report, LTX_CMD_TABLE_LISTINGS, "\n")
        writer.latex_command(self._report, LTX_CMD_ADD_CONTENTS_LINE, LTX_START_CHAR_CMD + LTX_CMD_NUMBERLINE + "{}" + LTX_CMD_HSPACE + "{-1.5em}" + PLAN_TABLES_LOL, "\n")
        writer.latex_command_simple(self._report, LTX_CMD_CLEARDOUBLEPAGE, "\n\n")

    def _write_lot(self):
        r"""Write the List of Tables in the Tables
        """
        writer = Writer()
        writer.latex_comment(self._report, 2, LTX_CMT_TABLES_LOT)
        writer.latex_command_simple(self._report, LTX_CMD_TABLE_TABLES, "\n")
        writer.latex_command(self._report, LTX_CMD_ADD_CONTENTS_LINE, LTX_START_CHAR_CMD + LTX_CMD_NUMBERLINE + "{}" + LTX_CMD_HSPACE + "{-1.5em}" + PLAN_TABLES_LOT, "\n")
        writer.latex_command_simple(self._report, LTX_CMD_CLEARDOUBLEPAGE, "\n\n")

    def _write_toc(self):
        r"""Write the Table of Contents in the Tables
        """
        writer = Writer()
        writer.latex_comment(self._report, 2, LTX_CMT_TABLES_TOC)
        writer.latex_command_simple(self._report, LTX_CMD_TABLE_CONTENTS, "\n")
        writer.latex_command_simple(self._report, LTX_CMD_CLEARDOUBLEPAGE, "\n\n")


#####################################################################################
class Overviewer(Report):
    r""""""
    def show_properties(self, properties):
        r"""Get an overview of the properties

        properties: the overviewed properties

        """
        dicochecker = Dicochecker()
        dicochecker.line(properties, HDR_DICT_AUTHOR_NAME_FIRST)
        dicochecker.line(properties, HDR_DICT_AUTHOR_NAME_LAST)
        dicochecker.line(properties, HDR_DICT_DATE)
        dicochecker.line(properties, HDR_DICT_COMPANY)
        dicochecker.line(properties, HDR_DICT_SUPERVISOR_NAME_FIRST)
        dicochecker.line(properties, HDR_DICT_SUPERVISOR_NAME_LAST)
        dicochecker.line(properties, HDR_DICT_TITLE)
        dicochecker.line(properties, HDR_DICT_SUBTITLE)

    def show_plan(self, plan):
        r"""Get an overview of the plan

        plan: the overviewed plan

        """
        listchecker = Listchecker()
        listchecker.all_elements(plan)

    def show_template(self, template):
        r"""Print a template

        template: the template to print

        """
        print template


########################################################################################## 
class Tools:
    r"""Tools: A bunch of tools 
    """


#####################################################################################
class Downloader(Tools):
    r"""Downloader: download the necessary files for creating a new report
    """
    def __init__(self, name, path):
        r"""Downloader initialization

        name: file downloaded name
        path: file downloaded path

        """
        self._name = name
        self._path = path
        self._path_full = self._path + self._name

    def download(self, url):
        r"""Download a file

        url: the file's URL

        If the download was successful, print a message.
        Else, print an error message.

        """
        path = self._path_full
        if os.path.exists(path):
            pass
        else:
            file_downloaded = urllib.URLopener()
            file_downloaded.retrieve(url, path)
            if os.path.exists(path):
                class_file_successfully_downloaded = Messager(MSG_KIND_INFO, "", MSG_TEXT_INFO_CLASS_FILE_SUCCESSFULLY_DOWNLOADED)
                class_file_successfully_downloaded.show()
            else:
                class_file_failed_download = Messager(MSG_KIND_ERROR, "", MSG_TEXT_ERROR_CLASS_FILE_FAILED_DOWNLOAD)
                class_file_failed_download.show()


#####################################################################################
class Maker(Tools):
    r"""Maker: generate the Makefile
    """
    def generate(self):
        print "Generating the Makefile"
        # Create the Makefile
        make_file = File(RPTX_MAKE_FILE, PATH_RPTX_MAIN) 
        make_file.make()
        make_file_name = make_file.get_path_full()
        make_file = open(make_file_name, 'w')
        # Write header
        self._header(make_file)
        # Write variables
        self._variables(make_file)
        # Write 'archive-tar' rule
        self._rule_archivetar(make_file)
        # Write 'archive-zip' rule
        self._rule_archivezip(make_file)
        # Write 'build-full' rule
        self._rule_buildfull(make_file)
        # Write 'build-simple' rule
        self._rule_buildsimple(make_file)
        # Write 'clean' rule
        self._rule_clean(make_file)
        # Write 'view' rule
        self._rule_view(make_file)
        print "Done"

    def _header(self, makefile):
        r"""Write the header
        """
        writer = Writer()
        writer.bash_comment(makefile, BSH_CMT_MAKEFILE_HEADER)
        writer.blank_line(makefile, 2)

    def _rule_archivetar(self, makefile):
        r"""Write the 'archive-tar' rule
        """
        writer = Writer()
        writer.bash_comment(makefile, BSH_CMT_RULE_ARCHIVETAR)
        writer.bash_command_simple(makefile, "", BSH_RULE_ARCHIVETAR)
        writer.bash_command_simple(makefile, "\n\t", BSH_CMD_TAR)
        writer.bash_command(makefile, " ", BSH_CMD_ARCHIVE, EXT_TAR + "\\\n")
        writer.bash_command(makefile, "\t\t", BSH_CMD_MAKEFILE, "\\\n")
        writer.bash_command(makefile, "\t\t", BSH_CMD_REPORT, EXT_TEX + "\\\n")
        writer.bash_command(makefile, "\t\t", BSH_CMD_REPORT, "/" + "\\\n")
        writer.bash_command(makefile, "\t\t", BSH_CMD_CLASS, "\\\n")
        writer.bash_command(makefile, "\t\t", BSH_CMD_REPORTMAKER, "\n")
        writer.blank_line(makefile, 1)

    def _rule_archivezip(self, makefile):
        r"""Write the 'archive-zip' rule
        """
        writer = Writer()
        writer.bash_comment(makefile, BSH_CMT_RULE_ARCHIVEZIP)
        writer.bash_command_simple(makefile, "", BSH_RULE_ARCHIVEZIP)
        writer.bash_command_simple(makefile, "\n\t", BSH_CMD_ZIP)
        writer.bash_command(makefile, " '", BSH_CMD_ARCHIVE, EXT_ZIP + "'\\\n")
        writer.bash_command(makefile, "\t\t", BSH_CMD_MAKEFILE, "\\\n")
        writer.bash_command(makefile, "\t\t", BSH_CMD_REPORT, EXT_TEX + "\\\n")
        writer.bash_command(makefile, "\t\t", BSH_CMD_REPORT, "/" + "\\\n")
        writer.bash_command(makefile, "\t\t", BSH_CMD_CLASS, "\\\n")
        writer.bash_command(makefile, "\t\t", BSH_CMD_REPORTMAKER, "\n")
        writer.blank_line(makefile, 1)

    def _rule_buildfull(self, makefile):
        r"""Write the 'build-full' rule
        """
        writer = Writer()
        writer.bash_comment(makefile, BSH_CMT_RULE_BUILDFULL)
        writer.bash_command_simple(makefile, "", BSH_RULE_BUILDFULL)
        writer.bash_command_simple(makefile, "\n\t", BSH_CMD_RM + " *.pdf" + "\n")
        writer.bash_command(makefile, "\t", BSH_VAR_TEX_NME, "")
        writer.bash_command(makefile, " ", BSH_CMD_REPORT, EXT_TEX + "\n")
        writer.bash_command(makefile, "\t", BSH_VAR_GLO_NME, "")
        writer.bash_command(makefile, " ", BSH_CMD_REPORT, "\n")
        writer.bash_command(makefile, "\t", BSH_VAR_BIB_NME, "")
        writer.bash_command(makefile, " ", BSH_CMD_REPORT, "\n")
        writer.bash_command(makefile, "\t", BSH_VAR_TEX_NME, "")
        writer.bash_command(makefile, " ", BSH_CMD_REPORT, "\n")
        writer.bash_command(makefile, "\t", BSH_VAR_TEX_NME, "")
        writer.bash_command(makefile, " ", BSH_CMD_REPORT, "\n")
        writer.blank_line(makefile, 1)

    def _rule_buildsimple(self, makefile):
        r"""Write the 'build-simple' rule
        """
        writer = Writer()
        writer.bash_comment(makefile, BSH_CMT_RULE_BUILDSIMPLE)
        writer.bash_command_simple(makefile, "", BSH_RULE_BUILDSIMPLE)
        writer.bash_command(makefile, "\n\t", BSH_VAR_TEX_NME, " ")
        writer.bash_command(makefile, "", BSH_CMD_REPORT, EXT_TEX + "\n")
        writer.blank_line(makefile, 1)

    def _rule_clean(self, makefile):
        r"""Write the 'clean' rule
        """
        writer = Writer()
        writer.bash_comment(makefile, BSH_CMT_RULE_CLEAN)
        writer.bash_command_simple(makefile, "", BSH_RULE_CLEAN)
        writer.bash_command_simple(makefile, "\n\t", BSH_CMD_RM + " *.acn" + \
                                                                  " *.acr" + \
                                                                  " *.alg" + \
                                                                  " *.aux" + \
                                                                  "\n")
        writer.bash_command_simple(makefile, "\t", BSH_CMD_RM + " *.bbl" + \
                                                                " *.bcf" + \
                                                                " *.blg" + \
                                                                " *.bib" + \
                                                                "\n")
        writer.bash_command_simple(makefile, "\t", BSH_CMD_RM + " *.dvi" + \
                                                                "\n")
        writer.bash_command_simple(makefile, "\t", BSH_CMD_RM + " *.fdb_latexmk" + \
                                                                " *.fls" + \
                                                                "\n")
        writer.bash_command_simple(makefile, "\t", BSH_CMD_RM + " *.glg" + \
                                                                " *.glo" + \
                                                                " *.gls" + \
                                                                " *.glsdefs" + \
                                                                "\n")
        writer.bash_command_simple(makefile, "\t", BSH_CMD_RM + " *.idx" + \
                                                                " *.ilg" + \
                                                                " *.ind" + \
                                                                " *.ist" + \
                                                                "\n")
        writer.bash_command_simple(makefile, "\t", BSH_CMD_RM + " *.listing" + \
                                                                " *.lof" + \
                                                                " *.log" + \
                                                                " *.lol" + \
                                                                " *.lot" + \
                                                                "\n")
        writer.bash_command_simple(makefile, "\t", BSH_CMD_RM + " *.maf" + \
                                                                " *.mtc" + \
                                                                "\n")
        writer.bash_command_simple(makefile, "\t", BSH_CMD_RM + " *.out" + \
                                                                "\n")
        writer.bash_command_simple(makefile, "\t", BSH_CMD_RM + " *.ps" + \
                                                                " *.ptc" + \
                                                                "\n")
        writer.bash_command_simple(makefile, "\t", BSH_CMD_RM + " *.run.xml" + \
                                                                "\n")
        writer.bash_command_simple(makefile, "\t", BSH_CMD_RM + " *.synctex.gz" + \
                                                                "\n")
        writer.bash_command_simple(makefile, "\t", BSH_CMD_RM + " *.toc" + \
                                                                "\n")
        writer.bash_command_simple(makefile, "\t", BSH_CMD_RM + " *.xdy" + \
                                                                "\n")
        writer.blank_line(makefile, 1)

    def _rule_view(self, makefile):
        r"""Write the 'view' rule
        """
        writer = Writer()
        writer.bash_comment(makefile, BSH_CMT_RULE_VIEW)
        writer.bash_command_simple(makefile, "", BSH_RULE_VIEW)
        writer.bash_command(makefile, "\n\t", BSH_VAR_PDF_NME, "")
        writer.bash_command(makefile, " ", BSH_CMD_REPORT, EXT_PDF + " &\n")
        writer.blank_line(makefile, 1)

    def _variables(self, makefile):
        r"""Write the variables
        """
        writer = Writer()
        writer.bash_comment(makefile, BSH_CMT_VAR_APPLICATIONS)
        writer.bash_command_simple(makefile, "", BSH_VAR_BIB_NME + BSH_VAR_BIB_VLE + "\n")
        writer.bash_command_simple(makefile, "", BSH_VAR_GLO_NME + BSH_VAR_GLO_VLE + "\n")
        writer.bash_command_simple(makefile, "", BSH_VAR_PDF_NME + BSH_VAR_PDF_VLE + "\n")
        writer.bash_command_simple(makefile, "", BSH_VAR_TEX_NME + BSH_VAR_TEX_VLE + "\n")
        writer.blank_line(makefile, 1)
        writer.bash_comment(makefile, BSH_CMT_VAR_VARIABLES)
        writer.bash_command_simple(makefile, "", BSH_VAR_ARCHIVE_NME + BSH_VAR_ARCHIVE_VLE + "\n")
        writer.bash_command_simple(makefile, "", BSH_VAR_CLASS_NME + BSH_VAR_CLASS_VLE + "\n")
        writer.bash_command_simple(makefile, "", BSH_VAR_MAKEFILE_NME + BSH_VAR_MAKEFILE_VLE + "\n")
        writer.bash_command_simple(makefile, "", BSH_VAR_REPORT_NME + BSH_VAR_REPORT_VLE + "\n")
        writer.bash_command_simple(makefile, "", BSH_VAR_REPORTMAKER_NME + BSH_VAR_REPORTMAKER_VLE + "\n")
        writer.blank_line(makefile, 2)


########################################################################################## 
class Utils:
    r"""A bunch of tools
    """


#####################################################################################
class Checker(Utils):
    r"""Checker: ask to the user to validate by 'yes' or 'no' after checking
    """
    def ask(self, question, choice_default):
        r"""Ask the user to validate by 'yes' or 'no'

        question: the question to print
        choice_default: the answer by default to the question

        Attribute a value to the choices selector depending on the choice by default value
        Write the question with the choices selector
        Format the user's answer
        Return a boolean
        """
        # Possible values for the choice by default
        choice_default_values = {CKR_ANS_YES: True, 
                                 CKR_ANS_Y: True,
                                 CKR_ANS_NO: False,
                                 CKR_ANS_N: False}

        # Values the choices selector will print depending on the choice by default
        if choice_default is None:
            choices_selector = CKR_SEL_NONE
        elif choice_default == CKR_ANS_YES:
            choices_selector = CKR_SEL_YES
        elif choice_default == CKR_ANS_NO:
            choices_selector = CKR_SEL_NO
        else:
            err_invalid_default_answer = Messager(MSG_KIND_ERROR, "", MSG_TEXT_ERROR_INVALID_DEFAULT_ANSWER)
            err_invalid_default_answer.show()

        # Question, choices selector, return value
        while True:
            print(colored("%s %s" %(question, choices_selector), "magenta", attrs = ["bold"])),
            choice_user = raw_input().lower()
            # No answers
            if choice_default is not None and choice_user == "":
                return choice_default_values[choice_default]
            # User's answer in choice default values
            elif choice_user in choice_default_values:
                return choice_default_values[choice_user]
            # Error
            else:
                err_incorrect_answer_checker = Messager(MSG_KIND_ERROR, "", MSG_TEXT_ERROR_INCORRECT_ANSWER_CHECKER)
                err_incorrect_answer_checker.show()


#####################################################################################
class Cleaner(Utils):
    r"""Cleaner: clean the prompt for giving a better overview during the creating process
    """
    def clean(self):
        r"""Clean the prompt
        """
        os.system("clear")


#####################################################################################
class Dicochecker(Utils):
    r"""Dicochecker: give an overview of a dictionary
    """
    def line(self, dictionary, line):
        r"""Give an overview of a dictionary with a specifc format for each line

        dictionary: the dictionary to overview
        line: the line to print

        """
        print(colored("%s:" %(line), "cyan", attrs = ["bold"])),
        info_value = Messager(MSG_KIND_INPUT, "", dictionary[line])
        info_value.show()

    def value(self, dictionary, key):
        r"""Return the value in function of a given key for a dictionary

        dictionary: the dictionary to overview
        key: the key to define where the line is

        """
        return dictionary[key]


#####################################################################################
class Leaver(Utils):
    r"""Leaver: exit the script with an error
    """
    def exit_os(self):
        r"""Exit the script, and raise an exception (os)
        """
        os._exit(0)

    def exit_sys(self):
        r"""Print an error message, exit the script, and raise an exception (sys)
        """
        err_exit_script = Messager(MSG_KIND_ERROR, "", MSG_TEXT_ERROR_EXIT_SCRIPT)
        err_exit_script.show()
        sys.exit(0)


#####################################################################################
class Listchecker(Utils):
    r"""Listchecker: a tool for lists
    """
    def all_elements(self, checklist):
        r"""Print all elements of a list

        checklist: the list where the elements will be printed

        """
        for element in checklist:
            print(colored("%s" %(element), "magenta", attrs = ["bold"]))

    def remove_empty_elements(self, checklist):
        r"""Remove empty elements of a list

        checklist: the list where the possible empty elements need to be removed

        """
        checklist_sorted = filter(None, checklist)
        return checklist_sorted


#####################################################################################
class Matcher(Utils):
    r"""Matcher: match regular expressions to strings
    """
    def __init__(self, pattern, line):
        r"""Match initialization

        pattern: regular expression to be matched
        line: the string which would be searched to match the pattern

        """
        self._pattern = pattern
        self._line = line
        self._result = re.match(pattern, line, re.M|re.I)

    def get_first_group(self):
        r"""Get the group before the pattern
        """
        if self._result:
            return self._result.group(1)
        
    def get_full_result(self):
        r"""Get all the groups of the result
        """
        if self._result:
            return self._result.group()

    def get_last_group(self):
        r"""Get the group after the pattern
        """
        if self._result:
            return self._result.group(2)


#####################################################################################
class Messager(Utils):
    r"""Messager: print several kinds of message
    """
    def __init__(self, kind, number, message):
        r"""Message initialization

        kind: kind of message (Info/Info with an ID/Error)
        number: info's number
        message: the text to print

        """
        self._kind = kind
        self._number = "[" + str(number) + "/" + str(MSG_INFO_TOTAL) + "]"
        self._message = message

    def show(self):
        r"""Print the message on the terminal
        """
        # "ERROR"
        if (self._kind == MSG_KIND_ERROR):
            print(colored("%s %s" %(MSG_PREFIX_ERROR, self._message), "red", attrs = ["bold"]))
        # "INFO"
        elif (self._kind == MSG_KIND_INFO):
            print(colored("%s %s" %(MSG_PREFIX_INFO, self._message), "green", attrs = ["bold"]))
        # "INFO" with an ID
        elif (self._kind == MSG_KIND_INFO_ID):
            print(colored("%s %s" %(self._number, self._message), "blue", attrs = ["bold"]))
        # "INPUT"
        elif (self._kind == MSG_KIND_INPUT):
            print(colored("%s" %(self._message), "magenta", attrs = ["bold"]))
        # Exit the script
        else:
            leaver = Leaver()
            leaver.exit_sys()


#####################################################################################
class Spellchecker(Utils):
    r"""Spellchecker: correct the user inputs
    """
    def remove_space_all(self, string):
        r"""Remove all spaces

        string: the string to correct

        """
        string_corrected = string.replace(" ", "")
        return string_corrected

    def remove_space_duplicated(self, string):
        r"""Remove duplicated spaces

        string: the string to correct

        """
        string_corrected = ' '.join(string.split())
        return string_corrected

    def remove_space_leadend(self, string):
        r"""Remove leading and ending spaces

        string: the string to correct

        """
        string_corrected = string.strip()
        return string_corrected

    def replace_space_underscore(self, string):
        r"""Replace spaces by underscores

        string: the string to correct

        """
        string_corrected = string.replace(" ", "_")
        return string_corrected
        

#####################################################################################
class Writer(Utils):
    r"""Writer: write LaTeX/Bash commands/comments, and several lines
    """
    def bash_command(self, make_file, before, command, additional):
        r"""Write a Bash command

        make_file: the file where commands have to be written
        before: the text before the command
        command: the command in the brackets
        additional: additional text

        """
        command_with_brackets = self.brackets(command)
        make_file.write(before + "$" + command_with_brackets + additional)

    def bash_command_simple(self, make_file, before, command):
        r"""Write a simple Bash command

        make_file: the file where commands have to be written
        before: the text before the command
        command: the command to write

        """
        make_file.write(before + command)

    def bash_comment(self, make_file, comment):
        r"""Write a Bash comment

        make_file: the file where commands have to be written
        comment: the comment to write

        """
        make_file.write("# " + comment + "\n")

    def blank_line(self, report_file, times):
        r"""Write blank lines

        report_file: the file where blank lines have to be written
        times: the number of blank lines to write

        """
        for x in range (0, times):
            report_file.write("\n")

    def brackets(self, string):
        r"""Write a pair of brackets

        string: the text to write inside the brackets

        """
        string_with_brackets = "{" + string + "}"
        return string_with_brackets

    def latex_command(self, report_file, command, string, additional):
        r"""Write a LaTeX command

        report_file: the file where commands have to be written
        command: the LaTeX command
        string: the text inside the brackets
        additional: additional content if needed

        ex: \command{string}additional

        """
        string_with_brackets = self.brackets(string)
        report_file.write(LTX_START_CHAR_CMD + command + string_with_brackets + additional)

    def latex_command_simple(self, report_file, command, additional):
        r"""Write a LaTeX command without brackets

        report_file: the file where commands have to be written
        command: the LaTeX command
        additional: additional content if needed

        ex: \command + additional

        """
        report_file.write(LTX_START_CHAR_CMD + command + additional)

    def latex_comment(self, report_file, times, comment):
        r"""Write a LaTeX comment

        report_file: the file where the line has to be written
        times: number of times the character '%' will be written before the comment
        comment: the LaTeX comment

        """
        comment_title = ''.join([LTX_START_CHAR_CMT for cnt in range(times)])
        report_file.write(comment_title + " " + comment + "\n")

    def latex_comment_header(self, report_file, comment_header):
        r"""Write a LaTeX comment header

        report_file: the file where the line has to be written
        comment_header: the LaTeX comment header

        """
        report_file.write(LTX_START_CHAR_CMT + '-' * 119 + "\n" + \
                          LTX_START_CHAR_CMT + '    ' + comment_header + "\n" + \
                          LTX_START_CHAR_CMT + '-' * 119 + "\n")

    def line(self, report_file, line):
        r"""Write a simple line

        report_file: the file where the line has to be written
        line: the line to write

        """
        report_file.write(line)


########################################################################################## 
def main():
    r"""Main function

    Manage script arguments

    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--download", help = ARG_D_DOWNLOAD, action = "store_true")
    parser.add_argument("-m", "--makefile", help = ARG_M_MAKEFILE, action = "store_true")
    parser.add_argument("-n", "--new", help = ARG_N_NEW, action = "store_true")
    args = parser.parse_args()

    # '-d'/'--download'
    if args.download:
        downloader = Downloader(RPTX_CLASS_FILE, PATH_RPTX_CLASS_FILE)
        downloader.download(URL_REPORTEX_CLASS)
    # '-m'/'--makefile'
    elif args.makefile:
        maker = Maker()
        maker.generate()
    # '-n'/'--new'
    elif args.new:
        report = Report()
        report.make()
    # No arguments
    else:
        err_no_args = Messager(MSG_KIND_ERROR, "", MSG_TEXT_ERROR_NO_ARGS)
        err_no_args.show()
        leaver = Leaver()
        leaver.exit_sys()


########################################################################################## 
if __name__ == "__main__":
    r"""Execute 'main()' function or print error message if KeyboardInterrupt
    """
    try:
        main()
    # Handling 'Ctrl + c' during the creation process
    except KeyboardInterrupt:
        print "\n"
        try:
            err_keyboard_interrupt = Messager(MSG_KIND_ERROR, "", MSG_TEXT_ERROR_KEYBOARD_INTERRUPT)
            err_keyboard_interrupt.show()
            leaver_sys = Leaver()
            leaver_sys.exit_sys()
        except SystemExit:
            leaver_os = Leaver()
            leaver_os.exit_os()
    # Error while downloading the class file 'reportex.cls' from GitHub
    except IOError:
        class_file_failed_download = Messager(MSG_KIND_ERROR, "", MSG_TEXT_ERROR_CLASS_FILE_FAILED_DOWNLOAD)
        class_file_failed_download.show()
        leaver = Leaver()
        leaver.exit_sys()
