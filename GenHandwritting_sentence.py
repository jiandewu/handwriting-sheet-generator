#!/usr/bin/python
#coding=utf-8
#Filename:GenPoem.py

import os
import time
import codecs, random

def isint(value):
  try:
    int(value)
    return True
  except:
    return False
    
#  \setmainfont{Lakesight Personal Use Only}
def genhand(lines):
	prefix=r'''\documentclass[12pt]{article}
\let\oldthepage\thepage
\renewcommand*\thepage{\small{\ttfamily-- \oldthepage\ --}}
\makeatletter
\newcommand\HUGE{\@setfontsize\Huge{25}{33}}
\makeatother
\usepackage[top=0.5in,bottom=0.7in,left=0.5in,right=0.5in]{geometry}
\setlength\parindent{0pt}
\setlength{\parskip}{0em}
\usepackage{tikz}
  \usetikzlibrary{calc}
\usepackage{fontspec}
  \setmainfont{DN Manuscript}
\usepackage{setspace}
\setstretch{1.5}
\newcommand{\baseheight}{-0.1ex}
\newcommand{\lowercaseheight}{1ex}
\newcommand{\uppercaseheight}{2ex}
\newcommand{\descenderdepth}{-0.6ex}
\usepackage{lineno}
\newenvironment{drillsheet}{
    \setlength\linenumbersep{0pt}
    \renewcommand{\thelinenumber}{
        \begin{tikzpicture}[overlay]
                \draw [line width=0.25mm] ((0.85ex,\baseheight) -- ++(\textwidth,0);
                \draw [line width=0.01mm,dashed] ((0.85ex,\lowercaseheight) -- ++(\textwidth,0);
                \draw [line width=0.01mm] (0.85ex,\uppercaseheight) -- ++(\textwidth,0);
                %%\draw [line width=0.01mm] (0.85ex,\descenderdepth) -- ++(\textwidth,0);
                \draw [line width=0.25mm] (0.85ex,{-2.0 * \uppercaseheight + \baseheight}) -- ++(\textwidth,0);
                \draw [line width=0.01mm,dashed] (0.85ex,{-2.0 * \uppercaseheight + \lowercaseheight}) -- ++(\textwidth,0);
                \draw [line width=0.01mm] (0.85ex,{-2.0 * \uppercaseheight + \uppercaseheight}) -- ++(\textwidth,0);
                %%\draw [line width=0.01mm] (0.85ex,{-2.0 * \uppercaseheight + \descenderdepth}) -- ++(\textwidth,0);
        \end{tikzpicture}
    }
    \renewcommand\linenumberfont{\normalfont\color{black}}
    \begin{linenumbers}
        \color{black}
}{
    \end{linenumbers}
}
\linespread{2.2}
\usepackage[none]{hyphenat}
\usepackage[document]{ragged2e}
\begin{document}
\HUGE
\begin{drillsheet}
\begin{flushleft}
'''
	afterfix=r'''
\end{flushleft}
\end{drillsheet}
\end{document}'''


	bkdir=os.environ.get('jTMP')
	tmpdir=bkdir.replace('\\','/')+'/'
	hwdir=bkdir.replace('\\','/')+'/'

	filename=tmpdir+'hndstnc'
	texfile=filename+'.tex'

	handtex=open(texfile,'w')
	handtex.write(prefix)

	handtex.write('\n\n'.join(lines))

	handtex.write(afterfix)
	handtex.close()

	latex_command="xelatex -output-directory %s \"%s\"" %(tmpdir,texfile)
	if os.system(latex_command)==0:
		# if os.system(latex_command)==0:
			pdfname=hwdir+time.strftime('%Y%m%d%H%M%S')+'Sentence'+'.pdf'
			print "Successful generate PDF file, Now copy %s..."%pdfname
			os.system("mv -f "+filename+".pdf "+pdfname)
			#os.system("mv -f "+filename+".tex "+"test.tex")
			os.system("rm -f "+filename+"*")
	else:
		print "First xelatex Failed!!!"

fin = open("chapter-101.txt",'r')
alllines=[]
for line in fin.readlines():
	alllines.append(line)
fin.close()

genhand(alllines)
