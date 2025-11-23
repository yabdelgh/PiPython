def ft_filter(func, iter):
    if func is None:
        return [x for x in iter if x]
    return [x for x in iter if func(x)]


ft_filter.__doc__ = "filter(function or None, iterable) --> filter object \n\n\
\rReturn an iterator yielding those items of iterable for which \n\
\rfunction(item) is true. If function is None, return the items that are true."
