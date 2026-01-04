# Angels & Demons 👼⚔️😈

A unique asymmetric chess variant built with Python and Pygame. Play as the lone Angel King with pawn-spawning abilities, or command the Demon army to hunt down the King!

![Game Type](https://img.shields.io/badge/Type-Strategy%20Game-blue)
![Python](https://img.shields.io/badge/Python-3.7%2B-green)
![Pygame](https://img.shields.io/badge/Pygame-2.5%2B-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📖 Table of Contents

- [About the Game](#about-the-game)
- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Game Rules](#game-rules)
- [Controls](#controls)
- [Screenshots](#screenshots)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## 🎮 About the Game

**Angels & Demons** is an innovative chess variant featuring asymmetric gameplay:

- **Angels (White):** Control a single King that can spawn pawns adjacent to itself. Your goal is to reach the opposite side of the board.
- **Demons (Black):** Command 2 Rooks, 2 Knights, and 2 Bishops. Your goal is to capture the Angel King.

The Angel King possesses unique abilities:
1. **Pawn Placement:** Right-click the King to place a pawn on any adjacent empty square (counts as one move)
2. **Normal Movement:** The King and pawns can move normally according to chess rules

This creates deep strategic gameplay where resource management and tactical planning are crucial!

## ✨ Features

- ✅ **Asymmetric Gameplay:** Two completely different play styles
- ✅ **Unique Mechanics:** Pawn spawning and removal system
- ✅ **Beautiful UI:** Clean interface with turn indicators and instructions
- ✅ **Win Detection:** Automatic game-over detection with victory screens
- ✅ **Restart Functionality:** Quick restart with R key
- ✅ **Visual Feedback:** Move highlighting and turn indicators
- ✅ **Smooth Gameplay:** Responsive controls and clean graphics
- ✅ **Complete Documentation:** Extensive gameplay guide included

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Step 1: Clone the Repository

```bash
git clone https://github.com/Pran-Ker/Angles-Demons.git
cd Angles-Demons
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- `pygame>=2.5.0` - Game engine and graphics
- `certifi>=2022.12.7` - SSL certificates

### Step 3: Run the Game

```bash
python ChessMain.py
```

That's it! The game window should open and you're ready to play.

## 🎯 How to Play

### Quick Start

1. Run `python ChessMain.py`
2. Angels (White) move first
3. **Angels Turn Options:**
   - Left-click the King to move it normally, OR
   - Left-click a pawn to move it forward/diagonally (attack), OR
   - Right-click the King, then click an adjacent square to place a new pawn
4. **Demons Turn:** Left-click any piece to select, then click a valid square to move
5. Angels win by reaching the top row, Demons win by capturing the King

### Detailed Rules

For comprehensive gameplay instructions, strategies, and tactics, see **[GAMEPLAY.md](GAMEPLAY.md)**.

## 📋 Game Rules

### Setup

**Angels (White):**
- 1 King (starts at bottom-center)

**Demons (Black):**
- 2 Rooks (corners)
- 2 Knights
- 2 Bishops

### Victory Conditions

| Team | Win Condition |
|------|---------------|
| **Angels** | King reaches row 0 (top of board) |
| **Demons** | Capture the Angel King |

### Special Abilities

**Angel King:**
- Can place a pawn on any adjacent empty square (right-click King, then click adjacent square)
- Pawn placement counts as one move and ends the turn
- Pawns move forward and attack diagonally like normal chess pawns

**Demon Pieces:**
- All move according to standard chess rules
- Work together to capture the King

## 🎮 Controls

### Mouse

| Action | Control |
|--------|---------|
| Select/Move piece | Left-click piece, then left-click destination |
| Place pawn (Angels only) | Right-click King, then left-click adjacent empty square |
| Cancel pawn placement | Press SPACE or click elsewhere |

### Keyboard

| Key | Action |
|-----|--------|
| `SPACE` | Skip pawn placement (when in pawn placement mode) |
| `R` | Restart game (when game over) |
| `ESC` | Quit game |

## 📸 Screenshots

### Gameplay

![Angels & Demons Gameplay](screenshot.png)

*Mid-game showing Angels (White) with King and pawns vs Demons (Black) with Rooks, Knights, and Bishops. Notice the colored halos around pieces for better visibility!*

**Key Visual Features:**
- 🟡 **Gold halos** around White pieces (Angels)
- 🔴 **Red halos** around Black pieces (Demons)
- 🟢 **Green highlights** show where you can place pawns (when King is right-clicked)
- 🔵 **Blue highlights** show valid moves for selected pieces
- Dynamic turn indicator at the top
- Context-aware instructions at the bottom

## 🛠️ Development

### Project Structure

```
Angles-Demons/
├── ChessMain.py        # Main game file with UI and game loop
├── ChessEngine.py      # (Future) Separated game logic
├── requirements.txt    # Python dependencies
├── README.md          # This file
├── GAMEPLAY.md        # Detailed gameplay guide
├── plan.md            # Development plan
├── LICENSE            # MIT License
└── images/            # Chess piece images
    ├── wK.png         # White King
    ├── wP.png         # White Pawn
    ├── bR.png         # Black Rook
    ├── bN.png         # Black Knight
    ├── bB.png         # Black Bishop
    └── ...
```

### Key Files

- **ChessMain.py** - Contains the entire game implementation including:
  - Piece classes and movement logic
  - Board setup and rendering
  - Game state management
  - Win condition detection
  - UI elements and controls

### Technologies Used

- **Python 3.7+** - Core language
- **Pygame 2.5+** - Graphics and game engine
- **Standard Chess Piece Images** - PNG format

## 🤝 Contributing

Contributions are welcome! Here are some ways you can help:

### Ideas for Contributions

- [ ] AI opponent for single-player mode
- [ ] Sound effects and background music
- [ ] Animation for piece movements
- [ ] Undo/Redo functionality
- [ ] Move history tracking
- [ ] Save/Load game state
- [ ] Online multiplayer
- [ ] Different difficulty levels
- [ ] Achievement system
- [ ] Leaderboard

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Style

- Follow PEP 8 Python style guide
- Add comments for complex logic
- Update documentation for new features
- Test your changes thoroughly

## 🐛 Known Issues

- None currently! If you find a bug, please [open an issue](https://github.com/Pran-Ker/Angles-Demons/issues).

## 📝 TODO

- [ ] Separate game logic into ChessEngine.py
- [ ] Add unit tests
- [ ] Implement AI opponent
- [ ] Add animations
- [ ] Create a settings menu
- [ ] Add sound effects
- [ ] Implement undo functionality

## 🎓 Learning Resources

This game is a great project for learning:
- Python game development with Pygame
- Game state management
- Event-driven programming
- UI/UX design in games
- Algorithmic thinking (move validation, win detection)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Authors

- **Pran-Ker** - Initial work and game design

## 🙏 Acknowledgments

- Chess piece images from standard chess sets
- Pygame community for excellent documentation
- Chess variant enthusiasts for inspiration

## 📞 Support

If you have questions or need help:

1. Check [GAMEPLAY.md](GAMEPLAY.md) for gameplay questions
2. Search [existing issues](https://github.com/Pran-Ker/Angles-Demons/issues)
3. Open a new issue if needed

## 🌟 Show Your Support

If you enjoyed this game:
- ⭐ Star this repository
- 🍴 Fork it and create your own variant
- 🐛 Report bugs to help improve it
- 💡 Suggest new features

---

**Have fun playing Angels & Demons!** 👼⚔️😈

*May the best side win!*
