import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import shutil
import threading
from textgenrnn import textgenrnn

exit_thread = False
exit_success = False


class RNNGui:

    __root = Tk()

    __thisWidth = 400
    __thisHeight = 600
    __thisDatasetPath = StringVar()
    __thisNumGen = IntVar()
    __thisNewModelName = StringVar()
    __thisPrefix = StringVar()
    __thisMaxGenLength = IntVar()
    __thisMaxWords = IntVar()
    __thisNewModel = BooleanVar()
    __thisWordLevel = BooleanVar()
    __thisLargeText = BooleanVar()

    #__thisDatasetButton = Button(__root, text="Choose dataset", bg="pink")
    __thisModelNameLabel = Label(__root, text="Model name")
    __thisModelName = Entry(__root)
    __thisNewModelCheckbox = Checkbutton(
        __root, text="New model", onvalue=True, offvalue=False, variable=__thisNewModel)
    __thisLargeTextCheckbox = Checkbutton(
        __root, text="Large text", onvalue=True, offvalue=False, variable=__thisLargeText)
    __thisWordLevelCheckbox = Checkbutton(
        __root, text="Word level", onvalue=True, offvalue=False, variable=__thisWordLevel)
    __thisModelSaveCheckbox = Checkbutton(
        __root, text="Save as new model?", onvalue=True, offvalue=False)
    __thisModelSaveName = Entry(__root)
    __thisModelName.insert(0, "mymodel")
    __thisNewModelCheckbox.select()
    __thisLargeTextCheckbox.deselect()
    __thisWordLevelCheckbox.deselect()
    __thisEpochLabel = Label(__root, text="Epochs to train")
    __thisNumEpochs = Scale(__root, from_=1, to=10, orient=HORIZONTAL)
    __thisNumEpochs.set(1)
    __thisTemperatureLabel = Label(__root, text="Temperature (creativity)")
    __thisTemperature = Scale(__root, from_=0, to=1,
                              resolution=0.01, orient=HORIZONTAL)
    __thisTemperature.set(0.5)
    __thisMaxGenLengthLabel = Label(__root, text="Max gen length")
    __thisMaxGenLength = Entry(__root)
    __thisMaxGenLength.insert(0, 1000)
    __thisMaxWordsLabel = Label(__root, text="Max Vocab")
    __thisMaxWords = Entry(__root)
    __thisMaxWords.insert(0, 2000)
    __thisPrefixLabel = Label(__root, text="Optional prefix")
    __thisPrefixEntry = Entry(__root)
    __thisNumGenLabel = Label(__root, text="Num to generate")
    __thisNumGenEntry = Entry(__root)
    __thisNumGenEntry.insert(0, 10)
    __thisTrainingLabel = Label(__root, text="\nTRAINING\n")
    __thisSamplingLabel = Label(__root, text="\nSAMPLING\n")
    # default window width and height
    __thisWidth = 640
    __thisHeight = 800
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)

    def __init__(self, **kwargs):

        # Set icon
        try:
            self.__root.wm_iconbitmap("RNNGui.ico")
        except:
            pass

        # Set window size (the default is 300x300)

        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass

        # Set the window text
        self.__root.title("textgenrnn gui")

        # Center the window
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        # For left-alling
        left = (screenWidth / 2) - (self.__thisWidth / 2)

        # For right-allign
        top = (screenHeight / 2) - (self.__thisHeight / 2)

        # For top and bottom
        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth,
                                              self.__thisHeight,
                                              left, top))

        self.__thisDatasetButton = Button(
            self.__root, text="Choose dataset", bg="pink", command=self.__setDatasetPath)
        self.__thisTrainButton = Button(
            self.__root, text="Train", bg="pink", command=self.__goTrain)
        self.__thisSampleButton = Button(
            self.__root, text="Sample!", bg="pink", command=self.__goSample)

        # To make the textarea auto resizable
        self.__thisTrainingLabel.grid(row=0, columnspan=2)
        self.__thisDatasetButton.grid(row=1, columnspan=2, pady=(10, 10))
        self.__thisModelNameLabel.grid(row=2)
        self.__thisModelName.grid(row=2, column=1)
        self.__thisNewModelCheckbox.grid(row=3)
        self.__thisLargeTextCheckbox.grid(row=4)
        self.__thisWordLevelCheckbox.grid(row=5)
        self.__thisModelSaveCheckbox.grid(row=6)
        self.__thisModelSaveName.grid(column=1, row=6)
        self.__thisEpochLabel.grid(row=7)
        self.__thisNumEpochs.grid(row=7, column=1)
        self.__thisMaxWordsLabel.grid(row=8)
        self.__thisMaxWords.grid(row=8, column=1)
        self.__thisTrainButton.grid(row=9, columnspan=2, pady=(10, 10))

        self.__thisSamplingLabel.grid(row=10, columnspan=2)
        self.__thisNumGenLabel.grid(row=11)
        self.__thisNumGenEntry.grid(row=11, column=1)
        self.__thisMaxGenLengthLabel.grid(row=12)
        self.__thisMaxGenLength.grid(row=12, column=1)
        self.__thisPrefixLabel.grid(row=13)
        self.__thisPrefixEntry.grid(row=13, column=1)
        self.__thisTemperatureLabel.grid(row=14)
        self.__thisTemperature.grid(row=14, column=1)
        self.__thisSampleButton.grid(row=15, columnspan=2, pady=(10, 10))
        # To make the textarea auto resizable
        #self.__root.grid_rowconfigure(99, weight=1)
        #self.__root.grid_columnconfigure(2, weight=1)

        # To open new file
        self.__thisFileMenu.add_command(label="New",
                                        command=self.__newFile)

        # To open a already existing file
        self.__thisFileMenu.add_command(label="Open",
                                        command=self.__openFile)

        # To save current file
        self.__thisFileMenu.add_command(label="Save",
                                        command=self.__saveFile)

        # To create a line in the dialog
        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label="Exit",
                                        command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="File",
                                       menu=self.__thisFileMenu)

        # To create a feature of description of the notepad
        self.__thisHelpMenu.add_command(label="About RNNGui",
                                        command=self.__showAbout)
        self.__thisMenuBar.add_cascade(label="Help",
                                       menu=self.__thisHelpMenu)

        self.__root.config(menu=self.__thisMenuBar)

    def __setDatasetPath(self):
        self.__thisDatasetPath = askopenfilename(defaultextension=".txt",
                                                 filetypes=[("All Files", "*.*"),
                                                            ("Text Documents",
                                                             "*.txt"),
                                                            ("CSV Text Documents", "*.csv")])
        if self.__thisDatasetPath == "":

            # no file to open
            self.__thisDatasetPath = None
        else:
            self.__root.title(os.path.basename(
                self.__thisDatasetPath) + " - RNNGui")

    def __goTrain(self):
        if self.__thisNewModel.get():
            my_model = textgenrnn()
        else:
            load_loc = os.path.join('weights', self.__thisModelName.get())
            weights_loc = os.path.join(load_loc,'textgenrnn_weights.hdf5')
            vocab_loc = os.path.join(load_loc,'textgenrnn_vocab.json')
            config_loc = os.path.join(load_loc,'textgenrnn_config.json')
            my_model = textgenrnn(weights_path=weights_loc, vocab_path=vocab_loc, config_path=config_loc)

        if self.__thisWordLevel.get():
            print('Using word-level mode.')
            my_model.train_from_file(self.__thisDatasetPath, num_epochs=self.__thisNumEpochs.get(
            ), new_model=True, word_level=True, max_words=int(self.__thisMaxWords.get()))
        elif self.__thisLargeText == True:
            print('Using large text mode.')
            my_model.train_from_largetext_file(
                self.__thisDatasetPath, num_epochs=self.__thisNumEpochs.get(), new_model=True)
        else:
            print('Beginning training.')
            my_model.train_from_file(self.__thisDatasetPath, num_epochs=self.__thisNumEpochs.get(), new_model=True)

        # save results before training in case user aborts
        save_dir = os.path.join('weights', save_name)
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)
        files = ['textgenrnn_weights.hdf5', 'textgenrnn_vocab.json', 'textgenrnn_config.json']
        for f in files:
            shutil.copy(f, save_dir)

    def __goSample(self):
        print ("Sample!\n")

    def __quitApplication(self):
        self.__root.destroy()
        # exit()

    def __showAbout(self):
        showinfo("RNNGui", "Mrinal Verma")

    def __openFile(self):

        self.__file = askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files", "*.*"),
                                                 ("Text Documents", "*.txt")])

        if self.__file == "":

            # no file to open
            self.__file = None
        else:

            # Try to open the file
            # set the window title
            self.__root.title(os.path.basename(self.__file) + " - RNNGui")
            self.__thisTextArea.delete(1.0, END)

            file = open(self.__file, "r")

            self.__thisTextArea.insert(1.0, file.read())

            file.close()

    def __newFile(self):
        self.__root.title("Untitled - RNNGui")
        self.__file = None
        self.__thisTextArea.delete(1.0, END)
        my_model = textgenrnn()
        my_model.train_from_file(
            "/home/jwmatthys/my_rnn/video_games.txt", num_epochs=2, new_model=True)

    def __saveFile(self):

        if self.__file == None:
            # Save as new file
            self.__file = asksaveasfilename(initialfile='Untitled.txt',
                                            defaultextension=".txt",
                                            filetypes=[("All Files", "*.*"),
                                                       ("Text Documents", "*.txt")])

            if self.__file == "":
                self.__file = None
            else:

                # Try to save the file
                file = open(self.__file, "w")
                #file.write(self.__thisTextArea.get(1.0, END))
                file.close()

                # Change the window title
                self.__root.title(os.path.basename(self.__file) + " - RNNGui")

        else:
            file = open(self.__file, "w")
            #file.write(self.__thisTextArea.get(1.0, END))
            file.close()

    def run(self):

        # Run main application
        self.__root.mainloop()


# Run main application
rnngui = RNNGui(width=360, height=600)
rnngui.run()
