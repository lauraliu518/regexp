import re

inputFileName = input()
inputFile = open(inputFileName, "r")
content = inputFile.read()
outputFile = open("dollar_output.txt", "w")

pattern = re.compile(r"""
                        \$\d{1,3}(?:,\d{3})*(?:\.\d{1,2})?  #$6.57, $10,000.99
                        |
                        \$?\d{1,3}(?:,\d{3})*(?:\.\d{1,2})?\s*(million|billion|trillion)?\s*(dollars?|USD)  # 500 million dollars, 1.5 billion USD
                        |
                        \d+\s*dollars?(?:\s+and\s+\d+\s+cents?)?  # 1 dollar and 7 cents
                        |
                        \d+\s*cents?  # 75 cents, 1 cent
                        |
                        \$?(?!hundreds?|thousands?|millions?|billions?)\b\w+(\s(?:hundreds?|thousands|millions|billions|of))*\s(?:USD|dollars?|cents?)\b #five million dollar,  
                    """, re.IGNORECASE | re.VERBOSE)
matches = pattern.finditer(content)

for m in matches:
    outputFile.write(m.group(0)+"\n")

inputFile.close()
outputFile.close()
