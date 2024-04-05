from appscript import app # type: ignore

class AppleMusic:
    def __init__(self):
        self.music_app = app("Music")

    def get_current_track_info(self) -> tuple:
        try:
            current_track = self.music_app.current_track.get()
            return (
                current_track.name.get(),
                current_track.artist.get(),
                current_track.duration.get(),
            )
        except Exception as e:
            print(f"Failed to get current track info: {e}")
            return None, None, None
