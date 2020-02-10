import selenium
import re

webpage = "Nearly 50 per cent MPs in new Lok Sabha have criminal records.html"
#webpage = "The plight of our education system.html"
f = open(webpage,"r+",encoding="utf8")

content = f.read()

subst1 = re.subn("<p>", '<p class="textborder" style="border:1px solid black;padding:5px;">', content)[0]

subst2 = re.subn(r'<h(\d)>', r'<h\1 class = "headingborder" style="border:1px solid blue;padding:5px;">', subst1)[0]

final = subst2

f.truncate(0)
f.seek(0)
f.write(final)
f.close()
