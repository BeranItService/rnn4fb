# rnn4fb
A RNN text generator that trains on Facebook posts.

Inspired by the RNN tutorial found on http://www.wildml.com/2015/09/recurrent-neural-networks-tutorial-part-1-introduction-to-rnns/

The tutorial is very well written check the page out. 

This project is broken into two parts:
1) Processing of raw data
2) Building of RNN structure and training the RNN


1. Processing of raw data
Before you can do anything fancy with the data, you need to get the data and make it usable.
I didn't come up with any fancy schmanzy way of mining data from facebook. To get a copy of
your own personal posts from facebook, goto settings>general>Download a copy of your Facebook data
A link will be sent to the email linked to your facebook account. Download the zipped file and unzip
to a location. In fb2csv.py, specify the location of timeline.htm file. The file will extract text
written and extract it to a csv file. The timeline.htm file is found in /html folder. Once this is 
accomplished, you will have a .csv file with sentences split into separate rows.
