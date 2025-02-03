import re

count = 0
inputFileName = input()
inputFile = open(inputFileName, "r")
content = inputFile.read()
outputFile = open("dollar_output.txt", "w")

pattern = re.compile(r"""
                        (?<!\S) 
                        (   
                            \$\d{1,3}(?:,\d{3})*(?:\.\d{1,2})?  #$6.57, $10,000.99
                            |
                            \$?\d{1,3}(?:,\d{3})*(?:\.\d{1,2})?\s*(million|billion|trillion)?\s*(dollars?|USD)  # 500 million dollars, 1.5 billion USD
                            |
                            \d+\s*dollars?(?:\s+and\s+\d+\s+cents?)?  # 1 dollar and 7 cents
                            |
                            \d+\s*cents?  # 75 cents, 1 cent
                            |
                            \$?(?!hundreds?|thousands?|millions?|billions?)\b\w+(\s(?:hundreds?|thousands|millions|billions|of))*\s(?:USD|dollars?|cents?)\b #five million dollar, 
                        ) 
                        (?!\S)  
                    """, re.IGNORECASE | re.VERBOSE)
matches = pattern.finditer(content)

for m in matches:
    outputFile.write(m.group(0)+"\n")
    # count += 1
    # print(m.group(0))

inputFile.close()
outputFile.close()




# re.compile(r"""(\$?\d{1,3}(?:,\d{3})*(?:\.\d{1,2})?\s*(?:million|billion|trillion)?\s*(dollar|dollars|cent|cents)?|\$\d{1,3}(?:,\d{3})*(?:\.\d{1,2})?|\d+\s*dollars?(?:\s+and\s+\d+\s+cents?)?|\d+\s*cents?)""", re.IGNORECASE)  # Matches 75 cents, 1 cent    
#"""(\$?\d{1,3}(?:,\d{3})*(?:\.\d+)?(?:\s(hundred(?:s)?|thousand(?:s)?|million(?:s)?|billion(?:s)?|trillion(?:s)?))?\s(USD|dollar(?:s)?|cent(?:s)?))""", re.IGNORECASE)
# ((\$)?(?:\b(?!hundred(?:s)?|thousand(?:s)?|million(?:s)?|billion(?:s)?|trillion|the|per)\w+|(?:\d+(?:,\d{3})*(?:\.\d+)?))\s?\b(hundred(?:s)?|thousand(?:s)?|million(?:s)?|billion(?:s)?|trillion(?:s)?|the|per)?\s
#                (?:\b(USD|dollar( ?:s)?|cent(?:s)?)\b))|(?:\$?\d{1,3}(?:,\d{3})*(?:\.\d+)?)""",re.IGNORECASE)
# (r"""((\$)?(?:\b(?!hundred(?:s)?|thousand(?:s)?|million(?:s)?|billion(?:s)?|trillion|the|per)\w+|\d+(?:,\d{3})*(?:\.\d+)?)\s?\b(hundred(?:s)?|thousand(?:s)?|million(?:s)?|billion(?:s)?|trillion(?:s)?|the|per)?\s(?:\b(USD|dollar(?:s)?|cent(?:s)?)\b))|
#                         (\$(\d{1,3}(?:,\d{3})*(?:\.\d+)?)|
#                         (\d+))""",re.IGNORECASE) #$number only (allow digits), no currency/number words followed
# \$?(?:(\b(?!hundred|hundreds|thousand|thousands|million|millions|billion|billions|trillion|trillions))\w+|\d+(?:,\d{3})*)(?:\.\d+)?\s(?:USD|dollar|dollars|cent|cents)| #$? word/number currency
# \$?\b(?!hundred|hundreds|thousand|thousands|million|millions|billion|billions|of|us|the)\b(?:\w+|\d+(?:\.\d+)?)\s(?:USD|dollar|dollars|cent|cents)\b|
# \$?(\b(?!hundred|hundreds|thousand|thousands|million|millions|billion|billions|trillion|trillions|of|us|the)\w+|\d+(?:,\d{3})*(?:\.\d+)?\s(?:hundred|hundreds|thousand|thousands|million|millions|billion|billions|trillion|trillions)\s?)+(?:USD|dollar|dollars|cent|cents)\b
# \$?(?:\b(?!hundred|hundreds|thousand|thousands|million|millions|billion|billions|trillion|trillions|of|us|the)\b(?:\w+|\d+(?:,\d{3})*(?:\.\d+)?)\s(?:hundred|hundreds|thousand|thousands|million|millions|billion|billions|trillion|trillions)\s?)+(?:USD|dollar|dollars|cent|cents)\b
# \$?(?:\w+|\d+(?:,\d{3})*(?:\.\d+)?)\s(?:hundred|hundreds|thousand|thousands|million|millions|billion|billions|trillion|trillions)?\s(?:USD|dollar|dollars|cent|cents)\b
# \$?(?!hundred|thousand|million|billion|of)\b(?:\w+|\d+(?:\.\d+)?)\s(?:hundred|hundreds|thousand|thousands|million|millions|billion|billions)\s(?:USD|dollar|dollars|cent|cents)\b
# pattern = re.compile(r"""\$?\b(?!hundred|hundreds|thousand|thousands|million|millions|billion|billions|of|us|US|the)(?:\w+|\d+(?:\.\d+)?)\s(?:USD|dollar|dollars|cent|cents)\b|
#                          \$\d+(?:,\d{3})*(?:\.\d+)?|
#                          \$?(?!million|billion)\b(\w+|\d+(?:\.\d+)?)\s(?:hundred|hundreds|thousand|thousands|million|millions|billion|billions|of)\s(?:USD|dollar|dollars|cent|cents)\b""")
#                         #  \$?(?!(?:hundred|hundreds|thousand|thousands|million|millions|billion|billions|of)\b)(\w+|\d+(?:\.\d+)?)\s(?:hundred|hundreds|thousand|thousands|million|millions|billion|billions|of)\s(?:USD|dollar|dollars|cent|cents)\b""")



