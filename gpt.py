from telegram.ext import Updater, CommandHandler, MessageHandler, filters
import openai

# Your OpenAI API key here
openai.api_key = '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'

def start(update, context):
    update.message.reply_text('Hello! I am your AI bot. How can I assist you?')

def respond(update, context):
    user_input = update.message.text
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=50
    )
    update.message.reply_text(response.choices[0].text.strip())

def main():
    updater = Updater('7305964065:AAHy6gqik-I41vDM6lasd4vukp6TONYexqE', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(filters.Text & ~filters.Command, respond))  # updated filter syntax
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
