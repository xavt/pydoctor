"""
This is a module demonstrating reST code documentation features.

Most part of this documentation is using Python type hinting.

:var v: 
        A description of the module variable v.
"""

def demo_fields_docstring_arguments(m, b):  # type: ignore
    """
    Fields are used to describe specific properties of a documented object.

    This function can be used in conjuction with L{demo_typing_arguments} to
    find an arbitrary function's zeros.

    :type  m: number
    :param m: The slope of the line.
    :type  b: number
    :param b: The y intercept of the line.
    :rtype:   number
    :return:  the x intercept of the line M{y=m*x+b}.
    """
    return -b/m

def demo_consolidated_fields(a:float, b):  # type: ignore
    """
    Fields can be condensed into one "consolidated" field. Looks better in plain text. 

    :Parameters:
        - `a`: The size of the fox (in meters)
        - `b`: The weight of the fox (in stones)
    :rtype: str
    :return: The number of foxes
    """
    return -b/a

def demo_typing_arguments(name: str, size: bytes) -> bool:
    """
    Type documentation can be extracted from standard Python type hints.

    :param name: The human readable name for something.
    :param size: How big the name should be.
    :return: Always `True`.
    """
    return True


def demo_cross_reference() -> None:
    r"""
    The inline markup construct ```object``` is used to create links to the documentation for other Python objects.
    'text' is the text that should be displayed for the link, and 'object' is the name of the Python object that should be linked to.

    If you wish to use the name of the Python object as the text for the link, you can simply write ```object``` -> `object`.

    - `demo_typing_arguments`
    """



class _PrivateClass:
    """
    This is the docstring of a private class.
    """

    def method_inside_private(self) -> bool:
        """
        A public method inside a private class.

        :return: Something.
        """
        return True


    def _private_inside_private(self) -> bool:
        """
        A private method inside a private class.

        :return: Something.
        """
        return True


class DemoClass:
    """
    This is the docstring of this class.

    :ivar v: 
        A description of the class instance variable v.
    :cvar cv: 
        A description of the static class variable v.
    :type v: 
        The type of the instance variable v. 
    """

    def __init__(self, one: str, two: bytes) -> None:
        """
        Documentation for class initialization.

        :param one: Docs for first argument.
        :param two: Docs for second argument.
        """

    @property
    def read_only(self) -> int:
        """
        This is a read-only property.
        """
        return 1

    @property
    def read_and_write(self) -> int:
        """
        This is a read-write property.
        """
        return 1

    @read_and_write.setter
    def read_and_write(self, value: int) -> None:
        """
        This is a docstring for setter.
        """

    @property
    def read_and_write_delete(self) -> int:
        """
        This is a read-write-delete property.
        """
        return 1

    @read_and_write_delete.setter
    def read_and_write_delete(self, value: int) -> None:
        """
        This is a docstring for setter.
        """

    @read_and_write_delete.deleter
    def read_and_write_delete(self) -> None:
        """
        This is a docstring for deleter.
        """
    
    def fields_demo(self) -> None: 
        """
        This docstring demonstrates a large variety of fields. 

        The same goes for Epytext fields. 

        This docstring includes fields that are not supported yet. 

        :param p: A description of the parameter p for a function or method.
        :type p: Type
        :return: 
            The return value for a function or method.
        :rtype: 
            The type of the return value for a function or method.
        :keyword p: 
            A description of the keyword parameter p.
        :raise e: 
            A description of the circumstances under which a function or method raises exception e. 
        :note: 
            A note about an object. Multiple note fields may be used to list separate notes.
        :since: 
            The date or version when an object was first introduced.
        :author: 
            The author(s) of an object. Multiple author fields may be used if an object has multiple authors.
        :warns UserWarning: if something.
        :yields: the ``dict``
        :param type p: 
            Not supported yet. Idem as ``:param:`` but with type specification inline (would work only if single word types)
        :group g: c1,...,cn
        :sort: c1,...,cn
        :attention: ...
            An important note about an object. Multiple attention fields may be used to list separate notes.
        :bug: 
            A description of a bug in an object. Multiple bug fields may be used to report separate bugs.
        :warning: 
            A warning about an object. Multiple warning fields may be used to report separate warnings.
        :version: 
            The current version of an object.
        :todo [ver]: 
            A planned change to an object. If the optional argument ver is given, then it specifies the version for which the change will be made. Multiple todo fields may be used if multiple changes are planned.
        :deprecated: 
            Indicates that an object is deprecated. The body of the field describe the reason why the object is deprecated.
        :status: 
            The current status of an object.
        :change: 
            A change log entry for this object.
        :permission: 
            The object access permission, for systems such Zope/Plone supporting this concept. It may be used more than once to specify multiple permissions
        :requires: 
            A requirement for using an object. Multiple requires fields may be used if an object has multiple requirements.
        :precondition: 
            A condition that must be true before an object is used. Multiple precondition fields may be used if an object has multiple preconditions.
        :postcondition: 
            A condition that is guaranteed to be true after an object is used. Multiple postcondition fields may be used if an object has multiple postconditions.
        :invariant: 
            A condition which should always be true for an object. Multiple invariant fields may be used if an object has multiple invariants. 
        :organization: 
            The organization that created or maintains an object.
        :copyright: 
            The copyright information for an object.
        :license: 
            The licensing information for an object.
        :contact: 
            Contact information for the author or maintainer of a module, class, function, or method. Multiple contact fields may be used if an object has multiple contacts. 
        """
        
