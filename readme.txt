# Music Status Updater

This is a Python application that fetches the currently playing track from either Apple Music or Spotify and sets it as your status on Mattermost.

## Features
- Fetches current playing track from `Apple Music` or `Spotify`
- Sets the track as your status on Mattermost
- Using Appscript and Osascript for Music Track Information on MacOS

## Dependencies
- MacOS
- Python 3
- Apple Music or Spotify
- Mattermost

## Environment Variables
`MUSIC_APP`: This variable determines which music service the application will fetch the currently playing track from. It can be either `apple_music` or `spotify`.

## How to Run
1. Clone the repository
2. Install the dependencies with `pip install -r requirements.txt`
3. Set Mattermost token and host in `.env`
4. Set the `MUSIC_APP` environment variable to your preferred music service
5. Run the application with `python music_app.py`

## Note
The application runs in an infinite loop, constantly checking for changes in the currently playing track and updating your Mattermost status accordingly.
