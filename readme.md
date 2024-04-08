# Music Status Updater

This is a Python application that fetches the currently playing track from either Apple Music or Spotify and sets it as your status on Mattermost or GitLab.

## Features
- Fetches current playing track from `Apple Music` or `Spotify`
- Sets the track as your status on Mattermost
- Using Appscript and Osascript for Music Track Information on MacOS

## Dependencies
- MacOS
- Python 3

## Sources
- Apple Music
- Spotify
- Random - generate random status with emoji icon

## Destionations
- Mattermost
- GitLab

## Environment Variables
`SOURCE` - This variable determines which music service the application will fetch the currently playing track from. It can be set to `autodetect` to automatically detect the running music application.
`DESTINATION` - This variable determines the destination of the status update.

`MATTERMOST_SERVER_URL` - variable represents the URL of the Mattermost server.

`MATTERMOST_ACCESS_TOKEN` - the access token for the Mattermost API, which is obtained by generating a personal access token from the Mattermost user settings and is used to authenticate and authorize API requests to the Mattermost server.

`GITLAB_SERVER_URL` - the URL of the Mattermost server.
`GITLAB_ACCESS_TOKEN` - the access token for the GitLab API


## How to Run
1. Clone the repository
2. Install the dependencies with `pip install -r requirements.txt`
3. Set Mattermost token and host in `.env`
4. Set the `SOURCE` environment variable to your preferred music service
5. Set the `DESTINATION` environment variable
6. Run the application with `python main.py`

## Note
The application runs in an infinite loop, constantly checking for changes in the currently playing track and updating your Mattermost status accordingly.
