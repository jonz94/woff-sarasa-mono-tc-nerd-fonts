import os
from fontTools.ttLib import TTFont


def generate_font(outputsDir, filename, flavor):
    print("generating... " + filename.replace("ttf", flavor))
    font = TTFont(outputsDir + filename)
    font.flavor = flavor
    font.save(outputsDir + filename.replace("ttf", flavor))
    font.close()


def main():
    workspace = os.environ.get("GITHUB_WORKSPACE") or os.path.abspath(__file__).replace(
        "/ci/scripts/main.py", ""
    )

    outputsDir = workspace + "/ci/outputs/"

    for file in os.listdir(os.fsencode(outputsDir)):
        filename = os.fsdecode(file)
        if filename.endswith(".ttf"):
            generate_font(outputsDir, filename, "woff")


if __name__ == "__main__":
    main()
