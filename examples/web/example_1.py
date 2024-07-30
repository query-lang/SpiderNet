from SpiderWeb import HashMap , ForEach , GenSpider , Str


string=Str("https://readallcomics.com/category/chakra-the-invincible/")
s=GenSpider(string)
x=s.find_all_tags_by_classname('ul','list-story')
arr=HashMap()
for d in x:
  
    w=s.find_all_html_tags('a',text=d)
    num=1
    link_content=s.get_href_from_a_tags(text=d)
    for y in range(len(w)):
        text_content = s.extract_text_from_html(w[y]).split(" ")[3]
        
        arr.add(text_content,link_content[y])
        num+=1

ForEach(arr).unit()
print("------------------------")
print(arr.value('010'))
