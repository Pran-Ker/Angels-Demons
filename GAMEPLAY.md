# Angels & Demons - Gameplay Guide

## Overview

Angels & Demons is a unique chess variant that pits a lone King (Angels) against a small army of pieces (Demons) in an asymmetric battle. The Angel King must use cunning strategy and its special pawn-spawning ability to reach the opposite side of the board, while the Demons hunt it down.

## Game Setup

### Board Layout

```
  0   1   2   3   4   5   6   7
0 R   N   B   -   -   B   N   R   ← Demons (Black)
1 -   -   -   -   -   -   -   -
2 -   -   -   -   -   -   -   -
3 -   -   -   -   -   -   -   -
4 -   -   -   -   -   -   -   -
5 -   -   -   -   -   -   -   -
6 -   -   -   -   -   -   -   -
7 -   -   -   K   -   -   -   -   ← Angels (White)
```

### Starting Pieces

**Angels (White - Bottom):**
- 1 King (starts at position d1/column 3)

**Demons (Black - Top):**
- 2 Rooks (corners: a8, h8)
- 2 Knights (b8, g8)
- 2 Bishops (c8, f8)
- NO King, Queen, or Pawns

## Game Rules

### Objective

**Angels Win:** The White King must reach any square on row 0 (the top row of the board).

**Demons Win:** Capture the White King (checkmate or capture).

### Turn Order

1. Angels (White) move first
2. Players alternate turns
3. Each player makes one move per turn (except when using special abilities)

### Piece Movement

All pieces move according to standard chess rules:

- **King:** One square in any direction (horizontally, vertically, or diagonally)
- **Rook:** Any number of squares horizontally or vertically
- **Knight:** L-shaped move (2 squares in one direction, 1 square perpendicular)
- **Bishop:** Any number of squares diagonally
- **Pawn:** One square forward, captures diagonally (see Special Abilities)

## Special Abilities

### Angel's Pawn Spawning

**The most important mechanic in the game!**

Whenever the White King moves, a White Pawn automatically spawns on the square the King just vacated.

**Example:**
```
Before:              After:
-  -  -              -  -  -
-  K  -    →         -  -  K
-  -  -              -  P  -
```

The King moved from the center to the right, leaving a pawn behind!

**Strategic Uses:**
- Create defensive barriers
- Block enemy pieces from attacking routes
- Build a "stairway" of pawns to help the King advance
- Control key squares

### Pawn Removal

Angels have the special ability to remove their own pawns from the board **without losing a turn**.

**How to Remove Pawns:**
- Right-click on any White Pawn to remove it instantly
- This does NOT consume your turn
- You can remove multiple pawns in one turn if needed

**Strategic Uses:**
- Clear the King's path when pawns become obstacles
- Remove pawns that are blocking your own advancement
- Adjust your defensive formation quickly

### Pawn Movement

White Pawns spawned by the King move according to standard chess rules:
- Move one square forward (toward row 0)
- Can move two squares forward on their first move (from starting position)
- Capture diagonally one square forward
- Can capture Demon pieces

**Important:** Unlike standard chess, there is NO en passant and NO pawn promotion (the game ends when the King reaches row 0).

## Controls

### Mouse Controls

**Left-Click:**
1. Click on a piece to select it
2. Valid moves will be highlighted in BLUE
3. Click on a highlighted square to move the piece
4. Click on an enemy piece (if highlighted) to capture it

