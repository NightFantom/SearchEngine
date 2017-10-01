import pickle
from nltk import word_tokenize


class SearchEngine:
    def __init__(self, data_path):
        index = SearchEngine.load_obj(data_path + "indexes.pkl")
        self.__index = index
        stop_words = set()
        with open(data_path + "stop_words.txt") as f:
            line = f.readline().strip()
            while line != "":
                stop_words.add(line)
                line = f.readline().strip()
        self.__stop_words = stop_words

    def load_obj(name):
        with open(str(name), 'rb') as f:
            return pickle.load(f)

    def search(self, query):
        document_index_list = []
        for token in word_tokenize(query):
            if token in self.__stop_words:
                continue
            tok_doc_index_tuple = self.__index.get(token, None)
            if tok_doc_index_tuple is not None:
                document_index_list.append((token, tok_doc_index_tuple))

        result = []
        if len(document_index_list) > 0:
            doc_name_intersection = set(document_index_list[0][1].keys())
            for tok_doc_index_tuple in document_index_list:
                doc_name_intersection = doc_name_intersection & tok_doc_index_tuple[1].keys()

            rank_list = []

            for doc_name in doc_name_intersection:
                rank = 0
                position = []
                for tok_doc_index_tuple in document_index_list:
                    rank += tok_doc_index_tuple[1][doc_name]["TFIDF"]
                    position.append((tok_doc_index_tuple[0], tok_doc_index_tuple[1][doc_name]["pos"][0]))
                rank_list.append((doc_name, rank, position))

            result = sorted(rank_list, key=lambda r: -r[1])
        return result
