from random import *
def Loe_failist(fail:str)->list:
    """Loeme failist

    """
    f=open(fail,'r',encoding='utf-8-sig')
    jarjend=[]
    for rida in f:
        jarjend.append(rida.strip())
    f.close()
    return jarjend
def Kirjuta_failisse(fail:str,jarjend:list):
    f=open(fail,'a',encoding='utf-8-sig')
    for line in jarjend:
        f.write(line+'\n')
    f.close()

def tolk(fail1:str,fail2:str):
    rus=[] 
    est=[]
    f=open(fail1,'r',encoding='utf-8-sig')
    for line in f:
        rus.append(line.strip())
    f.close()
    f=open(fail2,'r',encoding='utf-8-sig')
    for line in f:
        est.append(line.strip()) 
    f.close()
    word=input('Kirjutage sõna, mida soovite tõlkida ')
    while word.isdigit():
        word=input('Kirjuta palun õige sõna')
    if word not in rus and word not in est:
        print('Seda sõna pole sõnastikus ')
        vale=input('Kas soovite selle sõna sõnaraamatusse lisada? (jah või ei) ').lower() 
        while vale not in ['jah','ei']:
            vale=input('Kirjuta ainult jah või ei ') 
        if vale=='jah':
            keel=input('Vene või eesti keeles sa tahad lisa sõnu? (vene keeles või eesti keeles').lower()
            while keel not in ['vene keeles','eesti keeles']:
                keel=input('Kirjutage ainult vene keeles või eesti keeles ')
            if keel=='vene keeles':
                f=open(fail1,'a',encoding='utf-8-sig') 
                f.write('\n'+word) 
                f.close()
                tolke=input('Kirjutage sõna tõlge ') 
                while tolke.isdigit():
                    tolke=input('Kirjuta õige sõna ')
                f=open(fail2,'a',encoding='utf-8-sig')
                f.write('\n'+tolke) 
                f.close()
            else: 
                f=open(fail2,'a',encoding='utf-8-sig') 
                f.write('\n'+word) 
                f.close()
                tolke=input('Kirjutage sõna tõlge ') 
                while tolke.isdigit():
                    tolke=input('Kirjuta õige sõna ')
                f=open(fail1,'a',encoding='utf-8-sig')
                f.write('\n'+tolke) 
                f.close()
        else:
            print('Olgu, hüvasti')
    for i in range(len(rus)):
        if word==rus[i]:
            print(f'{rus[i]} - {est[i]}')
        elif word==est[i]:
            print(f'{est[i]} - {rus[i]}')

def parandama(fail1:str,fail2:str):
    rus=[]
    est=[]
    f=open(fail1,'r',encoding='utf-8-sig')
    for line in f:
        rus.append(line.strip())
    f.close()
    f=open(fail2,'r',encoding='utf-8-sig')
    for line in f:
        est.append(line.strip()) 
    f.close()
    keel=input('Kas parandame vene või eesti sõnaraamatus? ').lower()
    while keel not in ['vene','eesti']:
        keel=input('Kirjuta vene või eesti ')
    if keel=='vene':
        indv=input('Millist sõna soovite parandada? ')
        while indv not in rus:
            indv=input('Kirjutage õige sõna ')
        for i in range(len(rus)):
            if indv==rus[i]:
                ind=rus.index(indv) 
        par=input('Kirjutage parandatud sõna ')
        while par.isdigit():
            par=input('Kirjutage õige sõna ')
        rus[ind]=par
        for i in range(len(rus)):
            rus[i]=rus[i]+'\n'
        f=open(fail1,'w',encoding='utf-8-sig')
        f.writelines(rus)
        f.close()
    else:
        indv=input('Mis sõnu sa tahad paranda? ')
        while indv not in est:
            indv=input('Kirjutage õige sõna ')
        for i in range(len(rus)):
            if indv==est[i]:
                ind=est.index(indv) 
        par=input('Kirjutage parandatud sõna ')
        while par.isdigit():
            par=input('Kirjutage õige sõna ')
        est[ind]=par
        for i in range(len(rus)):
            est[i]=est[i]+'\n'
        f=open(fail2,'w',encoding='utf-8-sig')
        f.writelines(est)
        f.close()

def Test(fail1:str,fail2:str):
    rus=[] 
    est=[]
    game=[] 
    a=[]
    v=k=0
    f=open(fail1,'r',encoding='utf-8-sig')
    for line in f:
        rus.append(line.strip())
    f.close()
    f=open(fail2,'r',encoding='utf-8-sig')
    for line in f:
        est.append(line.strip()) 
    f.close() 
    for i in range(len(rus)):
        num=randint(0,(len(rus)-1))
        while num in a:
            num=randint(0,(len(rus)-1))
        keel=input('Mis keeles me harjutame? ( vene või eesti) ').lower()
        while keel not in ['vene','eesti']:
            keel=input('Ainult vene või eesti ').lower() 
        n=input('Mitu? ')

        if keel=='vene':
            test=rus[num] 
            tolk=input(f'Mis on {test}? ') 
            if tolk==est[num]:
                game.append(f'{i+1} {keel} mäng - võit')
                print('Õige') 
                v+=1
            else:
                game.append(f'{i+1}, {keel} mäng - Vale') 
                print('Vale')
                k+=1
        else:
            test=est[num] 
            tolk=input(f'Mis on {test}? ') 
            if tolk==rus[num]:
                game.append(f'{i+1} {keel} mäng - Õige')
                print("Õige")
                v+=1
            else:
                game.append(f'{i+1}, {keel} mäng - Vale') 
                print('Vale')
                k+=1
        a.append(num)
    print(game)
    resV=round((v/len(rus)*100),2)
    resK=round((k/len(rus)*100),2)
    print(f'Õige protsent - {resV}%')
    print(f'Vale protsent - {resK}%')
