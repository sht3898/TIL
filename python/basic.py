import requests
key = '6b31a8a5101c31e7f9ae3dcdfc249792'
targetDt = '20190713' # yyyymmdd
api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={targetDt}&weekGb=1'
print(api_url)
response = requests.get(api_url).json()
print(response)
