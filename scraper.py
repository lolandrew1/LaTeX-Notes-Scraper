import re, pyperclip

regexScrape = re.compile(r'''
[A-Z]    # begin with capital letter
.* 
\\it\s
.*
\.
''', re.VERBOSE)

regexPrim = re.compile(r'''
(\s{\\it
(.*)
})
''', re.VERBOSE)



text = pyperclip.paste()
exstractedLines = regexScrape.findall(text)

text_file = open("latexOutput.txt", "wt")
text_top = """\\documentclass{article}
\\usepackage{amssymb, mathrsfs, enumitem}
\\usepackage{tikz-cd}
\\usepackage{multicol}
\\usepackage{graphicx}
\\usepackage{color}
\\usepackage{amsthm}
\\usepackage{hyperref}
\\usepackage{verbatim}
\\usepackage{caption}
\\usepackage{subcaption}
\\usepackage{amsmath, epsfig, colortbl}
\\usepackage[breakable, skins]{tcolorbox}
\\setlength{\parskip}{8pt}
\\usepackage{geometry}
\\geometry{
 a4paper,
 total={170mm,257mm},
 left=20mm,
 top=20mm,
 }
\\begin{document}
\\section{Important Terms}
\\begin{itemize}
\n"""

text_bot = '''
\end{itemize}
\end{document}'''

text_add = '\\item '

text_file.write(text_top)

for line in exstractedLines:
    text_file.write(text_add + line + '\n')

text_file.write(text_bot)

text_file.close()