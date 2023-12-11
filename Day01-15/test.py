import json

import requests


def main():
    resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
    print(resp)
    data_model = json.loads(resp.text)
    print(data_model)
    for news in data_model['msg']:
        print(news)


if __name__ == '__main__':
    main()
