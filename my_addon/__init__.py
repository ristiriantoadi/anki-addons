# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo
# import all of the Qt GUI library
from aqt.qt import *

import json 

# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.

def testFunction():
    # get the number of cards in the current collection, which is stored in
    # the main window
    # cardCount = mw.col.cardCount()
    ids = mw.col.find_cards("added:1")
    # showInfo(typeof(cards))
    tiddlers=[]
    for id in ids:     
        # show a message box
        # showInfo("Card count: %d" % cardCount)
        # showInfo("Card question: "+str(card.question))
        question = mw.col.getCard(id).render_output().question_text
        # question = card.q()
        # showInfo(question)
        tiddler = {
            "text": "",
            "title": question,
            "created": id,
        }
        tiddlers.append(tiddler)
        # print(card.question)
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