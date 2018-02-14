def bash_sanitize(in_str, extra_excluded=None):
    """
    Returns true if in_str is sanitized, false otherwise
    in_str could be an array of strings, in this case, returns
    false if any element is not sanitized, true otherwise.
    """
    if not isinstance(in_str, list):
        in_str = [in_str]

    # mezclo todas las cadenas
    container_string = u"{}" * len(in_str)
    in_str = container_string.format(*in_str)

    # defino los caracteres que estan prohibidos
    excluded_chars = [';', '<', '>', '|']
    if extra_excluded:
        excluded_chars.extend(extra_excluded)

    matches = []
    for exc in excluded_chars:
        if exc in in_str:
            matches.append(exc)


    import ipdb; ipdb.set_trace()
    if len(matches):
        matches = ", ".join(matches)
        return (False, matches)
    else:
        return (True, None)
