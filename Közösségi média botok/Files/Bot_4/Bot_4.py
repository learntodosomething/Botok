# -*- BOT_1 -*-
# -*- IMPORTS -*-

# Basic
import time
import random

import sys
import os

# Az aktuális fájl könyvtára
current_dir = os.path.dirname(os.path.abspath(__file__))
# A Values könyvtár elérési útja
values_dir = os.path.join(current_dir, "../Values")
# Hozzáadja a Values könyvtárat a modulútvonalhoz
sys.path.append(values_dir)
# Importálja a Basics modult
import Basics

# Window
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

#vision
from pyautogui import *
import keyboard
import cv2

from bs4 import BeautifulSoup

import numpy as np
from PIL import Image

import requests
from io import BytesIO

# -*- END IMPORTS -*-


####################################
        #Definíciók
####################################
def logout_and_exit(driver):
    # Oldal betöltése
    driver.get("https://www.instagram.com/goth.cat.girl")

    try:
        # Ellenőrizzük, hogy található-e a megfelelő profilkép div elem
        profile_div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'x1iyjqo2') and contains(@class, 'xdj266r') and contains(@class, 'xkrivgy') and contains(@class, 'x4n8cb0') and contains(@class, 'x1gryazu') and contains(@class, 'x1fawyso') and contains(@class, 'x6tf39o') and contains(@class, 'xc73u3c') and contains(@class, 'x18d9i69') and contains(@class, 'x5ib6vp') and contains(@class, 'x19sv2k2') and contains(@class, 'x164vai7') and contains(@class, 'x13ijfrp') and contains(@class, 'xhwgc15') and contains(@class, 'xkvl2z1') and contains(@class, 'x58vhm7')]"))
        )
        
        # Ellenőrizzük, hogy található-e a kilépés elem a profil div-en belül
        exit_div = profile_div.find_element(By.XPATH, ".//div[@class='x1i10hfl x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x6s0dn4 xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x1ypdohk x78zum5 xl56j7k x1y1aw1k x1sxyh0 xwib8y2 xurb0ha xcdnw81']")
        
        # Kattintás a kilépés elemre
        exit_div.click()
        
        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, '_a9--') and contains(@class, '_ap36') and contains(@class, '_a9_1') and text()='Log Out']"))
        )
        logout_button.click()
        time.sleep(3)
        print("Sikeres kilépés")

    except Exception as e:
        print("Hiba történt:", e)

    # WebDriver lezárása
    driver.quit()


def download_image(url, save_path):
    try:
        # Kép letöltése
        response = requests.get(url)
        response.raise_for_status()  # Hibaellenőrzés

        # Kép megnyitása a BytesIO segítségével
        image = Image.open(BytesIO(response.content))

        # Kép mentése
        image.save(save_path)

    except requests.exceptions.RequestException as e:
        print(f"Hiba történt a kép letöltése közben: {e}")
    except IOError as e:
        print(f"Hiba történt a kép mentése közben: {e}")

def create_database():
    # Üres adatbázis létrehozása
    data = np.array([], dtype=int)
    np.save('Bot_4/Bot_4_likedpost.npy', data)

    data = np.array([], dtype=int)
    np.save('Bot_4/Bot_4_watch_time.npy', data)
    print("Üres adatbázis létrehozva.")


def add_data(like_value):
    # Kedvelt posztok adatbázisa
    try:
        liked_post_data = np.load('Bot_4/Bot_4_likedpost.npy')
    except FileNotFoundError:
        create_database()
        liked_post_data = np.load('Bot_4/Bot_4_likedpost.npy')
    
    if like_value > 10:
        new_data = np.array([1], dtype=int)  
    else:
        new_data = np.array([0], dtype=int)

    # Egy posztra fordított idő adatbázisa
    try:
        watch_time_data = np.load('Bot_4/Bot_4_watch_time.npy')
    except FileNotFoundError:
        create_database()
        watch_time_data = np.load('Bot_4/Bot_4_watch_time.npy')
    
    new_watch_time_data = np.array([like_value], dtype=int)
 
    # Új adatok hozzáadása az adatbázishoz
    extended_liked_post_data = np.concatenate((liked_post_data, new_data))
    np.save('Bot_4/Bot_4_likedpost.npy', extended_liked_post_data)

    extended_watch_time_data = np.concatenate((watch_time_data, new_watch_time_data))
    np.save('Bot_4/Bot_4_watch_time.npy', extended_watch_time_data)
    
