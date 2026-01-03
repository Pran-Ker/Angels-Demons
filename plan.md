# Angels-Demons Game Completion Plan

## Project Overview
Complete the Angels-Demons chess variant game - a unique chess game where the Angel's King spawns pawns as it moves and must reach the opposite side of the board while being hunted by the Demons' pieces.

## Current State Analysis

### What's Implemented
- ✅ Basic pygame board rendering (8x8 grid)
- ✅ Chess piece classes and movement logic
- ✅ Standard chess piece movements (King, Pawn, Rook, Bishop, Knight, Queen)
- ✅ Piece selection and move highlighting
- ✅ Turn-based movement system
- ✅ Basic move validation

### What's Missing
- ❌ Correct starting board setup (currently uses standard chess setup)
- ❌ Pawn spawning mechanic when King moves
- ❌ Pawn removal mechanic (special ability)
- ❌ Win condition detection
- ❌ Game state management (game over, win/loss screens)
- ❌ UI improvements (turn indicators, game status)
- ❌ Code cleanup and organization

## Implementation Plan

### Phase 1: Core Game Mechanics

#### Task 1.1: Fix Starting Board Setup
**File:** `ChessMain.py`
**Priority:** HIGH

- [ ] Update `create_board()` function to match game rules:
  - Angels (White) side: Place 1 King at position (7, 3) or (7, 4)
  - Demons (Black) side:
    - 2 Rooks at (0, 0) and (0, 7)
    - 2 Knights at (0, 1) and (0, 6)
    - 2 Bishops at (0, 2) and (0, 5)
  - Remove all pawns from initial setup
  - Remove Queen from both sides
  - Remove King from Demons side
- [ ] Update `starting_order` dictionary to match new setup
- [ ] Test that board renders correctly with new setup

#### Task 1.2: Implement Pawn Spawning Mechanic
**File:** `ChessMain.py`, `ChessEngine.py`
**Priority:** HIGH

- [ ] Create `spawn_pawn()` function that:
  - Takes the King's previous position
  - Places a White pawn at that position
  - Adds the pawn to the board state
- [ ] Modify the King's move logic in `main()`:
  - Track King's previous position before move
  - After King moves successfully, call `spawn_pawn()` at old position
  - Update both `board` array and `starting_order` dictionary
- [ ] Add visual feedback for pawn spawning (optional animation)
- [ ] Test pawn spawning works correctly for all King movements

#### Task 1.3: Implement Pawn Removal Mechanic
**File:** `ChessMain.py`, `ChessEngine.py`
**Priority:** HIGH

- [ ] Add right-click detection for pawn removal:
  - Detect `pygame.MOUSEBUTTONDOWN` with button 3 (right-click)
  - Check if clicked square contains a White pawn
  - Remove pawn without consuming a turn
- [ ] Alternative: Add keyboard shortcut (e.g., 'R' key) to remove selected pawn
- [ ] Ensure removal doesn't count as a move/turn
- [ ] Add visual feedback for pawn removal
- [ ] Test pawn removal works correctly

#### Task 1.4: Implement Win Condition Detection
**File:** `ChessMain.py` or new `GameLogic.py`
**Priority:** HIGH

- [ ] Create `check_angel_win()` function:
  - Check if White King reached row 0 (top of board)
  - Return True if Angel wins
- [ ] Create `check_demon_win()` function:
  - Check if White King has been captured (no longer on board)
  - Optional: Implement checkmate detection
  - Return True if Demons win
- [ ] Add win condition checks after each move
- [ ] Trigger game over state when win detected
- [ ] Test both win conditions work correctly

### Phase 2: Game State Management

#### Task 2.1: Add Game State System
**File:** `ChessMain.py`
**Priority:** MEDIUM

- [ ] Create game state enum/class:
  - PLAYING
  - ANGEL_WIN
  - DEMON_WIN
  - PAUSED
- [ ] Add current game state variable
- [ ] Update main game loop to respect game state
- [ ] Prevent moves when game is not in PLAYING state

#### Task 2.2: Create Win/Loss Screens
**File:** `ChessMain.py`
**Priority:** MEDIUM

- [ ] Design end game screen:
  - Display winner (Angels or Demons)
  - Show "Play Again" button
  - Show "Quit" button
- [ ] Implement `draw_game_over()` function
- [ ] Add button click detection for restart/quit
- [ ] Implement game restart functionality
- [ ] Test end game flow

#### Task 2.3: Add Game UI Improvements
**File:** `ChessMain.py`
**Priority:** LOW

- [ ] Add turn indicator:
  - Display "Angels' Turn" or "Demons' Turn"
  - Update after each move
- [ ] Add move counter display
- [ ] Add game title/header
- [ ] Improve piece selection visual feedback
- [ ] Add sound effects (optional):
  - Piece move sound
  - Capture sound
  - Pawn spawn sound
  - Win sound

### Phase 3: Code Quality & Polish

#### Task 3.1: Refactor and Organize Code
**Files:** `ChessMain.py`, `ChessEngine.py`
**Priority:** MEDIUM

- [ ] Separate concerns:
  - Move all game logic to `ChessEngine.py`
  - Keep only UI/rendering in `ChessMain.py`
- [ ] Create `GameState` class to encapsulate:
  - Board state
  - Current turn
  - Game status
  - Move history
- [ ] Clean up global variables
- [ ] Add proper function documentation
- [ ] Remove unused code (standard chess queen, extra pawns, etc.)
- [ ] Improve variable naming consistency

#### Task 3.2: Fix Image Loading Issues
**File:** `ChessMain.py`
**Priority:** MEDIUM

