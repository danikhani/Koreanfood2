import datetime
import tkinter as tk


UNITS = {
    "seconds": 1,
    "minutes": 60,
    "hours": 3600,
    "days": 3600 * 24,
    "weeks": 3600 * 24 * 7,
    "years": 3600 * 24 * 365.2422
}


class HybridLabel(tk.Label):

    def __init__(self, parent, *args, **kwargs):
        self.text = kwargs.pop("text", "{}")
        self.textvariable = kwargs.pop("textvariable", tk.StringVar(parent))
        self.textvariable.trace_add("write", self._update_text)
        super().__init__(parent, *args, **kwargs)
        self._update_text()

    def _update_text(self, *args, **kwargs):
        self.config(text=self.text.format(self.textvariable.get()))


class Stopwatch(tk.Frame):

    def __init__(
        self, parent, prefix="", suffix="", unit="seconds",
        update_every=10, precision=2, time_elapsed=0, *args, **kwargs
    ):
        super().__init__(parent, *args, **kwargs)
        self.value = tk.DoubleVar()
        self.value.set(time_elapsed)
        self.label = HybridLabel(
            self,
            text=prefix + "{{:.{}f}}".format(precision) + suffix,
            textvariable=self.value,
        )
        self.label.pack(fill="both", expand=True)
        self.unit = unit
        self.update_every = update_every
        self.precision = precision
        self.time_elapsed = time_elapsed
        self.starting_point = None
        self.paused_point = None
        self.continue_point = None
        self.paused = False
        self.been_paused = 0

    def start(self):
        if self.paused:
            self.paused = False
            self.continue_point = datetime.datetime.now()
            self.been_paused += (self.continue_point - self.paused_point).total_seconds()
        else:
            self.starting_point = datetime.datetime.now()
        self._update()

    def pause(self):
        self.paused = True
        self.paused_point = datetime.datetime.now()

    def _update(self):
        if self.paused:
            return

        diff = ((datetime.datetime.now() - self.starting_point).total_seconds()
               - self.been_paused + self.time_elapsed)

        self.value.set(diff / UNITS[self.unit])
        self.after(self.update_every, self._update)

class Countdown(tk.Frame):

    def __init__(
        self, parent, prefix="", suffix="", unit="seconds",
        beginning=10, update_every=10, precision=2, *args, **kwargs
    ):
        super().__init__(parent, *args, **kwargs)
        self.value = tk.DoubleVar()
        self.value.set(beginning / UNITS[unit])
        self.label = HybridLabel(
            self,
            text=prefix + "{{:.{}f}}".format(precision) + suffix,
            textvariable=self.value,
        )
        self.label.pack(fill="both", expand=True)
        self.unit = unit
        self.update_every = update_every
        self.beginning = beginning
        self.precision = precision
        self.paused = False

    def start(self):
        if self.paused:
            self.paused = False
        self._update()

    def pause(self):
        self.paused = True

    def _update(self):
        if self.paused or not round(self.value.get(), self.precision):
            return

        self.beginning -= self.update_every / 1000

        self.value.set(self.beginning / UNITS[self.unit])
        self.after(self.update_every, self._update)
