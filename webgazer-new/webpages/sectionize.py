from selenium import webdriver
import os
import pyautogui
import pygetwindow as gw
import pythoncom, pyHook
import threading


unlock = (False, False)
def uMad_mouse(event):
    global unlock
    return unlock[0]

def uMad_keyboard(event):
    global unlock
    return unlock[1]

def main_pyhook():
    hm = pyHook.HookManager()
    hm.MouseAll = uMad_mouse
    hm.KeyAll = uMad_keyboard
    hm.HookMouse()
    hm.HookKeyboard()
    pythoncom.PumpMessages()
    
threading.Thread(target = main_pyhook).start()
wd = webdriver.Chrome()

pyautogui.FAILSAFE = False

mywindow = gw.getWindowsWithTitle('data:, ')[0]
mywindow_hWnd = mywindow._hWnd

mywindow.activate()

unlock = (False, True)

pyautogui.press('tab',presses=3)
pyautogui.press('enter')

unlock = (True, True)

wd.fullscreen_window() #Better view

webpage = "9 Compelling Reasons Why Students Should Study Abroad.html"
wd.get(os.path.join(os.getcwd(), webpage))

with open("jquery.min.js","r") as jquery_js:
    jquery = jquery_js.read()
    wd.execute_script(jquery)
    wd.execute_script('''$(document).ready(function () {
        console.log(window.innerWidth, window.innerHeight);
	var Hcount = 0;
	var Pcount = 0;
	$( "h1, h2, h3, h4, h5, h6, p" ).each(function( index ) {
	if($(this).is("p"))
	{++Pcount;
	var temp_str = ("<label class = 'word'>" + $( this ).text().replace(new RegExp(" ", "g"), "</label> <label class = 'word'>") + "</label>");
	$( this ).text('');
	$(temp_str).appendTo($( this ));
	$( this ).attr('id', 'para'+Hcount+'-'+Pcount);
	$( this ).attr('class', 'paragraph');
	$( this ).attr('style', 'border:1px solid black;padding:5px;');
	}
	else{
	++Hcount;
	Pcount = 0;
	var temp_str = ("<label class = 'word'>" + $( this ).text().replace(new RegExp(" ", "g"), "</label> <label class = 'word'>") + "</label>");
	$( this ).text('');
	$(temp_str).appendTo($( this ));
	$( this ).attr('id', 'head'+Hcount);
	$( this ).attr('class', 'heading');
	$( this ).attr('style', 'border:1px solid blue;padding:5px;');}
        });

        $(".word").mouseover(function() {
            console.log( $( this ).text(), $( this ).parent().attr('id'), Date.now());
            //console.log(document.elementFromPoint(460, 126));
        });
    });''')
pyautogui.moveTo(0,0)
