#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Title          :creator.py
# Description    : 
# Author         :Simon L. J. Robin
# Created        :2014-12-11 09:57:31
# Modified       :2014-12-11 09:58:04
##########################################################################################


#“A goal without a plan is just a wish.”
# ― Antoine de Saint-Exupéry
#


import argparse

import os


STR_NAME_ABSTRACT = "abstract.tex"
STR_HEADER_ABSTRACT = "\\begin{abstract}\n"
STR_FOOTER_ABSTRACT = "\\end{abstract}"


STR_PREFIX_COMMAND = "\\newcommand"

VLE_TITLE = "35"




#class Cleaner:
##########################################################################################


class Component:
    "Abstract, chapter, etc."

    def __init__(self, name, header, footer):
        self.name = name
        self.header = header
        self.footer = footer
    


    def get_name(self):
        return self.name



    def create(self):
        if os.path.exists(self.name):
            print(self.name + " already exists!")
        else:
            component = open(self.name, "w")
            component.write(self.header)
            component.write(self.footer)
            component.write(POT_POURRI)
            component.close()





class Report:
    "Creation of a report"
    
    def __init__(self, author):
        self.name = "report.tex"
        self.author = author

    def create_dependencies(self):
        if os.path.exists(self.name):
            print(self.name + " already exists!")
        else:
            component = open(self.name, "w")
            component.close()

    def write_title(self):
        user_value = raw_input("Title: ")
        truncated_value = user_value[:35]
        title = truncated_value
        return title

    def write_subtitle(self):
        user_value = raw_input("Subtitle: ")
        truncated_value = user_value[:35]
        subtitle = truncated_value
        return subtitle


    def write_author(self):
        user_value = raw_input("First name: ")
        truncated_value = user_value[:20]
        firstname = truncated_value

        user_value = raw_input("Last name: ")
        truncated_value = user_value[:20]
        lastname = truncated_value

        author = firstname + "\\textsc{" + lastname + "}"
        return author


    def complete_rptx_property(self, prefix, command, name):
        rptx_property = prefix + command + "{" + name + "}\n"
        return rptx_property
        

    def create_report(self):
        title = self.write_title()
        subtitle = self.write_subtitle()
        author = self.write_author()

        print "the title is " + title
        rptx_title = self.complete_rptx_property(STR_PREFIX_COMMAND, "{\\reportTitle}", title)
        rptx_subtitle = self.complete_rptx_property(STR_PREFIX_COMMAND, "{\\reportSubtitle}", subtitle)
        rptx_author = self.complete_rptx_property(STR_PREFIX_COMMAND, "{\\reportAuthor}", author)

        component = open(self.name, "w")
        component.write(rptx_title)
        component.write(rptx_subtitle)
        component.write(rptx_author)
        component.close()
    

##########################################################################################


def create():
    print("Creation of a new report")
    
    report = Report("Simon")
    report.create_report()

#    abstract = Component(STR_NAME_ABSTRACT, STR_HEADER_ABSTRACT, STR_FOOTER_ABSTRACT)
#    abstract.create()
#    abstract.replace_field(POT_POURRI, "")







##########################################################################################
parser = argparse.ArgumentParser()

parser.add_argument("-n", "--new", help="create a new report", action="store_true")
args = parser.parse_args()

# "-n", "--new"
if args.new:
    create()






##########################################################################################
#if __name__ == '__main__':
