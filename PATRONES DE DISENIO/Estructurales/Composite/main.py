from leaf import File
from composite import Directory

def main():
    file1 = File("file1.txt")
    file2 = File("file2.txt")
    directory1 = Directory("directory1")

    directory1.add(file1)
    directory1.add(file2)

    directory1.show_details()

if __name__ == "__main__":
    main()