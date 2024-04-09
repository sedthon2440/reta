import asyncio
from pyrogram import Client, filters
from strings import get_string
from strings.filters import command
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)



REPLY_MESSAGE = "**اختار ما تريد من القائمة 🕊️ **"

REPLY_MESSAGE_BUTTONS = [
    [
        ("المطور")
    ],
    
    [
        ("اقتباس"),
        ("شعر")
    ],
    [
        ("صور")
    ],
   
    [
        ("لو خيروك"),
        ("هيدرات")
    ],
    [
        ("يوت")
    ],
    [
        ("اذكار")
    ],
    [
        ("غنيلي"),
        ("تلاوات")
    ],
    [
        ("الشيخ نقشبندي"),
        ("متحركه")
        
    ],
    [
        ("لو خيروك"),
        ("حساب العمر")
    ],    
 [
        
             ("أضف البـوت لمجموعـتك ✅")
        
    ],    
  
]

@app.on_message(filters.regex("^/start"), group=39)
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("اضـف البـوت لمجموعـتك ✅") & filters.group)
async def down(client, message):
          m = await message.reply("**- بخدمتك حجي خفيت الازرار\n- اذا تريد تطلعها مرة ثانية اكتب الاوامر**", reply_markup= ReplyKeyboardRemove(selective=True))


@app.on_message(filters.regex("يـوتيوب. 📽"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://graph.org/file/caeef4bf2ba9bf4f723cd.jpg",
        caption=f"""**يتم استخدام هذا الامر لعرض تحميل من اليوتيوب**\n**استخدم الامر بهذا الشكل** `تنزيل` ** او ** `يوتيوب` ** كمثل تنزيل سوره الرحمن اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("ᯓ سورس ميوزك سيدثون", url=f"https://t.me/veevvw"),
            ]
         ]
     )
  )

#write by BiLaL @NUNUU
