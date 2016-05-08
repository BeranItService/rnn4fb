"""
Collection of RNN functions to preprocess data
"""
from __future__ import print_function
import csv
import os
import nltk

class csvTools(object):
    def __init__ (self, csv_file,
                  unknown_token = "UNKNOWN_TOKEN",
                  sentence_start_token = "SENTENCE_START",
                  sentence_end_token = "SENTENCE_END"
                  ):
        """
        Load csv file in reader specify file path
        Tokenizes the sentences into word for RNN

        :param csv_file: file path of csv file to process (str)
        :param unknown_token: unknown token default "UNKNOWN_TOKEN" (str)
        :param sentence_start_token: start token for sentence default "SENTENCE_START" (str)
        :param sentence_end_token: end token for sentence default "<SENTENCE_END>" (str)
        :return:
        """
        self.csv_file = csv_file
        self.unknown_token = unknown_token
        self.sentence_start_token = sentence_start_token
        self.sentence_end_token = sentence_end_token

        self.sentences = []
        self.tokens = []

        assert os.path.exists(self.csv_file)
        assert self.csv_file[-3:] == "csv"

        # Load selected csv file and processes the sentences
        print("Loading {} ...".format(csv_file))
        with open(self.csv_file, mode = "rb") as f:
            self.reader = csv.reader(f)
            for i in self.reader:
                # In event of empty cells, to prevent IndexError
                if i != []:
                    i0 = i[0].decode("utf-8").lower()
                    self.sentences.append("%s %s %s" % (self.sentence_start_token, i0, self.sentence_end_token))

        # extract tokens
        self.tokens = [nltk.word_tokenize(x) for x in self.sentences]
        # flatten it out
        self.tokens = [item for sublist in self.tokens for item in sublist]

        #nltk frequency dist
        self.word_freq = nltk.probability.FreqDist(self.tokens)

    def num_sentence(self):
        """
        Gets the number of sentences
        :return: int
        """
        return len(self.sentences)

    def num_unique_words(self):
        """
        Gets the frequency of words, return number of unique word tokens
        :return: int
        """
        return len(self.word_freq.items())

    def most_used_words(self, n = 50):
        """
        Returns the most used word. n indicates number of top word displayed. By default, shows top 50 words.
        :param m: indicate the top __?__ words default 50 (int)
        :return: list of tuples
        """
        return self.word_freq.most_common(n)




if __name__ == "__main__":
    read_csv = csvTools("FBextract.csv")
    print("Total number of sentences: {}".format(read_csv.num_sentence()))
    print("Number of unique words: {}".format(read_csv.num_unique_words()))
    print("Most common words (ignore the tags):\n {}".format(read_csv.most_used_words(20)))
