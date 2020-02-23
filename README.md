### English-Bangla Dictionary
This is dictionary made with Flask, Scrapy.py and Vue.js

* The words are first scraprd from http://www.english-bangla.com/browse/index/a
and stored in a database.
* The scraping part is done in file dist_scrapy
* An api is made using the database which returns  
6 matched data according to the search.
* A Vue.js project(file dict_vue) used this api to retrieve the data and show the result.

### Features:
* A word can be searched in the search box.
* Six nearby words are shown as suggestion.
* If any suggestion is selected, it will redirect to another page
and show the meaning.
* An about page is also added here.

**The website is responsive**
