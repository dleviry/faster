import telebot,random,time,datetime,requests

from telebot import types

from ZaidPP import Zaid

id = '1620749704'

#التاريخ والوقت

now = datetime.datetime.today()

mm = str(now.month)

dd = str(now.day)

yyyy = str(now.year)

hour = str(now.hour)

mi = str(now.minute)

ss = str(now.second)

day = dd + '/' + mm + '/' + yyyy

taim = hour + ':' + mi + ':' + ss

#توكن البوتات

bot = telebot.TeleBot('5933435321:AAHOMuKFnbV18xabFLzNQqiUHgWYVvD9b6o')

boty = telebot.TeleBot('5701926726:AAFFlP7Us_BywcUvm0fuCNQHY4J8OiM8WGU')

#الازرار

ali =types.InlineKeyboardMarkup(row_width=1)

moh=types.InlineKeyboardButton('📞',url='https://t.me/JLVVJL')

ali.add(moh)

keyboard1 = types.ReplyKeyboardMarkup()

a1 = types.KeyboardButton('سوبرماركت 🛒')

a2 = types.KeyboardButton('مطعم 🍽')

a3 = types.KeyboardButton('كافيه ☕️')

a4 = types.KeyboardButton('خضروات ولحوم 🥩🥬')

a5 = types.KeyboardButton('تاكسي 🚖')

a6 = types.KeyboardButton('خدمات صيانة 🛠')

a7 = types.KeyboardButton('خدمة العملاء 📞')

keyboard1.row(a1, a2,a3)

keyboard1.row(a4, a5, a6)

keyboard1.row(a7)

keyboard2 = types.ReplyKeyboardMarkup()

b1 = types.KeyboardButton('تأكيد الطلب')

b2 = types.KeyboardButton('عودة')

keyboard2.row(b1, b2)

keyboard3 = telebot.types.ReplyKeyboardMarkup(True,True)

keyboard3.row('تم')

keyboard4 = types.ReplyKeyboardMarkup()

c1 = types.KeyboardButton('مطاعم وبروست الوادي')

c2 = types.KeyboardButton('مطاعم وبروست الطويلة')

c3 = types.KeyboardButton('مطاعم الرومانسية')

c4 = types.KeyboardButton('مطعم البحار')

c5 = types.KeyboardButton('مطعم أطايب')

c6 = types.KeyboardButton('مطاعم وبروست شموخ اليمن')

c7 = types.KeyboardButton('فاير بيتزا')

c8 = types.KeyboardButton('ستار بيتزا')

c9 = types.KeyboardButton('على كيفك')

c10 = types.KeyboardButton('عودة')

keyboard4.row(c1, c2,c3)

keyboard4.row(c4, c5,c6)

keyboard4.row(c7, c8,c9)

keyboard4.row(c10)

keyboard5 = types.ReplyKeyboardMarkup()

d1 = types.KeyboardButton('لافيتا كافيه')

d2 = types.KeyboardButton('موكا كافيه')

d3 = types.KeyboardButton('وقت القهوة')

d4 = types.KeyboardButton('عشق')

d5 = types.KeyboardButton('عودة')

keyboard5.row(d1,d2)

keyboard5.row(d3,d4)

keyboard5.row(d5)

#تشغيل البوت

@bot.message_handler(commands=['start'])

def register(message):

    allusers = Zaid.store_open('faster.delevery.alimh.778437754')

    us=message.from_user.id

    us=str(us)

    if us in allusers:

    	bot.send_message(message.chat.id, 'أهلاً بك عزيزي العميل في خدمة فاستر دلفري 🔥\nاختر الخدمة التي تريدها من الأزرار الموجودة بالأسفل', reply_markup=keyboard1)    else:

    	keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)

    	reg_button = types.KeyboardButton(text="مشاركة", request_contact=True)

    	keyboard.add(reg_button)

    	response = bot.send_message(message.chat.id, "يجب عليك عزيزي العميل تفعيل اشتراكك في الخدمة ✅\nعن طريق مشاركة رقم هاتفك بالظغط على زر مشاركة", reply_markup=keyboard)

    

@bot.message_handler(content_types=['contact'])

