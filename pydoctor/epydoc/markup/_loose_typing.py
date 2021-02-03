"""Type pre-processing"""

from collections import deque
import re
import ast
from typing import Callable, Deque, Dict, Iterator, List, Mapping, Optional, Tuple, Union
from pydoctor.epydoc.markup import DocstringLinker, ParseError, ParsedDocstring
from pydoctor.epydoc.markup import epytext
from pydoctor.napoleon.iterators import peek_iter
import docutils.nodes
from twisted.web.template import Tag

def epytext2docutils(element: epytext.Element) -> docutils.nodes.Node:
    ...




    # def _convert_obj_tokens_to_stan(self, docstring_linker: DocstringLinker) -> List[Tuple[Union[str, Tag], str]]:
    #     """
    #     Convert "obj" and "obj_delim" type to L{Tag} objects, merge them together. Leave the rest untouched. 

    #     Exemple:

    #     >>> ann._tokens = [("list", "obj"), ("(", "obj_delim"), ("int", "obj"), (")", "obj_delim")]
    #     >>> ann._convert_obj_tokens_to_stan(NotFoundLinker())
    #     ... [(Tag('code', children=['list', '(', 'int', ')']), 'obj')]
        
    #     @param types: List of tuples: C{(token, type)}
    #     """

    #     combined_tokens: List[Tuple[Union[str, Tag], str]] = []

    #     open_parenthesis = 0
    #     open_square_braces = 0

    #     for _token, _type in self._tokens:

    #         if _type == "obj":
    #             new_token = docstring_linker.link_xref(_token, _token, self._lineno)
    #             if open_square_braces + open_parenthesis > 0:
    #                 try: last_processed_token = combined_tokens[-1]
    #                 except IndexError: 
    #                     # weird
    #                     combined_tokens.append((_token, _type))
    #                 else:
    #                     if last_processed_token[1] == "obj" and isinstance(last_processed_token[0], Tag):
    #                         # Merge with last Tag
    #                         last_processed_token[0](*new_token.children)
    #                     else:
    #                         # weird
    #                         combined_tokens.append((new_token, _type))
    #             else:
    #                 combined_tokens.append((new_token, _type))

    #         elif _type == "obj_delim": 
    #             if _token == "[": open_square_braces += 1
    #             elif _token == "(": open_parenthesis += 1

    #             if open_square_braces + open_parenthesis > 0:
    #                 try: last_processed_token = combined_tokens[-1]
    #                 except IndexError: 
    #                     # weird
    #                     combined_tokens.append((_token, _type))
    #                 else:
    #                     if last_processed_token[1] == "obj" and isinstance(last_processed_token[0], Tag): 
    #                         # Merge with last Tag
    #                         last_processed_token[0](_token)
    #                     else:
    #                         # weird
    #                         combined_tokens.append((_token, _type))
    #             else:
    #                 combined_tokens.append((_token, _type))

    #             if _token == "]": open_square_braces -= 1
    #             elif _token == ")": open_parenthesis -= 1
    #         else:
    #             combined_tokens.append((_token, _type))

    #     if open_parenthesis != 0: #TODO: test
    #         self._warnings.append(ParseError("unbalanced parenthesis in type expression", linenum=self._lineno, is_fatal=False))
    #     if open_square_braces != 0:
    #         self._warnings.append(ParseError("unbalanced square braces in type expression", linenum=self._lineno, is_fatal=False))

    #     return combined_tokens

    # def _convert_type_spec_to_stan(self, docstring_linker:DocstringLinker) -> Tag:
    #     """
    #     Convert type to L{Tag} object.
    #     """

    #     tokens = self._convert_obj_tokens_to_stan(docstring_linker)

    #     _warnings: List[ParseError] = []

    #     converters: Dict[str, Callable[[Union[str, Tag]], Union[str, Tag]]] = {
    #         "literal":      lambda _token: Tag('span')(class_="literal")(_token),
    #         "control":      lambda _token: Tag('em')(_token),
    #         "delimiter":    lambda _token: Tag('span')(_token), 
    #         "reference":    lambda _token: self.parse_docstring(_token, _warnings).to_stan(docstring_linker), 
    #         "default":      lambda _token: self.parse_docstring(_token, _warnings).to_stan(docstring_linker), 
    #         "obj":          lambda _token: _token, # These convertions are done in _convert_obj_tokens_to_stan()
    #         "obj_delim":    lambda _token: _token, 
    #     }

    #     for w in _warnings:
    #         self._warnings.append(ParseError(w.descr(), self._lineno, is_fatal=False))

    #     converted = Tag('span')

    #     for token, type_ in tokens:
    #         converted_token = converters[type_](token)
    #         converted(converted_token)

    #     return converted
    

        # @classmethod
    # def _tokenize_node_type_spec(cls, spec: docutils.nodes.document):
        
    #     class Tokenizer(docutils.nodes.GenericNodeVisitor):
            
    #         def __init__(self, document: docutils.nodes.document):
    #             super().__init__(document)
    #             self.tokens = []
    #             self.rest = docutils.nodes.document

    #         def default_visit(self, node:docutils.nodes.Node):
    #             # Tokenize only the first level text, pass the rest as is
    #             #  root doc        para or list 
    #             if node.parent and node.parent.parent:
    #                 if isinstance(node.parent.parent, docutils.nodes.document):
    #                     # only text in paragraph nodes are taken into account
    #                     if isinstance(node.parent, docutils.nodes.paragraph):  
    #                         if isinstance(node, docutils.nodes.Text):
    #                             # Tokenize
    #                             self.tokens.extend(cls._tokenize_type_spec(node.astext()))
    #                             # # Remove the text from the tree.
    #                             # node.parent.remove(node)
    #                         else:
    #                             self.tokens.append(node)
    #                             raise docutils.nodes.SkipNode()
    #                     else:
    #                         self.tokens.append(node.parent)
    #                         raise docutils.nodes.SkipNode()
        
    #     tokenizer = Tokenizer(spec)
    #     spec.walk(tokenizer)
    #     return tokenizer.tokens
