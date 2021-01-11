##>>> import subprocess
##>>> si = subprocess.STARTUPINFO()
##>>> si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
##>>> subprocess.call('py headless.py', startupinfo=si)
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--headless")

wd = webdriver.Chrome(options=chrome_options)


webpage = "Modified_Opinion _ The greater role of schools and teachers in shaping democracy.html"#"9 Compelling Reasons Why Students Should Study Abroad[~].html"
#wd.get(os.path.join(os.getcwd(), webpage))
wd.get("http://www.duo.com")

f = open('tempfile.txt','w')
f.write(wd.execute_script("return localStorage.getItem('__insp_lml')"))
f.close()
