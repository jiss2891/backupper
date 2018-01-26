def bash_sanitize(in_str, extra_excluded=None):
    """
    Returns true if in_str is sanitized, false otherwise
    in_str could be an array of strings, in this case, returns
    false if any element is not sanitized, true otherwise.
    """
    if not isinstance(in_str, list):
        in_str = [in_str]

    # mezclo todas las cadenas
    in_str = ("{}" * len(in_str)).format(*in_str)

    # defino los caracteres que estan prohibidos
    excluded_chars = [';', '<', '>', '|']
    if extra_excluded:
        excluded_chars.extend(extra_excluded)

    return not (True in map(lambda x: x in excluded_chars, in_str))
