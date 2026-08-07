# 🎮 Tic Tac Toe - AI Roast Edition

A dynamic Tic Tac Toe game with a twist - the AI doesn't just beat you, it roasts you! Featuring 3x3, 4x4, and 5x5 boards with adaptive AI difficulty and a live trash-talking chat system.

## ✨ Features

### 🎯 Multiple Board Sizes
- **3x3** - Classic mode, perfect for beginners (IMPOSSIBLE difficulty)
- **4x4** - More space, more ways to lose (HARD difficulty)
- **5x5** - Big board, big mistakes (MEDIUM difficulty)

### 🤖 Adaptive AI
- **Full Minimax** for 3x3 - unbeatable perfect play
- **Depth-Limited Minimax** for 4x4 and 5x5 with heuristic evaluation
- **Random Move Chance** - 30% for 4x4, 50% for 5x5 (makes it beatable!)
- **Smart Difficulty Scaling** based on board size

### 💬 Live Roast System
The AI trash-talks you throughout the game:
- **Opening Taunts** - Sets the tone
- **Mid-game Roasts** - Comments on your moves (35% chance)
- **Mistake Reactions** - Calls out bad moves (50% chance)
- **Rare Epic Roasts** - Special messages for quick wins
- **End-game Messages** - Victory, defeat, or tie reactions

### 🎨 Modern UI
- **Dark Theme** - Sleek black background
- **White Board** - Clean, contrasting game board
- **Chat Interface** - Live AI commentary on the right
- **Score Tracking** - Keeps track of wins, losses, and ties
- **Responsive Design** - Works on mobile, tablet, and desktop

## 🚀 Quick Start

### Option 1: Play Online
Simply open the `index.html` file in any modern browser.

### Option 2: Run Locally
```bash
# Clone the repository
git clone https://github.com/yourusername/tic-tac-toe-ai-roast.git

# Navigate to the directory
cd tic-tac-toe-ai-roast

# Open in browser (macOS)
open index.html

# Or on Windows
start index.html

# Or on Linux
xdg-open index.html
```

## 🎮 How to Play

1. **Select Board Size** - Choose 3x3, 4x4, or 5x5
2. **Make Your Move** - Click any empty cell to place your 'X'
3. **Watch the AI** - The AI responds with its 'O' and roasts you
4. **Win or Lose** - The game ends with appropriate celebrations or roasts
5. **Track Scores** - See your wins, losses, and ties
6. **Reset** - Start a new game or reset scores anytime

## 🧠 AI Strategy

### 3x3 (IMPOSSIBLE)
- Full minimax search (9 depth)
- Perfect play - you can't win if AI plays optimally
- Best for learning and challenging yourself

### 4x4 (HARD)
- Depth-limited minimax (4 depth)
- Heuristic evaluation for depth cutoff
- 30% chance of random move
- Beatable but challenging

### 5x5 (MEDIUM)
- Very limited minimax (3 depth)
- Heuristic evaluation for depth cutoff
- 50% chance of random move
- More forgiving, good for casual play

## 🎯 Sledging (Trash Talk) System

The AI comes with over 150 unique roasts:

### Categories
| Category | Purpose | When Triggered |
|----------|---------|----------------|
| `AI_WIN_LINES` | Victory taunts | AI wins |
| `PLAYER_WIN_LINES` | Sarcastic congratulations | Player wins |
| `TIE_LINES` | Draw commentary | Game is a tie |
| `GAME_LINES` | Mid-game roasts | Random during play |
| `RARE_LINES` | Epic roasts | Quick AI wins |
| `OPENING_LINES` | Game starts | First move |
| `MISTAKE_LINES` | Error reactions | Bad moves |

## 🛠️ Technology Stack

- **HTML5** - Structure
- **CSS3** - Styling with animations
- **Vanilla JavaScript** - Game logic and AI
- **Minimax Algorithm** - AI decision making
- **Heuristic Evaluation** - Performance optimization

## 📁 File Structure

```
tic-tac-toe-ai-roast/
├── index.html          # Complete game file
├── README.md           # This file
└── assets/             # (Optional) Images and assets
```

## 🔧 Customization

### Adjust AI Difficulty
```javascript
// In getAIMove() function
if (dimension === 4) {
    maxDepth = 4;           // Increase for harder AI
    if (Math.random() < 0.3) // Decrease for harder AI
}
```

### Add Your Own Roasts
```javascript
const AI_WIN_LINES = [
    "Your roast here",
    "Another roast",
    // Add more...
];
```

### Change Board Colors
```css
.cell.X {
    color: #667eea;  /* Your color for X */
}
.cell.O {
    color: #764ba2;  /* Your color for O */
}
```

## 🐛 Known Issues

- **Performance**: 4x4 and 5x5 boards can be slow on older devices due to minimax complexity
- **Mobile**: Small screens may have cramped board display

## 🚧 Future Improvements

- [ ] Add sound effects for moves and roasts
- [ ] Implement online multiplayer
- [ ] Add difficulty selection per board size
- [ ] Create tournament mode
- [ ] Add more roast categories
- [ ] Performance optimization for larger boards
- [ ] Save game state in localStorage

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch
3. **Commit** your changes
4. **Push** to the branch
5. **Open** a Pull Request

### Areas to Contribute
- New roast messages
- UI/UX improvements
- Performance optimizations
- Additional board sizes
- Mobile responsiveness
- Bug fixes

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by classic Tic Tac Toe games
- Roast messages inspired by AI trash-talking bots
- UI design influenced by modern dark theme applications

