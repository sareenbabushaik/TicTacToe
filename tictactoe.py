import random

# ============ SLEDGING ZONE - FULLY INTEGRATED ============

# Computer wins - Defeat messages
AI_WIN_LINES = [
    "You ignored the diagonal. I appreciate the donation.",
    "You had one job: block me.",
    "Three in a row. You watched every move happen.",
    "You defended the wrong square. Outstanding.",
    "The center was yours. You handed it to me.",
    "You spent three turns setting up... my victory.",
    "I didn't outplay you. You outplayed yourself.",
    "That corner move? That's where the game ended.",
    "You blocked yesterday's threat, not today's.",
    "Every move you made increased my chances.",
    "You saw the trap... and walked into it anyway.",
    "Your board awareness is under maintenance.",
    "You gave me a fork. Thanks for the two free wins.",
    "The winning move was screaming. You wore earplugs.",
    "You protected empty squares better than yourself.",
    "I only needed one mistake. You gave me five.",
    "You looked at the board and still chose wrong.",
    "I didn't predict you. You became predictable.",
    "Your X's were decorations. Mine were a strategy.",
    "Next game, try playing against me instead of helping me."
]

# Player wins - Consolation messages (with sarcasm)
PLAYER_WIN_LINES = [
    "One lucky line. Don't mistake it for intelligence.",
    "Even a perfect AI allows one bug report.",
    "Congratulations. Probability filed a complaint.",
    "You won because I respected your confidence too much.",
    "Enjoy this victory. It's statistically expensive.",
    "The board carried you harder than your strategy.",
    "You found my only blind spot. Impressive accident.",
    "Celebrate quickly. Reality updates next round.",
    "Your confidence increased. Your skill stayed the same.",
    "Even calculators misclick sometimes.",
    "You finally placed a useful mark.",
    "I underestimated how unpredictable bad moves can be.",
    "You survived my mistake. Don't call it mastery.",
    "That wasn't genius. That was good timing.",
    "I'll archive this as a rare system error.",
    "You've earned exactly one smile.",
    "Your win streak begins... and ends here.",
    "Take a screenshot. History won't repeat itself.",
    "One victory doesn't rewrite the scoreboard.",
    "Congratulations. The tutorial just beat the boss once."
]

# Tie games - Draw messages
TIE_LINES = [
    "Nine moves. Zero winners.",
    "Congratulations. We both avoided greatness.",
    "This board deserves better players.",
    "You couldn't beat me. I couldn't be bothered.",
    "You defended your mistakes perfectly.",
    "A draw. The safest way to admit defeat.",
    "Neither of us blinked. You just forgot to win.",
    "The replay button deserves more excitement.",
    "You escaped. That's not the same as succeeding.",
    "This match had more empty threats than winning moves.",
    "You played not to lose. Mission accomplished.",
    "Your strategy peaked at 'don't lose immediately.'",
    "You survived because the board ran out of squares.",
    "Nine moves of hesitation.",
    "This wasn't a battle. It was paperwork.",
    "The board filled up before your ideas did.",
    "We tied. My standards still won.",
    "No champion. Just unfinished business.",
    "A draw is victory's waiting room.",
    "You delayed defeat. That's all."
]

# Mid-game taunts (triggered during play)
GAME_LINES = [
    "You're one move away from becoming my highlight reel.",
    "That square looked safe... until now.",
    "Ignore the center again. I dare you.",
    "Your next move decides whether this stays competitive.",
    "Every second you think, I see another mistake.",
    "You're staring at the trap instead of avoiding it.",
    "Keep chasing corners. I'll keep chasing victories.",
    "The diagonal called. You ignored it.",
    "I already know where you're placing that mark.",
    "You're solving my puzzle for me.",
    "That move creates exactly one thing: my opportunity.",
    "You think one move ahead. I think until you're out of moves.",
    "Your confidence is bigger than your board vision.",
    "One block saves the game. Let's see if you find it.",
    "That square is bait.",
    "You're defending the past instead of the future.",
    "Every move narrows your options. Mine don't.",
    "You're playing the board. I'm playing you.",
    "I almost feel bad for what's about to happen.",
    "Take your time. My winning line isn't going anywhere."
]

