# Python Projects Collection

A collection of Python learning projects exploring GUI development, web automation, game logic, encryption, and various Python libraries. These projects represent hands-on exploration of Python's ecosystem during my learning phase.

## Projects

### 🎮 Games & Simulations

**Snake Game** (`turtle_project/snake_game/`)
- Classic snake game built with Turtle graphics
- Collision detection, scoring system, and food generation
- Keyboard controls (arrow keys and WASD)

**Pong Game** (`turtle_project/ping_pong/`)
- Two-player Pong implementation
- Customizable match points, real-time scoring
- Progressive ball speed increase

**Turtle Crossing** (`turtle_project/turtle_crossing/`)
- Frogger-style game with increasing difficulty
- Dynamic car generation and collision detection
- Level progression system

**Turtle Race** (`turtle_project/turtle_race.py`)
- Interactive betting game with 6 racing turtles
- Random movement mechanics

**Hangman** (`hangman/`)
- Word-guessing game with ASCII art
- 6-life system with visual feedback

**PIG Dice Game** (`PIG_game.py`)
- 2-4 player dice game to reach 50 points
- Risk-reward mechanics (roll vs. bank points)

### 🖥️ GUI Applications

**Text Editor** (`textEditor.py`)
- Full-featured text editor with Tkinter
- Features: Bold/italic formatting, color customization, undo/redo
- File operations (open, save, save as)
- Syntax highlighting support

**Pomodoro Timer** (`pomodoro_app/main.py`)
- Productivity timer following Pomodoro Technique
- Work/break cycle automation (25 min work, 5 min short break, 15 min long break)
- Visual progress tracking with checkmarks

**Typing Speed Test** (`type_speed_test.py`)
- Terminal-based WPM (words per minute) calculator
- Real-time visual feedback using curses library
- Color-coded accuracy display

### 🔐 Utilities

**Password Manager** (`password_protect.py`)
- Encrypted password storage using Fernet (cryptography library)
- Add/view functionality with master key protection
- File-based persistence

**File Converter** (`file_converter.py`)
- Format conversion tool using ConvertAPI
- Supports multiple file formats
- Custom path specification

### 🎨 Creative Projects

**Hirst Painting Generator** (`turtle_project/hirst_paint/hirst_painting.py`)
- Generates dot paintings inspired by Damien Hirst
- Uses colorgram for color extraction
- 10x10 grid with random color selection

### 📚 Educational

**US State Guessing Game** (`US_state_guess/main.py`)
- Interactive geography quiz with Pandas and Turtle
- Click-to-place state names on map
- Tracks missing states and generates CSV

**MadLibs Generator** (`MadLibs_gen.py`)
- Interactive story generator
- Custom word replacement using file I/O


## Tech Stack

**Languages & Frameworks**
- Python 3.x
- Tkinter (GUI)
- Turtle Graphics

**Libraries**
- `selenium` - Web automation
- `beautifulsoup4` - Web scraping
- `pandas` - Data manipulation
- `cryptography` - Encryption
- `curses` - Terminal UI
- `colorgram` - Color extraction
- `convertapi` - File conversion

**Development Tools**
- Git version control
- Virtual environments

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd python-projects

# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage Examples

**Run Text Editor:**
```bash
python textEditor.py
```

**Run Typing Speed Test:**
```bash
python type_speed_test.py
```

**Run Snake Game:**
```bash
cd turtle_project/snake_game
python main.py
```

**Run Password Manager:**
```bash
python password_protect.py
# First run: Creates encryption key
# Subsequent runs: Add/view passwords
```

## Project Structure

```
.
├── turtle_project/
│   ├── snake_game/
│   ├── ping_pong/
│   ├── turtle_crossing/
│   ├── hirst_paint/
│   └── turtle_race.py
├── hangman/
│   ├── main
│   ├── hangman_art.py
│   └── hangman_words.py
├── US_state_guess/
│   ├── main.py
│   └── 50_states.csv
├── pomodoro_app/
│   └── main.py
├── textEditor.py
├── type_speed_test.py
├── password_protect.py
├── file_converter.py
├── MadLibs_gen.py
├── PIG_game.py
└── README.md
```

## Learning Outcomes

- **GUI Development**: Built interactive applications with Tkinter, learned event handling and widget management
- **Web Automation**: Mastered Selenium for browser automation and BeautifulSoup for web scraping
- **Game Logic**: Implemented collision detection, scoring systems, and game state management
- **File I/O**: Worked with various file formats (CSV, TXT) and encryption
- **Threading**: Basic understanding of concurrent operations (Pomodoro timer)
- **Data Structures**: Applied lists, dictionaries, and OOP principles across projects
- **External APIs**: Integrated third-party services (ConvertAPI)

## Notes

- These are learning projects, not production-ready applications
- Some projects use tutorial resources (acknowledged in code)
- API keys required for file converter (ConvertAPI)
- Selenium projects require ChromeDriver installation

## License

Educational projects - free to use and modify

## Acknowledgments

Built during Python learning phase, exploring various libraries and frameworks to understand the Python ecosystem.
