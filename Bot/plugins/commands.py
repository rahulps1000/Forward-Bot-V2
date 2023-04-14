from Bot import CodeXBotz, filters
from pyrogram.types import Message, InlineKeyboardMarkup

from Bot.customisation import start_text, start_keyboard, help_text, help_keyboard, about_text, about_keyboard


@CodeXBotz.on_message(filters.command('start') & filters.private)
async def start(client: CodeXBotz, message: Message):
    await message.reply(
        text=start_text.format(mention=message.from_user.mention),
        quote=True,
        reply_markup=InlineKeyboardMarkup(start_keyboard)
    )


@CodeXBotz.on_message(filters.command('help') & filters.private)
async def help(client: CodeXBotz, message: Message):
    await message.reply(
        text=help_text,
        quote=True,
        reply_markup=InlineKeyboardMarkup(help_keyboard)
    )


@CodeXBotz.on_message(filters.command('about') & filters.private)
async def about(client: CodeXBotz, message: Message):
    await message.reply(
        text=about_text,
        quote=True,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(about_keyboard)
    )

@CodeXBotz.on_message(filters.private & ~filters.admin)
async def not_admin(client: CodeXBotz, message: Message):
    await message.reply(
        text="You are not an admin of this bot",
        quote=True
    )
    return


@CodeXBotz.on_callback_query(filters.regex('^about|help|close$'))
async def callback(client: CodeXBotz, query):
    data = query.data
    if data == 'help':
        await query.message.edit(
            text=help_text,
            reply_markup=InlineKeyboardMarkup(help_keyboard)
        )
        return

    elif data == "about":
        await query.message.edit(
            text=about_text,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(about_keyboard)
        )
        return

    elif data == 'close':
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
        try:
            await query.message.delete()
        except:
            pass
        return
    else:
        return
