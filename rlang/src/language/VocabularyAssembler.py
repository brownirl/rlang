import importlib
import os


class VocabularyAssembler:
    def __init__(self, vocab_json):
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
        self.lmdp_objects = {}

        # import the objects mentioned in vocabulary
        for k, v in vocab_json['vocabulary'].items():
            # print(f"Importing {k}")
            for var_info in v:
                grounding_info = var_info['grounding'].split('.')
                grounding_mod_name = grounding_info[0]
                grounding_var_name = grounding_info[1]
                grounding_mod = self.modules[grounding_mod_name]
                the_var = vars(grounding_mod)[grounding_var_name]
                self.lmdp_objects.update({var_info['name']: the_var})
