<div align="center">
<img src="SpiderWeb.png" height=20% width=20%>
</div>
<br>
<div align="center">
<p>A simple and lightweight library for scraping the web</p>
</div>
<br>
<p>Built on Curl and Regex in python , SpiderWeb offers similar functionality to the (BeautifulSoup and requests) alternative . For the package to work , you need to have <a href="https://help.ubidots.com/en/articles/2165289-learn-how-to-install-run-curl-on-windows-macosx-linux">curl</a> installed in your system . </p>

### Install the latest version from Pypi or the <a href="https://github.com/query-lang/SpiderWeb/releases/tag/SpiderWeb">releases page</a> 
```shell
pip install SpiderWeb
```
- Features 
  - [x] Scrape tags from websites 
  - [x] Scrape the text within the tags
  - [x] Obtain href attributes for the <a> tag (anchor tag)
  - [x] Obtain src attribute for the <img> tag (image tag)
  - [x] The package contains new <a href="https://github.com/query-lang/SpiderWeb/tree/main/examples/DataTypes">Datatypes</a> made for easier workflow which integrate with the parameters and values of the package.  

### The main class is ```GenSpider``` . 

```python
from SpiderWeb import GenSpider
web=GenSpider(<website>)
```
### The methods are 
<ol>
  <ul>
    <li><code>website_text</code></li>
    This method returns the markup text of the website . <br>
    <li><code>find_all_html_tags</code></li>
    This method finds all html tags passed in the parameter. If the tags are nested then 
    upon looping them you can add the 'text' keyword in the function to target the initial looped text . <br>
    <li><code>extract_text_from_html</code></li>
    This method extracts text from the looped instance of the tag! <br>
    <li><code>find_all_tags_by_classname</code></li>
    This method finds all html tags passed in the parameter with the given class only , also passed in the parameter. If the tags are nested then 
        upon looping them you can add the 'text' keyword in the function to target the initial looped text. <br>
    <li><code>get_href_from_a_tags</code></li>
    Returns a list of all href attributes of anchor tag . Optional text parameter if you want to target a particualr text piece. Default is extracting href from the entire page.<br>
    <li><code>get_src_from_img_tags</code></li>
    Returns a list of all src attributes of img tag . Optional text parameter if you want to target a particualr text piece. Default is extracting src from the entire page.<br>

  </ul>
</ol>
<br>

### Example code of extracting Comic Book Chapters from <a href="https://readallcomics.com/">readallcomics</a> , using the new DataTypes , and their respective href attributes 

```python
from SpiderWeb import HashMap , ForEach , GenSpider , Str


string=Str("https://readallcomics.com/category/chakra-the-invincible/")
web=GenSpider(string)
x=web.find_all_tags_by_classname('ul','list-story')
arr=HashMap()
for d in x:
  
    w=web.find_all_html_tags('a',text=d)
    num=1
    link_content=web.get_href_from_a_tags(text=d)
    for y in range(len(w)):
        text_content = web.extract_text_from_html(w[y])
        
        arr.add(text_content,link_content[y])
        num+=1

ForEach(arr).unit()
```

### The output of the code will be as follows 
```shell
Chakra The Invincible 010 (2016) => https://readallcomics.com/chakra-the-invincible-010-2016/
Chakra The Invincible 009 (2016) => https://readallcomics.com/chakra-the-invincible-009-2016/
Chakra The Invincible 008 (2016) => https://readallcomics.com/chakra-the-invincible-008-2016/
Chakra The Invincible 007 (2016) => https://readallcomics.com/chakra-the-invincible-007-2016/
Chakra The Invincible 006 (2015) => https://readallcomics.com/chakra-the-invincible-006-2015/
Chakra The Invincible 005 (2015) => https://readallcomics.com/chakra-the-invincible-005-2015/
Chakra The Invincible 004 (2015) => https://readallcomics.com/chakra-the-invincible-004-2015/
Chakra The Invincible 003 (2015) => https://readallcomics.com/chakra-the-invincible-003-2015/
Chakra The Invincible 002 (2015) => https://readallcomics.com/chakra-the-invincible-002-2015/
Chakra The Invincible 001 (2015) => https://readallcomics.com/chakra-the-invincible-001-2015/
```
<br>

<p>For more examples look at : </p>
<ul>
  <li><a href="https://github.com/query-lang/SpiderWeb/tree/main/examples/web">Web Scraping code examples</a></li>
  <li><a href="https://github.com/query-lang/SpiderWeb/tree/main/examples/DataTypes">Data Types code examples</a></li>
  
</ul>

