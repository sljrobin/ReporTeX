# ReporTeX
[ReporTeX] is a helper and a class which are designed for writing LaTeX reports faster and to focus as much as possible on the content and not on the layout. Feel free to check out the [ReporTeX webpage].

## Table of contents
* [Requirements]
* [How to start]

* [License]

## Requirements
* A TeX distribution
* An editor
* Python
    * colorama

## How to start
1. Download the [ReportMaker]
    * Option 1: _Download the full repository_: `git clone git://github.com/sljrobin/ReporTeX/.git`
    * Option 2: _Download only the [ReportMaker]_
        * Go to the [ReportMaker source webpage]
        * Right click on the `Raw` button
        * Select `Save Link As...`
* Download the last version of the class if you downloaded only the [ReportMaker]: `python reportmaker.py -d`
* Create a new report: `python reportmaker -n`
* Generate the [makefile]: `python reportmaker -m`

## Content
The following files and folders will be created after executed the commands described in the [How to start] section.
* `makefile` Makefile
* `report/` Main folder
    * assets/` Non-TeX files
        * `codes/` Source code
        * `graphics/` TikZ files
        * `images/` Figures
        * `tables/` Tables
    * `back/` Back
    * `chapters/` Chapters
    * `prelims/` Prelims
* `reportex.cls` LaTeX class
* `report.tex` Main file

## Options
* ReportMaker
    * `-d`, `--download`: download the ReporTeX class
    * `-h`, `--help`: show the help
    * `-m`, `--makefile`: generate the makefile
    * `-n`, `--new`: create a new report
    * __Usage__: `python reportmaker.py <option>`
* Makefile
    * `archive-tar`: compress the files in a `.tar.gz` archive
    * `archive-zip`: compress the files in a `.zip` archive
    * `build-full`: clean and compile
    * `build-simple`: compile only the main file
    * `clean`: remove the odd files
    * `view`: read the PDF
    * __Usage__: `make <option>`

## License
The content of this project is licensed under the GPL license.

[ReportMaker]: /reportmaker.py "ReportMaker"
[ReportMaker source webpage]: https://github.com/sljrobin/ReporTeX/blob/master/reportmaker.py "ReportMaker source webpage"


[Content]: /README.md#content "Content"
[Requirements]: /README.md#requirements "Requirements"
[How to start]: /README.md#how-to-start "How to start"
[Options]: /README.md#options "Options"
[License]: /README.md#license "License"

[`reportex.cls`]: /reportex.cls "reportex.cls"

[ReporTeX]: https://github.com/sljrobin/ReporTeX "ReporTeX"
[ReporTeX webpage]: http://work.sljrobin.com/reportex "ReporTeX webpage"
