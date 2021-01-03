import json
import requests
from links import *
from check import *
def subquery(ch_id,m_id):
  key=json.dumps({'inline_keyboard':[[{'text':'Compiler Design','callback_data':'cd'},{'text':'Software Engineering','callback_data':'se'}],[{'text':'Cryptography and Network Security','callback_data':'cns'},{'text':'Digital Image Processing','callback_data':'dip'}],[{'text':'Machine Learning','callback_data':'ml'},{'text':'Enterprise Resource Planning','callback_data':'erp'}],[{'text':'Go back','callback_data':'0'}]]})
  params={'chat_id':ch_id,'message_id':m_id,'text':'-- /cd - Compiler Design\n-- /se - Software Engineering\n-- /cns - Cryptography and Network Security\n-- /dip - Digital Image Processing\n-- /ml - Machine Learning\n-- /erp - Enterprise Resource Planning\n\n (OR) Click the buttons below','reply_markup':key,'parse_mode':'HTML'}
  return params
def notifying(ch_id,m_id):
  key=json.dumps({'inline_keyboard':[[{'text':'Fees payment','url':'www.google.com'}],[{'text':'Go back','callback_data':'0'}]]})
  params={'chat_id':ch_id,'message_id':m_id,'message_id':m_id,'text':'<b>NOTIFICATION\n\n</b>'+notification(),'reply_markup':key,'parse_mode':'HTML'}
  return params
def subject(ch_id,m_id,data):
  key=json.dumps({'inline_keyboard':[[{'text':'Go back','callback_data':'4'}]]})
  text=' '
  #key = None
  if data == 'cd':
    
    text='<b><u>Compiler Design\n\n</u></b>'+cd()
    if 'todays classes are over' in cd().lower() or 'holiday' in cd().lower() or 'link not updated' in cd().lower() or 'offline class' in cd().lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Go back','callback_data':'4'}]]})
    else:
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':cd()}],[{'text':'Go back','callback_data':'4'}]]})
      
  elif data == 'se':
     text='<b><u>Software Engineering\n\n</u></b>'+se()
     if 'todays classes are over' in se().lower() or 'holiday' in se().lower() or 'link not updated' in se().lower() or 'offline class' in se().lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Go back','callback_data':'4'}]]})
     else:
       
       key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':se()}],[{'text':'Go back','callback_data':'4'}]]})
  elif data == 'cns':
    text='<b><u>Cryptography and Network Security\n\n</u></b>'+cns()
    if 'todays classes are over' in cns().lower() or 'holiday' in cns().lower() or 'link not updated' in cns().lower() or 'offline class' in cns().lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Go back','callback_data':'4'}]]})
    else:
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':cns()}],[{'text':'Go back','callback_data':'4'}]]})
  elif data == 'dip':
    text='<b><u>Digital Image Processing\n\n</u></b>'+dip()
    if 'todays classes are over' in dip().lower() or 'holiday' in dip().lower() or 'link not updated' in dip().lower() or 'offline class' in dip().lower() or 'today no class' in dip().lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Go back','callback_data':'4'}]]})
    else:
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':dip()}],[{'text':'Go back','callback_data':'4'}]]})
  elif data == 'ml':
    text='<b><u>Machine Learning\n\n</u></b>'+ml()
    if 'todays classes are over' in ml().lower() or 'holiday' in ml().lower() or 'link not updated' in ml().lower() or 'offline class' in ml().lower() or 'today no class' in ml().lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Go back','callback_data':'4'}]]})
    else:
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':ml()}],[{'text':'Go back','callback_data':'4'}]]})
  elif data == 'erp':
    text='<b><u>Enterprise Resource Planning\n\n</u></b>'+erp()
    if 'todays classes are over' in erp().lower() or 'holiday' in erp().lower() or 'link not updated' in erp().lower() or 'offline class' in erp().lower() or 'today no class' in erp().lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Go back','callback_data':'4'}]]})
    else:
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':erp()}],[{'text':'Go back','callback_data':'4'}]]})
      """
  elif data == 'it':
    text='<b><u>Industrial training\n\n</u></b>'+it()
    if 'todays classes are over' in it().lower() or 'holiday' in it().lower() or 'link not updated' in it().lower() or 'offline class' in it().lower() or 'today no class' in it().lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Go back','callback_data':'6'}]]})
    else:
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':it()}],[{'text':'Go back','callback_data':'6'}]]})
      """
  elif data == 'pt':
    text='<b><u>Placement and training\n\n</u></b>'+pt()
    if 'todays classes are over' in pt().lower() or 'holiday' in pt().lower() or 'link not updated' in pt().lower() or 'offline class' in pt().lower() or 'today no class' in pt().lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Go back','callback_data':'6'}]]})
    else:
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':pt()}],[{'text':'Go back','callback_data':'6'}]]})
  params={'chat_id':ch_id,'message_id':m_id,'text':text,'reply_markup':key,'parse_mode':'HTML'}
  return params
