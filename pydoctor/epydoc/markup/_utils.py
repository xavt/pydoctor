
from typing import Iterable, Iterator, List, Optional, Sequence, Union, cast
from . import Field, epytext
from docutils import nodes
from docutils.utils import new_document
from twisted.web.template import Tag

def epytext2docutils(element: epytext.Element) -> nodes.Node:
    converter = Epytext2DocutilsConverter(element)
    return converter.to_node()

class Epytext2DocutilsConverter(epytext.ParsedEpytextDocstring):
    
    def __init__(self, body: Optional[epytext.Element]):
        super().__init__(body, ())
        self._node: Optional[nodes.document] = None

    def to_node(self) -> nodes.document:
        if self._node is not None:
            return self._node
        else:
            self._node = new_document('epytext')
        if self._tree is not None:
            self._node.extend(self._to_node(self._tree))
        return self._node


    def _to_node(self,
            tree: Union[epytext.Element, str],
            seclevel: int = 0
            ) -> Iterable[nodes.Node]:
        if isinstance(tree, str):
            return [nodes.Text(tree)]

        if tree.tag == 'section':
            seclevel += 1

        # Process the children first.
        variables: List[nodes.Node] = []
        for c in tree.children:
            variables.extend(self._to_node(c, seclevel))

        # Perform the approriate action for the DOM tree type.
        if tree.tag == 'para':
            if tree.attribs.get('inline'):
                return [nodes.inline('', '', *variables)]
            else: 
                return [nodes.paragraph('', '', *variables)]
        elif tree.tag == 'code':
            return [nodes.literal('', '', *variables)]
        elif tree.tag == 'uri':
            label, target = variables
            return [nodes.reference(
                    '', label, internal=False, refuri=target)]
        elif tree.tag == 'link':
            label, target = variables
            return [nodes.title_reference(
                    '', label, internal=False, refuri=target)]
        elif tree.tag == 'target':
            value, = variables
            return [value]
        elif tree.tag == 'italic':
            return [nodes.emphasis('', '', *variables)]
        elif tree.tag == 'math':
            node = nodes.math('', '', *variables)
            node.set_class('math')
            return [node]
        elif tree.tag == 'bold':
            return [nodes.strong('', '', *variables)]
        elif tree.tag == 'ulist':
            return [nodes.bullet_list('', *variables)]
        elif tree.tag == 'olist':
            return [nodes.enumerated_list('', *variables)]
        elif tree.tag == 'li':
            return [nodes.list_item('', *variables)]
        elif tree.tag == 'heading':
            return [nodes.title('', '', *variables)]
        elif tree.tag == 'literalblock':
            return [nodes.literal_block('', '', *variables)]
        elif tree.tag == 'doctestblock':
            return [nodes.doctest_block(tree.children[0], tree.children[0])]
        elif tree.tag in ('fieldlist', 'tag', 'arg'):
            raise AssertionError("There should not be any field lists left")
        elif tree.tag in ('epytext', 'section', 'name'):
            return variables
        elif tree.tag == 'symbol':
            symbol = cast(str, tree.children[0])
            char = chr(self.SYMBOL_TO_CODEPOINT[symbol])
            return [nodes.inline('', '', char)]
        else:
            raise AssertionError(f"Unknown epytext DOM element {tree.tag!r}")
