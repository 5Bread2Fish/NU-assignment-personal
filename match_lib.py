def match(pattern, source):
    """Attempt to match pattern to source. % matches a sequence of zero or
        more words and _ matches any single word.

    Args:
        pattern - a list of strings. % and/or _ are utilized as placeholder
                  to match/extract words from the source
        source - a list of string. A phrase/sentence/question represented as
                 a list of words (strings).

    Returns:
        if a match is detected, returns a list of strings - a list of matched
        words (words in the source corresponding to _'s or %'s, in the
        pattern, if any).
        else if no match is detected, returns None. 

    """
    #the following should pass tests
    #1 and 2
    sind=0
    pind=0
    result=[]

    if len(pattern) == len(source):
        while pind != len(pattern) or sind != len(source):
            #correspond to #5 on right
            if source[sind] == pattern[pind]:
                pind += 1
                sind += 1
            #correspond to #6 on right
            elif pattern[pind]=="_" or pattern[pind]== "%":
                result.append(source[sind])
                pind += 1
                sind += 1
            else:
                return None
        return result #empty list
    elif '_' in pattern or '%' in pattern: #_ != %, #compare, slice, join ''.join[0:2] # refer to 9_22_22.pdf page 8. pseudocode to crunch number10
        while pind != len(pattern):
            source.remove(pattern[pind])
            pind += 1
        return source
    else:
        return None