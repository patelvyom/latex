#!/usr/bin/python3

import os
import sys

class File:
	name = None
	contents = None

	def __init__(self, name, contents):
		self.name = name
		self.contents = contents

if len(sys.argv) < 2:
	print(f'usage: {os.path.basename(sys.argv[0])} <project name>')
	sys.exit(1)

PROJECT = sys.argv[1]
NEWLINE = '\n'
SPACE = ' '
INTERMEDIATE_FILES = [ '*.aux',
					   '*.log',
					   '*.out',
					   '*.bbl',
					   '*.bcf',
					   '*.blg',
					   '*.xml',
					 ]

PROJECT_FILE = File('.project', f"""{PROJECT}""")
GITIGNORE = File('.gitignore', NEWLINE.join(INTERMEDIATE_FILES + ['*.pdf']))

MAKEFILE = File('Makefile',
"""
# A Simple Makefile for working with small latex projects.

PROJECT=$(shell basename $(shell cat .project))
TARGET_PDF=${PROJECT}.pdf

all: ${PROJECT}

DEPENDS=\\
		title.tex\\
		body.tex\\
		bibliography.bib\\
		macros.sty\\
        ${PROJECT}.xmpdata

${TARGET_PDF}: ${PROJECT}.tex ${DEPENDS}
\tpdflatex -interaction=nonstopmode $<
#\tbiber ${PROJECT}                     # Uncomment for bibliography
#\tpdflatex -interaction=nonstopmode $< # Uncomment for bibliography
#\tpdflatex -interaction=nonstopmode $< # Uncomment for bibliography

${PROJECT}: ${TARGET_PDF}

clean:"""
f"""
	rm -f {SPACE.join(INTERMEDIATE_FILES)}
"""
"""
Clean: clean
	rm -f ${TARGET_PDF}

"""
)

