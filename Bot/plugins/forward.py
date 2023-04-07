from Bot import CodeXBotz,filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from Bot.helpers import Variables, generate_settings, generate_settings_btns
from Bot.customisation import already_forwarding_text

@CodeXBotz.on_message(filters.command('forward','To intialise a forward task') & filters.private)
async def forward(bot: CodeXBotz, message: Message):
    vars = Variables(message.from_user.id)
    if vars.status == 'forwarding':
        return await message.reply(already_forwarding_text)
    await message.reply('Bot is Ready to Start Forwarding')
    await message.reply('Forward a message from the channel you want to forward <b>FROM</b>')
    msg = await bot.listen_message(chat_id=message.from_user.id, filters=filters.forwarded, timeout=60)
    try:
        await bot.get_chat_member(chat_id=msg.forward_from_chat.id, user_id="me")
    except:
        return await message.reply('You need to add the bot to the chat you want to forward <b>FROM</b>.\nSend /forward again after adding the bot to the chat.')
    vars.from_chat = msg.forward_from_chat.id
    await message.reply('Forward a message from the channel you want to forward <b>TO</b>')
    msg = await bot.listen_message(chat_id=message.from_user.id, filters=filters.forwarded, timeout=60)
    if msg.forward_from_chat.id == vars.from_chat:
        return await message.reply('You cannot forward to the same chat you are forwarding from.')
    try:
        await bot.get_chat_member(chat_id=msg.forward_from_chat.id, user_id="me")
    except:
        return await message.reply('You need to add the bot to the chat you want to forward <b>TO</b>.\nSend /forward again after adding the bot to the chat.')
    vars.to_chat = msg.forward_from_chat.id
    reply_markup = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text='Edit Settings 🛠', callback_data='edit_settings')],
            [InlineKeyboardButton(text='Start ▶', callback_data='forward_start')]
        ]
    )
    text = generate_settings(vars)
    await message.reply(text, reply_markup=reply_markup)
