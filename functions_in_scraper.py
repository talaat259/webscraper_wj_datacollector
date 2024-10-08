from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

import time
import csv

#global i
#i=1

def links_generator(url,rows):
    #driver = webdriver.Chrome()
    global i
    i=1
    for date_ in rows:
        tar = date_[0]
        parsed_date = tar.replace("-", "/")  # Format the date correctly for the URL
        url_new = url + parsed_date + "#:~:text=Search%20WSJ's%20digital%20archive%20of%20news"
        print(f"Fetching URL: {url_new}")
        #global i
        print(f'i in links generator {i}')
        
        extractor(url_new,parsed_date)
        print("@"*10)
        print("out")
        print("@"*10)
        i=1

        

def article_extractor(articles,parsed_date):
    print('articles')
    for article in articles:
        # Extract the headline
        headline_tag = article.find('span', class_='WSJTheme--headlineText--He1ANr9C')
        headline = headline_tag.text.strip() if headline_tag else 'No headline'

        # Extract the article link
        link_tag = article.find('a', href=True)
        link = link_tag['href'] if link_tag else 'No link'

        # Extract the timestamp
        timestamp_tag = article.find('p', class_='WSJTheme--timestamp--22sfkNDv')
        timestamp = timestamp_tag.text.strip() if timestamp_tag else 'No timestamp'

        # Print or save the extracted data
        print(f"Headline: {headline}")
        print(f"Link: {link}")
        print(f"Timestamp: {timestamp}")
        print(f"date:{parsed_date}")
        print(f"type of link is {type(link)}")
        print("-" * 50)
        content_creator(headline,link,parsed_date)





def extractor(url_new,parsed_date):
    global i
    #driver = webdriver.Chrome()
    print("ana hena")
    driver.get(url_new)
    print("we hena")
   
    time.sleep(3)  

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # Find all articles on the page (based on the actual structure sof the page)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    #pages=soup.find_all("div",class_="WSJTheme--pagepicker--3FhvdbqK ")
    span_element = driver.find_element(By.CLASS_NAME, "WSJTheme--pagepicker-total--Kl350I1l")

    text_content = span_element.text

# Split the text to get the second part (page number)
# Assuming the text is always in the format "of X", where X is the page number
    page_number_end = int(text_content.split()[-1])
    #page_rakam=text_content.split()[-1]

    #print(f"pages====>{type(page_number_end)}")
    #print(f"page====>{page_number_end}")
    #print(f"number of pages left={len(page_number_end)}")
    print("////////////////////////////////////////////////////////////////////////////////////////////////////////////")
    while(i<=page_number_end):
        print(f'page++>{i}')
        print(f"parsed date===>{parsed_date}")
        articles = soup.find_all('article', class_='WSJTheme--story--XB4V2mLz')
        time.sleep(3)
        #button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".WSJTheme--next--2r7-j2I8")))
        #button.click()

        # Print the number of articles found
        print(f"Number of articles found: {len(articles)}")
        article_extractor(articles,parsed_date)
        i=i+1
        strr=str(i)
        linkawi="https://www.wsj.com/news/archive/2000/01/03?page="+strr
        extractor(linkawi,parsed_date)
        
    print("tele3t we shaklak ryaal")
    print("badong_al_dong"*10)
    

    # Print the number of articles found
    #print(f"Number of articles found: {len(articles)}")
    #article_extractor(articles,parsed_date)

def content_creator(headline,link,date):
    Edge_options=Options()
    Edge_options.add_argument("/home/talaat/.config/microsoft-edge/Default")

    driver1 = webdriver.Edge()
    
    file_name=date
    driver1.get(link)
    #section = driver.find_element(By.CLASS_NAME, ".ef4qpkp0.css-uouibe-Container.etunnkc21")
    time.sleep(5)
    page_source = driver1.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    section = soup.find_all("section")
    time.sleep(20)

    section_text=section.text
    #content = "\n".join([p.text for p in paragraphs])
    print("contentttttt"*10)
    print(section_text)
    print("contentttttt"*10)
    exit()
    #with open(f"/home/talaat/Dates_Dataset_Articles/{file_name}.txt","a")as document:
        #document.write(headline)
       # pass





if __name__=="__main__":
    global driver
    #global i
    #driver = webdriver.Edge(executable_path="/home/talaat/Downloads/edge_extract/edgedriver_linux64/msedgedriver")
    Edge_options=Options()
    Edge_options.add_argument("/home/talaat/.config/microsoft-edge/Default")

    driver = webdriver.Edge()
    rows = []
    with open("/home/talaat/Desktop/dates_list.csv", "r") as document:
        dates = csv.reader(document)
        for row in dates:
            rows.append(row)

        # Remove the header row
    rows.pop(0)
    print("gowa al main")

    # Define the base URL for the WSJ archive
    url = "https://www.wsj.com/news/archive/"
    #i=1
    links_generator(url,rows)





