# get the coordinates of the window (macOS only)
import time
import AppKit
import screeninfo

# UX Client size
WINDOW_SIZE_UXCLIENT = [1280, 720]
WINDOW_SIZE_GAMECLIENT = [1280, 720]
SCREEN_SIZE = [screeninfo.get_monitors()[0].width,
               screeninfo.get_monitors()[0].height]
WINDOW_POS_UXCLIENT_SE = [SCREEN_SIZE[0] - WINDOW_SIZE_UXCLIENT[0],
                          SCREEN_SIZE[1] - WINDOW_SIZE_UXCLIENT[1]]
WINDOW_POS_GAMECLIENT_SE = [SCREEN_SIZE[0] - WINDOW_SIZE_GAMECLIENT[0],
                            SCREEN_SIZE[1] - WINDOW_SIZE_GAMECLIENT[1]]

if __name__ == "__main__":
    pass