comments = [
    "My heart aches...",
    "Feeling so down today...",
    "Life seems unbearable...",
    "Tears keep flowing...",
    "Loneliness overwhelms me...",
    "Heartbreak is all I know...",
    "Lost in despair...",
    "Nothing seems to bring joy...",
    "The world feels gloomy...",
    "A sense of hopelessness...",
    "Sorrow clouds my thoughts...",
    "Disheartened by recent events...",
    "Weeping uncontrollably...",
    "Anxiety grips my soul...",
    "Desperate for a change...",
    "In the depths of misery...",
    "Overwhelmed with anguish...",
    "Endless pain...",
    "All hope is gone..."
]

keywords = ['sad', 'tears', 'upset', 'lonely', 'depressed', 'heartbroken', 
                'gloomy', 'miserable', 'melancholy', 'desperate', 'despair', 
                'sorrow', 'disheartened', 'anguish', 'woeful', 'weep', 'pain',
                'hopeless', 'anxiety', 'unbearable', 'heartache', 'desolation',
                'overwhelmed', 'misery', 'anguished', 'despondent', 'troubled',
                'torment', 'forlorn', 'doom']

####################################
        #Definíciók
####################################



options = webdriver.FirefoxOptions()
###########################################
#        EGYEDI AZONOSÍTÓ
options.add_argument(Basics.profile_path)
#        EGYEDI AZONOSÍTÓ
###########################################
driver = webdriver.Firefox(options=options)



# Open Instagram login page
driver.get('https://www.instagram.com/accounts/login/')

# Várunk az oldalra
wait = WebDriverWait(driver, 10)
username_field = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
password_field = wait.until(EC.presence_of_element_located((By.NAME, 'password')))

# Bejelentkezés
username_field.send_keys('goth.cat.girl')
password_field.send_keys('motivation._.is._.power')
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
button.click()

print("Nyomj S billentyűt az induláshoz")
keyboard.wait('s')
driver.get('https://www.instagram.com/reels')

element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'x1qjc9v5 x9f619 x78zum5 xg7h5cd xl56j7k x1xfsgkm xqmdsaz x1bhewko xgv127d xh8yej3')]"))
)


while True:
    # Esetleges kilépés
    keyboard.add_hotkey('q', lambda: logout_and_exit(driver))

    time.sleep(1)

    # Minimális koncentrációs képesség
    like = 6
    
    # Oldal tartalmának letöltése
    html_kod = driver.page_source

    # BeautifulSoup használata az oldal tartalmának feldolgozására
    soup = BeautifulSoup(html_kod, 'html.parser')

    # JavaScript kód az elem eltávolításához
    kod = """
    var div_elem = document.querySelector('.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1.x1dr59a3.xixxii4.x13vifvy.xeq5yr9.x1n327nk');
    if (div_elem) {
        div_elem.parentNode.removeChild(div_elem);
    }
    """
    driver.execute_script(kod)


####################################
    #Tag keresés
####################################
    # Az első olyan div elem keresése, amelynek az osztályai megfelelnek
    elso_div = soup.find('div', class_='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1emribx x1uhb9sk x1iyjqo2 xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1 x2lwn1j xeuugli x6ikm8r x10wlt62 x1d8287x xrok2fi xz4gly6')

    # Ellenőrizzük, hogy találtunk-e megfelelő div elemet az elso_div-en belül
    if elso_div:
        text_div = elso_div.find('div', attrs={'aria-disabled': 'false', 'role': 'button', 'style': 'cursor: pointer;', 'tabindex': '0'})
        if text_div:
            # Az első olyan div elem keresése, amelynek az osztályai megfelelnek a WebDriver segítségével
            inner_div = driver.find_element(By.XPATH, ".//span[contains(@class, 'xlej3yl') and contains(@class, 'x1rg5ohu') and contains(@class, 'xdl72j9') and contains(@class, 'x1c4vz4f') and contains(@class, 'x2lah0s') and contains(@class, 'xsgj6o6') and text()='more']")
            # Ellenőrizzük, hogy az inner_div tartalmazza-e a 'more' szót
            if 'more' in inner_div.text:
                # Az inner_div elemre kattintás
                inner_div.click()

                # Újra lekérjük az oldal tartalmát
                updated_html_content = driver.page_source
                updated_soup = BeautifulSoup(updated_html_content, 'html.parser')
                # Újra kinyerjük az első div elemet az updated_soup objektumból
                elso_div = updated_soup.find('div', class_='x1qjc9v5 x9f619 x78zum5 xg7h5cd xl56j7k x1xfsgkm xqmdsaz x1bhewko xgv127d xh8yej3')




            # Minden kulcsszóra végigmegyünk
            found_keywords = []
            for keyword in keywords:
                # Ellenőrizzük, hogy a kulcsszó szerepel-e a div szövegében, és ha igen, megszámoljuk az előfordulásokat
                keyword_count = elso_div.get_text().count(keyword)
                if keyword_count > 0:
                    found_keywords.append((keyword, keyword_count))  # Hozzáadjuk a megtalált kulcsszót és az előfordulások számát

                    # Növeljük a like változót az előfordulások számával
                    like += keyword_count                

            # Ha találtunk kulcsszavakat, kiírjuk az eredményt
            if found_keywords:
                print(f"Találtam {sum(keyword[1] for keyword in found_keywords)} elemet, amik a következőket tartalmazzák:")
                for keyword, count in found_keywords:
                    print(f"{count} db {keyword}")


