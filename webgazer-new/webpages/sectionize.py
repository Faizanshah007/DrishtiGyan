from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os, time
import pyautogui
import pygetwindow as gw
import pythoncom, PyHook3
import threading


unlock = (False, False)
def uMad_mouse(event):
    global unlock
    return unlock[0]

def uMad_keyboard(event):
    global unlock
    return unlock[1]

def main_PyHook3():
    hm = PyHook3.HookManager()
    hm.MouseAll = uMad_mouse
    hm.KeyAll = uMad_keyboard
    hm.HookMouse()
    pyautogui.press('esc', presses=10)  # Close any open system tray object
    hm.HookKeyboard()
    pythoncom.PumpMessages()
    
threading.Thread(target = main_PyHook3).start()

chrome_options = Options()
chrome_options.add_argument("--use-fake-ui-for-media-stream")

wd = webdriver.Chrome(options=chrome_options)

pyautogui.FAILSAFE = False

mywindow = gw.getWindowsWithTitle('data:, ')[0]
mywindow_hWnd = mywindow._hWnd

mywindow.activate()

unlock = (False, True)
pyautogui.press('tab',presses=3)
pyautogui.press('enter')
unlock = (False, False)


wd.fullscreen_window() #Better view


def run_mode():
    global wd
    with open("jquery.min.js","r") as jquery_js, open("js/webgazer.js","r") as webgazer_js:
        jquery = jquery_js.read()
        webgazer = webgazer_js.read()
        wd.execute_script(jquery)
        wd.execute_script(webgazer)
        wd.execute_script('''window.wrk_mode = (window.location.href).slice(-1);

        if(window.wrk_mode == 1)
        {$(document).ready(function () {
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
            console.log( $( this ).text(), $( this ).parent().attr('id'), Date.now(), "- cursor");
        });
        });

        function getGazedElement(x,y)
        {
            var ele = document.elementFromPoint(x, y); 
            console.log(ele.textContent, ele.parentNode.id, Date.now(), "- gaze");
        }
        
        }

        else{
                window.go_to_main_page = false;
                $("body").empty();
                $("html").append('<style>html{ background: url(ket.png) no-repeat center center fixed; -webkit-background-size: cover;-moz-background-size: cover; -o-background-size: cover;background-size: cover;} </style>');
        }
        
        
        /*webgazer.setGazeListener(function(data, elapsedTime) {
            if (data == null) {
                return;
            }
            var xprediction = data.x; //these x coordinates are relative to the viewport
            var yprediction = data.y; //these y coordinates are relative to the viewport
            //console.log(elapsedTime); //elapsed time is based on time since begin was called
        });*/
        webgazer.showPredictionPoints(1); // 1 to show
        ////////////////////////////////////////////////////////
        if(window.wrk_mode == 1)
        {webgazer.params.showVideo = false;
        webgazer.params.showFaceOverlay = false;
        webgazer.params.showFaceFeedbackBox = false;}
        //////////////////////////////////////////////////////
        webgazer.begin();

        function checkIfReady() {
                if (webgazer.isReady()) {
                    webgazer.removeMouseEventListeners();
                } else {
                    setTimeout(checkIfReady, 0);
                }
            }
        if(window.wrk_mode == 1)
        {setTimeout(checkIfReady,0);}//////////////////////////////

        flag = 0;
        $(document).keydown(function(e) {
          if (e.keyCode === 27) {
          webgazer.end();
          if(window.wrk_mode == 1)
              {clearInterval(loopCall);}////////////////////////////
          else
              {setTimeout(function(){window.go_to_main_page = true;}, 5000);}
          }

          if (e.ctrlKey) {
          flag = 1;
          }

          if(flag && e.keyCode === 67) {
          webgazer.clearData();
          if(window.wrk_mode == 1)
              {clearInterval(loopCall);}/////////////////////////////////
          flag = 0;
          }
        });

        function sortProperties(obj)
        {
        // convert object into array
        var sortable=[];
        for(var key in obj)
                if(obj.hasOwnProperty(key))
                        sortable.push([key, obj[key]]); // each item is an array in format [key, value]

        // sort items by value
        sortable.sort(function(a, b)
        {
                var x=a[1], y=b[1];
                return x<y ? -1 : x>y ? 1 : 0;
        });
        return sortable; // array in format [ [ key1, val1 ], [ key2, val2 ], ... ]
        }

        function getprediction() {
            var dict = {};
            for (i=0;i<50;++i)
            {
            var prediction = webgazer.getCurrentPrediction();
            if (prediction) {
                    webgazer.util.bound(prediction);
                    var x = prediction.x;
                    var y = prediction.y;
                    //console.log(x,y);
                    if(dict[[x,y]] == undefined)
                            dict[[x,y]] = 1;
                    else
                            dict[[x,y]] += 1;
                    }
            }

            if(Object.keys(dict).length == 0)  //RETURN now itself if no prediction
                    return;

            sortlst = sortProperties(dict);
            if((sortlst[sortlst.length - 1])[1] > 11)
            {
                    var res = (sortlst[sortlst.length - 1])[0].split(",");
                    var avg = [parseInt(res[0]),parseInt(res[1])];
                    var i = sortlst.length - 1;
                    while(i>0 && ((sortlst[i-1])[1] == (sortlst[sortlst.length - 1])[1]))
                    {
                            console.log('- Mode AVG ');
                            --i;
                            var temp = (sortlst[i])[0].split(",");
                            avg[0] += parseInt(temp[0]);
                            avg[1] += parseInt(temp[1]);
                    }
                    var deno = sortlst.length - i;
                    avg[0] = Math.round(avg[0] / deno);
                    avg[1] = Math.round(avg[1] / deno);
                    console.log(avg[0], avg[1], '- Mode');
                    getGazedElement(avg[0],avg[1]);
            }
            else {
                    var avg = [0,0];
                    var tot = 0;
                    for(var i = sortlst.length - 1; i >= 0; --i)
                    {
                            var temp = (sortlst[i])[0].split(",");
                            avg[0] += parseInt(temp[0]) * sortlst[i][1];
                            avg[1] += parseInt(temp[1]) * sortlst[i][1];
                            tot += sortlst[i][1];
                    }
                    avg[0] = Math.round(avg[0] / tot);
                    avg[1] = Math.round(avg[1] / tot);
                    console.log(avg[0], avg[1], '- AVG');
                    getGazedElement(avg[0],avg[1]);
            }
        }

        if(window.wrk_mode == 1)
        {console.log("check");
        window.loopCall = setInterval(getprediction,2000);}//////////////////////////////////////////////////////////''')


webpage = "9 Compelling Reasons Why Students Should Study Abroad[~].html"
#wd.get(os.path.join(os.getcwd(), webpage))
wd.get("http://localhost/webgazer-new/webpages/" + webpage )#+ "?1")
run_mode()
unlock = (True, True)
pyautogui.moveTo(0,0)
while(not wd.execute_script("return window.go_to_main_page")):
    pass
wd.get("http://localhost/webgazer-new/webpages/" + webpage + "?1")
run_mode()

