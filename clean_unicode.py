#!/usr/bin/env python3
"""
Clean Unicode characters from LaTeX content
"""
import re

with open('/Users/fei/.openclaw/workspace/rl-paper/content_fixed.tex', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove box drawing characters and other problematic Unicode
content = re.sub(r'[─│┌┐└┘├┤┬┴┼]', '', content)
content = re.sub(r'[━┃┏┓┗┛┣┫┳┻╋]', '', content)
content = re.sub(r'[═║╔╗╚╝╠╣╦╩╬]', '', content)

# Remove other potentially problematic characters
content = re.sub(r'[^\x00-\x7F\n]', '', content)

# Fix common issues
content = content.replace('\\section{1.', '\\section{')
content = content.replace('\\section{2.', '\\section{')
content = content.replace('\\section{3.', '\\section{')
content = content.replace('\\section{4.', '\\section{')
content = content.replace('\\section{5.', '\\section{')
content = content.replace('\\section{6.', '\\section{')
content = content.replace('\\section{7.', '\\section{')
content = content.replace('\\section{8.', '\\section{')
content = content.replace('\\section{9.', '\\section{')
content = content.replace('\\section{10.', '\\section{')
content = content.replace('\\section{11.', '\\section{')

with open('/Users/fei/.openclaw/workspace/rl-paper/content_clean.tex', 'w', encoding='utf-8') as f:
    f.write(content)

print("Cleaned content saved to content_clean.tex")
