"""
Author: Bisnu Ray
Telegram: https://t.me/SmartBisnuBio
"""

import os
import io
import logging
import PIL.Image
import google.generativeai as genai
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode, ChatActions
from aiogram.utils import executor

# Create the bot object.
bot = Bot(token='12345678:AAGNaKh6J5jrK4og9FWkiGR1jifbZjTniik')
dp = Dispatcher(bot)

# Use os.getenv for the Google API key
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Configure the API key for Gemini
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro-vision')


@dp.message_handler(commands=['gemi'])
async def gemi_handler(message: types.Message):
    loading_message = None  # Initialize loading_message outside the try block
    try:
        # Display a loading message
        loading_message = await message.answer("<b>Generating response, please wait...</b>", parse_mode='html')

        # Check if there's a prompt or not
        if len(message.text.strip()) <= 5:  
            await message.answer("<b>Please provide a prompt after the command.</b>", parse_mode='html')
            return

        # Get the text following the /gemi command as the prompt
        prompt = message.text.split(maxsplit=1)[1:]

        # Example: Generate text from a prompt
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)

        response_text = response.text

        # Split the response if it's over 4000 characters
        if len(response_text) > 4000:
            # Split the response into parts
            parts = [response_text[i:i+4000] for i in range(0, len(response_text), 4000)]
            for part in parts:
                await message.answer(part, parse_mode='markdown')
        else:
            # Send the response as a single message
            await message.answer(response_text, parse_mode='markdown')

    except Exception as e:
        await message.answer(f"An error occurred: {str(e)}")
    finally:
        # Delete the loading message regardless of whether an error occurred or not
        if loading_message:
            await bot.delete_message(chat_id=loading_message.chat.id, message_id=loading_message.message_id)


@dp.message_handler(commands=['imgai'])
async def generate_from_image(message: types.Message):
    user_id = message.from_user.id

    if message.reply_to_message and message.reply_to_message.photo:
        image = message.reply_to_message.photo[-1]
        prompt = message.get_args() or message.reply_to_message.caption or "Describe this image."

        processing_message = await message.answer("<b>Generating response, please wait...</b>", parse_mode='html')

        try:
            # Fetch image from Telegram
            img_data = await bot.download_file_by_id(image.file_id)
            img = PIL.Image.open(io.BytesIO(img_data.getvalue()))

            # Generate content
            response = model.generate_content([prompt, img])
            response_text = response.text

            # Send the response as plain text
            await message.answer(response_text, parse_mode=None)
        except Exception as e:
            logging.error(f"Error during image analysis: {e}")
            await message.answer("<b>An error occurred. Please try again.</b>", parse_mode='html')
        finally:
            await bot.delete_message(chat_id=processing_message.chat.id, message_id=processing_message.message_id)
    else:
        await message.answer("<b>Please reply to an image with this command.</b>", parse_mode='html')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
