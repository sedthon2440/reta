from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from AarohiX import app
import config

@app.on_message(
    command(["اوامر", "الاوامر"])
)
async def mmmezat(client, message):
    await message.reply_text(
        f"""مرحبًا بك عزيزي {message.from_user.mention} في بوت ريتا\nللحصول على الأوامر راسل البوت 🤍.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "للدخول للبوت", url=f"https://t.me/X_FT5Bot"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "- مسح .", callback_data="close"
                    ),
                ],
            ]
        ),
    )

@app.on_message(
    command(["المطور", "السورس", "المصنع"])
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo="https://telegra.ph/file/3c4a1eb0ceac848e26bc8.jpg",
        caption="• Name Bot ↦ ريتا \n ━━━━━━━━━━━━ \n • Dev ↦  بلال  \n • Bio ↦ أشعر بالفخر لأني شيعي، ولغـتي اللغـة العربيـة 🕌 -  .",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "المطور", url=f"tg://openmessage?user_id={config.OWNER_ID}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        " تحديثـات ريتا 🇵🇸🤍 .", url=config.SUPPORT_CHAT
                    ),
                ],
            ]
        ),
    )
