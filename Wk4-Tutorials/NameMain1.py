
#def main():
#    print("First Module's Name: {}".format(__name__))

#if __name__ == '__main__':
#    main()      # so if this is imported by another file, it will not run
# ---
#if __name__ == '__main__':
#    print("Run Directly")
#else:
#    print("Run From Import")
#---
print("This will always be run")

def main():
    print("First Module's Main Method")

if __name__ == '__main__':
    main()
