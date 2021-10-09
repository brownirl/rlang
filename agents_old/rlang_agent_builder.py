from abc import abstractmethod


class RLangBuilderFactory:
    @abstractmethod
    def inform(self, rlang_program):
        '''
            returns all.preset.PresetBuilder
        '''
        pass