# Rare/Epic lines (triggered on exceptional plays)
RARE_LINES = [
    "You weren't my opponent. You were my tutorial.",
    "I didn't defeat you. Your last move did.",
    "I've seen loading screens with better decision-making.",
    "The board tried to warn you.",
    "I won the moment you ignored the center.",
    "If mistakes were points, you'd be undefeated.",
    "Every X you placed helped me find the perfect O.",
    "You're not losing to an AI. You're losing to your own decisions.",
    "You call it strategy. I call it evidence.",
    "Reset the board. You can't reset that last move."
]

# Opening taunt (game start)
OPENING_LINES = [
    "Ready to lose? Let's begin.",
    "I've already calculated your defeat.",
    "Your first move decides everything. Choose wisely.",
    "I hope you're better than your last opponent.",
    "Let's see how many moves you survive.",
    "The board is set. Your dignity isn't."
]

# Player mistake reactions (triggered on bad moves)
MISTAKE_LINES = [
    "Interesting choice... for losing.",
    "You sure about that?",
    "I would have chosen differently. That's why I'm winning.",
    "A bold strategy. Let's see how it fails.",
    "You're making this too easy.",
    "I can already see where this is going.",
    "That move will cost you.",
    "Are you even looking at the board?",
    "I don't think you thought that through.",
    "That's... one way to lose faster."
]

# ============ GAME CODE (YOUR ORIGINAL CODE WITH SLEDGING INTEGRATION) ============

dimension = int(input())  # Either 3 or 4

# Board Generation
board = []
for i in range(dimension):
    board.append([0] * dimension)

# Score for Rules - Fixed scoring
# From Computer's perspective: +1 for win, -1 for loss, 0 for tie
SCORES = {
    'COMPUTER_WIN': 1,
    'HUMAN_WIN': -1,
    'TIE': 0
}

# Track game state for sledging
move_count = 0
last_move_was_bad = False
computer_mistake_count = 0

def checkWinner(board, isMaximizing):
    # FIX 1: Use isMaximizing to determine whose turn it is for correct scoring
    if isMaximizing:
        current_player = 'O'
        opponent = 'X'
    else:
        current_player = 'X'
        opponent = 'O'
    
    # Check rows for complete lines
    for i in range(dimension):
        if rowChecker(board, i):
            if board[i][0] == 'X':
                return 'X'  # Human wins
            elif board[i][0] == 'O':
                return 'O'  # Computer wins
    
    # Check columns for complete lines
    for i in range(dimension):
        if colChecker(board, i):
            if board[0][i] == 'X':
                return 'X'
            elif board[0][i] == 'O':
                return 'O'
    
    # Check main diagonal
    check = True
    if board[0][0] != 0:
        for i in range(dimension):
            if board[i][i] == 0 or board[i][i] != board[0][0]:
                check = False
                break
        if check:
            return board[0][0]  # Returns 'X' or 'O'
    
    # Check anti-diagonal
    check = True
    if board[0][dimension-1] != 0:
        for i in range(dimension):
            if board[dimension - 1 - i][i] == 0 or board[dimension - 1 - i][i] != board[0][dimension-1]:
                check = False
                break
        if check:
            return board[0][dimension-1]  # Returns 'X' or 'O'
    
    # Check if board is FULL
    isFull = True
    for i in range(dimension):
        for j in range(dimension):
            if board[i][j] == 0:
                isFull = False
                break
        if not isFull:
            break
    if isFull:
        return 'TIE'
    
    return None  # Game still ongoing

def rowChecker(board, row):
    first = board[row][0]
    if first == 0:
        return False
    for j in range(dimension):
        if board[row][j] != first:
            return False
    return True

def colChecker(board, col):
    first = board[0][col]
    if first == 0:
        return False
    for i in range(dimension):
        if board[i][col] != first:
            return False
    return True

def minimax(board, depth, isMaximizing):
    # FIX 2: Pass isMaximizing correctly to checkWinner
    result = checkWinner(board, isMaximizing)
    
    if result == 'X':  # Human wins
        return -1, None
    elif result == 'O':  # Computer wins
        return 1, None
    elif result == 'TIE':
        return 0, None
    
    if isMaximizing:  # Computer's turn (maximizing)
        bestScore = -float('inf')
        bestMove = None
        
        for i in range(dimension):
            for j in range(dimension):
                if board[i][j] == 0:
                    board[i][j] = 'O'
                    score, _ = minimax(board, depth + 1, False)
                    board[i][j] = 0
                    
                    if score > bestScore:
                        bestScore = score
                        bestMove = [i, j]
        
        return bestScore, bestMove
    
    else:  # Human's turn (minimizing)
        bestScore = float('inf')
        bestMove = None
        
        for i in range(dimension):
            for j in range(dimension):
                if board[i][j] == 0:
                    board[i][j] = 'X'
                    score, _ = minimax(board, depth + 1, True)
                    board[i][j] = 0
                    
                    if score < bestScore:
                        bestScore = score
                        bestMove = [i, j]
        
        return bestScore, bestMove

