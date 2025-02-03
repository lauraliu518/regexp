# Regular Expression
The **dollar_program.py** program extracts all monetary values incluing (but not limited to): numerical monetary values including decimals and separators ($5, 23.12 usd or 456,445,4444, etc.); text-based monetary values (two dollars, one hundred million usd, seven dollars and two cents, etc.).<br>  

The **phone_regexp.py** program extracts all telephone numbers and considers combinations of standard american 10-digit phone numbers, as well as area codes. Some match examples include: +1 234-567-8910; (1)123456789; 123456789; 123.456.789; 123-456-789.

All programs are designed and tested using all-OANC.txt (training corpus). 
Final assessment was made with test_dollar_phone_corpus.txt (test corpus).
Final test results are stored in dollar_output.txt and telephone_output.txt, with one match per line. 

## Run the program with:
**dollar_program.py fileToBeProcessed** for monetary value extraction<br>  

**phone_regexp.py fileToBeProcessed** for telephone number extraction
