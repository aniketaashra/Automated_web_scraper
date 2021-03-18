# *Scraping university data*
## *Problem Statement*
### *Building a repository of universities of UK*
1. Write a scraper to scrape the information about all the universities based out of UK from Wikipedia: https://en.wikipedia.org/wiki/List_of_universities_in_England 
2. For Each University, scrape additional information from their individual pages. Minimum information to be scraped (wherever available): 
    
    a. Former Names 
    
    b. Students 
    
    c. Location 
    
    d. Undergraduates 
    
    e. PostGraduates 
3. Design the Schema to optimize for search. The search term will be on the name of the universities (both current name and former names). 

## *Solution*

##### Scrapy :
An open source and collaborative framework for extracting the data you need from websites.
In a fast, simple, yet extensible way.
###### Installation :
```pip install scrapy```

##### Elastic Search :
Elasticsearch is a distributed, free and open search and analytics engine for all types of data, including textual, numerical, geospatial, structured, and unstructured.
###### Installation :
Please refer ```https://www.elastic.co/downloads/elasticsearch```

##### ScrapyElasticSearch :
Scrapy-ElasticSearch is a pipeline which allows Scrapy objects to be sent directly to ElasticSearch
###### Installation :
```pip install ScrapyElasticSearch```

#### Libraries to be installed :
For Scrapy ```pip install scrapy```

For ScrapyElasticSearch ```pip install ScrapyElasticSearch```

##### *Why we use scrapy to scrape the websites ?*
1. Scrapy enables you to easily post-process any data you find. Data on the web is a mess! It is very unlikely that the data you find will be in the exact format that you would like it to be: it may have extra line breaks; funky styling; extra commas in random places; or simply be in all upper case. Scrapy will let you handle these cases in a straight forward fashion.

2. Data can often be incomplete in the wild - if you are writing your own script you will have to try doubly hard to ensure it is resilient to these cases. Scrapy will make the process of working around incomplete data much easier for you.

3. You will often find when scraping that web pages just blow up in your face: pages won’t be found, servers will have errors or you could have internet connectivity issues half way through a large scrape. Scrapy lets you handle errors gracefully and even has inbuilt ability for resuming a scrape from the last page it encountered. You get all this for free.

4. Some websites will be behind a login wall. Scrapy has built in form handling which you can setup to login to the websites before beginning your scrape.

5. As a tool built specifically for the task of web scraping, Scrapy provides the building blocks you need to write sensible spiders. What are sensible spiders? Spiders that require a minimum amount of maintenance. Individual websites change their design and layouts on a frequent basis and as we rely on the layout of the page to extract the data we want - this causes us headaches. Scrapy separates out the logic so that a simple change in layout doesn’t result in us having to rewrite out spider from scratch.

6. Scraping can cause issues for the sites you are targeting; for example, fetching too many pages at once can put a strain on the target server and take it offline. This will inevitably result in your spider getting banned for abuse - so it’s best to be a good citizen on the web. Scrapy allows you to be one by enabling you to easily throttle the rate at which you are scraping.

7. Scrapy can do multiple requests at the same time which allows scraping runs to be much faster. If you are writing a Python script from scratch that tries to do that, you will likely find that things can go wrong in a horrible million ways. Scrapy has years of use in actual large organisations that avoid this.


##### *How can we connect scrapy with elasticsearch ?*
In Settings.py file add below line's
```
ITEM_PIPELINES = [
  'scrapyelasticsearch.ElasticSearchPipeline',
]

ELASTICSEARCH_SERVER = 'localhost' # If not 'localhost' prepend 'http://'
ELASTICSEARCH_PORT = 9200 # If port 80 leave blank
ELASTICSEARCH_USERNAME = ''
ELASTICSEARCH_PASSWORD = ''
ELASTICSEARCH_INDEX = 'universities'
ELASTICSEARCH_TYPE = 'university'
ELASTICSEARCH_UNIQ_KEY = 'url'
```

### System Requirement 
python 3.6+

### Steps to run the program and get the desired output :
1. Run the ElasticSearch In the background
2. Clone the repo 
    ```https://github.com/saurabh9997/Scraping_university_data.git```
3. Run the requirements.txt  
   ```pip install -r requirements.txt```
4. Change directory to universities 
    ```cd universities```
5. Check status of elasticsearch in backrground(Active/Inactive)
6. Once in above dir 
    ```scrapy crawl university```
7. After scraping done, use desire browser like chrome/firefox/safari etc. and search for
    Former Name using ```http://localhost:9200/universities/_search?pretty&filter_path=hits.hits._source&q=former_name:"Birmingham Polytechnic"```
    or Current Name using ```http://localhost:9200/universities/_search?pretty&filter_path=hits.hits._source&q=current_name:"Birmingham City University"```
    
### Time Complexity
Scrapy took around 8 seconds to scrape all 134 university data.
Searching was done in miliseconds on elasticsearch.

### Schema to optimize search 
 refer Db Design Search.jpg file for class diagram or 
 [!Db](https://github.com/saurabh9997/Scraping_university_data/blob/master/Db%20Design%20Search.jpg?raw=true)
 


