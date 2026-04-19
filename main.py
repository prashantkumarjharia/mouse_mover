import pyautogui
import time
import sys
import ctypes

def prevent_sleep():
    # prevent Windows from going to sleep or locking the screen.
    ES_CONTINOUS = 0x80000000
    ES_SYSTEM_REQUIRED = 0x00000001
    ES_DISPLAY_REQUIRED = 0x00000002

    # Keep system and dispaly active
    ctypes.windll.kernel32.SetThreadExecutionState(
        ES_CONTINOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED
    )

def allow_sleep():
    # Allow windows to sleep normally again.
    ES_CONTINOUS = 0x80000000
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINOUS)

def main():
    print("Mouse Mover Utility Started.")
    print("Moving cursor 10px left and right with 5-second delay")
    print("Press Ctrl+C to stop...")
    print()

    # Prevent system from sleeping or locking
    prevent_sleep()

    # Disable fail-safe to prevent accidental stops
    pyautogui.FAILSAFE = False

    # Get screen size for safe positioning
    screen_width, screen_height = pyautogui.size()

    # Define a safe center position (middle of screen)
    center_x, center_y = screen_width // 2, screen_height // 2

    # Move cursor to center position
    pyautogui.moveTo(center_x, center_y)
    print(f"Center position: ({center_x}, {center_y})")
    print()

    try:
        while True:
            # Move 10 pixels to the left from center
            pyautogui.moveTo(center_x - 10, center_y, duration=0.1)
            print(f"Moved left to: {pyautogui.position()}")

            # Wait for 5 seconds
            time.sleep(5)

            # Move 10 pixels to the right from center
            pyautogui.moveTo(center_x + 10, center_y, duration=0.1)
            print(f"Moved right to: {pyautogui.position()}")

            # Wait for 5 seconds
            time.sleep(5)

    except KeyboardInterrupt:
        print("\n\n Ctrl+C detected. Stopping mouse movement...")
        allow_sleep()
        sys.exit(0)
    except Exception as e:
        print(f"\n\n Error occured: {e}")
        allow_sleep()
        sys.exit(1)

if __name__ == "__main__":
    main()