MACROS = File('macros.sty',
"""
\\usepackage{geometry}
%Uhh maybe change a4paper to letter if someone may print it. Stupid US Standards.
\\geometry{a4paper,margin=0.75in}
%Import some ams packages for math sybmols/fonts/etc.
\\usepackage{amsmath, amsthm, amssymb, amsfonts}
\\usepackage{physics} % Easy math symbols like norm, abs, etc
\\usepackage{todonotes} % Easily add todo notes
\\usepackage{marvosym} % Extra Symbols
\\usepackage{xcolor}
\\usepackage{xspace}
\\usepackage{float} % For position `H`
\\usepackage{enumitem}
\\usepackage{ifthen} %Use if-else statement
\\usepackage{pdfpages} %Used in including pdf's
\\usepackage{graphicx} %Used to manage images in latex
\\usepackage{setspace} %setting the spacing between lines in a document.
\\usepackage{extarrows} %add fancy-arrows for eg. arrow with super-script etc.
\\usepackage{mathtools} %basically more math symbols
\\usepackage{cancel} % Place diaogonal-lines(cancelling) across math terms
\\usepackage{wrapfig} % Wrap text around figures
\\usepackage{algorithm}
\\usepackage{algorithmic}
\\usepackage{subcaption}
\\usepackage[a-1b]{pdfx}
\\usepackage{nicematrix}
% \\usepackage{minted} % Requires python package installed
\\usepackage{hyperref}
\\definecolor{LightGray}{gray}{0.9}
\\definecolor{aquamarine}{rgb}{0.5, 1.0, 0.83}
\\definecolor{orangepeel}{rgb}{1.0, 0.62, 0.0}
\\hypersetup{
  linkcolor  = violet,
  citecolor  = orangepeel,
  urlcolor   = blue,
  colorlinks = true,
}
\\let\\C\\relax % hyperref uses \C for a certain accent when using bookmarks I guess

\\onehalfspacing
\\allowdisplaybreaks %Allow page-breaks between math env

% FONT STUFF
% See: https://tex.stackexchange.com/questions/59702/suggest-a-nice-font-family-for-my-basic-latex-template-text-and-math

\\usepackage{microtype}
\\usepackage[utf8]{inputenc} % inputenc allows the user to input accented characters directly from the keyboard; 
                             % utf8x : much broader but less compatible ; latin1 : old?
                             % https://tex.stackexchange.com/questions/44694/fontenc-vs-inputenc

\\usepackage[T1]{fontenc}    % fontenc is oriented to output, that is, what fonts to use for printing characters. 
                             % https://tex.stackexchange.com/questions/44694/fontenc-vs-inputenc 
                             % https://tex.stackexchange.com/questions/664/why-should-i-use-usepackaget1fontenc
% mathpazo is obsolete, use newpxtext and newpxmath. newpxtext sets Serif: Palatino, Sans-Serif: Helvetica, Monospace:
% Bera Mono. It also scales as required.
\\usepackage[osf]{newpxtext}  % osf: Old style figures numbers, sc: small caps
\\usepackage{newpxmath}
% \\usepackage{eulervm}
\\usepackage[margin=15pt, font=small, labelfont={bf,sf}]{caption} % Tweak caption labels

% Set font for section headings
\\usepackage{sectsty}
\\allsectionsfont{\\sffamily}

\\usepackage{bm}           % load after all math to give access to bold math

\\DeclarePairedDelimiter{\\floor}{\\lfloor}{\\rfloor}
\\DeclarePairedDelimiter{\\ceil}{\\lceil}{\\rceil}
\\DeclarePairedDelimiter{\\inner}{\\langle}{\\rangle}
\\renewcommand\\qedsymbol{$\\blacksquare$} %Black square looks nice
\\renewcommand{\\bf}[1]{\\textbf{#1}}
\\renewcommand{\\it}[1]{\\textit{#1}}
\\newcommand{\\mbf}[1]{\\mathbf{#1}}
\\newcommand{\\vect}[1]{\\mathbf{#1}}
\\newcommand{\\mcal}[1]{\\mathcal{#1}}
\\newcommand{\\latex}{\\LaTeX}
\\newcommand{\\tex}{\\TeX\\xspace}
\\newcommand{\\etal}{\\textit{et al. }}
\\newcommand{\\numberthis}{\\addtocounter{equation}{1}\\tag{\\theequation}}

\\newcommand{\\field}[1]{\mathbb{#1}}
\\newcommand{\\N}{\\field{N}}
\\newcommand{\\Q}{\\field{Q}}
\\newcommand{\\R}{\\field{R}}
\\newcommand{\\Z}{\\field{Z}}
\\newcommand{\\C}{\\field{C}}
\\newcommand{\\fn}[3]{#1 : #2 \\rightarrow #3}
\\newcommand{\\br}[1]{\\left( #1 \\right)}
\\newcommand{\\curly}[1]{\\left \\{ #1 \\right\\}}
\\newcommand{\\set}[2]{\\curly{#1 \\textbf{:}\\ #2}}
\\newcommand{\\im}{\\textbf{im }}
\\newcommand{\\codom}{\\textbf{codom }}
\\newcommand{\\sbr}[1]{\\left[ #1 \\right]}
\\newcommand{\\eqn}[1]{\\begin{eqnarray*} #1 \\end{eqnarray*}}
\\newcommand{\\eps}{\\varepsilon}%varepsilon is better
\\newcommand{\\del}{\\delta}
\\newcommand{\\limit}[3]{\\lim_{#1 \\rightarrow #2}#3}
\\newcommand{\\bmat}[1]{\\ensuremath{\\begin{bmatrix} #1 \\end{bmatrix}}}
\\newcommand{\\vmat}[1]{\\ensuremath{\\begin{vmatrix} #1 \\end{vmatrix}}}
\\newcommand{\\smat}[1]{\\ensuremath{\\left[\\begin{smallmatrix} #1 \\end{smallmatrix}\\right]}}
\\newcommand{\\diff}[3][]{%                                                                                                          
	\\ifthenelse{\\equal{#1}{}}{%
		\\ensuremath{\\frac{d{#2}}{d{#3}}}%
	}{%                                                                                                                                  
		\\ensuremath{\\frac{d^{#1}\\!{#2}}{d{#3}^{#1}}}%
	}%
}
\\newcommand{\\overbar}[1]{%Between overline and overbar
		\\mkern 1.5mu\\overline{\\mkern-1.5mu#1\\mkern-1.5mu}%
		\\mkern 1.5mu%
}
"""
)

TITLE = File('title.tex',
"""
\\title{\\textbf{\\huge{TITLE HERE}}
	
		\\huge{TEXT HERE}
}
\\author{Vyom Patel}
\\date{\\today}
\\maketitle

%\\pagebreak

""")

BIBLIOGRAPHY = File('bibliography.bib',
"""
@book{DDSE,
	title={Data-Driven Science and Engineering},
	subtitle={Machine Learning, Dynamical Systems, and Control.},
	author={Brunton, Steven L., and Jose Nathan Kutz.},
	publisher={Cambridge University Press},
	year={2019}
}

""")

