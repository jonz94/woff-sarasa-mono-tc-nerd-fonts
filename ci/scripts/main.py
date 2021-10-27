import os
from fontTools.ttLib import TTFont

workspace = os.environ.get(
    "GITHUB_WORKSPACE", os.environ.get("HOME") + "/repos/woff-ci"
)

print("workspace: " + workspace)

outputsDir = workspace + "/ci/outputs/"

directory = os.fsencode(outputsDir)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".ttf"):
        print("generating... " + filename.replace(".ttf", ".woff"))
        font = TTFont(outputsDir + filename)
        font.flavor = "woff"
        font.save(outputsDir + filename.replace(".ttf", ".woff"))
        font.close()