def labsub(ch_id,m_id,data):
  #text=' '
  #key = None
  if data == 'cdl':
     text='<b><u>Computer Design LAB\n\n</u></b>'+cdlab()
     if 'todays classes are over' in cdlab().lower() or 'holiday' in cdlab().lower() or 'link not updated' in cdlab().lower() or 'offline class' in cdlab().lower() or 'today no class' in cdlab().lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Go back','callback_data':'5'}]]})
     else:
       
       key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':cdlab()}],[{'text':'Go back','callback_data':'5'}]]})
  elif data == 'sel':
     text='<b><u>Software Engineering LAB\n\n</u></b>'+selab()
     if 'todays classes are over' in selab().lower() or 'holiday' in selab().lower() or 'link not updated' in selab().lower() or 'offline class' in selab().lower() or 'today no class' in selab().lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Go back','callback_data':'5'}]]})
     else:
       key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':selab()}],[{'text':'Go back','callback_data':'5'}]]})
       """
  elif data == 'mpl':
    text='<b><u>Microprocessor LAB\n\n</u></b>'+mplab()
    if 'todays classes are over' in mplab().lower() or 'holiday' in mplab().lower() or 'link not updated' in mplab().lower() or 'offline class' in mplab().lower() or 'today no class' in mplab().lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Go back','callback_data':'5'}]]})
    else:
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':mplab()}],[{'text':'Go back','callback_data':'5'}]]})
      """
  params={'chat_id':ch_id,'message_id':m_id,'text':text,'reply_markup':key,'parse_mode':'HTML'}
  return params
def labquery(ch_id,m_id):
  key=json.dumps({'inline_keyboard':[[{'text':'Compiler Design LAB','callback_data':'cdl'}],[{'text': 'Software Engineering LAB','callback_data':'sel'}],[{'text':'Go back','callback_data':'0'}]]})
  params={'chat_id':ch_id,'message_id':m_id,'text':'LAB CLASSES \n\n-- /cdl - Compiler Design LAB\n-- /sel - Software Engineering LAB\n\n(OR) Click the buttons below','reply_markup':key,'parse_mode':'HTML'}
  return params
  
