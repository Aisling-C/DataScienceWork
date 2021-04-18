def percent_there(d_f,a,b,class_):
    #d_f= Data Frame
    #a: First Columns
    #b: last column
    #Class column indicates if positive or negative case
    #Returns a dictionary with features as keys, and the following values (in order):
    #Number of Negative Cases with a feature value present
    #Number of Positive Cases with a feature value present
    #Percentange of Positive cases with feature value present over positive+negative total (with feature present)
    dict_={}
    for feature in list(d_f.loc[:,a:b].columns):
        d_f2=d_f.loc[d_f[feature]>0]
        Neg=d_f2[class_].value_counts()[0]
        Pos=d_f2[class_].value_counts()[1]
        Pct=round(Pos/(Neg+Pos)*100,2)
        dict_[feature]=[Neg,Pos,Pct]
    return dict_