import re

inputFileName = input()
outputFile = open("telephone_output.txt", "w")
inputFile = open(inputFileName, "r")
inputContent = inputFile.read()

pattern = re.compile(r"""
                        (?<!\S) 
                        (
                            \b\d{3}[-.]?\d{3}[-.]?\d{4}\b #standard 10 digit xxx.xxx.xxxx or xxx-xxx-xxxx or xxxxxxxxxx
                            |
                            \(?\d{3}\)?[-.]?\d{3}[-.]?\d{4}\b #standard 10 digit with (xxx) as start
                            |
                            [+]?\d\s?\d{3}[-.]?\d{3}[-.]?\d{4}\b #+x area code
                            |
                            \(\d{1}\)\s?\d{3}[-.]?\d{3}[-.]?\d{4}\b #(x) area code
                        )
                        (?!\S) 
                    """, re.IGNORECASE | re.VERBOSE)

matches = pattern.finditer(inputContent)
count = 0
for m in matches:
    outputFile.write(m.group(0)+"\n")
    count += 1
    # print(m.group(0))
print(count)


inputFile.close()
outputFile.close()

# \b\+?\d{1}?\(?\d{3}[-.)]?\d{3}[-.]?\d{4}\b