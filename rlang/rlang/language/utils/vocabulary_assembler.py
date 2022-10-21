import importlib
import os


class VocabularyAssembler:
    def __init__(self, vocab_json):
        self.modules = {}
        self.lmdp_objects = {}
        self.state_size = None  # TODO: Replace this with a dataclass for MDP info (i.e. state size, dtype, etc.)

        self.import_modules(vocab_json)
        self.import_lmdp_objects(vocab_json)
        self.retrieve_state_size(vocab_json)

    def import_modules(self, vocab_json):
        if 'modules' not in vocab_json:
            return
        # Add grounding modules to self.modules
        modules_json = vocab_json['modules']
        modules = {}

        for mod_info in modules_json:
            mname = mod_info['module_name']
            fname = f"{os.getcwd()}/{mod_info['file_name']}"
            spec = importlib.util.spec_from_file_location(mname, fname)
            foo = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(foo)
            modules.update({mname: foo})

        self.modules = modules

    def import_lmdp_objects(self, vocab_json):
        if 'vocabulary' not in vocab_json:
            return
        # import the objects mentioned in vocabulary
        for k, v in vocab_json['vocabulary'].items():
            # print(f"Importing {function}")
            for var_info in v:
                grounding_info = var_info['grounding'].split('.')
                grounding_mod_name = grounding_info[0]
                grounding_var_name = grounding_info[1]
                grounding_mod = self.modules[grounding_mod_name]
                the_var = vars(grounding_mod)[grounding_var_name]
                self.lmdp_objects.update({var_info['name']: the_var})

    def retrieve_state_size(self, vocab_json):
        # TODO: This needs to see if state is actually a set or a vector. We'll limit to vectors of a single dimension
        self.state_size = vocab_json['mdp_metadata']['state_space']['size']