def nextnow(ch_id,m_id,data):
  key=json.dumps({'inline_keyboard':[[{'text':'Go back','callback_data':'0'}]]})
  if data=='2':
    text=check()
    if 'no class scheduled' in text.lower() or 'holiday' in text.lower() or 'link not updated' in text.lower() or 'break' in text.lower() or 'offline' in text.lower() :
      key=json.dumps({'inline_keyboard':[[{'text':'Go back','callback_data':'0'}]]})
    elif 'compiler design lab' in text.lower() :
       key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':cdlab()}],[{'text':'Go back','callback_data':'0'}]]})
    elif 'software engineering lab' in text.lower() :
       key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':selab()}],[{'text':'Go back','callback_data':'0'}]]})
       """
    elif 'microprocessor lab' in text.lower() :
       key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':mplab()}],[{'text':'Go back','callback_data':'0'}]]})
   """
    elif 'compiler design' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':cd()}],[{'text':'Go back','callback_data':'0'}]]})
    elif 'software engineering' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':se()}],[{'text':'Go back','callback_data':'0'}]]})
    elif 'Cryptography and network security' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':cns()}],[{'text':'Go back','callback_data':'0'}]]})
    elif 'digital image processing' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':dip()}],[{'text':'Go back','callback_data':'0'}]]})
    elif 'machine learning' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':ml()}],[{'text':'Go back','callback_data':'0'}]]})
    elif 'enterprise resource planning' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':erp()}],[{'text':'Go back','callback_data':'0'}]]})
    elif 'compiler design lab' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':cdl()}],[{'text':'Go back','callback_data':'0'}]]})
    elif 'software engineering lab' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':sel()}],[{'text':'Go back','callback_data':'0'}]]})
      """"
    elif 'microprocessor' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':mp()}],[{'text':'Go back','callback_data':'0'}]]})
    elif 'industrial training' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':it()}],[{'text':'Go back','callback_data':'0'}]]})
      """
    elif 'placement and training' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':pt()}],[{'text':'Go back','callback_data':'0'}]]})
  elif data=='3':
    text=nextcl()
    if 'no classes scheduled' in text.lower() or 'holiday' in text.lower() or 'link not updated' in text.lower() or 'break' in text.lower() or 'offline' in text.lower() :
      key=json.dumps({'inline_keyboard':[[{'text':'Go back','callback_data':'0'}]]})
    elif 'compiler design' in text.lower() :
       key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':cd()}],[{'text':'Go back','callback_data':'0'}]]})
    elif 'software engineering' in text.lower() :
       key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':se()}],[{'text':'Go back','callback_data':'0'}]]})
    elif 'cryptography and network security' in text.lower() :
       key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':cns()}],[{'text':'Go back','callback_data':'0'}]]})
   
    elif 'digital image processing' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':dip()}],[{'text':'Go back','callback_data':'0'}]]})
    elif 'machine learning' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':ml()}],[{'text':'Go back','callback_data':'0'}]]})
    elif 'enterprise resource planning' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':erp()}],[{'text':'Go back','callback_data':'0'}]]})
    elif 'compiler design lab' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':cdlab()}],[{'text':'Go back','callback_data':'0'}]]})
    elif 'software engineering lab' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':selab()}],[{'text':'Go back','callback_data':'0'}]]})
      """
    elif 'microprocessor lab' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':mplab()}],[{'text':'Go back','callback_data':'0'}]]})
    elif 'computer graphics' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':cg()}],[{'text':'Go back','callback_data':'0'}]]})
    elif 'computer networks' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':cn()}],[{'text':'Go back','callback_data':'0'}]]})
    elif 'microprocessor' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':mp()}],[{'text':'Go back','callback_data':'0'}]]})
    elif 'industrial training' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':it()}],[{'text':'Go back','callback_data':'0'}]]})
      """
    elif 'placement and training' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':pt()}],[{'text':'Go back','callback_data':'0'}]]})
  params={'chat_id':ch_id,'message_id':m_id,'text':text,'reply_markup':key,'parse_mode':'HTML'}
  return params
def noti(ch_id,m_id):
  key=json.dumps({'inline_keyboard':[[{'text': 'Notification','callback_data':'1'}],[{'text': 'Current class','callback_data': '2'},{'text': 'Next class','callback_data':'3'}],[{'text': 'Theory classes','callback_data': '4'}],[{'text': 'Lab classes','callback_data':'5'}],[{'text': 'Seminar classes','callback_data': '6'}],[{'text': 'Source code','url':'https://github.com/Renolin7/telegram-bot'}]]})
 
  tex='Hey! My name is Syntax_error. I am an online class link management bot, here to help you get the class links and time table! PM me on @niloner_bot\n\nFor further queries use the buttons below.\n\n\nThis bot was created by @Renolin'
  params={'chat_id':ch_id,'message_id':m_id,'text':tex,'reply_markup':key,'parse_mode':'HTML'}
  return params
def seminar(ch_id,m_id):
  key=json.dumps({'inline_keyboard':[[{'text':'Placement and training','callback_data':'pt'}],[{'text':'Go back','callback_data':'0'}]]})
  params={'chat_id':ch_id,'message_id':m_id,'text':'\n\n-- /pt - Placement and training\n\n(OR) Click the buttons below.','reply_markup':key,'parse_mode':'HTML'}
  return params
