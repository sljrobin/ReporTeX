# ReporTeX
[ReporTeX] is a template designed for writing LaTeX reports faster and to focus as much as possible on the content and not on the layout.

## Table of contents
* [Content]
* [Usage]
    * [Requirements]
    * [Creation of a new report]
* [License]

## Content
* [`api/`] Layout files
    * [`env/`] Variables
        * [`commands.tex`] Personal commands
        * [`paths.tex`] General paths
    * [`pckg/`] Packages
        * [`packages.tex`] Packages list
    * [`style/`] Design
        * [`listings.tex`] Code
        * [`style.tex`] Miscellaneous settings
* [`report/`] Report files
    * [`chapters/`] Chapters
    * [`components/`] Other files
        * [`abstract.tex`] Abstract
        * [`title.tex`] First page
    * [`materials/`] Non-tex files
        * [`codes/`] Source codes
        * [`images/`] Figures
* [`report.pdf`] Formatted version
* [`report.tex`] TeX version

## Usage
#### Requirements
* A TeX distribution
* An editor

#### Creation of a new report
* Download the repo: `git clone git://github.com/sljrobin/ReporTeX.git`
* Edit the properties in [`report.tex`]
    * Title: `{\reportTitle}{Title}`
    * Subtitle: `{\reportSubtitle}{Subitle}`
    * Author: `{\reportAuthor}{John Smith}`
    * Company: `{\reportCompany}{Company}`
    * Date: `{\reportDate}{dd/mm/yyyy}`
* Change the company's logo in [`report/materials/images/`]
* Write a new chapter
    * Create a new file in [`report/chapters/`]
    * Import it in [`report.tex`] with the `\input` command

## License
The content of this project is licensed under the GPL license.


[Content]: /README.md#content "Content"
[Usage]: /README.md#usage "Usage"
[Requirements]: /README.md#requirements "Requirements"
[Creation of a new report]: /README.md#creation-of-a-new-report "Creation of a new report"
[License]: /README.md#license "License"

[`api/`]: /api/ "api/"
[`env/`]: /api/env/ "env/"
[`commands.tex`]: /api/env/commands.tex "commands.tex"
[`paths.tex`]: /api/env/paths.tex "paths.tex"
[`pckg/`]: /api/pckg/ "pckg/"
[`packages.tex`]: /api/pckg/packages.tex "packages.tex"
[`style/`]: /api/style/ "style/"
[`listings.tex`]: /api/style/listings.tex "listings.tex"
[`style.tex`]: /api/style/style.tex "style.tex"
[`report/`]: /report/ "report/"
[`chapters/`]: /report/chapters/ "chapters/"
[`components/`]: /report/components/ "components/"
[`abstract.tex`]: /report/components/abstract.tex "abstract.tex"
[`title.tex`]: /report/components/title.tex "title.tex"
[`materials/`]: /report/materials/ "materials/"
[`codes/`]: /report/materials/codes/ "codes/"
[`images/`]: /report/materials/images/ "images/"
[`report.pdf`]: https://github.com/sljrobin/ReporTeX/raw/master/report.pdf "report.pdf"
[`report.tex`]: /report.tex "report.tex"
[`report/chapters/`]: /report/chapters/ "report/chapters/"
[`report/materials/images/`]: /report/materials/images/ "report/materials/images/"

[ReporTeX]: https://github.com/sljrobin/ReporTeX "ReporTeX"
