from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from config import BOT_TOKEN
from database import register_user, set_board, get_user, add_log
from ai_engine import generate_answer

boards_keyboard = [["CBSE", "State Board", "ICSE"]]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    register_user(user.id, user.first_name)
    reply_markup = ReplyKeyboardMarkup(boards_keyboard, one_time_keyboard=True)
    await update.message.reply_text("Select your board:", reply_markup=reply_markup)

async def board_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    board = update.message.text
    if board in ["CBSE", "State Board", "ICSE"]:
        set_board(update.effective_user.id, board)
        await update.message.reply_text(f"{board} selected successfully!")
    else:
        await update.message.reply_text("Please select valid board.")

async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = get_user(update.effective_user.id)
    if not user or not user["board"]:
        await update.message.reply_text("Please select board first using /start")
        return
    question = " ".join(context.args)
    if not question:
        await update.message.reply_text("Usage: /ask your question")
        return
    answer = generate_answer(question, user["board"])
    await update.message.reply_text(answer)

async def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        hours = int(context.args[0])
        subject = context.args[1]
        add_log(update.effective_user.id, subject, hours)
        await update.message.reply_text("Study log added successfully!")
    except:
        await update.message.reply_text("Usage: /log hours subject")

async def progress(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = get_user(update.effective_user.id)
    if not user:
        return
    total = sum(log["hours"] for log in user["logs"])
    await update.message.reply_text(f"Total study hours: {total}")

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("ask", ask))
app.add_handler(CommandHandler("log", log))
app.add_handler(CommandHandler("progress", progress))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, board_selection))

app.run_polling()
