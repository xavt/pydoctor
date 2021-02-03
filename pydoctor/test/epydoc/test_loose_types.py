def test_rst_type_spec_convert_obj_tokens() -> None:

    convert_obj_tokens_cases = [
                ([("list", "obj"), ("(", "obj_delim"), ("int", "obj"), (")", "obj_delim")], 
                [(Tag('code', children=['list', '(', 'int', ')']), 'obj')]),    

                ([("list", "obj"), ("(", "obj_delim"), ("int", "obj"), (")", "obj_delim"), (", ", "obj_delim"), ("optional", "control")], 
                [(Tag('code', children=['list', '(', 'int', ')']), 'obj'), (", ", "obj_delim"), ("optional", "control")]),
                
            ] 

    ann = TypeDocstring("", 0)

    for tokens_types, expected_token_types in convert_obj_tokens_cases:

        assert str(ann._convert_obj_tokens(tokens_types, NotFoundLinker()))==str(expected_token_types)
