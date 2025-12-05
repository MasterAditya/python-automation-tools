import os

folder = "files/"

for i, filename in enumerate(os.listdir(folder)):
    ext = filename.split(".")[-1]
    new_name = f"file_{i}.{ext}"
    os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))

print(f"Renamed {i+1} files in '{folder}'")
