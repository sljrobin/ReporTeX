#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Title          :creator.py
# Description    : 
# Author         :Simon L. J. Robin
# Created        :2014-12-11 09:57:31
# Modified       :2015-03-25 22:37:59
##########################################################################################

#“A goal without a plan is just a wish.”
# ― Antoine de Saint-Exupéry
#
import argparse
import os

#class Cleaner:
##########################################################################################
class Component:
    "Abstract, chapter, etc."

    def __init__(self, name, header, footer):
        self.name = name
        self.header = header
        self.footer = footer
    
class Report:
    "Creation of a report"
    
    def __init__(self):
        self.name = "report.tex"
        self.author = ""
        self.title = ""
        self.subtitle = ""

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


    def complete_rptx_property(self, prefix, command, name):
        rptx_property = prefix + command + "{" + name + "}\n"
        return rptx_property

    def check_class(self):
        if not os.path.exists("reportex.cls"):
            print("Warning! 'reportex.cls' is not in the current directory")

    def create_report(self):
        self.title = self.write_title()
        self.subtitle = self.write_subtitle()
        author = self.write_author()

##########################################################################################
def create():
    print("Creation of a new report")
    
    report = Report()
    report.create_report()

##########################################################################################
parser = argparse.ArgumentParser()

parser.add_argument("-n", "--new", help="create a new report", action="store_true")
args = parser.parse_args()

# "-n", "--new"
if args.new:
    create()

##########################################################################################
#if __name__ == '__main__':
