from datetime import datetime

from Bot import CodeXBotz,filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from Bot.helpers import Variables, generate_settings, forward
from Bot.customisation import already_forwarding_text

@CodeXBotz.on_message(filters.command('forward','To intialise a forward task') & filters.private & filters.admin)
async def forward_cmd(bot: CodeXBotz, message: Message):
    vars = Variables(message.from_user.id)
    if vars.status == 'forwarding':
        return await message.reply(already_forwarding_text)
    await message.reply('Bot is Ready to Start Forwarding')
    await message.reply('Forward a message from the channel or send the group id from where you want to forward <b>FROM</b>')
    msg: Message = await bot.listen_message(chat_id=message.from_user.id, filters=filters.forwarded | filters.text, timeout=60)
    if msg.forward_from_chat:
        chat_id = msg.forward_from_chat.id
    else:
        try:
            chat_id = int(msg.text)
        except:
            return await message.reply('Invalid Chat ID')
    try:
        await bot.get_chat_member(chat_id=chat_id, user_id="me")
    except:
        return await message.reply('You need to add the bot to the chat you want to forward <b>FROM</b>.\nSend /forward again after adding the bot to the chat.')
    vars.from_chat = chat_id
    await message.reply('Forward a message from the channel or send the group id to where you want to forward <b>TO</b>')
    msg = await bot.listen_message(chat_id=message.from_user.id, filters=filters.forwarded | filters.text, timeout=60)
    if msg.forward_from_chat:
        chat_id = msg.forward_from_chat.id
    else:
        try:
            chat_id = int(msg.text)
        except:
            return await message.reply('Invalid Chat ID')
    if chat_id == vars.from_chat:
        return await message.reply('You cannot forward to the same chat you are forwarding from.')
    try:
        m = await bot.send_message(chat_id=chat_id, text='Checking permissions...')
        await m.delete()
    except:
        return await message.reply('You need to add the bot as ADMIN with SEND MESSAGE permission to the chat you want to forward <b>TO</b>.\nSend /forward again after adding the bot to the chat.')
    vars.to_chat = chat_id
    reply_markup = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text='Edit Settings 🛠', callback_data='edit_settings')],
            [InlineKeyboardButton(text='Start ▶', callback_data='forward_start')]
        ]
    )
    text = generate_settings(vars)
    await message.reply(text, reply_markup=reply_markup)


@CodeXBotz.on_callback_query(filters.regex('^forward_start$'))
async def forward_start(bot: CodeXBotz, update:CallbackQuery):
    vars = Variables(update.from_user.id)
    status = vars.status
    if status == 'stopped':
        print('starting.......')
        await bot.send_message(update.from_user.id,'Starting....')
        now = datetime.now()
        vars.count = 0
        vars.time = now
        vars.status = 'forwarding'
        await forward(bot, update.from_user.id)
        vars.status = 'stopped'
        print('Done')
    else:
        await update.answer('Already an instance if Forwarding.',show_alert=True)

# this command will be removed in fututre and auto continue will be added
@CodeXBotz.on_message(filters.command('continue') & filters.private  & filters.admin)
async def continue_cmd(bot: CodeXBotz, message: Message):
    vars = Variables(message.from_user.id)
    if vars.status == 'forwarding':
        await forward(bot, message.from_user.id)
    else:
        await message.reply('No task is running.')
