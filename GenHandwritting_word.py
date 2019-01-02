#!/usr/bin/python
#coding=utf-8
#Filename:GenPoem.py

import os
import time
import codecs, random

def genhand(words):
	prefix=r'''\documentclass[12pt,twoside]{article}
\let\oldthepage\thepage
\renewcommand*\thepage{\small{\ttfamily-- \oldthepage\ --}}

\makeatletter
\newcommand\HUGE{\@setfontsize\Huge{45}{60}}
\makeatother

\usepackage[top=0.45in,bottom=0.5in,left=0.5in,right=0.5in]{geometry}
\setlength\parindent{0pt}
\setlength{\parskip}{1em}
\usepackage{tikz}
  \usetikzlibrary{calc}

\usepackage{fontspec}
  \setmainfont{kiddySans}

\newlength{\lengthoftext}
\newcommand\threelines[1]{
\settowidth{\lengthoftext}{#1}
\begin{tikzpicture}[baseline=(char.base)]
  \pgfmathtruncatemacro\numberofwords{int((\textwidth+\wordsep)/(\lengthoftext+\wordsep))}
  \pgfmathtruncatemacro\wordsep{int((\textwidth-\lengthoftext*\numberofwords)/(\numberofwords-1))}
  \draw[help lines,thick]
    (0,0) -- (\textwidth,0);
  \draw[help lines,dashed]
    (0,0.68*\linesep) -- (\textwidth,0.68*\linesep);
  \draw[help lines,ultra thin]
    (0,\linesep) -- (\textwidth,\linesep);
  \foreach \col in {1,...,\numberofwords} {
    \node[inner sep=0pt,anchor=base west]
      (char) at ({(\col-1)*(\lengthoftext+\wordsep)},\gridraiseamount) {#1};
  }
\end{tikzpicture}}

\begin{document}
\HUGE
\newlength{\linesep}
\settoheight{\linesep}{X}
\newcommand{\lineseps}{0.25em}
\newcommand{\parseps}{0.2em}
\newcommand\gridraiseamount{0em}
\newlength{\wordsep}
\settowidth{\wordsep}{xx}
'''
	afterfix=r'''\end{document} '''

	handfile='tmphand'
	handtexfile=handfile+'.tex'
	
	handtex=open(handtexfile,'w')
	handtex.write(prefix)

	worditems=[]
	num=0
	for i in words:
		num+=1
		item=r'''\threelines{%s}\vspace{-\lineseps}
\threelines{}\vspace{-\lineseps}
\underline{\hspace{\textwidth}}\vspace{-\parseps}'''%i
		if num==5:
			item+='\\clearpage\n'
			num=0
		worditems.append(item)

	handtex.write('\n'.join(worditems))

	handtex.write(afterfix)
	handtex.close()

	latex_command="xelatex %s" %(handtexfile)
	if os.system(latex_command)==0:
		# if os.system(latex_command)==0:
			pdfname='hwwords'+time.strftime('%Y%m%d%H%M')+'.pdf'
			print "Successful generate PDF file, Now copy %s..."%pdfname
			os.system("mv -f "+handfile+".pdf "+pdfname)
			# os.system("rm -f "+handfile+"*")
	else:
		print "First xelatex Failed!!!"

fin = open("words.txt",'r')
allwords=[]
for line in fin.readlines():
	allwords.append(line.split())
fin.close()

genhand(allwords[-1])
