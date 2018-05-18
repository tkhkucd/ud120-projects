import sys
sys.path.append("../tools/")
from parse_out_email_text import parseOutText

words = parse_out_email_test(open("test_email.txt"))
print(words)
