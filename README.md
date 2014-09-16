# ReporTeX
[ReporTeX] is a template designed for writing LaTeX reports faster and to focus as much as possible on the content and not on the layout.

## Table of contents
* [Features]
* [Installation]
* [Content]
* [Links]
* [License]

## Features
## Installation
#### Requirements
* Before using the sources, make sure that you have installed:
    * [Ruby]
    * [Nanoc]
    * [Bundler]
* If not, launch these commands (_you might need root privileges to run this command_):
```
aptitude install ruby
gem install nanoc
gem install bundler
```
* If you're using _Windows_, _OS X_ or not a _Debian-based distribution_, check out the [Help and Docs] section for more information about installation.

#### Compiling and Viewing
* Download the repo: `git clone git://github.com/sljrobin/sljrobin.com.git`
* Go to the working directory: `cd sljrobin.com/`
* Install the required gems: `bundle install`
* Compile the sources: `nanoc compile`
* Start the web server: `nanoc view`
* Open your web browser
* Navigate to `http://localhost:3000`

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

## Links

## License
The content of this project is licensed under the GPL license.


[Features]: /README.md#features "Features"
[Installation]: /README.md#installation "Installation"
[Content]: /README.md#content "Content"
[Links]: /README.md#links "Links"
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
[`report.pdf`]: /report.pdf "report.pdf"
[`report.tex`]: /report.tex "report.tex"


[ReporTeX]: / "ReporTeX"
