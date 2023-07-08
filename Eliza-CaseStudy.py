letters = "abcdefghijklmnopqrstuvwxyzABCEDFGHIJKLMNOPQRSTUVWXYZ"

def is_variable(pattern):
    return (type(pattern) is str
            and pattern[0] == '?‘
            and len(pattern) > 1
            and pattern[1] != '*‘
            and pattern[1] in letters
            and ' ' not in pattern)
def match_variable(var, value, bindings):
    binding = bindings.get(var)
    if not binding:
        bindings.update({var: value})
        return bindings
        if value== bindings[var]:
            return bindings
            return False

def contains_tokens(pattern):
    return type(pattern) is list
    and len(pattern) > 0

def match_pattern(pattern, input, bindings=None):
    if bindings is False:
        return False
        if pattern == input:a
        return bindings
        bindings = bindings or {}
        if is_variable(pattern):
            var = pattern[1:]
            return match_variable(var, [input], bindings)
            elif contains_tokens(pattern) and contains_tokens(input):
            return match_pattern(pattern[1:],
                                 input[1:],
                                 match_pattern(pattern[0], input[0],bindings))
            else:
            return False


def match_seg(var, pattern, input, bindings, s=0):
    if not pattern:
       return match_var(var, input, bindings)
    word = pattern[0]
    try:
        pos = start + input[start:].index(word)
    except ValueError:
        return False
    ans1= match_var(var, input[:pos], bindings)
    match = match_pattern(pattern, input[pos:], ans1)
    if not match:
        return match_seg(var, pattern,input,bindings,s + 1)
    return match

def match_pattern(pattern, input, bindings=None):
    if bindings is False:
        return False
    if pattern == input:
        return bindings
    bindings = bindings or {}
    if is_variable(pattern):
        var = pattern[1:]
        return match_variable(var, [input], bindings)
   if is_segment(pattern):
       token = pattern[0]
       var = token[2:]
       return match_segment(var, pattern[1:], input, bindings)
    elif contains_tokens(pattern) and contains_tokens(input):
      return match_pattern(pattern[1:],   input[1:],    match_pattern(pattern[0], input[0], bindings))
    else:
        return False


def match_seg(var, pattern, input, bindings, s=0):
    if not pattern:
        return match_var(var, input, bindings)
        word = pattern[0]
        try:
            pos = start + input[start:].index(word)
            except ValueError:
            return False
            ans1= match_var(var, input[:pos], bindings)
            match = match_pattern(pattern, input[pos:], ans1)
            if not match:
                return match_seg(var, pattern,input,bindings,s + 1)    return match





