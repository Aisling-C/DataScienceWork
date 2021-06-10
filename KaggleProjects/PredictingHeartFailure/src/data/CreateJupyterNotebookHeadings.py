def jupyternotebookheadings1(list1):
    #Make Headings
    #Pass List of Names
    k=1
    for i in list1:
        j=str(k)
        m=i.replace(" ","")
        print('* ['+j+'. '+i+'](#'+j+'.'+m+')')
        k=k+1
    k=1
    for i in list1:
        j=str(k)
        m=i.replace(" ","")
        print('## {}. {} <a class="anchor" id="{}.{}"></a>'.format(j,i,j,m))
        k=k+1

def jupyternotebookheadings2(list1,level):
    #Make Subheadings
    #Pass list of names
    #Pass level (e.g. 1, 2 or 3)
    p=str(level)
    k=1
    for i in list1:
        j=str(k)
        m=i.replace(" ","")
        print('* ['+p+'.'+j+'. '+i+'](#'+p+'.'+j+'.'+m+')')
        k=k+1
    k=1
    for i in list1:
        j=str(k)
        m=i.replace(" ","")
        print('## {}.{}. {} <a class="anchor" id="{}.{}.{}"></a>'.format(p,j,i,p,j,m))
        k=k+1