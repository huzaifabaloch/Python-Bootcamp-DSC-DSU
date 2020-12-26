from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import credentials


class FacebookBot:
    def __init__(self, post_url):
        self.post_url = post_url

        # Chrome drive path
        self.chrome_driver = r'chrome driver\chromedriver.exe'

        self.driver = webdriver.Chrome(executable_path=self.chrome_driver)
        self.driver.maximize_window()
   
    # TASK - 01    
    def hit_link_and_login(self):

        self.driver.get(self.post_url)
        # Xpath for login button with click event
        self.driver.find_element_by_xpath("(//*[contains(@href, 'login.php')])[1]").click()

        # Xpath for email/phone and password
        email_or_phone = self.driver.find_element_by_xpath("//input[@name='email']")
        passowrd = self.driver.find_element_by_xpath("//input[@name='pass']")

        # filling up fields with user email/phone and password
        email_or_phone.send_keys(credentials.PHONE)
        passowrd.send_keys(credentials.PASSWORD)

        # Xpath for login button with click event
        self.driver.find_element_by_xpath("//button[@name='login']").click()
        self.driver.implicitly_wait(10)
    
    
    def like_and_share(self):

        caption = 'Hi I"m Autofish Bot. This post was shared using a bot that I learnt to create from Python Bootcamp 2020 held by DSC@DSU. #DSCDSU #DeveloperStudentClubs #DSCPakistan #Python #Bot'
        
        # Xpath for like button with click event
        self.driver.find_element_by_xpath("//a[@data-sigil='touchable ufi-inline-like like-reaction-flyout']").click()
        
        # To make bot share the post with caption on it.
        # Xpath for share button popup with click event
        self.driver.find_element_by_xpath("//a[@data-sigil='share-popup']").click() 
        # Xpath for write button on share popup with click event
        self.driver.find_element_by_xpath("//a[@data-sigil='touchable touchable share-with-message-button']").click() 
        self.driver.implicitly_wait(10)
        # Xpath for textarea, making it focused
        text_area = self.driver.find_element_by_xpath("//textarea[contains(@class, 'share')]")
        text_area.click()
        text_area.send_keys(caption)
        # Click the post button.
        self.driver.find_element_by_xpath("//button[@id='share_submit']").click()
        print("\n\n\tFINISHED LIKING AND SHARING THE POST")


    
    # TASK - 02 - OPTIONAL
    def comment_by_comment(self):

        # To split the comments by newline so can add one by one in the comment box.

        comments = """ My aims and goals after this bootcamp would be to get start doing some freelancing.
                    I will keep on learning.
                    The automation is a real game changer.
                    The instructors and the management are really cooperative.
                    They taught us alot of things that can be done using python.
                    I learnt basics of python.
                    I learnt file handling.
                    I learnt web scraping.
                    I learnt web automation.
                    I will learn GUI and flask web apps this week.
                    And I will keep on learning with python.
                    I don't know what to say next. :D
                    I've couple of ideas that need to be automated.
                    I will try to automate them.
                    One of them would be.
                    I will try to automate my home network.
                    Really tired of adding and removing users.
                    Should be a quick way.
                    Tarun Sir you are great :)
                    Bahawal Sir you too :)
                    Thank you for teaching the great stuff for free 
                    And continue teaching
                    let us know the beauty of python what we can do with it 
                    Thank you so much :) """

        comments = [ comment.strip() for comment in comments.split('\n')]

        return comments
        
    # OPTIONAL - TO ADD COMMENTS IB SUCCESSION ON THE PAGE
    def comments_on_original_post(self):

        comments = self.comment_by_comment()

        self.hit_link_and_login()
        self.driver.implicitly_wait(10)

        for comment in comments:

            # Click on comment box to focus 
            comment_box = self.driver.find_element_by_xpath("//textarea[@class='_uwx mentions-input']")
            comment_box.click()
            comment_box.send_keys(comment)

            # Click to publish comment
            post_button = self.driver.find_element_by_xpath("//button[@class='_54k8 _52jg _56bs _26vk _3lmf _3fyi _56bv _653w']")
            self.driver.execute_script("arguments[0].click();", post_button)

            time.sleep(2)
        
        print("\n\n\tFINISHED COMMENTING ON THE POST")


        

post_url = 'https://m.facebook.com/DeveloperStudentClubDHASuffaUniversity/posts/2838706263116774'

bot = FacebookBot(post_url)

#TASK 01
bot.hit_link_and_login()
bot.like_and_share()

# TASK 02 
bot.comments_on_original_post()

