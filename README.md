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

Choose the number of Epochs to train. One epoch is one full run through the dataset.

## Sampling from an already-trained model

To sample from the model you just trained, adjust the sampling options and click Generate.

If the Generate button is disabled, you do not have a currently loaded model.

To load a model, click "Load existing model" and open the directory that contains a trained model.

## Continue training an already-trained model

Click "Load existing model" and open the directory that contains a trained model.

Click "Choose dataset" to locate your dataset. You may continue on your original dataset, or transfer learning by selecting a different dataset to train your model on.


## Word level and Large text mode:

If you are training a large text or want to train at the word level instead of the character level, check these boxes.

The Max Vocab setting is only used if you have enabled word level training.

## Buy me a coffee

If this code is useful to you, please consider buying me a coffee. https://ko-fi.com/D1D07KX5
