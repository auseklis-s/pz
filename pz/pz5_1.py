# С помощью функций получить вертикальную и горизонтальную линии. Линия
# проводится многократной печатью символа. Заключить слово в рамку из
# полученных линий.
def create_horizontal_line(length, symbol):
    return symbol * length

def create_vertical_line(height, symbol):
    return '\n'.join(symbol for i in range(height))

def create_frame(word, horizontal_line, vertical_line):
    frame_top = f"{horizontal_line}\n"
    frame_middle = f"{vertical_line} {word} {vertical_line}\n"
    frame_bottom = f"{horizontal_line}"
    return frame_top + frame_middle + frame_bottom

word = "как дела?"
symbol_lines = "="

horizontal_line = create_horizontal_line(len(word) + 5, symbol_lines)
vertical_line = create_vertical_line(2, symbol_lines)

framed_word = create_frame(word, horizontal_line, vertical_line)
print(framed_word)
