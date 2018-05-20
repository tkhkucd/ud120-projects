import sys
sys.path.append("../tools/")
from parse_out_email_text import parseOutText

words = parseOutText(open("test_email.txt", 'r'))
print(words)
