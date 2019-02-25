#coding:utf-8

def getCarTypeList():
    cartypelist=open(r'../config/cartype.txt').read().replace(' ','').split('\n')
    return cartypelist
    


if __name__=='__main__':
    #print getCarTypeList()
    cartypelist=getCarTypeList()
    for index,i in enumerate(cartypelist):
        typelist=i.split(',')
        print typelist
        print typelist[0]
        print typelist[3]
    

