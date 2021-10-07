text=open("meigen.csv", "r",encoding='utf-8')
kotoba=text.read()
list=kotoba.split("\n")
text.close()

import random
print(random.choice(list))
