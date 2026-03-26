#!/usr/bin/env python3
"""
Convert markdown to LaTeX for academic paper
"""
import re
import sys

def markdown_to_latex(md_content):
    latex = md_content
    
    # Convert headers
    latex = re.sub(r'^# (.*?)$', r'\\\\section{\1}', latex, flags=re.MULTILINE)
    latex = re.sub(r'^## (.*?)$', r'\\\\subsection{\1}', latex, flags=re.MULTILINE)
    latex = re.sub(r'^### (.*?)$', r'\\\\subsubsection{\1}', latex, flags=re.MULTILINE)
    
    # Convert bold
    latex = re.sub(r'\*\*(.*?)\*\*', r'\\\\textbf{\1}', latex)
    
    # Convert italic
    latex = re.sub(r'\*(.*?)\*', r'\\\\textit{\1}', latex)
    
    # Convert inline code
    latex = re.sub(r'`(.*?)`', r'\\\\texttt{\1}', latex)
    
    # Convert bullet lists
    lines = latex.split('\n')
    result = []
    in_list = False
    
    for line in lines:
        if line.strip().startswith('- ') or line.strip().startswith('* '):
            if not in_list:
                result.append('\\\\begin{itemize}')
                in_list = True
            content = line.strip()[2:]
            result.append('    \\item ' + content)
        else:
            if in_list and line.strip() and not line.strip().startswith('-') and not line.strip().startswith('*'):
                result.append('\\\\end{itemize}')
                in_list = False
            result.append(line)
    
    if in_list:
        result.append('\\\\end{itemize}')
    
    latex = '\n'.join(result)
    
    # Convert numbered lists
    lines = latex.split('\n')
    result = []
    in_enum = False
    
    for line in lines:
        match = re.match(r'^\s*\d+\.\s+(.*)$', line)
        if match:
            if not in_enum:
                result.append('\\\\begin{enumerate}')
                in_enum = True
            result.append('    \\item ' + match.group(1))
        else:
            if in_enum and line.strip() and not re.match(r'^\s*\d+\.', line):
                result.append('\\\\end{enumerate}')
                in_enum = False
            result.append(line)
    
    if in_enum:
        result.append('\\\\end{enumerate}')
    
    latex = '\n'.join(result)
    
    # Remove reference sections (will be handled by bibtex)
    latex = re.sub(r'## References.*?(?=\n#|$)', '', latex, flags=re.DOTALL)
    
    # Clean up multiple newlines
    latex = re.sub(r'\n{3,}', '\n\n', latex)
    
    return latex

if __name__ == '__main__':
    with open('/Users/fei/.openclaw/workspace/rl-paper/all_content.md', 'r') as f:
        md_content = f.read()
    
    latex_content = markdown_to_latex(md_content)
    
    # Wrap in document structure
    output = """% Content file for RL Environments for Agentic AI paper
% Generated from markdown

""" + latex_content
    
    with open('/Users/fei/.openclaw/workspace/rl-paper/content.tex', 'w') as f:
        f.write(output)
    
    print("Converted markdown to LaTeX: content.tex")
