
from Time import *
from links import *
sp="____________________________"
notify=[' The last date to pay the Tution Fees for 2020-21 with fine - From 31.10.2020 to 14.11.2020 payment of tuition fee with a fine of Rs 1000/-']
def notification():
   return(notify[0])
def change_notify(h):
   notify[0]=h
def check():
  y = day()
  if d()=='mon' or d()=='tue' or (c[0]=='1' and ( c[1]=='1' or c[1]=='2')) :
    kkk=0
  else :
    kkk=1
  t = gettime()
  if y=='0' or c[0]=='0':
    return('Today is a holiday !')

  elif t>='09:00:00' and t<'10:00:00' :
    return('Now :-'+y[0])
  elif t>='10:00:00' and t<'11:00:00' :
    return('Now :-\n'+y[1])
  elif t>='11:00:00' and t<'11:30:00' :
    return('Now :-\n'+y[2])
  elif t>='11:30:00' and t<'12:30:00' :
    return('Now :-\n'+y[3])
  elif t>='12:30:00' and t<'13:30:00' :
    return('Now :-\n'+y[4])
  elif t>='13:30:00' and t<'14:30:00' :
    return('Now :-\n'+y[5])
  elif t>='14:30:00' and t<'15:30:00' :
    return('Now :-\n'+y[6])
  elif t>='15:30:00' and t<'16:30:00' :
    return('Now :-\n'+y[7])
  elif t>='16:30:00' and t<'17:30:00' and kkk==0 :
    return('Now :-\n'+y[8])
  else:
    return('Now there is no class scheduled !')
def nextcl():
  y = day()
  if d()=='mon' or d()=='tue' or (c[0]=='1' and ( c[1]=='1' or c[1]=='2')) :
    kkk=0
  else :
    kkk=1
  #z = link()
  t = gettime()
  if y=='0' or c[0]=='0':
    return('Today is a holiday !')
  elif t>='00:00:00' and t<'09:00:00':
    return('Next ->'+y[0])
  elif t>='09:00:00' and t<'10:00:00' :
    return('Next ->\n'+y[1])
  elif t>='10:00:00' and t<'11:00:00' :
    return('Next ->\n'+y[2])
  elif t>='11:00:00' and t<'11:30:00' :
    return('Next ->\n'+y[3])
  elif t>='11:30:00' and t<'12:30:00' :
    return('Next ->\n'+y[4])
  elif t>='12:30:00' and t<'13:30:00' :
    return('Next ->\n'+y[5])
  elif t>='13:30:00' and t<'14:30:00' :
    return('Next ->\n'+y[6])
  elif t>='14:30:00' and t<'15:30:00' :
    return('Next ->\n'+y[7])

  elif t>='15:30:00' and t<'16:30:00' and kkk==1:
    return('No classes scheduled next !')
  elif t>='15:30:00' and t<'16:30:00' :
    return('Next ->\n'+y[8])
  else:
    return('No classes scheduled next !')