**Right-Click:**
- Click on any White Pawn to remove it (Angels only, doesn't use a turn)

### Keyboard Controls

**During Game:**
- `ESC` - Quit the game

**Game Over Screen:**
- `R` - Restart the game
- `ESC` - Quit the game

## Visual Indicators

### Turn Indicator
At the top of the screen, you'll see whose turn it is:
- **GOLD text:** Angels' Turn (White)
- **DARK RED text:** Demons' Turn (Black)

### Move Highlighting
- **BLUE squares:** Valid moves for the selected piece
- **BLUE on piece:** Enemy piece that can be captured

### Board Colors
- **White/Grey:** Standard chessboard pattern
- **Gold:** Angel King and UI elements
- **Dark Red:** Demon pieces and UI elements

## Winning Strategies

### For Angels (White):

1. **Use Pawns Defensively**
   - Create walls of pawns to block Demon attacks
   - Form a protective "shell" around your King

2. **Plan Your Path**
   - Think ahead about which squares the King will traverse
   - Remember: each move leaves a pawn behind
   - Don't trap yourself with your own pawns!

3. **Control the Center**
   - Pawns in the center control more squares
   - Central pawns can threaten multiple Demon pieces

4. **Sacrifice When Needed**
   - Sometimes you need to sacrifice pawns to capture Demon pieces
   - Trading pawns for Demons is usually favorable

5. **Remove Blocking Pawns**
   - Use right-click to remove pawns that block your advance
   - Clear your own path strategically

### For Demons (Black):

1. **Coordinate Your Pieces**
   - Use multiple pieces to attack the King
   - Create inescapable traps

2. **Control Key Squares**
   - Prevent the King from advancing
   - Block the path to row 0

3. **Beware of Pawn Walls**
   - Don't let the King build an impenetrable fortress
   - Attack early before the Angel builds too many pawns

4. **Use Knights Effectively**
   - Knights can jump over pawn walls
   - Perfect for attacking the King from unexpected angles

5. **Cut Off Escape Routes**
   - Use Bishops and Rooks to control long diagonals and files
   - Force the King into corners

## Common Mistakes

### Angels:
❌ **Creating too many pawns** - You can trap yourself!
✅ **Solution:** Use right-click to remove blocking pawns

❌ **Moving too quickly** - Rushing forward without protection
✅ **Solution:** Build a defensive wall before advancing

❌ **Forgetting pawns can capture** - Pawns aren't just obstacles!
✅ **Solution:** Use pawns to eliminate key Demon pieces

### Demons:
❌ **Attacking individually** - Single pieces are easily blocked
✅ **Solution:** Coordinate 2-3 pieces for attacks

❌ **Ignoring pawn buildup** - Letting Angels create massive walls
✅ **Solution:** Attack early and often

❌ **Poor piece positioning** - Pieces blocking each other
✅ **Solution:** Maintain flexible positions with escape routes

## Advanced Tactics

### The Pawn Ladder
Create a diagonal staircase of pawns that the King can use to advance safely:
```
-  -  P  -        The King can advance
-  P  K  -        using the pawns as
P  K  -  -   →    protection, climbing
K  -  -  -        toward row 0
```

### The Fortress Gambit
Build a massive pawn wall, then remove key pawns to create sudden breakthroughs:
```
P  P  P  P        -  P  P  P
P  K  P  P   →    P  K  -  P    King escapes!
-  -  -  -        -  -  -  -
```

### The Sacrifice Play
Trade your King's position to capture a crucial Demon piece:
```
-  R  -           -  P  -
-  K  -    →      -  -  K       Rook captured!
```

### Knight Defense
Against Knights (who jump over pawns), create diamond formations:
```
   -  P  -         Knights can't attack
-  P  K  P  -      the King without
   -  P  -         being captured!
```

## Frequently Asked Questions

**Q: Can pawns move backward?**
A: No, pawns only move forward (toward row 0).

**Q: What happens if the King is in check?**
A: Unlike regular chess, there is no formal "check" - the King can move into danger. However, if the King is captured, Demons win immediately.

**Q: Can I remove pawns on the Demons' turn?**
A: Yes! Pawn removal is instant and doesn't use a turn. You can do it anytime.

**Q: Can the King capture Demon pieces?**
A: Yes! The King can capture any adjacent Demon piece.

**Q: What if I run out of moves?**
A: If the King cannot move and is not being attacked, it's a stalemate. However, with pawn removal ability, this is rare. The game typically ends in either Angel victory (reaching row 0) or Demon victory (King captured).

**Q: Do pawns promote to Queens at row 0?**
A: No. When the King reaches row 0, the Angels win immediately. Pawns don't promote.

**Q: How many pawns can be on the board?**
A: The King leaves a pawn every time it moves, so theoretically many pawns. However, you can remove them at will.

## Tips for Beginners

1. **Start Slow:** Take your time to understand pawn spawning
2. **Practice Removal:** Get comfortable with right-click pawn removal
3. **Plan Ahead:** Think 2-3 moves in advance
4. **Use the Demons:** Play both sides to learn strategies
5. **Experiment:** Try different pawn formations

## Estimated Game Length

- **Quick Game:** 5-10 minutes (aggressive Demon play)
- **Standard Game:** 10-20 minutes (balanced strategies)
- **Epic Battle:** 20-30 minutes (defensive Angel play)

## Difficulty Assessment

**Angels (White):** ⭐⭐⭐⭐ (Hard)
Requires strategic planning, resource management, and clever use of pawn spawning/removal mechanics.

**Demons (Black):** ⭐⭐⭐ (Medium)
Requires piece coordination and tactical awareness, but more straightforward than playing Angels.

## Conclusion

Angels & Demons is a game of asymmetric strategy where creative thinking and tactical planning are rewarded. Master the art of pawn manipulation, and you'll discover countless ways to achieve victory!

Good luck, and may the best side win! 👼⚔️😈
