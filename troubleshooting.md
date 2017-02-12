I've tried to organize this in order of most frequent issues.  I'm assuming you've installed python 3.x, and if not just install it now so we're all on the same page.  It's alright to have both python 2.x and 3.x installed simultaneously.

1) I double click on the bat file but it dissapears instantly!
  - This means that the first command had some error and could not execute, so the batch job ended instantly.  This is most likely a cause of both python and pip not being added to the path (make sure you check the box during installation).  To test, type cmd into your windows search bar, and open command prompt.  Type "python" without the quotes, it should bring you to a >>.  If it says it is not a recognized internal or external blah blah blah, that means it is certainly not added to your path.  Try doing the same for "pip" without quotes.  
    These are programs you're trying to run from command line, and the only way windows will know the location is if you add them to some list, which I've been calling the path.  Try reinstalling python 3 with the box ticked, or if you're brave you can try to add python and pip to your path  (try google, it's a very common problem!).  After reinstalling, make sure you close and open cmd again so your cmd instance has the latest path from windows and try typing them in again.  If that works, try to run the .bat file.
  
2) There are a ton of errors! HELP!
  - It's hard to know what kind of errors you got without reading them, but I have a hunch it may say "Access Denied" in some of them.  If it does, try running your .bat file in administrator mode.
    If they don't, please send them to me and I'll take a look and add them as a clause here.  There's not much that can go wrong, so you shouldn't have many issues actually running the script, getting there is usually the hard part.
    
Please feel free to contribute to this list by either emailing me, or if you're brave enough fork this to your own repo, edit and remerge.  I'll either approve or leave some feedback.
