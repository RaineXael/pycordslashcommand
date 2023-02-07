# XaelBot
A bot with various fun features and API fetching from various services.
# Features
* Song of the Day: On request, post a song randomly that only changes per each day. (DONE)
* Houry Animal API: Get a random animal image on request from [tinyfox.dev](https://tinyfox.dev/)'s API. (DONE)
* Reminder system: Set custom reminders to remind you after a specified time.
* Fortnite API: Get info about the game's current map, players stats and cosmetics.

# Requirements
* [Python3](https://www.python.org/downloads/)
* [A Discord Bot](https://discord.com/developers/applications/)

# Install Instructions

## Setting up a python virtual environment
To set up the virtual environment, run python with the following command:

`python3 -m venv .venv`

This makes a .venv folder, which contains the environment.

To activate it on Windows, run 
`.venv\Scripts\activate`.

On Linux, run
`source .venv/bin/activate`.

Now that the virtual environment is set up and active, install all the required python packages by running the command

`pip install -r requirements.txt`.

## Setting up the bot

You need to aquire certain keys and provide them to the bot for it to be able to work to its full capacity. You will need:
* [Your discord bot's token](https://discord.com/developers/applications/)
* [A Fortnite-API key](https://dash.fortnite-api.com/account)

Once the packages are installed, create a copy of the included <b>template.env</b> file and rename it to <b>.env</b>

Add both the Discord Bot Token and the Fortnite-API key in their respective values, enclosed in double quotes.

(insert instructions for the reminder db when committed)

## Run the bot

To run the bot, launch the app.py file with python:

`python3 app.py`.

After a short moment, a message will appear when the bot becomes online.
