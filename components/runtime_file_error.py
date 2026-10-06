from utils.terminal import clear_screen, move_cursor, write


def runtime_file_error():
    clear_screen()
    move_cursor(1)
    write("BŁĄD APLIKACJI:")
    move_cursor(3)
    write("Pliki zostały zepsute podczas działania programu.")
    move_cursor(4)
    write("Dla bezpieczeństwa, uruchom aplikację ponownie. Wygeneruje ona pliki na nowo")
    move_cursor(5)
    write("(oraz, jesli będzie w stanie, kopie zapasowe")
    move_cursor(7)