def day():
  mon = ["\n\nCompiler Design\n\n"+cd()+"\n"+sp,"\nMachine Learning\n\n"+ml()+"\n"+sp,"\nBREAK\n"+sp,"\nSoftware Engineering\n\n"+se()+"\n"+sp,"\n(Offline) Enterprise Resource Planning\n\n"+sp,"\nBREAK\n"+sp,"\nCryptography and Network Security\n\n"+cns()+"\n"+sp,"\nDigital Image Processing\n\n"+dip()+"\n"+sp,"\nCompiler Design LAB\n\n"+cdlab()+"\n\n"]
  tue = ["\n\nSoftware Engineering\n\n"+se()+"\n"+sp,"\nDigital Image Processing\n\n"+dip()+"\n"+sp,"\nBREAK\n"+sp,"\nCryptography and Network Security\n\n"+cns()+"\n"+sp,"\n(Offline) Compiler Design\n\n"+sp,"\nBREAK\n"+sp,"\nEnterprise Resource Planning\n\n"+erp()+"\n"+sp,"\nMachine Learning\n\n"+ml()+"\n"+sp,"\nSoftware Engineering LAB\n\n"+selab()+"\n\n"]
  wed = ["\n\nMachine Learning\n\n"+ml()+"\n"+sp,"\nCryptography and Network Security\n\n"+cns()+"\n"+sp,"\nBREAK\n"+sp,"\nSoftware Engineering\n\n"+se()+"\n"+sp,"\n(Offline) Digital Image Processing\n\n"+sp,"\nBREAK\n"+sp,"\nEnterprise Resource Planning\n\n"+erp()+"\n"+sp,"\nCompiler Design\n\n"+cd()+"\n\n"]
  thu = ["\n\nCryptography and Network Security\n"+cns()+"\n"+sp,"\nDigital Image Processing\n\n"+dip()+"\n"+sp,"\nBREAK\n"+sp,"\nCompiler Design\n\n"+cd()+"\n"+sp,"\n(Offline) Machine Learning\n\n"+sp,"\nBREAK\n"+sp,"\nEnterprise Resource Planning\n\n"+erp()+"\n"+sp,"\nSoftware Engineering\n\n"+se()+"\n\n"]
  fri = ["\n\nDigital Image Processing\n\n"+dip()+"\n"+sp,"\nCompiler Design\n\n"+cd()+"\n"+sp,"\nBREAK\n"+sp,"\nMachine Learning\n\n"+ml()+"\n"+sp,"\n(Offline) Cryptography and Network Security\n\n"+sp,"\nBREAK\n"+sp,"\nEnterprise Resource Planning\n\n"+erp()+"\n"+sp,"\nPlacement and training\n\n"+pt()+"\n\n"]
  sat=' '
  #if c[0]=='0':
    #sat='0':
  if c[1]=='1':
    sat=mon
  elif c[1]=='2':
    sat=tue
  elif c[1]=='3':
    sat=wed
  elif c[1]=='4':
    sat=thu
  elif c[1]=='5':
    sat=fri

  if d() == 'Mon':
    return(mon)
  elif d() == 'Tue':
    return(tue)
  elif d() == 'Wed':
    return(wed)
  elif d() == 'Thu':
    return(thu)
  elif d() == 'Fri':
    return(fri)
  elif d() == 'Sat':
    return(sat)
  elif d() == 'Sun':
    return('0')
  else :
    return('0')
def table():
  g = day()
  k = gettime()
  print(k)
  if d() == 'mon' or d()=='tue' or ( c[0]=='1' and ( c[1]=='1' or c[1]=='2')) :
    kkk=0
  else :
    kkk=1
  if g == '0' or c[0]=='0':
    return('Today is a holiday')
  elif k <= '23:59:59' and k >= '16:30:00' and kkk==1:
    return('Todays classes are over !')
  elif k <= '23:59:59' and k >= '17:30:00':
    return('Todays classes are over !')
  elif kkk==0 :
    return("09:00 - 10:00   "+g[0]+"\n\n10:00 - 11:00   "+g[1]+"\n\n11:00 - 11:30   "+g[2]+"\n\n11:30 - 12:30   "+g[3]+"\n\n12:30 - 01:30   "+g[4]+"\n\n01:30 - 02:30   "+g[5]+"\n\n02:30 - 03:30   "+g[6]+"\n\n03:30 - 04:30   "+g[7]+"\n\n04:30 - 05:30   "+g[8])
  else :
    return("09:00 - 10:00   "+g[0]+"\n\n10:00 - 11:00   "+g[1]+"\n\n11:00 - 11:30   "+g[2]+"\n\n11:30 - 12:30   "+g[3]+"\n\n12:30 - 01:30   "+g[4]+"\n\n01:30 - 02:30   "+g[5]+"\n\n02:30 - 03:30   "+g[6]+"\n\n03:30 - 04:30   "+g[7])
