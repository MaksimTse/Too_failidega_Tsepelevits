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
from gtts import gTTS

import os
def Heli(text:str, keel:str):
    obj=gTTS(text=text,lang=keel,slow=False).save('heli.mp3')
    os.system('heli.mp3')