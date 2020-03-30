from selenium import webdriver
import os


class AutoCrawler:
    # use Chrome to access web
    # replace with the path to your chrome driver
    driver = webdriver.Chrome('C:/Users/zenit/Documents/Python/chromedriver_win32/chromedriver.exe')

    def __init__(self, position_css, location_css, search_css):

        self.position_box = position_css
        self.location_box = location_css
        self.search_button = search_css
        self.current_page_url = ''

    # go to job search site
    def go_to_site(self, site_url):
        return self.driver.get(site_url)

    # delete pre-filled data
    def clear_input_field(self):
        character_count = 0

        while character_count <= 30:
            self.driver.find_element_by_id(self.position_box).send_keys('\ue003')
            self.driver.find_element_by_id(self.location_box).send_keys('\ue003')
            character_count += 1

    # enter criteria and search
    def search(self, position_name, location_name):
        self.clear_input_field()
        self.driver.find_element_by_id(self.position_box).send_keys(position_name)
        self.driver.find_element_by_id(self.location_box).send_keys(location_name)
        self.driver.find_element_by_tag_name(self.search_button).click()

    # get the current url
    def get_page_url(self):
        self.current_page_url = self.driver.current_url

    #  run spider
    def run_spider(self, spider_name):
        return os.system(f"scrapy crawl {spider_name}")

    pass


searchIndeed = AutoCrawler('text-input-what', 'text-input-where', 'button')
searchIndeed.go_to_site('https://www.indeed.com/')
searchIndeed.search("Software Engineer", "Smyrna, GA")
searchIndeed.get_page_url()
searchIndeed.run_spider("indeed")

