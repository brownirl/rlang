from typing import Callable
from rlang.src.grounding.knowledge_grounding import Grounding
from rlang.src.grounding.utils.domain import Domain


class GroundingFunction(Grounding):
    """
        Grounded Function Specification Class
            - Represents function specification, with a given domain-codomain,
            in the form of a function by parts.
            - Implemented as Pairs of (boolean expressions, function).
        author: Rafael Rodriguez-Sanchez (rrs@brown.edu), Benjamin Spiegel
        (bspiegel@cs.brown.edu)
        date: January 2021, August 2021

        ...

        Attributes
        ----------
        says_str : str
            a formatted string to print out what the animal says
        name : str
            the name of the animal
        sound : str
            the sound that the animal makes
        num_legs : int
            the number of legs the animal has (default 4)

        Methods
        -------
        says(sound=None)
            Prints the animals name and what sound it makes
        """

    def __init__(self, domain: Domain, codomain: Domain, function: Callable, name: str = None):
        super().__init__(name)
        self._domain = domain
        self._codomain = codomain
        self._function = function

    def __call__(self, *args, **kwargs):
        return self._function(*args, **kwargs)