def contact_handler(message):

  us=message.from_user.id

  us=str(us)

  allusers = Zaid.store_open('faster.delevery.alimh.778437754')

  if us in allusers:

    	gg=0

  else:

    	nam = message.from_user.username

    	num = message.contact.phone_number

    	first = message.from_user.first_name

    	last = message.from_user.last_name

    	username=first+' '+last

    	boty.send_message(id, text=f"مستخدم جديد :\nاسمه   :    {username}\nرقمه   :   +{num}\nيوزره  :   @{nam}")

    	bot.send_message(message.chat.id, 'تم تفعيل اشتراكك بنجاح ✅')

    	bot.send_message(message.chat.id, 'أهلاً بك عزيزي العميل في خدمة فاستر دلفري 🔥\nاختر الخدمة التي تريدها من الأزرار الموجودة بالأسفل', reply_markup=keyboard1)

    	ading = Zaid.store_add(f'faster.delevery.alimh.778437754:{us}')

@bot.message_handler(content_types=['text'])

def send_text(message):

    if message.text.lower() == 'سوبرماركت 🛒':

      image = "https://i.postimg.cc/vmc649Lt/Transcribe-Speechto-Text-77aecf31ea5a428583eb0c6de20c1008.jpg"

      bot.send_photo(message.chat.id,image,f"""

— — — — — — — — — — — — — — — 

أكتب قائمة بالطلبات التي تريدها 📋\nوراعِ التفاصيل كاملة < اللون - الحجم - النوع > \nواظغط على زر تأكيد الطلب\nملاحظة : أسعار التوصيل تبدأ من 800 الئ 2000 حسب الموقع والطلبات

— — — — — — — — — — — — — — —  

 """, reply_markup=keyboard2)

        

    elif message.text.lower() == 'تأكيد الطلب':

    	n1 = str(''.join((random.choice('123456789') for i in range(5))))

    	bot.send_message(message.chat.id, f'''رقم طلبك هو [{n1}]\nتاريخ الطلب [{day}]\n التوقيت [{taim}]\nفضلاً أرسل البيانات التالية :\nالأسم :\nرقم الجوال :\nالموقع وصفاً بالتفصيل :''', reply_markup=keyboard3)

    	nam = message.from_user.username

    	bot.send_message(id, text=f"رقم الطلب [{n1}]\nتاريخ الطلب [{day}]\n التوقيت [{taim}]\nيوزر [@{nam}]")

        

    elif message.text.lower() == 'مطعم 🍽':

    	bot.send_message(message.chat.id, 'اختر المطعم الذي تريد الطلب منه', reply_markup=keyboard4)

    elif message.text.lower() == 'مطاعم وبروست الوادي':

        image = "https://i.postimg.cc/vmc649Lt/Transcribe-Speechto-Text-77aecf31ea5a428583eb0c6de20c1008.jpg"

        bot.send_photo(message.chat.id,image,f"""

— — — — — — — — — — — — — — — 

هذه هي قائمة وجبات مطعم الوادي قم باختيار طلبك بعناية ثم أظغط على زر تأكيد الطلب \nملاحظة : أسعار التوصيل تبدأ من 800 الئ 2000 حسب الموقع والطلبات 

— — — — — — — — — — — — — — —  

 """, reply_markup=keyboard2)

        

    elif message.text.lower() == 'كافيه ☕️':

    	bot.send_message(message.chat.id, 'اختر الكافيه الذي تريد الطلب منه', reply_markup=keyboard5)

    	

    elif message.text.lower() == 'تم':

        bot.send_message(message.chat.id, 'تم تأكيد طلبك بنجاح', reply_markup=keyboard1)

    elif message.text.lower() == 'عودة':

        bot.send_message(message.chat.id, 'تم الرجوع للقائمة الرئيسية', reply_markup=keyboard1)

    elif message.text.lower() == 'خدمة العملاء 📞':

    	bot.send_message(message.chat.id,"اضغط على هذا الزر للتواصل مع خدمة العملاء 👇🏻",reply_markup=ali)

    	

    elif message.text.lower() == 'خضروات ولحوم 🥩🥬':

        image = "https://i.postimg.cc/vmc649Lt/Transcribe-Speechto-Text-77aecf31ea5a428583eb0c6de20c1008.jpg"

        bot.send_photo(message.chat.id,image,f"""

— — — — — — — — — — — — — — — 

أكتب قائمة بالطلبات التي تريدها 📋\nوراعِ التفاصيل كاملة < اللون - الحجم - النوع > \nواظغط على زر تأكيد الطلب\nملاحظة : أسعار التوصيل تبدأ من 800 الئ 2000 حسب الموقع والطلبات

— — — — — — — — — — — — — — —  

 """, reply_markup=keyboard2)

        

    	

    	

    else:

        nam = message.from_user.username

        first = message.from_user.first_name

        last = message.from_user.last_name

        username=first+' '+last

        bot.send_message(id, text=f"اسمه   :    {username}\nيوزره  :   @{nam}")

        bot.forward_message(id,message.chat.id,message.message_id)

        

bot.polling()
