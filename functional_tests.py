from selenium import webdriver

browser = webdriver.Firefox()
# Edith heart about cool new web-app with todolist.
# She is going to visit its home page.
browser.get('http://localhost:8000')

# She sees words about todolist in page title and header.
assert 'ToDo' in browser.title

# Then her focus falls on the input field.

# She enters 'Buy Lego for son' there.

# When she clicks 'Enter' page updates and she see
# "1: Buy Lego for son" as first item of the list.

# Input field still focused and she decides to enter one more thing.
# She enters: 'Buy doll for daughter'.

# Page updates again and list have 2 items now.

# Edith wonders if the site remember her list.
# She sees that the site generated unique URL address for her
# - shows some info about this.

# She visits this URL address and sees that her site still there.

# Edith liked it and goes sleep.
browser.quit() 
