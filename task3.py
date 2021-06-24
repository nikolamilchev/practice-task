def dictonary(string):
    dictr = {}
    for i in range(len(string)):
        dictr.update({i+1:string[i]})
    return dictr

if __name__=="__main__":
    dictonary('test')