- [ ] Fix image path references:
  - Current code uses 'b_pawn.png' but images are in 'images/' folder
  - Update all image paths to 'images/bP.png', 'images/wK.png', etc.
- [ ] Add error handling for missing images
- [ ] Verify all piece images load correctly
- [ ] Add fallback rendering if images missing (colored rectangles)

#### Task 3.3: Add Game Configuration
**File:** New `config.py`
**Priority:** LOW

- [ ] Create configuration file for:
  - Window size
  - Colors
  - Starting positions
  - Game rules toggles
- [ ] Make game easily configurable
- [ ] Add difficulty settings (optional)

### Phase 4: Testing & Documentation

#### Task 4.1: Testing
**Priority:** MEDIUM

- [ ] Test all piece movements work correctly
- [ ] Test pawn spawning in all scenarios:
  - King moves to empty square
  - King captures a piece
  - King moves to edge of board
- [ ] Test pawn removal doesn't break game state
- [ ] Test win conditions:
  - Angel reaches top row
  - Demon captures King
- [ ] Test edge cases:
  - Pawn spawning when board is full
  - Multiple pawn removals
  - Game restart functionality
- [ ] Test game with different screen resolutions

#### Task 4.2: Update Documentation
**Files:** `README.md`, new `GAMEPLAY.md`
**Priority:** LOW

- [ ] Update README.md with:
  - Clear installation instructions
  - How to run the game
  - Requirements
- [ ] Create GAMEPLAY.md with:
  - Detailed game rules
  - Controls explanation
  - Strategy tips
- [ ] Add code comments for complex logic
- [ ] Create DEVELOPMENT.md for contributors

#### Task 4.3: Fix Dependencies
**File:** `requirements.txt`
**Priority:** LOW

- [ ] Remove unnecessary dependencies:
  - `chess==1.8.0` (not used for this variant)
  - Other unused packages
- [ ] Add pygame to requirements (currently missing!)
- [ ] Pin specific versions for stability
- [ ] Test clean install from requirements.txt

### Phase 5: Additional Features (Optional)

#### Task 5.1: Add Undo Move
- [ ] Implement move history stack
- [ ] Add undo button or keyboard shortcut
- [ ] Handle undo with pawn spawning/removal

#### Task 5.2: Add Move Validation
- [ ] Prevent illegal moves that would put King in check
- [ ] Highlight squares that would endanger King
- [ ] Add "check" warning indicator

#### Task 5.3: Add AI Opponent
- [ ] Implement basic AI for Demons side
- [ ] Add difficulty levels
- [ ] Make single-player mode available

#### Task 5.4: Add Animations
- [ ] Smooth piece movement animations
- [ ] Pawn spawn animation
- [ ] Piece capture animation
- [ ] Victory celebration animation

## Implementation Order (Recommended)

1. **Start Here:** Task 1.1 - Fix Starting Board Setup
2. Task 3.2 - Fix Image Loading Issues (prevents visual bugs)
3. Task 1.2 - Implement Pawn Spawning Mechanic
4. Task 1.3 - Implement Pawn Removal Mechanic
5. Task 1.4 - Implement Win Condition Detection
6. Task 2.1 - Add Game State System
7. Task 2.2 - Create Win/Loss Screens
8. Task 3.1 - Refactor and Organize Code
9. Task 2.3 - Add Game UI Improvements
10. Task 4.1 - Testing
11. Task 4.2 - Update Documentation
12. Task 4.3 - Fix Dependencies
13. Optional tasks as desired

## Key Files to Modify

| File | Purpose | Changes Needed |
|------|---------|----------------|
| `ChessMain.py` | Main game loop, UI, rendering | Fix setup, add pawn spawning/removal, add UI |
| `ChessEngine.py` | Game logic (if refactored) | Move game logic here from ChessMain |
| `requirements.txt` | Dependencies | Add pygame, remove chess package |
| `README.md` | Documentation | Update with proper instructions |
| `images/` | Game assets | Verify all images present |

## Testing Checklist

- [ ] Game starts with correct piece positions
- [ ] Angels (White) can only move King initially
- [ ] Demons (Black) can move all their pieces
- [ ] King spawns pawn when moving
- [ ] Pawns can be removed with right-click
- [ ] Angel wins when King reaches row 0
- [ ] Demon wins when King is captured
- [ ] Game over screen appears correctly
- [ ] Game can be restarted
- [ ] No crashes during gameplay
- [ ] All images load correctly
- [ ] Turn indicator updates properly

## Estimated Completion

- **Core Mechanics (Phase 1):** 4-6 hours
- **Game State (Phase 2):** 3-4 hours
- **Code Quality (Phase 3):** 3-4 hours
- **Testing & Docs (Phase 4):** 2-3 hours
- **Total:** 12-17 hours of development time

## Notes

- The current code has a mix of two different board representations (`board` array and `starting_order` dictionary) which can cause sync issues. Consider consolidating to one.
- The image loading uses wrong paths - need to prefix with 'images/' directory
- The game currently doesn't distinguish between the two sides properly for this variant
- Consider adding a visual indicator showing which pawns can be removed
- May want to add a move counter to track how efficiently the Angel can win

## Success Criteria

The game is considered complete when:
1. ✅ Correct starting setup (1 Angel King vs 6 Demon pieces)
2. ✅ King spawns pawns when moving
3. ✅ Pawns can be removed without losing turn
4. ✅ Angel win condition works (King reaches top)
5. ✅ Demon win condition works (King captured)
6. ✅ Game can be restarted after completion
7. ✅ No major bugs or crashes
8. ✅ Documentation is clear and complete