MAIN = File(f'{PROJECT}.tex',
"""\\documentclass[fleqn]{article}
\\usepackage{macros}
\\usepackage{fancyhdr}
\\pagestyle{fancy}
\\fancyhf{}
\\fancyhead[R]{Vyom Patel}
\\fancyhead[L]{QIC 890: Assignment 1}
\\fancyfoot[C]{\\thepage}
\\renewcommand{\\headrulewidth}{0.5pt}
\\renewcommand{\\footrulewidth}{0.25pt}

% Uncomment the following 3 lines for bibliography (also see Makefile):
% \\usepackage[style=numeric]{biblatex}
% \\renewcommand{\\subtitlepunct}{: }
% \\addbibresource{bibliography.bib}

\\begin{document}

\\input{title}

% Uncomment the following 2 lines for bibliography:
% \\pagebreak
% \\printbibliography

\\end{document}
"""
)

METADATA = File(f'{PROJECT}.xmpdata',
"""
% Replace the following information with your document's actual
% metadata. If you do not want to set a value for a certain parameter,
% just omit it.
%
% Symbols permitted in metadata
% =============================
% 
% Within the metadata, all printable ASCII characters except
% '\', '{', '}', and '%' represent themselves. Also, all printable
% Unicode characters from the basic multilingual plane (i.e., up to
% code point U+FFFF) can be used directly with the UTF-8 encoding. 
% Consecutive whitespace characters are combined into a single
% space. Whitespace after a macro such as \copyright, \backslash, or
% \sep is ignored. Blank lines are not permitted. Moreover, the
% following markup can be used:
%
%  '\ '         - a literal space  (for example after a macro)                  
%   \%          - a literal '%'                                                 
%   \{          - a literal '{'                                                 
%   \}          - a literal '}'                                                 
%   \backslash  - a literal '\'                                                 
%   \copyright  - the (c) copyright symbol                                      
%
% The macro \sep is only permitted within \Author, \Keywords, and
% \Org.  It is used to separate multiple authors, keywords, etc.
% 
% List of supported metadata fields
% =================================
% 
% Here is a complete list of user-definable metadata fields currently
% supported, and their meanings. More may be added in the future.
% 
% General information:
%
%  \Author           - the document's human author. Separate multiple
%                      authors with \sep.
%  \Title            - the document's title.
%  \Keywords         - list of keywords, separated with \sep.
%  \Subject          - the abstract. 
%  \Org              - publishers.
% 
% Copyright information:
%
%  \Copyright        - a copyright statement.
%  \CopyrightURL     - location of a web page describing the owner
%                      and/or rights statement for this document.
%  \Copyrighted      - 'True' if the document is copyrighted, and
%                      'False' if it isn't. This is automatically set
%                      to 'True' if either \Copyright or \CopyrightURL
%                      is specified, but can be overridden. For
%                      example, if the copyright statement is "Public
%                      Domain", this should be set to 'False'.
%
% Publication information:
%
% \PublicationType   - The type of publication. If defined, must be
%                      one of book, catalog, feed, journal, magazine,
%                      manual, newsletter, pamphlet. This is
%                      automatically set to "journal" if \Journaltitle
%                      is specified, but can be overridden.
% \Journaltitle      - The title of the journal in which the document
%                      was published. 
% \Journalnumber     - The ISSN for the publication in which the
%                      document was published.
% \Volume            - Journal volume.
% \Issue             - Journal issue/number.
% \Firstpage         - First page number of the published version of
%                      the document.
% \Lastpage          - Last page number of the published version of
%                      the document.
% \Doi               - Digital Object Identifier (DOI) for the
%                      document, without the leading "doi:".
% \CoverDisplayDate  - Date on the cover of the journal issue, as a
%                      human-readable text string.
% \CoverDate         - Date on the cover of the journal issue, in a
%                      format suitable for storing in a database field
%                      with a 'date' data type.

\\Title        {TITLE HERE}

\\Author       {Vyom Patel}

\\Copyright    {Copyright \copyright\ 2024 "Vyom Patel"}

\\Keywords     {some keyword\sep
               another keyword\sep
               some more keywords}

\\Subject      {SUBJECT HERE}

"""
)
FILES = [ GITIGNORE,
		  MACROS,
		  TITLE,
		  MAIN,
		  METADATA
		]

if '--makefile' in sys.argv[2:]:
    FILES.append(MAKEFILE, PROJECT_FILE)

if '--bib' in sys.argv[2:]:
	FILES.append(BIBLIOGRAPHY)

print(f'> Making directory {PROJECT}...')
os.mkdir(PROJECT)
for f in FILES:
	print(f'> Writing file {f.name}...')
	with open(f'{PROJECT}//{f.name}', 'w+') as fh:
		fh.write(f.contents)
if '--git' in sys.argv[2:]:
	os.chdir(f'./{PROJECT}')
	print(f'> Initializing git...')
	os.system('git init')
	os.system('git add .')
	os.system(f'git commit -m "Setup initial LaTeX project"')
	os.chdir('../')
