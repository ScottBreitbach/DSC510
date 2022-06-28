'''open file with "w" parameter to enable "write"'''

fout = open('output.txt', 'w')
print(fout)

# Add text line to file
line1 = "This here's the wattle,\n"
fout.write(line1)

# Add another line to end
line2 = "the emblem of our land.\n"
fout.write(line2)

# Close to "save" and end
fout.close()
