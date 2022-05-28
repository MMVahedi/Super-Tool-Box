import os, time, datetime 
a=0
from easygui import multchoicebox  , ccbox, msgbox        
def file_founder(x, larges, bads, logs, olds):
    w=os.listdir(x)
    for i in range(len(w)):
        if not os.path.isdir(w[i]):
            name = x+"//"+w[i]
            size = int(os.path.getsize(name)/1024.0)+1
            mtime = os.path.getmtime(name)
            mtime = datetime.datetime.strptime(time.ctime(mtime), "%a %b %d %H:%M:%S %Y").year
            print name, size, mtime
            name = name.lower()
            if size>200:
                larges.append(name)
            if ".log" in name:
                logs.append(name)
            if mtime<2013:
                olds.append(name)
            if ".ink" in name or ".bat" in name:
                bads.append(name)
        else:
            print x+"/"+w[i]
            file_founder(x+"/"+w[i], larges, bads, logs, olds)
def mahdi(page, x, larges, bads, logs, olds):
    file_founder(x, larges, bads, logs, olds)
    if page=="large" or page=="all":
        if len(larges)==0:
            msgbox("no large files found")
        else:
            x = multchoicebox(msg="selected the larges file to delete",title="larges files",choices=(larges))
            b=ccbox(msg='realy do you want to delete this file', title=' ', choices=('yes', 'no'))
        
        if b==True:
            for f in x:
                os.remove(f)

    if page=="bad" or page=="all":
        if len(bads)==0:
            msgbox("no bad files found")
        else:
            x = multchoicebox(msg="selected the bads file to delete",title="bads files",choices=(bads))
            b=ccbox(msg='realy do you want to delete this file', title=' ', choices=('yes', 'no'))
            
            if b==True:
               for f in x:
                    os.remove(f)

    if page=="log" or page=="all":
        if len(logs)==0:
            msgbox("no log files found")
        else:
            x = multchoicebox(msg="selected the log file to delete",title="logs files",choices=(logs))
            b=ccbox(msg='realy do you want to delete this file', title=' ', choices=('yes', 'no'))
           
        if b==True:
            for f in x:
                os.remove(f)

    if page=="old" or page=="all":
        if len(olds)==0:
            msgbox("no old files found")
        else:
            x = multchoicebox(msg="selected the old file to delete",title="olds files",choices=(olds))
            b=ccbox(msg='realy do you want to delete this file', title=' ', choices=('yes', 'no'))
        
        if b==True:
            for f in x:
                os.remove(f)
            

def mahdi2(page, x, larges, bads, logs, olds):
    if page=="large" or page=="all":
         if len(larges)==0:
            msgbox("no large files found")
         else:
            x = multchoicebox(msg="selected the large file to delete",title="bads files",choices=(larges))
            b=ccbox(msg='realy do you want to delete this file', title=' ', choices=('yes', 'no'))
            
            if b==True:
               for f in x:
                    os.remove(f)

       
    if page=="bad" or page=="all":
        if len(bads)==0:
            msgbox("no bad files found")
        else:
            x = multchoicebox(msg="selected the bads file to delete",title="bads files",choices=(bads))
            b=ccbox(msg='realy do you want to delete this file', title=' ', choices=('yes', 'no'))
            
            if b==True:
               for f in x:
                    os.remove(f)

    if page=="log" or page=="all":
         if len(logs)==0:
            msgbox("no log files found")
         else:
            x = multchoicebox(msg="selected the bads file to delete",title="bads files",choices=(logs))
            b=ccbox(msg='realy do you want to delete this file', title=' ', choices=('yes', 'no'))
            
            if b==True:
               for f in x:
                    os.remove(f)

        
    if page=="old" or page=="all":
        
        if len(olds)==0:
            msgbox("no old files found")
        else:
            x = multchoicebox(msg="selected the bads file to delete",title="old files",choices=(olds))
            b=ccbox(msg='realy do you want to delete this file', title=' ', choices=('yes', 'no'))
            
            if b==True:
               for f in x:
                    os.remove(f)

            

#w=multchoicebox(msg="selected the old file to delete",title="olds files",choices=(olds))
#y=multchoicebox(msg="selected the log file to delete",title="logs files",choices=(logs))
#a=multchoicebox(msg="selected the bads file to delete",title="bads files",choices=(bads))
