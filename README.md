# Path of Exile - Plague Bearer (PB) Macro

This script automates the use of the Plague Bearer skill in Path of Exile. It monitors the skill's icon and the buff status, pressing the assigned key (`T` by default) at the right times.

- **Function**: Activates Plague Bearer as soon as it's full and re-activates the buff if it's not present.
- **Fail-Safe**: Move your mouse cursor to the top-left corner of the screen to stop the script instantly.

---

## \!\! Important Warnings \!\!

1.  **Admin Privileges**: This script **requires Administrator permission** to run because it uses the `keyboard` library to send key presses to the game.
2.  **Replace Images**: The images in the `images/` folder are **examples**. You **must** replace them with your own screenshots for the macro to work.
3.  **Check Coordinates**: The script is configured for a specific screen resolution and UI layout (coordinates are set in the `.py` file). If your setup is different, you **must** edit the coordinates in `pb_macro.py`.

---

## Setup Guide (First-Time Use)

Follow these 3 steps to set up the macro on a new PC.

### Step 1: Install Python 3.11

This script is not compatible with newer Python versions (like 3.13+). You must use Python 3.11 or 3.12.

1.  Go to the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2.  Download an installer for **Python 3.11** (e.g., 3.11.9).
3.  Run the installer. **IMPORTANT:** On the first screen, check the box labeled **"Add python.exe to PATH"**.
4.  Complete the installation.

### Step 2: Download and Prepare the Macro

1.  Download this repository (Code \> Download ZIP) and extract it to a simple path (e.g., `C:\PoE-Macro`).
2.  Go into the `images/` sub-folder.
3.  **Replace the 3 PNG files** with your own screenshots. Make sure the file names match **exactly**:
    - `PB_DEFAULT.PNG`: The skill icon when it's on your bar but not charging (empty).
    - `PB_FULL.PNG`: The skill icon when it is fully charged and ready to use.
    - `PB_BUFF.PNG`: The buff icon as it appears at the top-left of your screen.

### Step 3: Install the Script's Libraries

This step only needs to be done once.

1.  Click the Start Menu, type `cmd` to find "Command Prompt".
2.  Right-click it and select **"Run as administrator"**.
3.  Navigate to the macro's folder using the `cd` command:
    ```bash
    cd C:\PoE-Macro
    ```
4.  Create the virtual environment (a "box" for this project's libraries):
    ```bash
    py -3.11 -m venv .venv
    ```
5.  Activate the environment:
    ```bash
    .\.venv\Scripts\activate
    ```
6.  Install the required libraries (the `(.venv)` prompt must be visible):
    ```bash
    pip install pyautogui opencv-python keyboard
    ```
7.  You can now close the command prompt. The installation is finished.

---

## How to Run the Macro (Daily Use)

After completing the setup (Steps 1-3), you only need to do the following to run the macro:

1.  Go to the project folder (e.g., `C:\PoE-Macro`).
2.  **Double-click** the `executar_pb_macro.bat` file.
3.  A User Account Control (UAC) window will pop up. Click **"Yes"** to grant administrator permissions.

The script will start in the terminal. You can press **Ctrl+C** in the terminal window to stop it, or use the **Fail-Safe** (move mouse to top-left corner).
