from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH_TO_DRIVER = "/Users/Alexiane/chromedriver"

def fetch_abstracts(key_word, file_no):
    driver = webdriver.Chrome(PATH_TO_DRIVER)
    driver.get("https://arxiv.org/")
    search_bar = driver.find_element_by_xpath("/html/body[@id='front']/div[@class='flex-wrap-footer']/header/div[@id='header']/div[@class='search-block level-right']/form[@class='level-item mini-search']/div[@class='field has-addons']/div[@class='control'][1]/input[@class='input is-small']")
    search_bar.clear()
    search_bar.send_keys(key_word)
    search_bar.send_keys(Keys.RETURN)
    f = open("abstractDataset.txt", "a")
    for i in range(1,file_no+1):
        abstract = driver.find_element_by_xpath(f"/html/body/main[@id='main-container']/div[@class='content']/ol[@class='breathe-horizontal']/li[@class='arxiv-result'][{i}]/p[@class='abstract mathjax']/span[@class='abstract-full has-text-grey-dark mathjax']").get_attribute('innerHTML')
        abstract = abstract.split("<a")[0].rstrip("/n").replace('<span class="search-hit mathjax">','').replace('</span>','')
        f.write(abstract)
    f.close()
    driver.close()

fetch_abstracts("kalman filter", 3)

