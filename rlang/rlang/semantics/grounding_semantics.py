class ProbabilisticFunction(GroundingFunction):
    """Represents a function that provides stochastic output.

    """

    def __init__(self, probability: float = 1.0, *args, **kwargs):
        self._probability = probability
        super().__init__(*args, **kwargs)

    @property
    def probability(self):
        return self._probability

    @probability.setter
    def probability(self, probability: float):
        self._probability = probability

    def compose_probability(self, probability: float):
        self._probability = self._probability * probability


class ProbabilityDistribution(MutableMapping):
    """
    
    """

    def __init__(self, distribution=None):
        if distribution is None:
            distribution = dict()
        # for function, v in distribution.items():
        #     if v < 0.0 or v > 1.0:
        #         raise RLangGroundingError(f"Must be bounded between 0.0 and 1.0, got {v}")

        self.domain = Domain.ANY
        self.distribution = distribution
        self.rng = default_rng()
        self.update_metadata()
        self.arg_store = list()
        self.kwarg_store = dict()
        self.true_distribution = dict()
        self.calculated = False

    def calculate_true_distribution(self):
        pass

    @classmethod
    def from_single(cls, k, *args, **kwargs):
        return cls({k: 1.0})

    @classmethod
    def from_list_eq(cls, ks, *args, **kwargs):
        sd_dict = dict()
        for k in ks:
            sd_dict[k] = 1.0
        return cls(sd_dict)

    def update_metadata(self):
        self.calculate_domain()

    def calculate_domain(self):
        self.domain = Domain.ANY
        for k, v in self.distribution.items():
            self.domain += k.domain

    def sample(self):
        random_variable = self.rng.uniform()
        offset = 0.0
        for k, v in self.true_distribution.items():
            offset += v
            if random_variable < offset:
                return k

    def join(self, new_distribution):
        for k, v in new_distribution.items():
            if k in self.distribution:
                self.distribution[k] += v
            else:
                self.distribution[k] = v
                self.domain += k.domain

    def compose_probabilities(self, probability):
        for k, v in self.distribution.items():
            self.distribution[k] = v * probability

    def __call__(self, *args, **kwargs):
        self.arg_store = args
        self.kwarg_store = kwargs
        self.calculate_true_distribution()
        return self

    def __getitem__(self, key: Grounding):
        if self.calculated:
            return self.true_distribution[key]
        else:
            return self.distribution[key]

    def __setitem__(self, key: Grounding, value: float):
        self.distribution[key] = value
        self.update_metadata()

    def __delitem__(self, key: Grounding):
        del self.distribution[key]
        self.update_metadata()

    def __iter__(self):
        if self.calculated:
            return iter(self.true_distribution)
        else:
            return iter(self.distribution)

    def __repr__(self):
        if self.calculated:
            return str(self.true_distribution)
        else:
            return str(self.distribution)

    def __len__(self):
        if self.calculated:
            return len(self.true_distribution)
        else:
            return len(self.distribution)

    def __hash__(self):
        return hash(frozenset(self))


class ActionDistribution(ProbabilityDistribution):
    """Represents a distribution of possible next actions, options, or policies

    Args:
        distribution: a dictionary of the form {Action/Option/Policy: probability,}

    
    """

    def calculate_true_distribution(self):
        # TODO: Might be able to change all isinstance(k__, Action) calls to isinstance(k__, PrimitiveGrounding)
        def update_dictionary(k_, v_):
            if isinstance(k_, (dict, ProbabilityDistribution)):
                for k__, v__ in k_.items():
                    if isinstance(k__, Action):
                        update_dictionary(k__, v_ * v__)
                    else:
                        update_dictionary(k__(*self.arg_store, **self.kwarg_store), v_ * v__)
            elif k_ is not None:
                if isinstance(k_, Action):
                    a = k_
                else:
                    a = Action(k_)
                if a in true_distribution:
                    true_distribution[a] += v_
                else:
                    true_distribution[a] = v_

        true_distribution = dict()
        update_dictionary(self.distribution, 1.0)
        self.true_distribution = true_distribution
        self.calculated = True


class StateDistribution(ProbabilityDistribution):
    def __init__(self, distribution=None):
        if distribution:
            pass
            # ensure that everything is a State or function of state or something
        super().__init__(distribution=distribution)

    def calculate_true_distribution(self):
        def update_dictionary(k_, v_):
            if isinstance(k_, (dict, ProbabilityDistribution)):
                for k__, v__ in k_.items():
                    if isinstance(k__, (VectorState, ObjectOrientedState)):
                        update_dictionary(k__, v_ * v__)
                    else:
                        update_dictionary(k__(*self.arg_store, **self.kwarg_store), v_ * v__)
            elif k_ is not None:
                if isinstance(k_, (VectorState, ObjectOrientedState)):
                    a = k_
                else:
                    a = VectorState(k_)
                if a in true_distribution:
                    true_distribution[a] += v_
                else:
                    true_distribution[a] = v_

        true_distribution = dict()
        update_dictionary(self.distribution, 1.0)
        self.true_distribution = true_distribution
        self.calculated = True


