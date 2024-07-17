from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class ChessGame:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 60)
        self.actions=ActionChains(self.driver)
        self.ce=0
        self.pro_list=[]

    def login(self, username, password):
        self.driver.get("https://www.chess.com")
        login_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Log In"]')))
        login_button.click()
        
        username_field = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Username or Email"]')))
        username_field.send_keys(username)
        
        password_field = self.driver.find_element(By.CSS_SELECTOR, '[aria-label="Password"]')
        password_field.send_keys(password)
        
        login_button = self.driver.find_element(By.NAME, "login")
        login_button.click()

    def start_game_with_bot(self):
        self.driver.get("https://www.chess.com/play/computer/Li-Bot")
        start_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Start']")))
        start_button.click()
        
        choose_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Choose']")))
        choose_button.click()
        
        play_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ui_v5-button-component.ui_v5-button-primary.ui_v5-button-large.ui_v5-button-full")))
        play_button.click()
        
    def start_10min(self):
        self.driver.get("https://www.chess.com/play/online/new?action=createLiveChallenge&base=600&timeIncrement=0")
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,"game-tab-scrollable")))
        
        pass
    
    def start_1min(self):
        self.driver.get("https://www.chess.com/play/online/new?action=createLiveChallenge&base=60&timeIncrement=0")
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,"game-tab-scrollable")))
        print("game start")
        
        pass
        
    def my_color(self):
        cl=self.driver.find_element(By.CLASS_NAME,"clock-bottom")
        self.colors=cl.get_attribute("class")
        print(self.colors)
        if "clock-black" in self.colors:
            
            return "black"
        else:
            return "white"
    def start_move(self):
        print("starting")
        mv=self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "square-52")))
        
        mv.click()
        print("s click")
        hs=self.driver.find_element(By.CLASS_NAME,"hover-square")
        cn="hover-square square-54"
        self.driver.execute_script(f"arguments[0].className = '{cn}';", hs)
        self.actions.move_to_element_with_offset(hs,30,30).perform()


        self.actions.click().perform()
        print("e click")

    def make_move(self, move):
        sm=move[:2]
        em=move[2:]
        sm="square-"+str(ord(sm[0])-96)+sm[1]
        em="square-"+str(ord(em[0])-96)+em[1]
        s=self.driver.find_element(By.CLASS_NAME,sm)
        self.actions.move_to_element_with_offset(s,30,30).perform()
        self.actions.click().perform()
        hs=self.driver.find_element(By.CLASS_NAME,"hover-square")
        cn="hover-square "+em
        self.driver.execute_script(f"arguments[0].className = '{cn}';", hs)
        self.actions.move_to_element_with_offset(hs,30,30).perform()
        self.actions.click().perform()
    
    def black_move(self):
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,"highlight")))
        return True
    
    def not_your_move(self):
        hi=self.driver.find_elements(By.CLASS_NAME,"highlight")
        t=[]
        for i in hi:
            t.append(i.get_attribute("class"))
        ce=t[0][-2:]+t[1][-2:]
        if (self.ce==ce) or not(self.ce):
            self.ce=ce
            return True
        else:
            return False


    def get_opp_move(self):
        self.hi=self.driver.find_elements(By.CLASS_NAME,"highlight")
        h1=self.hi[0].get_attribute("class")
        h2=self.hi[1].get_attribute("class")
        self.opp_move=chr(int(h1[-2])+96)+h1[-1]+chr(int(h2[-2])+96)+h2[-1]
        self.ce=0
        return self.opp_move
        
    def promotion(self,p):
        pw=self.driver.find_element(By.CLASS_NAME,"promotion-window")
        pp=pw.find_elements(By.CLASS_NAME,"promotion-piece")
        for i in pp:
            if i.get_attribute("class")[-1]==p:
                i.click()
                break
        
    
    def close_browser(self):
        self.driver.quit()
