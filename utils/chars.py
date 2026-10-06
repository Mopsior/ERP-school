horizontal_line = '─'
vertical_line = '│'
top_connector = '┴'
bottom_connector = '┬'
top_right = '┐'
top_left = "┌"
bottom_right = '┘'
bottom_left = '└'


start_invert = '\033[7m'
end_invert = '\033[27m'

def invert_text(content: str | None) -> str:
    if content is None: return ""
    return start_invert + content + end_invert