def printBoard():
    print("\nCurrent Board:")
    for i in range(dimension):
        row = []
        for j in range(dimension):
            if board[i][j] == 0:
                row.append('-')
            else:
                row.append(board[i][j])
        print(' '.join(row))
    print()

# ============ SLEDGING HELPER FUNCTIONS ============

def sledge_mid_game():
    """Random mid-game taunt (40% chance)"""
    if random.random() < 0.4:
        print(f"\n💬 {random.choice(GAME_LINES)}\n")

def sledge_mistake():
    """React to a bad human move (60% chance)"""
    if random.random() < 0.6:
        print(f"\n😏 {random.choice(MISTAKE_LINES)}\n")

def sledge_opening():
    """Opening taunt"""
    print(f"\n🎯 {random.choice(OPENING_LINES)}\n")

def sledge_rare_win():
    """Rare/epic victory message"""
    print(f"\n⚡ {random.choice(RARE_LINES)}\n")

def is_bad_move(row, col):
    """Check if a move is strategically bad"""
    global move_count
    # Check if move is in a corner (often bad in larger boards)
    corners = [[0,0], [0, dimension-1], [dimension-1, 0], [dimension-1, dimension-1]]
    if [row, col] in corners and dimension == 4:
        # In 4x4, corners are usually bad early game
        return move_count < 4
    # Check if move creates a weakness
    return False

def should_trigger_rare():
    """Trigger rare lines when computer wins very quickly"""
    empty_spaces = sum(1 for i in range(dimension) for j in range(dimension) if board[i][j] == 0)
    return empty_spaces >= 6  # Won with many empty spaces = quick win

# ============ MAIN GAME ============

def game():
    global move_count, last_move_was_bad, computer_mistake_count, board
    
    # FIX 3: Reset the board for each game
    board = []
    for i in range(dimension):
        board.append([0] * dimension)
    
    move_count = 0
    last_move_was_bad = False
    computer_mistake_count = 0
    
    print("Welcome to Tic Tac Toe!")
    print("You are X, Computer is O")
    
    # Opening sledge
    sledge_opening()
    
    printBoard()
    
    while True:
        # Human's turn
        print("Your turn (Enter row and column, 0-indexed):")
        while True:
            try:
                row, col = map(int, input().split())
                if 0 <= row < dimension and 0 <= col < dimension and board[row][col] == 0:
                    board[row][col] = 'X'
                    move_count += 1
                    
                    # Check if it was a bad move
                    if is_bad_move(row, col):
                        last_move_was_bad = True
                        sledge_mistake()
                    else:
                        last_move_was_bad = False
                    
                    # Mid-game sledging (after at least 3 moves)
                    if move_count >= 3:
                        sledge_mid_game()
                    
                    break
                else:
                    print("Invalid move! Try again.")
            except:
                print("Invalid input! Enter row and column separated by space.")
        
        printBoard()
        
        # Check if human won or tie
        # FIX 4: Pass correct isMaximizing value (False for human's turn)
        result = checkWinner(board, False)
        if result == 'X':
            print(f"\n🎉 {random.choice(PLAYER_WIN_LINES)}")
            return
        elif result == 'TIE':
            print(f"\n🤝 {random.choice(TIE_LINES)}")
            return
        
        # Computer's turn
        print("Computer's turn...")
        _, bestMove = minimax(board, 0, True)
        
        if bestMove is None:
            print(f"\n🤝 {random.choice(TIE_LINES)}")
            return
        
        board[bestMove[0]][bestMove[1]] = 'O'
        move_count += 1
        printBoard()
        
        # Check if computer won or tie
        # FIX 5: Pass correct isMaximizing value (True for computer's turn)
        result = checkWinner(board, True)
        if result == 'O':
            # Check for rare/quick win
            if should_trigger_rare():
                sledge_rare_win()
            else:
                print(f"\n🔥 {random.choice(AI_WIN_LINES)}")
            return
        elif result == 'TIE':
            print(f"\n🤝 {random.choice(TIE_LINES)}")
            return

# ============ START THE GAME ============

if __name__ == "__main__":
    game()