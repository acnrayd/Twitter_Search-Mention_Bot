# This part of script is used for searching in Twitter for a specific keyword, filtering them by date and showing just username to retrieve our targets.
# This file is not necessary for production env.
# Bu dosya yalnızca Twitter'da bildirdiğiniz belli keywordleri ve o keywordlere yazan kullanıcıların adlarını çeken scripti içerir.


## GEREKLI PAKET: TWPY. PIP3 INSTALL TWPY.

from twpy import TwpyClient
from twpy.serializers import to_pandas, to_json, to_list
import json
from datetime import date

### ONEMLI: ARAMA TERIMINI DEGISTIR.
aramaterimi = "hurriyet"

tc = TwpyClient()
bugununtarihi = date.today()

arama = tc.search(query=str(aramaterimi), since=str(bugununtarihi), limit=10)
b = to_json(arama)
c = (b[0]["tweet_link"])
#print(type(b))

for c in b:
    tivit_linkleri = (c["tweet_link"])
    #print(type(tivit_linkleri))
    d = json.dumps(tivit_linkleri)
    print(d)


#c = (b[2]["tweet_link"]

#print(c)




#print(b)

#c = (b["tweet_link"])
#print(c)

#caner = json.dumps (aramajson[:"content"])

# aramacontent = aramajson[:0]["content"]

# print (aramacontent)
