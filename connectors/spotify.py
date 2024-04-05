import osascript # type: ignore

class Spotify:
    def get_current_track_info(self) -> tuple:
        try:
            name_code = 'tell application "Spotify" to name of current track as string'
            artist_code = 'tell application "Spotify" to artist of current track as string'
            duration_code = 'tell application "Spotify" to duration of current track as string'

            name = osascript.osascript(name_code)[1]
            artist = osascript.osascript(artist_code)[1]
            duration = int(osascript.osascript(duration_code)[1]) / 1000  # Convert duration from ms to s

            return name, artist, duration
        except Exception as e:
            print(f"Failed to get current track info: {e}")
            return None, None, None
