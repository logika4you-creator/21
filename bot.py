from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# 🔑 ВСТАВ НОВИЙ ТОКЕН ВІД BotFather
BOT_TOKEN = "8753266217:AAFpOOAwInTnYvDvBp35v4Md8E060fQd2S4"

# 💬 ID ГРУПИ
GROUP_ID = -5259946038


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💛 Напиши питання — воно буде анонімно передано спікерам"
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    # 🔥 АНОНІМНА ПЕРЕСИЛКА
    await context.bot.send_message(
        chat_id=GROUP_ID,
        text=f"💌 АНОНІМНЕ ПИТАННЯ:\n\n{text}"
    )

    await update.message.reply_text("💛 Дякую! Передано спікерам.")


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
    