class RewardDistribution(ProbabilityDistribution):
    def __init__(self, distribution=None):
        if distribution:
            pass
            # ensure that everything is a Reward or something
        super().__init__(distribution=distribution)

    def calculate_true_distribution(self):
        def update_dictionary(k_, v_):
            if isinstance(k_, (dict, ProbabilityDistribution)):
                for k__, v__ in k_.items():
                    if isinstance(k__, Primitive):
                        update_dictionary(k__, v_ * v__)
                    else:
                        update_dictionary(k__(*self.arg_store, **self.kwarg_store), v_ * v__)
            elif k_ is not None:
                if isinstance(k_, Primitive):
                    a = k_
                else:
                    a = Primitive(k_)
                if a in true_distribution:
                    true_distribution[a] += v_
                else:
                    true_distribution[a] = v_

        true_distribution = dict()
        update_dictionary(self.distribution, 1.0)

        # print(true_distribution.keys())

        self.true_distribution = true_distribution
        self.calculated = True

    def expected(self):
        expected_reward = 0.0
        for k, v in self.true_distribution.items():
            expected_reward += k * v

        return expected_reward

    @classmethod
    def from_list_eq(cls, ks, *args, **kwargs):
        numeric_reward = 0.0
        sd_dict = dict()
        for k in ks:
            if isinstance(k, int):
                numeric_reward += k
            else:
                if k in sd_dict:
                    sd_dict[k] += 1.0
                else:
                    sd_dict[k] = 1.0
        # sd_dict[RewardFunction(lambda *args, **kwargs: numeric_reward, domain=Domain.ANY)] = 1.0
        return cls(sd_dict)

    def __call__(self, *args, **kwargs):
        super().__call__(*args, **kwargs)
        return self.expected()


class GroundingDistribution(ProbabilityDistribution):
    def __init__(self, grounding: Grounding, distribution=None, complete=False):
        if distribution:
            pass
            # ensure that everything is a groundingfunction or something
        self.grounding = grounding
        self.complete = complete
        super().__init__(distribution=distribution)

    def calculate_true_distribution(self):
        def update_dictionary(k_, v_):
            if isinstance(k_, (dict, ProbabilityDistribution)):
                for k__, v__ in k_.items():
                    if isinstance(k__, (Primitive, MDPObject)):
                        update_dictionary(k__, v_ * v__)
                    else:
                        update_dictionary(k__(*self.arg_store, **self.kwarg_store), v_ * v__)
            elif k_ is not None:
                if isinstance(k_, (Primitive, MDPObject)):
                    a = k_
                else:
                    a = Primitive(k_)
                if a in true_distribution:
                    true_distribution[a] += v_
                else:
                    true_distribution[a] = v_

        true_distribution = dict()
        update_dictionary(self.distribution, 1.0)
        self.true_distribution = true_distribution
        self.calculated = True

    @classmethod
    def from_list_eq(cls, ks, *args, **kwargs):
        sd_dict = dict()
        for k in ks:
            sd_dict[k] = 1.0
        return cls(args[0], sd_dict)
    

# class QuantifierSpecification:
#     def __init__(self, cls, quantifier, dot_exp=None):
#         self.cls = cls
#         self.quantifier = quantifier
#         self.dot_exp = dot_exp
#         self.name = f"{self.quantifier} {self.cls.__name__}"

#     def __repr__(self):
#         return f"<QuantifierSpecification {self.name}{'.'.join(self.dot_exp) if self.dot_exp else ''}>"



class ParameterizedActionExecution(GroundingFunction):
    def __init__(self, parameterized_action, arguments: List[GroundingFunction]):
        self.parameterized_action = parameterized_action
        self.arguments = arguments

        domain = Domain.ANY
        for arg in arguments:
            domain = domain + arg.domain

        argnames = ", ".join([arg.name if arg.name is not None else "unk" for arg in arguments])

        super().__init__(domain=domain, codomain=Domain.ACTION,
                         function=lambda *args, **kwargs:
                         parameterized_action(*[arg(*args, **kwargs) for arg in self.arguments], **kwargs),
                         name=parameterized_action.name + "(" + argnames + ")")

class PredicateEvaluation(GroundingFunction):
    def __init__(self, predicate, arguments: List[GroundingFunction]):
        self.parameterized_action = predicate
        self.arguments = arguments

        domain = Domain.ANY
        for arg in arguments:
            if isinstance(arg, GroundingFunction):
                domain = domain + arg.domain

        argnames = ", ".join([arg.name if arg.name is not None else "unk" for arg in arguments])

        super().__init__(domain=domain, codomain=Domain.REAL_VALUE+Domain.BOOLEAN,
                         function=lambda *args, **kwargs:
                         predicate(*[arg(*args, **kwargs) for arg in self.arguments], **kwargs),
                         name=predicate.name + "(" + argnames + ")")

class ActionReference(GroundingFunction):
    """Represents a reference to a specified action."""

    def __init__(self, action: Any, name=None):
        """
        Args:
            action: the action.
            name (optional): name of the action.

        """
        if isinstance(action, (int, float, list)):
            function = lambda *sargs, **skwargs: Action(np.array(action))
            domain = Domain.ANY
        elif isinstance(action, GroundingFunction):
            function = action.__call__
            domain = action.domain
        else:
            raise RLangGroundingError(f"Actions cannot be of type {type(action)}")
        super().__init__(domain=domain, codomain=Domain.ACTION, function=function, name=name)

    def __hash__(self):
        return hash(self.function)

    def __repr__(self):
        if self.name:
            return f"<ActionReference \"{self.name}\">"
        else:
            return f"<ActionReference>"
        
class ParameterizedAction:
    def __init__(self, function, name=None):
        self.function = function
        self.name = name if name else function.__name__

    def __call__(self, *args, **kwargs):
        return self.function(*args, **kwargs)
