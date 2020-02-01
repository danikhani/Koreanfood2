import time
import tkinter as tk
from enum import Enum
from Timer.Timer import Timer


TIME_FORMAT = '%M:%S'
UPDATE_TIME_MSEC = 500

BUTTON_START_NAME = "Start"
BUTTON_PAUSE_NAME = "Pause"
BUTTON_RESET_NAME = "Reset"

BUTTON_ENABLED = "normal"
BUTTON_DISABLED = "disabled"

BUTTON_WIDTH = 10
BUTTON_FONT = ("Arial", 16)

LABEL_FONT = ("Helvetica", 32)


class View:

    def __init__(self):
        self.presenter = Presenter(self)
        self.tkinter = tk.Tk()
        self.app = Application(tkinter=self.tkinter, view=self)
        self.auto_update()
        self.app.mainloop()

    def update(self, seconds, state):
        time_string = time.strftime(TIME_FORMAT, time.gmtime(seconds))
        is_running = state == State.RUNNING
        is_idle = state == State.IDLE
        self.app.update_widgets(time_string, is_running, is_idle)

    def auto_update(self):
        self.presenter.update_time()
        self.presenter.update_view()

        # schedule a call to auto_update() after some time interval
        self.app.after(UPDATE_TIME_MSEC, self.auto_update)

    # Widget interaction handlers

    def handle_start(self):
        self.presenter.handle_event(Button.START)

    def handle_reset(self):
        self.presenter.handle_event(Button.RESET)

    def handle_quit(self):
        self.tkinter.destroy()


class Application(tk.Frame):

    def __init__(self, tkinter, view):
        super().__init__(tkinter)
        self.tkinter = tkinter
        self.view = view
        self.tkinter.title("TKimer")
        self.tkinter.protocol("WM_DELETE_WINDOW", self.view.handle_quit)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.lbl_time = tk.Label(self, text="", font=LABEL_FONT)
        self.lbl_time.pack(side="bottom")

        self.btn_start = tk.Button(self)
        self.btn_start["text"] = BUTTON_START_NAME
        self.btn_start["font"] = BUTTON_FONT
        self.btn_start["width"] = BUTTON_WIDTH
        self.btn_start["command"] = self.view.handle_start
        self.btn_start.pack(side="left")

        self.btn_reset = tk.Button(self)
        self.btn_reset["text"] = BUTTON_RESET_NAME
        self.btn_reset["font"] = BUTTON_FONT
        self.btn_reset["width"] = BUTTON_WIDTH
        self.btn_reset["command"] = self.view.handle_reset
        self.btn_reset.pack(side="left")
        self.btn_reset["state"] = BUTTON_DISABLED

    def update_widgets(self, time_string, is_running, is_idle):
        start_name = BUTTON_PAUSE_NAME if is_running else BUTTON_START_NAME
        reset_state = BUTTON_DISABLED if is_idle else BUTTON_ENABLED
        self.lbl_time["text"] = time_string
        self.btn_start["text"] = start_name
        self.btn_reset["state"] = reset_state


class Presenter:
    def __init__(self, view):
        self.view = view
        # self.model = Model()
        self.timer = Timer()
        self.state = State.IDLE

        self.dispatch_table = {
            # Format: (button, current_state) : (action, new_state)
            (Button.START, State.IDLE): (self.do_run, State.RUNNING),
            (Button.START, State.RUNNING): (self.do_pause, State.PAUSED),
            (Button.START, State.PAUSED): (self.do_run, State.RUNNING),
            (Button.RESET, State.IDLE): (self.do_reset, State.IDLE),
            (Button.RESET, State.RUNNING): (self.do_reset, State.IDLE),
            (Button.RESET, State.PAUSED): (self.do_reset, State.IDLE)
        }

    def update_time(self):
        if self.state == State.RUNNING:
            self.timer.update()

    def update_view(self):
        self.view.update(self.timer.get_seconds(), self.state)

    def do_run(self):
        self.timer.start()

    def do_pause(self):
        self.update_time()

    def do_reset(self):
        self.timer.reset()

    def handle_event(self, button):
        action, new_state = self.dispatch_table[(button, self.state)]
        action()
        self.state = new_state
        self.update_view()


class Button(Enum):
    START = 1
    RESET = 2


class State(Enum):
    RUNNING = 1
    PAUSED = 2
    IDLE = 3