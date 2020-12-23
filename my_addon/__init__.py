# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo
# import all of the Qt GUI library
from aqt.qt import *

import json 
from datetime import datetime


# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.

def testFunction():
    ids = mw.col.find_cards("added:1")
    tiddlers=[]
    for id in ids:     

        #get the question from the card
        question = mw.col.getCard(id).render_output().question_text
        
        #parse the timestamp from anki card and format to tiddlywiki form
        date = datetime.fromtimestamp((id/1000)-28800)
        date = str(date)
        dayMonthYear =date.split()[0]
        dayMonthYear = dayMonthYear.split("-")
        time = date.split()[1]
        time = time.split(".")[0]
        time = time.split(":")
        created=""
        created += dayMonthYear[0]
        created += dayMonthYear[1]
        created += dayMonthYear[2]
        created += time[0]
        created += time[1]
        created += time[2]
        created += "000"

        #format python dict
        tiddler = {
            "text": "",
            "title": question,
            "created": created,
            "tags":"review"
        }
        tiddlers.append(tiddler)

    #write to json file
    with open('/home/ristirianto/Downloads/anki.json', 'w') as outfile:
        json.dump(tiddlers, outfile)

    showInfo("ok")

# create a new menu item, "test"
action = QAction("test", mw)
# set it to call testFunction when it's clicked
action.triggered.connect(testFunction)
# and add it to the tools menu
mw.form.menuTools.addAction(action)

# testFunction()