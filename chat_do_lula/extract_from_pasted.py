#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      alex
#
# Created:     15/06/2019
# Copyright:   (c) alex 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

with open("pasted.txt") as f:
    lines = [x.strip() for x in f.readlines() if x.strip() != ""]

lula_chat = []

last_line = lines[0].strip()
for line in lines[1:]:
    line = line.strip()
    if line[:len(last_line)] == last_line:
        if line.count(' ') < 3:
            continue # Ignore lines with less than 4 words (3 spaces). Probably just someone's name
        name = last_line
        text = line[len(name):].strip()
        lula_chat.append(name + "\t" + text)
    last_line = line

with open("lula_chat.csv", "w") as f:
    for line in lula_chat:
        f.write("%s\n" % line)

with open("lula_chat.html", "w") as f:
    f.write("<head></head><body><table>\n")
    for line in lula_chat:
        name, text = line.split("\t")
        f.write("<tr><td>%s</td><td>%s</td></tr>\n" % (name, text))
    f.write("</table></body>\n")

print "Done!"

