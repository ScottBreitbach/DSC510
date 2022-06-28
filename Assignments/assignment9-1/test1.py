import re

def process_line(line):

    print('line test: good job')

def main():
    nameFile = input('pick a file name: ')
    fileName = nameFile + '.txt'
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if regex.search(fileName) == None:
        try:
            with open(fileName, 'w') as output_file:    # creates output file
                pass
        except Exception as e:
            print('Error:', e)
            exit()
        else:
            try:
                gba_file = open('gettysburg.txt', 'r')
                for line in gba_file:
                    process_line(line)          # processes each line of text file
            except:
                print('Error: File could not be opened.')
                exit()
                gba_file.close()
            output_file.close()
    else:
        print('Special characters [@_!#$%^&*()<>?/\|}{~:] not accepted.\n'
              'Please try again.')
    with open(fileName, 'w')
    print('<Insert Length of dict here>')
    # process_file(wordCounts)
    # pretty_print(wordCounts)            # print results

if __name__ == "__main__":
    main()
