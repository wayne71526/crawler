import requests
from bs4 import BeautifulSoup
from pprint import pprint

DCARD_URL = 'https://www.dcard.tw/f/mood/p/234511181/b/'

def get_floor(url):
	r = requests.get(url)
	if r.status_code == requests.codes.ok:
		return r.text
	else:
		return None
	print(r.status_code)	
		
def get_comment(floor):
	soup = BeautifulSoup(floor, 'html.parser')
	name = soup.find('div', 'sc-7fxob4-4 dbFiwE').text
	comment = soup.find('div', 'phqjxq-0 fQNVmg').text
	return name, comment

def get_data():
	data = {}
	for i in range(250):
		url = f'{DCARD_URL}/{i+1}'
		floor = get_floor(url)
		if floor is None:
			break
		name, comment = get_comment(floor)
		if name == '這則回應已被刪除':
			continue
		if data.get(name, None) is None:
			data[name] = []
		data[name].append(comment)
	return data	

def main():
	data = get_data()
	sum_ = 0
	for d in data:
		sum_ = sum_ + len(data[d])
		print('{} 的總留言數: {}'.format(d, len(data[d])))
	print(sum_)	

if __name__ =='__main__':
	main()	








		