from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def get_valid_moves(request, slug):
    print("slug",slug)
    positions = request.data.get('positions', {})
    print("positions",positions)
    piece_position = positions.get(slug, None)
    print("piece_position",piece_position)
    if not piece_position:
        return Response({'error': f'Position not found for {slug}'}, status=400)
    
    valid_moves = calculate_valid_moves(slug, piece_position)
    
    return Response({'valid_moves': valid_moves})

def calculate_valid_moves(slug, piece_position):
    valid_moves = []

    if slug == 'knight':
        valid_moves = calculate_knight_moves(piece_position)
    elif slug == 'rook':
        valid_moves = calculate_rook_moves(piece_position)
    elif slug == 'bishop':
        valid_moves = calculate_bishop_moves(piece_position)
    elif slug == 'queen':
        valid_moves = calculate_queen_moves(piece_position)
    
    return valid_moves

def calculate_knight_moves(position):
    column = ord(position[0].upper()) - ord('A')
    row = int(position[1]) - 1
    
    potential_moves = [
        (column - 2, row - 1),
        (column - 2, row + 1),
        (column - 1, row - 2),
        (column - 1, row + 2),
        (column + 1, row - 2),
        (column + 1, row + 2),
        (column + 2, row - 1),
        (column + 2, row + 1),
    ]
    
    valid_moves = []
    
    for move in potential_moves:
        col, row = move
        if 0 <= col < 8 and 0 <= row < 8:
            valid_moves.append(f'{chr(col + ord("A"))}{row + 1}')
    
    return valid_moves

def calculate_rook_moves(position):
    column = ord(position[0].upper()) - ord('A')
    row = int(position[1]) - 1
    
    valid_moves = []
    
    # Calculate valid moves horizontally
    for col in range(8):
        if col != column:
            valid_moves.append(f'{chr(col + ord("A"))}{row + 1}')
    
    # Calculate valid moves vertically
    for r in range(8):
        if r != row:
            valid_moves.append(f'{chr(column + ord("A"))}{r + 1}')
    
    return valid_moves

def calculate_bishop_moves(position):
    column = ord(position[0].upper()) - ord('A')
    row = int(position[1]) - 1
    
    valid_moves = []
    
    # Calculate valid moves in the top-left direction
    c = column - 1
    r = row - 1
    while c >= 0 and r >= 0:
        valid_moves.append(f'{chr(c + ord("A"))}{r + 1}')
        c -= 1
        r -= 1
    
    # Calculate valid moves in the top-right direction
    c = column + 1
    r = row - 1
    while c < 8 and r >= 0:
        valid_moves.append(f'{chr(c + ord("A"))}{r + 1}')
        c += 1
        r -= 1
    
    # Calculate valid moves in the bottom-left direction
    c = column - 1
    r = row + 1
    while c >= 0 and r < 8:
        valid_moves.append(f'{chr(c + ord("A"))}{r + 1}')
        c -= 1
        r += 1
    
    # Calculate valid moves in the bottom-right direction
    c = column + 1
    r = row + 1
    while c < 8 and r < 8:
        valid_moves.append(f'{chr(c + ord("A"))}{r + 1}')
        c += 1
        r += 1
    
    return valid_moves

def calculate_queen_moves(position):
    rook_moves = calculate_rook_moves(position)
    bishop_moves = calculate_bishop_moves(position)
    
    valid_moves = rook_moves + bishop_moves
    
    return valid_moves
