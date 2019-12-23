from bs4 import BeautifulSoup 
import html2text
import re
import numpy
import pandas as pd
import json

def clean_up (content):
  
	soup = BeautifulSoup(content, features = "html.parser")

	real = str(soup.contents[15])
	real = real.split("\n")
	str_lens = list()

	for i in real:
		str_lens.append(len(i))

	max = str_lens[0]
	for i in range(len(str_lens)):
		if str_lens[i] > max:
		  max = str_lens[i]
		  max_index = i

	req = real[max_index]

	new_string = re.sub(r'<.+?>', '\n', req)
	new_string1 = new_string.split('\n')
	new_string2 = [i for i in new_string1 if i!='']
	
	flag = 0
	count = 0
	for i in new_string2:
		if i == '1':
			break
		else:
			count+=1
	new_string3 = new_string2[count:]
	print(new_string3)
	count = 0
	for i in new_string3:
		if (flag!=1 and i == '2'):
			flag = 1
			break
		else:
			count+=1
	count1 = 0
	print(count)
	for i in range(count, len(new_string3)):
		if i%count == 1:
			if re.search(r'^([1-9]|[12][0-9]|3[01])[/]([1-9]|1[012])[/](19|20)\d\d', new_string3[i]) == None:
				break
		else:
			count1=i

	new_string4 = new_string3[:count1]		
	keys = new_string4[1:count]
	a = numpy.reshape(new_string4, (int(len(new_string4)/count), count))	
	arr = numpy.array([i[1:] for i in a])	
	arr = arr[1:]
	df = pd.DataFrame(arr, columns=keys)
	print(new_string4)
	print(type(a))
	print(df)
	print(type(df))
	df.to_csv("abc.csv", header=True, index=False)
	jsON = json.dumps(json.loads(df.reset_index().to_json(orient='records')), indent = 4)
	return jsON
  
# with open("random", "r") as file:
#   file_data = file.read()
# clean_up(file_data)

