import fileinput
import string
import re

lines=list()
for line in fileinput.FileInput("playlist.txt",inplace=1):
        if line.rstrip():
          line = re.sub("\d+", "", line)
          line = re.sub(":\n","",line)
          line = re.sub("NOW PLAYING\n","",line)
          line = re.sub("▶\n","",line)
          lines.append(line)

with open("playlist.txt", "w") as f:
      i = 0 
      j = 1
      for x in range(len(lines)//2):
        f.write(lines[i]+lines[j])
        i+=2
        j+=2
