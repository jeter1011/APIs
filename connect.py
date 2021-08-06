import requests
api_key = "d72efd1f38fedc359d3705899249ed82"



# what is the HTTP method that we need?

##HTTP request Methods
"""
GET -> grab data
POST -> add/update data

PATCH
PUT
DELETE
"""

# what's our endpoint ( or a url)
"""
Endpoint
/movie/{movie_id}

https://api.themoviedb.org/3/movie/550?api_key=d72efd1f38fedc359d3705899249ed82
"""

movie_id = 500
api_version = 3
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"

r = requests.get(endpoint) # ={"api_key": api_key})
print(r.status_code)
print(r.text)
