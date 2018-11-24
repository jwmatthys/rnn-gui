# RNN-gui

A minimal python GUI to facilitate textgenrnn training and sampling.

Ice cream flavor and DnD datasets cloned from https://github.com/janelleshane.

For more extensive documentation, see textgenrnn: https://github.com/minimaxir/textgenrnn

## Installing dependencies

(Tested on Linux)
```
sudo apt-get install python3-pip python3-tk git
pip3 install tensorflow
pip3 install textgenrnn
git clone --recursive https://github.com/jwmatthys/rnn-gui
```

(See https://github.com/minimaxir/textgenrnn for information about installing GPU-enabled textgenrnn.)

## Running the GUI

RNN-gui and textgenrnn require Python3.

Open a terminal and run

```
cd rnn-gui
python3 rnn_gui.py
```

Outputs will appear in the terminal.

## Training a brand new model

Click "Choose dataset" and select a dataset file (usually a .txt or .csv file).

Click "Start with new model".

(optional) Choose a different name for your new model by changing the text in the "Save model as" textbox.

The "Train size" slider allows you to train on a portion of the full text rather than the entire file. The remaining portion of the text will be used for validation.

Choose the number of Epochs to train. One epoch is one full run through the dataset.

## Sampling from an already-trained model

To sample from the model you just trained, adjust the sampling options and click Generate.

If the Generate button is disabled, you do not have a currently loaded model.

To load a model, click "Load existing model" and open the directory that contains a trained model.

## Continue training an already-trained model

Click "Load existing model" and open the directory that contains a trained model.

Click "Choose dataset" to locate your dataset. You may continue on your original dataset, or transfer learning by selecting a different dataset to train your model on.

## Layers and bidirectionality

This tool uses only 128-cell networks, which generally work well for text. Increasing the number of layers may improve training accuracy but may also exponentially increase training time.

The "Bidirectional" option controls whether the recurrent neural network is bidirectional, that is, it processes the previous characters both forward and backward, which works great if text follows specific rules, like Shakespeare’s character headings).

## Line delimited and csv file options

If you are training on a text in which each line is a new entry (a list of ice cream flavors, for instance), check the "Line delimited" box. If your dataset is a csv (comma-separated value) textfile, check the "csv file" box.

## Train size

The "Train size" option determines what proportion of the original text will be used for training. Typically the portion not used for training would be used for validation; however, validation is disabled for this tool.

## Sequence length

The "Maximum sequence length" option determines the maximum number of characters for the network to use to predict the next character, which should be increased to let the network learn longer sequences, or decrease for shorter sequences.

## Word level mode

If you are training an extremely large text or want to train at the word level instead of the character level, check these boxes.

The Max Vocab setting is only used if you have enabled word level training and controls the number of unique words that will be used in sampling.

You are advised to significantly reduce the "Maximum sequence length" if you are doing word level training. 8 is a pretty good value.

## Buy me a coffee

If this code is useful to you, please consider buying me a coffee. https://ko-fi.com/D1D07KX5
