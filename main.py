### MAIN SCRIPT: THEY ONE YOU NEED.
### ANA SCRIPT: Yalnızca bu scripte ihtiyacınız var.

### What you are trying to do, might be against Twitter Terms of Service. Your account may be banned very quickly. This is just a simple PoC to show power of Selenium framework.
### Yapmaya çalıştığınız işlem Twitter servis kurallarına aykırı olabilir. Hesabınız hızla banlanabilir. Bu Selenium Framework'ünün gücünü göstermek adına tasarlanmış basit bir koddur.

# Requires Python version 3.7
# Dependencies (Bağımlılıklar): Selenium + Chromedriver & Twpy
# Look for comments: you only need to modify this file to add your: (Aşağıdaki bilgileri girmeniz gerekmektedir)
# 1) Credentials (Twitter giriş bilgileri) (twitter_username & twitter_password)
# 2) Your own search terms and target links (searchtermsandlinks) (Kendi arama terimleriniz ve hedef linkleriniz)
# 3) Messages (greetings, message, dontspam_message) (Tweetlenecek mesajlar)
# 4) Path of your Selenium chromedriver (executable_path) (Chromedriver'ın bulunduğu path)

from random import randint
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.common.action_chains import ActionChains
from twpy import TwpyClient
from twpy.serializers import to_pandas, to_json, to_list
import json
from datetime import date

# DO NOT FORGET TO CHANGE SEARCH TERMS AND TARGETED LINKS.
# TR: Arama terimleri ve hedef linklerinizi değiştirmeyi unutmayın.

searchtermsandlinks = {
     "eba şifresi" : "https://www.nasilalinir.com/eba-sifresi-nasil-alinir/",
     "eba paketi" : "https://www.nasilalinir.com/eba-sifresi-nasil-alinir/",
     "ücretsiz maske" : "https://www.nasilalinir.com/devletin-dagittigi-ucretsiz-maske-nasil-alinir/",
     "e nabız şifresi" : "https://www.nasilalinir.com/e-nabiz-sifresi-nasil-alinir/",
     "instagram gece modu" : "https://www.nasilalinir.com/instagram-gece-moduna-nasil-alinir/",
     "tesla hissesi" : "https://www.nasilalinir.com/tesla-hissesi-nasil-alinir/",
     "amazon hissesi" : "https://www.nasilalinir.com/amazon-hissesi-nasil-alinir/",
     "apple hissesi" : "https://www.nasilalinir.com/apple-hissesi-nasil-alinir/",
     }

################
# DO NOT FORGET TO ADD YOUR OWN INFORMATION HERE:
# COK ONEMLI! Kendi bilgilerinizi ekleyin.

twitter_username = "YOUR_TWITTERUSERNAME"
twitter_password = "YOUR_TWITTERPASSWORD"
greetings = [' Hello,', ' Merhaba,', ' Selamlar,', ' Selam,', ' Hey,', ' Dostum,', ' Sayın hocam,',
             ' Güzel kardeşim,',
             ' Kanki,', ' Biraderim,', ' Sayın biraderim,', ' Değerli kardeşim,', ' Selamınaleyküm,']
message = [' attığın bir tweeti okudum, bu makalenin sana yardımcı olabileceğini düşünüyorum: ',
           ' bu konuyla ilgilenebileceğini düşündüm: ', ' bu makaleyi okumanı öneririm: ',
           ' bu makaleyle ilgilenebileceğini düşünüyorum: ', ' bence bu tam işine yarayacak: ',
           ' sanırım böyle bir şey arıyorsun: ', ' bunun yardımcı olabileceğini düşünüyorum: ']
dontspam_message = [' Lütfen spamlemeyin, yalnızca yardımcı olmak istedim :/ ',
                    ' Umarım işine yaramıştır, lütfen spamlemeyin :/ ',
                    ' İşine yaradıysa ne mutlu bana! ']

################

# DO NOT FORGET TO CHANGE EXECUTABLE_PATH TO WHERE CHROMEDRIVER IS INSTALLED.

driver = webdriver.Chrome(
     executable_path='YOUR_CHROMEDRIVER_PATH')

################

driver.get('https://twitter.com/login');
time.sleep(1)
search_box = driver.find_element_by_name('session[username_or_email]')
search_box.send_keys(twitter_username)
search_box = driver.find_element_by_name('session[password]')
search_box.send_keys(twitter_password)
search_box.submit()

for search_term,link in searchtermsandlinks.items():
     tc = TwpyClient()

     bugununtarihi = date.today()

     # bugununtarihi = "2020-01-01"

     arama = tc.search(query=str(search_term), since=str(bugununtarihi), limit=10)
     b = to_json(arama)
     c = (b[0]["screen_name"])
     # print(type(b))

     for c in b:
          try:
               kullanici_adlari = (c["screen_name"])
               # print(type(tivit_linkleri))
               d = json.dumps(kullanici_adlari)
               # print(d)

               etli_kullanici_adi = "@" + kullanici_adlari
               print(etli_kullanici_adi)

               ########## Bu alanda rastgele bir mesaj, rastgele selamlamalar ve rastgele bir numara atıyoruz ######

               user = etli_kullanici_adi
               selamlama = random.choice(greetings)

               mesaj = random.choice(message)

               rastgele_bilgi_izin_no = randint(500, 1000)

               dontspam = random.choice(dontspam_message)

               mesaj = user + selamlama + mesaj + link + dontspam + str(rastgele_bilgi_izin_no)
               ##########

               driver.get('https://twitter.com/compose/tweet')

               ##### Spam filtrelerine takılmaması için bekleme_suresi ekledim, 5 ile 30 saniye arasında bir aşamada bekliyor. Aceleniz varsa değiştirin ama çok hızlı yaparsanız arada CAPTCHA sormaya başlıyor sistem.
               bekleme_suresi = randint(5, 30)
               print(bekleme_suresi)
               #####

               autotw1 = WebDriverWait(driver, bekleme_suresi).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, 'DraftEditor-root')))
               time.sleep(bekleme_suresi)
               autotw1.click()

               element = WebDriverWait(driver, bekleme_suresi).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, 'public-DraftEditorPlaceholder-root')))
               ActionChains(driver).move_to_element(element).send_keys(mesaj).perform()
               time.sleep(bekleme_suresi)

               sendTw = WebDriverWait(driver, bekleme_suresi).until(
                    EC.element_to_be_clickable((By.XPATH, '//div[@role="button"]/div/span/span')))
               sendTw.click()
               time.sleep(bekleme_suresi)


          # IT WILL PASS WHEN THERE IS AN EXCEPTION!! WILL NOT THROW ANY ERROR MESSAGES.

          except:
               pass

driver.quit()