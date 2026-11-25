# Image Transmutator

Turn any image into ASCII art right in your terminal, in plain text or in full color.

```
    ____
   /  _/___ ___  ____ _____ ____
   / // __ `__ \/ __ `/ __ `/ _ \
 _/ // / / / / / /_/ / /_/ /  __/
/___/_/ /_/ /_/\__,_/\__, /\___/
                    /____/
  ______                                      __        __
 /_  __/________ _____  _________ ___  __  __/ /_____ _/ /_____  _____
  / / / ___/ __ `/ __ \/ ___/ __ `__ \/ / / / __/ __ `/ __/ __ \/ ___/
 / / / /  / /_/ / / / (__  ) / / / / / /_/ / /_/ /_/ / /_/ /_/ / /
/_/ /_/   \__,_/_/ /_/____/_/ /_/ /_/\__,_/\__/\__,_/\__/\____/_/
```

<!-- Add a screenshot of the color output here, e.g. ![Color example](docs/example.png) -->

## Features

- **Two character sets**
  - *Detailed*: 70 characters, more shades of gray and finer detail
  - *Simple*: 10 characters, cleaner and higher contrast
- **Color mode**: each character is painted with the average color of the part of the image it represents (24-bit "truecolor" ANSI codes)
- **Export to `.txt`**: saves both a plain version and a color version
- **Correct proportions**: compensates for terminal characters being taller than they are wide, so images don't come out stretched

## Requirements

- Python 3.10 or newer
- [Pillow](https://pypi.org/project/pillow/) and [NumPy](https://pypi.org/project/numpy/) (installed in the steps below)
- For color mode: a terminal with truecolor support (Windows Terminal, the VS Code terminal, and most modern macOS/Linux terminals)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate it**
   - Windows (PowerShell):
     ```powershell
     .venv\Scripts\Activate.ps1
     ```
     If PowerShell says running scripts is disabled, run this once and try again:
     ```powershell
     Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
     ```
   - macOS / Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install the dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Using your own image

1. **Copy your image into the project folder**, next to `main.py`. Any format Pillow can open works (`.jpg`, `.png`, `.bmp`, `.gif`, …).

2. **Open `main.py` and change the `fileName` variable** to your image's name:
   ```python
   fileName = "my_image.jpg"
   ```
   Write the name **exactly** as it is, including the extension.

   > **Windows tip:** File Explorer hides file extensions by default, so a file you see as `photo` might really be `photo.jpg`, or even `photo.jpg.jpg` if you renamed it. Run `dir` in the terminal to see the real name.

   You can also use a full path to an image somewhere else. Put an `r` in front of the string so the backslashes work:
   ```python
   fileName = r"C:\Users\you\Pictures\photo.png"
   ```

3. **Run the program**
   ```bash
   python main.py
   ```

## How to use it

When it starts, choose a character set:

```
Choose character set:
1) Detailed (70 chars)
2) Simple (10 chars)
```

Then use the menu:

| Option | What it does |
|---|---|
| `1) ASCII` | Prints the ASCII art in the terminal |
| `2) SEND TO .TXT` | Saves `output.txt` (plain) and `output_color.txt` (color) |
| `3) COLOR` | Prints the ASCII art in color |
| `4) EXIT` | Closes the program |

**Tip:** make your terminal wide enough. If the lines wrap, the image will look broken.

### About `output_color.txt`

The color file stores the ANSI color codes along with the characters. That means:

- In **Notepad** or another text editor, you'll see the raw codes, like `[38;2;54;51;38m@`.
- In the **terminal**, it shows up in color:
  - Windows: `type output_color.txt`
  - macOS / Linux: `cat output_color.txt`

## Tweaking the output

`image_to_ascii` in `converter.py` takes a few optional settings:

| Argument | Default | What it changes |
|---|---|---|
| `cols` | `80` | Width of the result in characters. More columns means more detail, but you need a wider terminal. |
| `scale` | `0.5` | Width-to-height ratio of a character in your terminal font. If circles look squashed or stretched, try values between `0.4` and `0.55`. |
| `moreLevels` | `False` | `True` uses the detailed 70-character set. |
| `color` | `False` | `True` adds color codes to each character. |

Example:
```python
converter.image_to_ascii(fileName, cols=120, moreLevels=True, color=True)
```

## How it works

1. The image is opened and converted to **grayscale** with Pillow. An **RGB** copy is kept for color mode.
2. The image is split into a grid of blocks: `cols` blocks across, with each block's height adjusted by `scale` so characters keep the right proportions.
3. For each block, the program computes the **average brightness** and maps it to a character, from dense ones like `@` to light ones like `.` and spaces.
4. In color mode, it also computes the block's **average RGB color** with NumPy and puts an ANSI truecolor code in front of the character.

## Project structure

```
.
├── main.py           # Menu and user interaction
├── converter.py      # Image-to-ASCII conversion logic
├── requirements.txt  # Python dependencies
└── README.md
```

## Roadmap

- [ ] Pick the image with a file dialog (tkinter) instead of editing the code
- [ ] Inverted mode for dark-background terminals
- [ ] A shared `save_to_txt` function to avoid repeating code
- [ ] Choose `cols` from the menu
