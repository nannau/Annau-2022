# Borrowed from https://stackoverflow.com/questions/6169217/replace-console-output-in-python
def progress_bar(current, total, bar_length=20):
    fraction = (current + 1) / total

    arrow = int(fraction * bar_length - 1) * '-' + '>'
    padding = int(bar_length - len(arrow)) * ' '

    ending = '\n' if current == total else '\r'

    print(f'Progress: [{arrow}{padding}] {int(fraction*100)}%', end=ending)