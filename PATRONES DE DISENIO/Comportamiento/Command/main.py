from command import CopyCommand, PasteCommand
from invoker import Button
from receiver import TextEditor

def main():
    editor = TextEditor()
    copy_button = Button(CopyCommand(editor))
    paste_button = Button(PasteCommand(editor))

    copy_button.press()
    paste_button.press()

if __name__ == "__main__":
    main()