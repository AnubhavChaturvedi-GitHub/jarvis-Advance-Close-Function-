# Automated Dialog Box Closer

This Python script utilizes `pyautogui` to automate the process of closing dialog boxes. The script randomly selects a pre-defined closing dialogue, speaks it using text-to-speech, and then simulates the keyboard shortcut "Alt + F4" to close the active dialog box.

## Prerequisites

Ensure you have the required libraries installed before running the script:

```bash
pip install pyautogui
```

## Usage

```python
from your_script_name import close

# Example usage
close()
```

## Code Explanation

1. **Dependencies:**
   - `pyautogui`: Library for automating keyboard and mouse actions.
   - `speak`: Function for text-to-speech (assumed to be implemented in the `Body.speak` module).

2. **Functions:**
   - `close()`: Main function for closing dialog boxes.
      - Randomly selects a closing dialogue from the pre-defined options.
      - Uses text-to-speech (`speak`) to pronounce the closing dialogue.
      - Simulates the keyboard shortcut "Alt + F4" to close the active dialog box.

3. **Data:**
   - `closedlg`: List of pre-defined closing dialogues for a personalized touch.

## Note

Ensure that the script is executed in an environment where the keyboard shortcut "Alt + F4" is valid for closing dialog boxes. Additionally, provide a valid implementation for the `speak` function.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
