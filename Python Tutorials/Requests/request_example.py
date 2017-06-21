# Import the request module
import requests

# User input for the url
url = raw_input('Enter in your URL here: ')

# Here, requests will get the url and visit it, if the url happens to be a valid url
re = requests.get(url)

# This prints out the status code of the connection. 200 means everything is fine
print 'This is the current status code: {}'.format(re.status_code)
