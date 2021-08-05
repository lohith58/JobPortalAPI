import requests
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/blorejobsinfo/'
r=requests.get(BASE_URL+ENDPOINT)
data=r.json()
for job in data:
    print('Company Name:',job['company'])
    print('Eligibility:',job['eligibility'])
    print('Title:',job['title'])
    print('Mail Id:',job['email'])
    print('Phone Number:',job['phonenumber'])
    print()
