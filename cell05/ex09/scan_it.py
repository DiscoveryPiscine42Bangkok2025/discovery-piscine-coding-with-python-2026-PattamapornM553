import re
import sys

if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    sentence = sys.argv[2]
    found = re.findall(keyword, sentence)
    if found:
        print(len(found))
    else:
        print("none")