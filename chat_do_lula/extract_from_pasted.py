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

statistics_per_person = {}

last_line = lines[0].strip()
for idx,line in enumerate(lines[1:]):
    line = line.strip()
    if line[:len(last_line)] == last_line:
        if line.count(' ') < 3:
            continue # Ignore lines with less than 4 words (3 spaces). Probably just someone's name
        name = last_line
        text = line[len(name):].strip()
        try:
            likes = int(lines[idx+2].strip()) # number of likes appear oh the next line
        except:
            likes = 0
        lula_chat.append((name, text, likes))

        if not name in statistics_per_person.keys():
            statistics_per_person[name] = {'total_likes':0, 'total_msgs':0}

        statistics_per_person[name]['total_msgs'] += 1
        statistics_per_person[name]['total_likes'] += likes

    last_line = line

# Save to csv format
with open("lula_chat.csv", "w") as f:
    #for line in lula_chat:
    f.write("sep=\t\n")
    f.write("Nome\tTexto\tLikes\n")
    for (name, text, likes) in lula_chat:
        f.write("%s\t%s\t%s\n" % (name, text, likes))


# save to html format
with open("lula_chat.html", "w") as f:
    f.write("<html><head></head><body><table>\n")
    for idx, (name, text, likes) in enumerate(lula_chat):
        #name, text, likes = line.split("\t")
        f.write("<tr><td>%d</td><td>%s</td><td>%s</td><td>%s</td></tr>\n" % (idx+1, name, text, likes))
    f.write("</table></body></html>\n")

# save statistics
stats_msgs = {}
stats_likes = {}
for name, data in statistics_per_person.iteritems():
    stats_msgs[name] = data['total_msgs']
    stats_likes[name] = data['total_likes']
stats_msgs = sorted(stats_msgs.items(), reverse=True, key=lambda kv: kv[1] )
stats_likes = sorted(stats_likes.items(), reverse=True, key=lambda kv: kv[1] )
with open("lula_chat_statistics.csv", "w") as f:
    f.write("sep=\t\n")
    f.write("Nome\tMensagens\t\tNome\tLikes\n")
    #for name, data in statistics_per_person.iteritems():
    for i in xrange(len(stats_msgs)):
        f.write("%s\t%s\t\t%s\t%s\n" % (stats_msgs[i][0], stats_msgs[i][1], stats_likes[i][0], stats_likes[i][1])) # data['total_msgs'], data['total_likes']))


print "Done!"

