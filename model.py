import os
from dotenv import load_dotenv
import telegram.ext
from NST_TF import NST

load_dotenv()
TOKEN = os.getenv("TOKEN")

model = NST()
user_data = {}

async def start(update, context):
    id = update.effective_user.id
    name = update.effective_user.username
    name = name if name != None else "there"
    user_data[id] = {"Content" : None, "Style" : None}
    
    await update.message.reply_text(f"""**Hello {name}!**
                                    
To begin, please send me a **Content Image**""", parse_mode="Markdown")
    
async def image(update, context):
    id = update.effective_user.id
    img = update.message.photo[-1]

    file = await context.bot.get_file(img.file_id)
    byt = bytes(await file.download_as_bytearray())


    if id not in user_data:
        user_data[id] = {"Content" : None, "Style" : None}

    if user_data[id]["Content"] is None:
        user_data[id]["Content"] = byt
        await update.message.reply_text("Nice, Now send me a **Style Image**", parse_mode="Markdown")

    elif user_data[id]["Style"] is None:
        user_data[id]["Style"] = byt
        await update.message.reply_text("Let me Start the Process...")
        
        try:
            output = model(user_data[id]["Content"], user_data[id]["Style"])
            await update.message.reply_photo(photo=output)
            await update.message.reply_text("Done!!")
            await update.message.reply_text("Now send me a **Style Image**", parse_mode="Markdown")
        except:
            await update.message.reply_text("Error processing image")

        del user_data[id]


async def about(update):
    await update.message.reply_text(
        "<b>About Neural Style Transfer Bot</b>\n\n"
        "This bot uses <b>Neural Style Transfer</b> to blend the style of one image "
        "with the content of another, creating unique artistic visuals.\n\n"
        "Developed by Shudharshan P\n\n"
        "🔗 LinkedIn: www.linkedin.com/in/shudharshan-p-54546a315\n"
        "💻 GitHub: https://github.com/Shudharshan07/NST_API.git\n\n"
        "Feel free to connect, contribute, or report issues!",
        parse_mode="HTML"
    )


async def help(update):
    await update.message.reply_text(
        "**Neural Style Transfer Bot Help Guide**\n\n"
        "This bot lets you blend the *style* of one image with the *content* of another using AI.\n\n"
        "**How to use:**\n"
            "1. Type /start to begin.\n"
            "2. Send a **Content Image** (what you want to stylize).\n"
            "3. Then send a **Style Image** (the look you want to apply).\n"
            "4. Wait a few seconds, and get your new stylized image!\n\n"
        "**Tips:**\n"
            "- Larger images take more time and memory.\n"
            "- Try different combinations to get creative results.\n"
            "- You can restart anytime by sending a new content image.\n\n",
        parse_mode="Markdown"
    )



app = telegram.ext.Application.builder().token(TOKEN).build()
app.add_handler(telegram.ext.CommandHandler('start', start))
app.add_handler(telegram.ext.CommandHandler('about', about))
app.add_handler(telegram.ext.CommandHandler('help', help))
app.add_handler(telegram.ext.MessageHandler(telegram.ext.filters.PHOTO, image))

app.run_polling(poll_interval=3)
