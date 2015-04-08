#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Title          :creator.py
# Description    : 
# Author         :Simon L. J. Robin
# Created        :2014-12-11 09:57:31
# Modified       :2015-04-08 19:55:28
##########################################################################################

#“A goal without a plan is just a wish.”
# ― Antoine de Saint-Exupéry
#
import argparse
import os

#class Cleaner:
##########################################################################################
class Report:
    "Creation of a report"
    
    def __init__(self):
        self.name = "report.tex"
        self.author = ""
        self.title = ""
        self.subtitle = ""


##########################################################################################
parser = argparse.ArgumentParser()

parser.add_argument("-n", "--new", help="create a new report", action="store_true")
args = parser.parse_args()

