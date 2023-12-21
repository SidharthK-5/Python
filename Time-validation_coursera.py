# Time format validation
# time format hh:mm
inputs = ['18:29', '23:55', '123', 'ab:de', '18:299', '99:99']

import re
print([re.fullmatch('[0-9]{2}:[0-9]{2}', x) for x in inputs])

# Now validate time only between 00:00 to 23:59

regex = '([01][0-9]|2[0-3]):([0-5][0-9])'
print([re.fullmatch(regex, x) for x in inputs])