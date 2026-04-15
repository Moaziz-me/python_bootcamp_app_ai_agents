# waiting_list = ["Ahmad", "Mahmood", "Maqsod"]
# waiting_list.sort(reverse=True)
#
# for index, item in enumerate(waiting_list, start=1):
#     waiting_list = (f"{index}. {item}")
#
# file = open("file/report.txt", "w")
# file2 = open("file/presentation.txt", "w")
# file.writelines(waiting_list)
# file2.writelines("""
# Hi there,
# My name is Mohammad Omar Aziz, I am a research student and my area of study
# focuses on AI and ESG.
#
# Thank you for your attention
# """)
# file3 = open("file/doc.txt", "w")
# file2.writelines("""
# IRAN war is creating a global economic crises!""")
#
# file2.close()
# file3.close()
# file.close()

content = ["All carrots are to be sliced longitudinally.", "The carrosts were reportedly sliced", "The sliced process were well presented."]

files = ["doc.txt", "presentation.txt", "report.txt"]

for content, files in zip(content, files):
    file = open(f"/Users/mohammadaziz/python_bootcamp/file/{files}", "w")
    file.write(content)
from pathlib import Path

file_path = Path("/Users/mohammadaziz/python_bootcamp/filereport.txt")

if file_path.exists():
    file_path.unlink()
else:
    print("File not found")


import os

folder_path = "/Users/mohammadaziz/python_bootcamp/"

for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        os.remove(os.path.join(folder_path, filename))

file = open("todos.txt", 'w')
file.close()
