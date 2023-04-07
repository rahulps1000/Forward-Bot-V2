from Bot import CodeXBotz, filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from Bot.helpers import Variables, generate_settings, generate_settings_btns, all_checker
import asyncio

@CodeXBotz.on_callback_query(filters.regex('^NoneBtn$'))
async def none_settings(bot: CodeXBotz, update:CallbackQuery):
    await update.answer('Click the Emoji Next to it to Edit that Settings',show_alert=True)

@CodeXBotz.on_callback_query(filters.regex('^edit_settings$'))
async def edit_forward_settings(bot: CodeXBotz, update: CallbackQuery):
    vars = Variables(update.from_user.id)
    reply_markup = generate_settings_btns(vars)
    await update.edit_message_reply_markup(reply_markup=reply_markup)

@CodeXBotz.on_callback_query(filters.regex('^save_settings$'))
async def save_settings(bot: CodeXBotz, update:CallbackQuery):
    vars = Variables(update.from_user.id)
    text = generate_settings(vars)
    reply_markup = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text='Edit Settings 🛠', callback_data='edit_settings')],
            [InlineKeyboardButton(text='Start ▶', callback_data='forward_start')]
        ]
    )
    await update.edit_message_text(text=text,reply_markup=reply_markup)

@CodeXBotz.on_callback_query(filters.regex('^toogle_settings|[A-Z][a-z]{2,4}$'))
async def toogle_settings(bot: CodeXBotz, update:CallbackQuery):
    vars = Variables(update.from_user.id)
    type = update.data.split('|')[1]
    temp = []
    edited = 0
    if type == 'First':
        msg = await bot.send_message(update.message.chat.id,'Forward a message from the channel or send the message id from where you want to start forwarding')
        temp.append(msg.id)
        msg = await bot.listen_message(chat_id=update.message.chat.id)
        temp.append(msg.id)
        try:
            from_chat = msg.forward_from_chat.id
            msg_id = msg.forward_from_message_id
        except:
            from_chat = vars.from_chat
            if str(msg.text).isdigit():
                msg_id = int(msg.text)
            else:
                await update.answer('You can only send the message id as a number',show_alert=True)
                return await bot.delete_messages(update.message.chat.id, temp)
        if from_chat == vars.from_chat:
            vars.from_msg = msg_id
            edited = 1
        else:
            await update.answer('The Forwarded message is from another chat',show_alert=True)
    elif type == 'Last':
        msg = await bot.send_message(update.message.chat.id,'Forward a message from the channel or send the message id till where you want to stop forwarding')
        temp.append(msg.id)
        msg = await bot.listen_message(chat_id=update.message.chat.id)
        temp.append(msg.id)
        try:
            from_chat = msg.forward_from_chat.id
            msg_id = msg.forward_from_message_id
        except:
            from_chat = vars.from_chat
            if str(msg.text).isdigit():
                msg_id = int(msg.text)
            else:
                await update.answer('You can only send the message id as a number',show_alert=True)
                return await bot.delete_messages(update.message.chat.id, temp)
        if from_chat == vars.from_chat:
            vars.to_msg = msg_id
            edited = 1
        else:
            await update.answer('The Forwarded message is from another chat')
            await asyncio.sleep(5)
    elif type == 'Tag':
        if vars.tag == 'copy':
            vars.tag = 'forward'
        else:
            vars.tag = 'copy'
        edited = 1
    elif type == 'All':
        if vars.all == 'true':
            return
        vars.all = True
        vars.text = True
        vars.photo = True
        vars.video = True
        vars.audio = True
        vars.document = True
        edited = 1
    elif type == 'None':
        if vars.all == 'false':
            return
        vars.all = False
        vars.text = False
        vars.photo = False
        vars.video = False
        vars.audio = False
        vars.document = False
        edited = 1
    else:
        if type == 'Photo':
            if vars.photo:
                vars.photo = False
            else:
                vars.photo = True
            edited = 1
        elif type == 'Video':
            if vars.video:
                vars.video = False
            else:
                vars.video = True
            edited = 1
        elif type == 'Audio':
            if vars.audio:
                vars.audio = False
            else:
                vars.audio = True
            edited = 1
        elif type == 'Text':
            if vars.text:
                vars.text = False
            else:
                vars.text = True
            edited = 1
        elif type == 'Docs':
            if vars.document:
                vars.document = False
            else:
                vars.document = True
            edited = 1
        all_checker(vars)
    await bot.delete_messages(update.message.chat.id,temp)
    if edited:
        text = generate_settings(vars)
        btn = generate_settings_btns(vars)
        await update.edit_message_text(text,reply_markup=btn)