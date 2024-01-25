import re

def extract_code_from_markdown(string):
    pattern = r'```.*\n([\s\S]+?)\n```'  # regex pattern to match code block
    matches = re.findall(pattern, string)
    
    return matches