import pandas as pd
# Instead of pd.read_csv('huge.csv'), do:
data = pd.DataFrame({'x': [1,2,3], 'y': [4,5,6]})
# Then reproduce the bug on this tiny data.

'''
You have the MRE template for pandas. Good. The exercise was to write a plan for an MRE of a web scraper. I don’t see that plan in your notes – but you can just describe it in text. For example:

    Remove database – just print the extracted data.

    Replace live URL with a local HTML file or a short string that contains only the problematic HTML fragment.

    Keep only the parsing function (e.g., find_all('div', class_='xyz')).

    Remove all loop and error‑handling code not needed to trigger the bug.
'''