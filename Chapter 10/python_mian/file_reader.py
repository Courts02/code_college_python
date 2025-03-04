from pathlib import Path


path = Path('my_name.txt')
contents = path.read_text()
print(contents)

lines = contents.splitlines()
for line in lines:
    print(line)

new_path = Path("new_file.txt")
new_path.write_text("hey hey")
with new_path.open('a') as file:
    file.write("\nThe sun dipped below the horizon, casting a golden glow over the quiet town. Emma stood by the old oak tree, her fingers brushing the bark as memories flooded back. It had been years since she left, but the familiar scent of pine and earth still felt like home. She had promised herself she would never return, yet here she was, standing at the place where everything began. A soft breeze rust/")

read = new_path.read_text()
print(read)