'''copy a large picture file'''

# To work w/images, need to open files in binary mode (reading/writing bytes instead of text): (rb/wb)
with open('bronx.jpg', 'rb') as rf:
    with open('bronx_copy.jpg', 'wb') as wf:
        # for line in rf:
        #     wf.write(line)
# instead of doing this line by line, lets do it in specific chunk sizes:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
# make a while loop to work through
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
