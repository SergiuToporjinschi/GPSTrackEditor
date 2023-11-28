import re

pattern = r'^(?!.*(?:\|\||&&))(?=.*[|&])[^|&].*[^|&]$'

texts = [
    "This has a | and &",
    "NoDouble || or && in this text",
    "Ends with |",
    "& Starts with this",
    "teee & sss| sss"
]

for text in texts:
    if re.match(pattern, text):
        print(f"Text '{text}' is a full match.")
    else:
        print(f"Text '{text}' does not match the pattern.")