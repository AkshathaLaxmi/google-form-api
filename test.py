from bs4 import BeautifulSoup 
import html2text

def clean_up (content):
  
  soup = BeautifulSoup(content, features = "html.parser")

  #for i in soup.children:
  	#print(soup.contents[15])
  real = str(soup.contents[15])
  real = real.split("\n")
  str_lens = list()
  #print(len(real[69]))
  for i in real:
    str_lens.append(len(i))

  max = str_lens[0]
  for i in range(len(str_lens)):
    if str_lens[i] > max:
      max = str_lens[i]
      max_index = i
  
  req = real[max_index]

  new_req5 = []
  for i in req:
    i = i + " "
    new_req5.append(i)
  new_req = []
  for i in new_req5:
    if "<" in i:
      i = i.replace("<", " ")
      new_req.append(i)
  new_req2 = []
  for i in new_req:
    if "/" in i:
      i = i.replace("/", " ")
      new_req2.append(i)
    else:
      new_req2.append(i)
  new_req3 = []
  # for i in new_req2:
  #   if "freezebar" not in i :
  #     i = i.strip()
  #     new_req3.append(i)We <3 p
  for i in new_req2:
    if " td" in i:
      i = i.replace(" td", " ")
    new_req3.append(i)
  new_req4 = []
  for i in new_req3:
    if " tr " not in i:
      if "div class" not in i:
        if " th " not in i:
          if " thead " not in i:
            if " table " not in i:
              if " tbody " not in i:
                if "  class " not in i:
                  if " class=" not in i:
                    new_req4.append(i)
  

  soup2 = BeautifulSoup(req, 'html.parser')
  tags = soup2.findAll('tr')
  print(tags[:4])
  new_tags = []
  for i in tags:
    i = str(i.findAll('td'))
    new_tags.append(i)
  #print(new_tags[:4])
  
  new_tags2 = []

  for i in new_tags:
    i = i.split(">")
    for j in i:
      j = j.replace("</td", "")
      j = j.replace("</div", "")
      new_tags2.append(j)
  

  new_tags3 = []
  print(new_tags2[:4])
  # for i in new_tags2:
  #   print(i)
  #   if "<td" not in i:
  #     new_tags3.append(i)



  j = 0
  for i in new_tags3:
    print(j, ":", i)
    print("\n")
    j+=1
  soup = str(soup)
  h = html2text.HTML2Text()
  h.ignore_links = True
  print(h.handle("")) 
#   print(type(new_tags[0]))
  
with open("Random (Responses)", "r") as file:
  file_data = file.read()
clean_up(file_data)


