# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import re

def main():
    for line in sys.stdin.readlines():
        if line == '\n':
            continue
        # Determine operation
        params = line[:4].split(";")
        data = line[4:]
        result = ""
        # If is split operation
        if params[0] == 'S':
            if params[1] in ['M', 'V']:
                # Get all words starting with uppercase
                uppers = re.findall('[A-Z][^A-Z]*', data)
                # Find first uppercase letter index
                upperIdx = 4 + data.index("".join(uppers))
                # Add the first word to the result
                result += line[4:upperIdx]
                # Add consecutive words, converting to lower case
                for el in uppers:
                    result += (" " + el.lower().replace("()", ""))
            else:
                # For class names
                result = " ".join(re.findall('[A-Z][^A-Z]*', data)).lower()
        else:
            # For combine operation
            words = re.findall('[a-z]*', data)
            # Check if this is a class name
            if params[1] == "C":
                result += words[0][:1].upper() + words[0][1:]
            else:
                result += words[0]
            for i in range(1, len(words)):
                result += words[i][:1].upper() + words[i][1:]
            if params[1] == "M":
                result += "()"

        result = result.replace('\n', '')
        print(result)



main()