"""
1) Extracts <div class = "comments"> tags in the data extracted from facebook.
2) Extracts the sentences
3) Transfers the sentences

"""

from __future__ import print_function
import csv
import os
import io
import time
import nltk.data
from bs4 import BeautifulSoup



def extract_data(input_file):
    """
    Extracts data from the input_file '../../timeline.htm'
    looks out <div class = "comment"> and extracts the following comment information
    Dumps the comments in to a file, checks whether file already exists.

    :param input_file: specify location of 'timeline.htm' (str)
    :param output_file: specify the output filename (str)
    :return: data
    """

    #opens file and closes, stores the file in output
    print("Reading {}...".format(input_file))
    t0 = time.time()
    with open(input_file,"r") as f:
        output = f.read()

    #Parse output string data using BeautifulSoup
    soup = BeautifulSoup(output, "lxml")
    extract_div = soup.find_all("div", {"class":"comment"})

    #Extract lines and write to csv file
    data = []
    for line in extract_div:
        data.append(line.text)

    t1 = time.time()
    print("It took {} ms to extract the comments".format((t1-t0)*1000))

    return data

def process_txt(data):
    """
    Processes the data extracted from the facebook comments
    Converts the raw string in the list from into sentences using nltk punkt module
    :param data: list of values from extract_data
    :return: list of sentences to feed into write_file
    """

    print("\nSplitting Sentences...")
    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    sentence = []
    i = 0

    for item in data:
        i += 1
        temp = []
        temp = sent_detector.tokenize(item)
        for stuff in temp:
            sentence.append(stuff)

    return sentence



def write_file(data, output_file = "FBextract.csv"):
    """
    Writes the file into
    :param data: list of sentences split and extracted from timeline.htm from the previous two functions
    :param output_file: str value to indicate file name "FBextract.csv" is default
    :return: None
    """

    #Check if file exists
    if not os.path.exists(output_file):
        with io.open(output_file,'wb') as fp:
            #To write sentence in new line to avoid weird conflicts with ; or ,
            a = csv.writer(fp, delimiter = '\n')
            #encode utf-8 to ascii for weird texts in the csv file
            a.writerow([s.encode('utf8') for s in data])
        return

    else:
        raise Exception("{0} already exists. Choose a different output file name...".format(output_file))


if __name__ == "__main__":
    fb_data = './Data/html/timeline.htm'
    extracted_data = extract_data(fb_data)
    processed_data = process_txt(extracted_data)
    write_file(extracted_data)



