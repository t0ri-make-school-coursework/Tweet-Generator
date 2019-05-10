import sys, requests

def get_urls(source):
  urls = list()
  with open(source, 'r') as file:
    for line in file:
      urls.append(line)
  return urls

def api_request(url, params):
  r = requests.get(url, params) 
  data = r.json()
  response = data['objects'][0]['text']
  return response

def save_response(output, response):
  with open(output, 'a') as file:
    file.write(response)
  return

if __name__ == "__main__":
  source = sys.argv[1]
  output = sys.argv[2]

  urls = get_urls(source)

  api = 'https://api.diffbot.com/v3/article'
  for url in urls:
    response = api_request(api, params = {'token':'08da55b5078aebab3f50860182db3062', 'url': url, 'paging': False,} )
    save_response(output, response)
  