import requests


def query_yelp(data):
    """Send query to Yelp GQL api"""

    API_KEY = 'Bearer 3j_h366bhf63sjokMN12HtuBNtWfF9FY2fhbsbEGvsZy-FMjsI-h24lHRLfKKevkUbOi5aP55FW0CfxH08Z3aQT2NI19DJfVRumDUzBxLU84QrW_Z8m3MIATuW3_W3Yx'
    YELP_GQL = 'https://api.yelp.com/v3/graphql'
    CONTENT = 'application/graphql'

    r = requests.post(YELP_GQL, headers = {
            'Authorization': API_KEY,
            'Content-Type': CONTENT
            },
            data = data
        )

    return(r)


def yelp_search(location, category):
    query = '''{{
            search(location: "{city}", term: "{term}", sort_by: "rating"){{
                total
                business {{
                    name
                    id
                    rating
                    url
                }}
            }}
        }}'''.format(location= location, term= category)

    r = query_yelp(query)
    return(r.json()['data']['search'])
