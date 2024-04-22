class Television:

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        self._status = False
        self._muted = False
        self._volume = self.MIN_VOLUME
        self._channel = self.MIN_CHANNEL
        self._stored_volume = self.MIN_VOLUME

    def power(self) -> None:
        self._status = not self._status
        if self._status and self._muted:
            self._muted = False
            self._volume = self._stored_volume

    def mute(self) -> None:
        if self._status:
            if not self._muted:
                self._stored_volume = self._volume
                self._volume = self.MIN_VOLUME
            else:
                self._volume = self._stored_volume
            self._muted = not self._muted

    def channel_up(self) -> None:
        if self._status:
            self._channel = (self._channel + 1) % (self.MAX_CHANNEL + 1)

    def channel_down(self) -> None:
        if self._status:
            self._channel = (self._channel - 1) % (self.MAX_CHANNEL + 1)

    def volume_up(self) -> None:
        if self._status:
            if self._muted:
                self._muted = False
                self._volume = self._stored_volume
            self._volume = min(self._volume + 1, self.MAX_VOLUME)

    def volume_down(self) -> None:
        if self._status:
            if self._muted:
                self._muted = False
                self._volume = self._stored_volume
            self._volume = max(self._volume - 1, self.MIN_VOLUME)


    def __str__(self) -> str:
        return (f"Power = {'on' if self._status else 'off'}, "
                f"Channel = {self._channel}, "
                f"Volume = {'Muted' if self._muted else self._volume}") #I did this as muted it's better than saying zero or I can say NON.






                                            #Almukhtar Alghafri

