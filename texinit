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
INTERMEDIATE_FILES = [ '*.aux'
                     , '*.log'
                     , '*.out'
                     , '*.bbl'
                     , '*.bcf'
                     , '*.blg'
                     , '*.xml'
                     ]

PROJECT_FILE = File('.project', f"""{PROJECT}""")

GITIGNORE = File('.gitignore',
                 NEWLINE.join(INTERMEDIATE_FILES + ['*.pdf']))

MAKEFILE = File('Makefile',
"""
PROJECT=$(shell basename $(shell cat .project))
TARGET_PDF=${PROJECT}.pdf

all: ${PROJECT}

DEPENDS=\\
    title.tex\\
    body.tex\\
    bibliography.bib\\
    macros.sty

${TARGET_PDF}: ${PROJECT}.tex ${DEPENDS}
	pdflatex -interaction nonstopmode $<
#	biber ${PROJECT}                     # Uncomment for bibliography
#	pdflatex -interaction nonstopmode $< # Uncomment for bibliography

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
\\usepackage{amsmath}
\\usepackage{amsthm}
\\usepackage{amsfonts}

\\newcommand{\\N}{\\mathbb{N}}
\\newcommand{\\Q}{\\mathbb{Q}}
\\newcommand{\\R}{\\mathbb{R}}
\\newcommand{\\Z}{\\mathbb{Z}}
\\newcommand{\\C}{\\mathbb{C}}
\\newcommand{\\fn}[3]{#1 : #2 \\rightarrow #3}
\\newcommand{\\br}[1]{\\left( #1 \\right)}
\\newcommand{\\curly}[1]{\\left\\{ #1 \\right\\}}
\\newcommand{\\set}[2]{\\curly{#1\\ \\textbf{:}\\ #2}}
\\newcommand{\\im}{\\textbf{im }}
\\newcommand{\\codom}{\\textbf{codom }}
\\newcommand{\\bmat}[1]{\\begin{bmatrix} #1 \\end{bmatrix}}
\\newcommand{\\sbr}[1]{\\left[ #1 \\right]}
\\newcommand{\\eqn}[1]{\\begin{eqnarray*} #1 \\end{eqnarray*}}
\\newcommand{\\abs}[1]{\\left| #1 \\right|}
\\newcommand{\\eps}{\\epsilon}
\\newcommand{\\del}{\\delta}
\\newcommand{\\limit}[3]{\\lim_{#1 \\rightarrow #2}#3}
\\newcommand{\\diff}[2]{\\frac{d^{#1}}{d#2^{#1}}}
\\newcommand{\\sdiff}[3]{\\frac{d^{#1}#3}{d#2^{#1}}}

"""
)

TITLE = File('title.tex',
"""
\\title{An Interesting Paper}
\\author{Author}
\\date{\\today}
\\maketitle

\\pagebreak

""")

BODY = File('body.tex',
"""
We denote the set of real numbers as $\\R$ and that of complex numbers as
$\\C$.

A map is written as $\\fn{f}{X}{Y}$ where $\\im f = f(X)$ and $\\codom f = Y$.

These are large brackets:

\\[
\\br{\\frac{a}{b}}\\br{a + b}
\\]

A simple set:
\\[
  \\curly{\\frac{1}{2}, \\frac{2}{3}, \\frac{\\pi^2}{6}}
\\]

A set with a predicate:
\\[
  \\set{z}{\\zeta\\br{z} = 0}
\\]

Here is a matrix:
\\[
  \\bmat{
    1 & 1 \\\\
    0 & 1 \\\\
  }
\\]

Equivalence class of a sequence:
\\[
  \\sbr{\\frac{1}{n}}
\\]

This is an aligned equation:
\\eqn{
  A &=& 1\\\\
  B &=& 2\\\\
  C &=& 3
}

This is a limit:
\\eqn{
  \\limit{n}{\\infty}{\sum_{i = 1}^n \\frac{1}{i^2}}
}

Limits of functions $\\fn{f}{\\R^m}{\\R^n}$ are defined as follows:
\\eqn{
  \\limit{x}{a}{f(x)} = p \\iff
    \\forall \\eps > 0, \\exists \\del > 0, \\abs{x - a} < \\del
    \\implies \\abs{f(x) - f(a)} < \\eps
}

Here are some derivatives:
\\eqn{
  \\sdiff{n}{x}{y}\\\\
  \\diff{n}{x}\\br{\\sum_{k = 1}^{\infty}\\frac{1}{k^x}}
}

% Uncomment the following line for bibliography:
% Here is a ciatation of a great book \\cite{sheaves}.

""")

BIBLIOGRAPHY = File('bibliography.bib',
"""
@book{sheaves,
  title={Sheaves in Geometry and Logic},
  subtitle={A First Introduction to Topos Theory},
  author={Saunders Mac Lane and Ieke Moerdijk},
  publisher={Springer Verlag-New York, Inc.},
  year={1992}
}

""")

MAIN = File(f'{PROJECT}.tex',
"""
\\documentclass{article}

\\usepackage{macros}

% Uncomment the following 3 lines for bibliography (also see Makefile):
% \\usepackage[style=numeric]{biblatex}
% \\renewcommand{\\subtitlepunct}{: }
% \\addbibresource{bibliography.bib}

\\begin{document}

\\input{title}
\\input{body}

% Uncomment the following 2 lines for bibliography:
% \\pagebreak
% \\printbibliography

\\end{document}

"""
)

FILES = [ PROJECT_FILE
        , GITIGNORE
        , MAKEFILE
        , MACROS
        , TITLE
        , BODY
        , BIBLIOGRAPHY
        , MAIN
        ]

print(f'> Making directory {PROJECT}...')
os.mkdir(PROJECT)
for f in FILES:
  print(f'> Writing file {f.name}...')
  with open(f'{PROJECT}/{f.name}', 'w+') as fh:
    fh.write(f.contents)
if '--git' in sys.argv[2:]:
  os.chdir(f'./{PROJECT}')
  print(f'> Initializing git...')
  os.system('git init')
  os.system('git add .')
  os.system(f'git commit -m "Setup initial LaTeX project"')
  os.chdir('../')
