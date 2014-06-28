# Python imports
import operator
import time
from functools import wraps, partial

_py_hash = hash

# Constants
LIST_TYPES = (list, tuple, set)


def first(iterable, default=None):
    if not iterable:
        # Empty iterator (list)
        return default
    return iterable[0]


def rest(iterable):
    return iterable[1:]


def last(iterable):
    return iterable[-1]


def get(iterable, index, default=None):
    try:
        return iterable[index]
    except (IndexError, KeyError):
        return default


def next(iterable, value, n=1, default=None):
    if value in iterable:
        index = iterable.index(value)
        return get(iterable, index + n, default=default)
    return default


def prev(*args, **kwargs):
    kwargs['n'] = kwargs.get('n', 1) * -1
    return next(*args, **kwargs)


def chainable(method):
    @wraps(method)
    def f(self, *args, **kwargs):
        f(self, *args, **kwargs)
        return self
    f.is_chainable = True
    return f


def list_from_args(args):
    """
    Flatten list of args
    So as to accept either an array
    Or as many arguments
    For example:
    func(['x', 'y'])
    func('x', 'y')
    """
    # Empty args
    if not args:
        return []

    # Get argument type
    arg_type = type(args[0])
    is_list = arg_type in LIST_TYPES

    # Check that the arguments are uniforn (of same type)
    same_type = all([
        isinstance(arg, arg_type)
        for arg in args
    ])

    if not same_type:
        raise Exception('Expected uniform arguments of same type !')

    # Flatten iterables
    # ['x', 'y'], ...
    if is_list:
        args_lists = map(list, args)
        flattened_args = sum(args_lists, [])
        return flattened_args
    # Flatten set
    # 'x', 'y'
    return list(args)


# Decorator for list_from_args
def arglist(func):
    @wraps(func)
    def f(*args, **kwargs):
        args_list = list_from_args(args)
        return func(args_list, **kwargs)
    return f


# Decorator for methods
def arglist_method(func):
    @wraps(func)
    def f(self, *args, **kwargs):
        args_list = list_from_args(args)
        return func(self, args_list, **kwargs)
    return f


class Memoizer(object):
    def __init__(self, func):
        # Ugly hack but ...
        self.is_methodified = False
        self.orig_func = func
        self.func = func
        self.cache = {}
        self.class_obj = None

    def cache_key(self, args, kwargs):
        sorted_kwargs = kwargs.items()
        sorted_kwargs.sort()
        arg_tuple = (self.class_obj,) + args + tuple(sorted_kwargs)
        return hash(arg_tuple)

    def has_cache(self, cache_key):
        return cache_key in self.cache

    def get_cache(self, cache_key):
        return self.cache[cache_key]

    def set_cache(self, cache_key, value):
        self.cache[cache_key] = value

    def del_cache(self, cache_key):
        del self.cache[cache_key]

    def clear(self):
        self.cache = {}

    def __call__(self, *args, **kwargs):
        cache_key = self.cache_key(args, kwargs)
        if not self.has_cache(cache_key):
            value = self.func(*args, **kwargs)
            self.set_cache(cache_key, value)
        return self.get_cache(cache_key)

    def __get__(self, obj, objtype):
        """Support instance methods."""
        # Switch main object
        self.class_obj = obj
        self.func = partial(self.orig_func, obj)
        return self


class TimedMemoizer(Memoizer):
    def __init__(self, func, ttl):
        self.timestamps = {}
        self.ttl = ttl
        super(TimedMemoizer, self).__init__(func)

    def is_alive(self, cache_key):
        time_diff = time.time() - self.timestamps[cache_key]
        return time_diff < self.ttl

    def has_cache(self, cache_key):
        return super(TimedMemoizer, self).has_cache(cache_key) and self.is_alive(cache_key)

    def set_cache(self, cache_key, value):
        self.timestamps[cache_key] = time.time()
        return super(TimedMemoizer, self).set_cache(cache_key, value)

    def del_cache(self, cache_key):
        self.tinestamps[cache_key]
        return super(TimedMemoizer, self).del_cache(cache_key)

    def clear(self):
        self.timestamps = {}
        return super(TimedMemoizer, self).clear()


# Cache calls
def memoize(func):
    """Cache a functions output for a given set of arguments"""
    return Memoizer(func)


def timed_memoize(ttl):
    def wrapper(func):
        return wraps(func)(TimedMemoizer(func, ttl))
    return wrapper


def transform(transform_func):
    """Apply a transformation to a functions return value"""
    def decorator(func):
        @wraps(func)
        def f(*args, **kwargs):
            return transform_func(
                func(*args, **kwargs)
            )
        return f
    return decorator


def identity(x):
    return x


def hash_dict(obj):
    return _py_hash(
        tuple(
            obj.items()
        )
    )


def hash(obj):
    """Supports hashing dictionaires
    """
    if isinstance(obj, dict):
        return hash_dict(obj)
    return _py_hash(obj)


# Useful functions


def unique(collection, mapper=hash):
    return type(collection)(dict(
        (mapper(v), v)
        for v in collection
    ).values())


def true_only(iterable):
    return filter(bool, iterable)


def first_true(iterable):
    true_values = true_only(iterable)
    if true_values:
        return true_values[0]
    return None


def pluck_single(key, obj):
    if isinstance(obj, dict):
        return obj.get(key)
    return getattr(obj, key, None)


def pluck(collection, attribute_key):
    extractor = partial(pluck_single, attribute_key)
    return map(extractor, collection)


def subkey(dct, keys):
    """Get an entry from a dict of dicts by the list of keys to 'follow'
    """
    key = keys[0]
    if len(keys) == 1:
        return dct[key]
    return subkey(dct[key], keys[1:])


# Useful transforms
negate = transform(operator.not_)
uniquify = transform(unique)
