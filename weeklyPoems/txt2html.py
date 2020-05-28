import sys

# Takes in txt file and makes new outputfile
fileToConvert = sys.argv[1]
newOutputFile = fileToConvert[:-4] + ".html"

# Open and create new html file
with open("./"+newOutputFile, "w") as htmlFile:
    htmlFile.write("<pre>\n")

    # Grab data from txt file to convert
    with open("./"+fileToConvert, "r") as txtFile:
        data = txtFile.read().splitlines()

    # Makes poem's title as the header
    htmlFile.write("<h2>" + data[0].strip() + "</h2>\n")

    # Adds poem's body
    for line in data[1:]:
        htmlFile.write(line + "\n")

    # End hmtl
    htmlFile.write("</pre>")
