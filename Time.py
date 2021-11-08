from pyrogram import Client

api_id = 1203921

api_hash = "07efbc59f267f50db081a5aff8211fca"

with Client("my_account", api_id, api_hash) as app:

    app.send_message("me", "Greetings from **Pyrogram**!")
