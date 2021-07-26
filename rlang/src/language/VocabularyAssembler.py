class VocabularyAssembler:
    # Parse through objects in vocab, maybe return a list of lmdp objects
    def parseVocab(self, vocab_json):
        modules = vocab_json['modules']
        vocabulary = vocab_json['vocabulary']
        print(modules)
        print(vocabulary)
