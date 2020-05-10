import re, pyperclip, pprint

regexScrape = re.compile(r'''
[A-Z]    # begin with cpaital letter
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

text_file = open("latexFile.txt", "wt")

for line in exstractedLines:
    text_file.write(line + '\n')

text_file.close()
