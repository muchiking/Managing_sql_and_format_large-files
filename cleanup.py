import re

# Example target string
target_string = "Some text;   \nAnother line;  \nYet another line;"

# Compile the pattern
pattern = re.compile(r';\s*$')

# Find all matches in the target string
result = pattern.findall(target_string)
print(result)  # Output: [';', ';', ';']