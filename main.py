#!/usr/bin/env python3

import Xlib
import Xlib.display
import Xlib.X

from Xlib import X

class SimpleWindow:
    def __init__(self):
        self.display = Xlib.display.Display()
        self.screen = self.display.screen()
        self.root = self.screen.root
        self.window = self.root.create_window(
            100, 100, 400, 300, 1,
            X.CopyFromParent, X.InputOutput, X.CopyFromParent,
            event_mask=X.ExposureMask
        )
        self.window.change_attributes(back_pixel=self.screen.black_pixel)
        self.window.set_wm_name("Simple Window")

    def run(self):
        self.window.map()
        while True:
            event = self.display.next_event()
            if event.type == X.Expose:
                self.handle_expose(event)

    def handle_expose(self, event):
        self.window.clear_area(event.x, event.y, event.width, event.height, 0)

if __name__ == "__main__":
    window = SimpleWindow()
    window.run()

