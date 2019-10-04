from pathlib import Path

path = Path()
for file in path.glob("*"):
    print(file)

path1 = Path("eccomerce")
print(path.exists())