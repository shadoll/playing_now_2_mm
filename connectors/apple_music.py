from appscript import app  # type: ignore


class AppleMusic:
    def __init__(self):
        self.music_app = app("Music")

    def get_current_track_info(self) -> tuple:
        try:
            current_track = self.music_app.current_track.get()
            current_position = self.music_app.player_position.get()
            track_duration = current_track.duration.get()
            return (
                current_track.name.get(),
                current_track.artist.get(),
                track_duration,
                current_position,
            )
        except Exception as e:
            print(f"Failed to get current track info: {e}")
            return None, None, None, None
