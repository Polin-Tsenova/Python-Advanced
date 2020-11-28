with open('text.txt', 'w') as file:
    file.write("-I was quick to judge him, but it wasn't his fault.\n")
    file.write("-Is this some kind of joke?! Is it?\n")
    file.write("-Quick, hide here. It is safer.\n")

with open('text.txt', 'r') as file:
    with open('output.txt', 'w') as new_file:
        for idx, line in enumerate(file):
            punctiation_marks = 0
            letters = 0
            for chr in line:
                if chr.isalpha():
                    letters += 1
                for el in ".,!?-'":
                    if chr == el:
                        punctiation_marks += 1
            new_file.write(f"Line {idx + 1}: {line[:-2]} ({letters})({punctiation_marks})\n")
