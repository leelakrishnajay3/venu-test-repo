# from atlassian import Confluence

# Obtain an API token from: https://id.atlassian.com/manage-profile/security/api-tokens
# You cannot log-in with your regular password to these services.

# confluence = Confluence(
#     url='https://roshan-08.atlassian.net/',
#     username='zerothroshan@gmail.com',
#     password='LjZQfEOgdsdj9JGy00IVE96D',
#     cloud=True)

# if confluence.page_exists("CI20045"):
#     print("page exists")
# else:
#     print("page not found")


# This code sample uses the 'requests' library:
# http://docs.python-requests.org
# import requests
# from requests.auth import HTTPBasicAuth
# import json

# url = "https://roshan-08.atlassian.net/wiki/rest/api/space"

# auth = HTTPBasicAuth("zerothroshan@gmail.com", "LjZQfEOgdsdj9JGy00IVE96D")

# headers = {
#    "Accept": "application/json"
# }

# response = requests.request(
#    "GET",
#    url,
#    headers=headers,
#    auth=auth
# )

# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

#### Create the page
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://roshan-08.atlassian.net/wiki/rest/api/content"

auth = HTTPBasicAuth("zerothroshan@gmail.com", "LjZQfEOgdsdj9JGy00IVE96D")

headers = {
   "Accept": "application/json",
   "Content-Type": "application/json"
}

payload = json.dumps( {
     	    "space": {
			"key": "R12" 
	    },
	    "type": "page",
	    "title": "Page created from python Script",
	    "body": {
	    	    "storage": {
		    	       "value": "This is my page content",
			       "representation": "wiki"
		  }
	     }
      }
)

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


###################################################################



import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://roshan-08.atlassian.net/wiki/rest/api/content"

auth = HTTPBasicAuth("zerothroshan@gmail.com", "LjZQfEOgdsdj9JGy00IVE96D")

headers = {
   "Accept": "application/json",
   "Content-Type": "application/json"
}

payload = json.dumps( {
     	    'type': 'page',
    'title': "Tested CU",
    'ancestors': [{'id':1179649}],
    'space': {'key':'R12'},
    'body': {
        'storage':{
            'value': "This is child page",
            'representation':'storage',
        }
    }
      }
)

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


# url = 'https://example.com/confluence/rest/api/content/' + \
#           str(PAGE_ID) + '/child/attachment/'
# headers = {'X-Atlassian-Token': 'no-check'} #no content-type here!
# file = 'image.jpg'

#     # determine content-type
# content_type, encoding = mimetypes.guess_type(file)
# if content_type is None:
#     content_type = 'multipart/form-data'

#     # provide content-type explicitly
# files = {'file': (file, open(file, 'rb'), content_type)}

# auth = ('USR', 'PWD')
# r = requests.post(url, headers=headers, files=files, auth=auth)
# r.raise_for_status()

import requests
from requests.auth import HTTPBasicAuth
import json
import mimetypes

url = "https://roshan-08.atlassian.net/wiki/rest/api/content/1179662/child/attachment"

auth = HTTPBasicAuth("zerothroshan@gmail.com", "LjZQfEOgdsdj9JGy00IVE96D")

headers = {
   "Accept": "application/json"
}

file = 'Assessment_Angular_OSR_Application.xlsx'

    # determine content-type
content_type, encoding = mimetypes.guess_type(file)
if content_type is None:
    content_type = 'multipart/form-data'

files = {'file': (file, open(file, 'rb'), content_type)}

response = requests.request(
   "PUT",
   url,
   headers=headers,
   files=files,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))






















