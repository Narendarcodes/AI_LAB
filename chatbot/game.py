from google import genai

# Initialize Gemini client (using your API key and model)
client = genai.Client(api_key="AQ.Ab8RN6KTpoZzfmR68T6q0lPHVhOfuIBaxnAOt4FGiy_Bm8Bryg")

def generate_maze_with_gemini(width=10, height=10):
    prompt = f"""
    Generate a {width}x{height} ASCII maze.
    Use '#' for walls, '.' for paths, 'P' for player start at (1,1),
    and 'E' for exit at bottom-right corner.
    Return only the maze grid, no explanation.
    """
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite-preview",   # ✅ keep your model
        contents=prompt
    )
    maze_text = response.text.strip().splitlines()
    maze = [list(row) for row in maze_text]
    return maze

def print_maze(maze):
    for row in maze:
        print("".join(row))

def move_player(maze, direction):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == "P":
                new_x, new_y = x, y
                if direction == "W": new_y -= 1
                elif direction == "S": new_y += 1
                elif direction == "A": new_x -= 1
                elif direction == "D": new_x += 1

                target = maze[new_y][new_x]

                if target == "#":
                    print("⚠️ Warning: You hit a wall!")
                elif target == ".":
                    maze[y][x] = "."
                    maze[new_y][new_x] = "P"
                elif target == "E":
                    maze[y][x] = "."
                    maze[new_y][new_x] = "P"
                    print_maze(maze)
                    print("🎉 Congratulations! You reached the exit and won!")
                    exit()  # End the game
                return

def play_game():
    maze = generate_maze_with_gemini(10, 10)
    while True:
        print_maze(maze)
        move = input("Move (W/A/S/D): ").upper()
        move_player(maze, move)

if __name__ == "__main__":
    play_game()
