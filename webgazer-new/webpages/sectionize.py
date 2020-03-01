from selenium import webdriver
import os
import pyautogui

wd = webdriver.Chrome()
wd.fullscreen_window() #Better view
pyautogui.press(['tab','tab','tab','enter']) #Close the disclamer
win_width, win_height = pyautogui.size()
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
            //console.log( $( this ).text(), $( this ).parent().attr('id'));
            console.log(document.elementFromPoint(460, 126));
        });
    });''')
