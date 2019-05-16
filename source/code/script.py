import requests, sys

def get_pages(pages_src):
    pages = list()
    with open(pages_src) as file:
        for line in file:
            pages.append(line)
    return pages

def diff_request(params):
    res = requests.get('https://api.diffbot.com/v3/article', params=params)
    data = res.json()
    print(data)
    text = data['objects'][0]['text']
    return text

def get_data(output_file, pages):
    for url in pages:
        params = {'token': '08da55b5078aebab3f50860182db3062', 'url': url}
        res = diff_request(params)
        save_data(output_file, res)

def save_data(output_file, res):
    file = open(output_file, 'a+')
    file.write(res)

if __name__ == "__main__":
    pages_src = sys.argv[1]
    output_file = sys.argv[2]
    pages = get_pages(pages_src)

    get_data(output_file, pages)
    
