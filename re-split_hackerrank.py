# re.split() splits the string when the given re pattern is found
regex_pattern = r"[,.]" # Pattern to detect

import re
print("\n".join(re.split(regex_pattern, input()))) # when regex_pattern is found in the input, split breaks it at the pattern