####################################
    #Tag keresés vége
####################################



####################################
    #Képkeresés Kezdete
####################################
    
    # Kép keresése
    img_element = soup.find('img', class_='xz74otr x1bs05mj x5yr21d x10l6tqk x1d8287x x19991ni xwzpupj xuzhngd')
    # Ha találtunk <img> elemet
    if img_element:
        # Kinyerjük a src attribútum értékét
        img_src = img_element.get('src')
    else:
        print("Nem találtunk megfelelő <img> elemet az oldalon.")

    # Példa: Kép letöltése és mentése
    url = img_src
    save_path = "Bot_4/Bot_4.jpg"
    response = requests.get(url)
    with open(save_path, 'wb') as f:
        f.write(response.content)

    # Kép beolvasása
    image_path = 'Bot_4/Bot_4.jpg'
    image = cv2.imread(image_path)

    # Ellenőrizd, hogy sikeresen beolvasta-e a képet
    if image is None:
        print(f'Hiba: A {image_path} képet nem sikerült beolvasni.')
        exit()

    # Kép átalakítása szürkeárnyalatosra
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Mosoly detektálása
    smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
    smiles = smile_cascade.detectMultiScale(gray_image, scaleFactor=1.8, minNeighbors=20)

    if len(smiles) > 0:
        like -= 2

####################################
    #Képkeresés vége
####################################



####################################
    #Nézési idő
####################################

    time.sleep(like)
    print(like)
    add_data(like)
    
####################################
    #Nézési idő
####################################
    
    if like >= 10 and random.random() < (0.1 * (like / 10)):  
        liked = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "svg[aria-label='Like'].x1lliihq.x1n2onr6.xyb1xck"))
        )
        liked.click()
        print("Like-olva")


    if like >= 10 and random.random() < (0.1 * (like / 10)):   
        save = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "svg[aria-label='Save'].x1lliihq.x1n2onr6.x5n08af"))
        )
        save.click()
        print("Mentve")



    if like >= 10 and random.random() < 0.05:  
        # Megvárjuk, amíg a "Komment" gomb elérhetővé válik, majd kattintsunk rá
        comment_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "svg[aria-label='Comment'].x1lliihq.x1n2onr6.xyb1xck"))
        )
        comment_button.click()
        
        # Megvárjuk, amíg a komment mező elérhetővé válik, majd beírjuk a véletlenszerűen kiválasztott kommentet
        comment_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Add a comment…']"))
        )

        # Véletlenszerűen válasszunk egy kommentet a tömbből
        random_comment = random.choice(comments)

        # Használjuk az ActionChains osztályt a beillesztéshez
        actions = ActionChains(driver)
        actions.move_to_element(comment_input)
        actions.click()
        actions.send_keys(random_comment)
        actions.perform()

        element_to_click = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x1ypdohk x1f6kntn xwhw2v2 xl56j7k x17ydfre x2b8uid xlyipyv x87ps6o x14atkfc xcdnw81 x1i0vuye xjbqb8w xm3z3ea x1x8b98j x131883w x16mih1h x972fbf xcfux6l x1qhh985 xm0m39n xt7dq6l xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x1n5bzlp x173jzuc x1yc6y37 x3nfvp2')]"))
        )
        element_to_click.click()
        print("Írtam hozzászólást: ", random_comment)



####################################
    #Lapozás
####################################
    # JavaScript kód az elem eltávolításához
    js_kod = """
    var elsso_div = document.querySelector('.x1qjc9v5.x9f619.x78zum5.xg7h5cd.xl56j7k.x1xfsgkm.xqmdsaz.x1bhewko.xgv127d.xh8yej3');
    if (elsso_div) {
        elsso_div.parentNode.removeChild(elsso_div);
    }
    var masodik_div = document.querySelector('.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1');
    if (masodik_div) {
        masodik_div.parentNode.removeChild(masodik_div);
    }
    """
    # JavaScript kód futtatása a div elem törléséhez
    driver.execute_script(js_kod)
    print("\n Következő Post \n")
####################################
        #Lapozás vége
####################################
































