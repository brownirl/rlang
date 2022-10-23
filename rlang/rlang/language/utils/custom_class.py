from .language_exceptions import RLangSemanticError


def init_constructor(attrs_order_list):
    def init(self, *args, **kwargs):
        satisfied_args = list()
        for i in range(len(args)):
            self.__setattr__(attrs_order_list[i], args[i])
            satisfied_args.append(attrs_order_list[i])
        for k, v in kwargs.items():
            if k in satisfied_args:
                raise RLangSemanticError(f"Keyword argument '{k}' given despite arg list")
            self.__setattr__(k, v)
    return init


def object_class_constructor(name, bases, attrs_types_dict, attrs_order_list):
    def empty_attr_map(attr_class):
        if attr_class == list:
            return list()
        elif attr_class == set:
            return set()
        else:
            return None

    attrs = dict()

    for k, v in attrs_types_dict.items():
        attrs[k] = empty_attr_map(v)

    attrs['name'] = None
    attrs['attribute_types'] = attrs_types_dict

    attrs_order_list.insert(0, 'name')
    attrs['__init__'] = init_constructor(attrs_order_list)

    cls = type(name, bases, attrs)
    return cls
