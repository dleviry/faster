try:

	import requests,telebot,os,ZaidPP	from telebot import types as t

	from ZaidPP import Zaid

except:

	os.system('pip install requests')

	os.system('pip install telebot')

	os.system('pip install ZaidPP')

bot = telebot.TeleBot('6133624269:AAGI2I8F12J18t2Ism3KEdFGQC_cp314gh4')

@bot.message_handler(commands=['start'])

def start(Ali):

	bt=t.InlineKeyboardButton('تواصل مع المبرمج',url='t.me/v_6px')

	mark=t.InlineKeyboardMarkup(row_width=1)

	mark.add(bt)

	name=Ali.from_user.full_name

	id = str(Ali.from_user.id)

	user = Ali.from_user.username

	op = Zaid.store_open('thaka')

	if id in op :

		pass

	else:

		ad = Zaid.store_add(f'thaka:{name} > {id} > @{user}')

	bot.send_message(Ali.chat.id,text=f'''<strong>أهلاً بك {name} في بوت الذكاء الاصطناعي 🔮

بإمكانك سؤال هذا البوت أي سؤال ويمكنك التخاطب والدردشه معه في أي وقت تريد وبأي لغة تريد 🇾🇪✨

خالص تحياتي مبرمج البوت : علي محمد حسان </strong>''',parse_mode='html',reply_markup=mark)

@bot.message_handler(func=lambda m:True)

def send(M):

	text=M.text

	answr=requests.get(f'https://gptzaid.zaidbot.repl.co/1/text={text}').text

	bot.send_message(M.chat.id,text=f'{answr}')

bot.polling(True)
