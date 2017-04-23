"""Miscellaneous functions.
"""
import json
import os

from fnmatch import fnmatch
from timeit import default_timer

# logcalls() appears first in this file, so that it can be used to decorate
# other functions below
def logcalls(options='args/return/timer'): #---------------------------------<<<
    """Decorator to log (to console) information about calls to a function.

    options = string containing various options, delimited by /:
              'args' (default) - show arguments passed to function
              'args=pprint' - pretty-print the passed arguments
              'args=no' or 'args=off' - don't show arguments
              'return' (default) - show value returned by function
              'return=type' - only show the return value's type/size
              'return=pprint' - pretty-print the returned value
              'return=no' or 'return=off' - don't show returned value
              'timer' (default) - show elapsed time for wrapped function
              'timer=no' or 'timer=off' - don't show elapsed time

    Note that because we're passing an optional argument to the decorator, you
    must include the parenthese - @logcalls() - even if no options are passed.
    To log all calls to function funcname:
        @logcalls()
        def funcname(...):
            ...
    """
    # parse options string into an option dictionary
    option = dict()
    for option_string in options.lower().split('/'):
        if '=' in option_string:
            key, val = option_string.split('=')
            option[key] = val
        else:
            option[option_string] = ''

    def outer_wrapper(func):
        # use functools to preserve wrapped function metadata (for debugging)
        @functools.wraps(func)
        def inner_wrapper(*args, **kwargs):

            # display the wrapped function
            print((' ' + func.__name__ + '(): ').center(80, '-'))

            # display passed arguments
            if option.get('args', None) == 'pprint':
                print('arguments:')
                print(pprint.pprint(args))
                print(pprint.pprint(kwargs))
            elif option.get('args', None) in ['no', 'off']:
                pass # do nothing
            else:
                print('arguments: ' + str(args) + ', ' + str(kwargs))

            if not option.get('timer', None) in ['no', 'off']:
                start_seconds = default_timer()

            # call the wrapped function
            return_value = func(*args, **kwargs)

            if not option.get('timer', None) in ['no', 'off']:
                elapsed_msg = ' elapsed: {0:.3f} seconds '. \
                    format(default_timer() - start_seconds)
                print(40*' ' + elapsed_msg.center(40, '-'))

            # display the returned value
            returned_size = len(str(return_value))
            if option.get('return', None) == 'type':
                print('returned: ' + str(type(return_value)) +
                      ', size = {0} bytes'.format(returned_size))
            elif option.get('return', None) == 'pprint':
                print('returned:')
                print(str(pprint.pprint(return_value)))
            elif option.get('return', None) in ['no', 'off']:
                pass # do nothing
            else:
                print('returned: ' + str(return_value)) # default behavior

            return return_value
        return inner_wrapper
    return outer_wrapper

def bytecount(numbytes): #---------------------------------------------------<<<
    """Convert byte count to display string as bytes, KB, MB or GB.

    1st parameter = # bytes (may be negative)
    Returns a short string version, such as '17 bytes' or '47.6 GB'
    """
    retval = '-' if numbytes < 0 else '' # leading '-' for negative values
    absvalue = abs(numbytes)
    if absvalue < 1024:
        retval = retval + format(absvalue, '.0f') + ' bytes'
    elif 1024 <= absvalue < 1024*100:
        retval = retval + format(absvalue/1024, '0.1f') + ' KB'
    elif 1024*100 <= absvalue < 1024*1024:
        retval = retval + format(absvalue/1024, '.0f') + ' KB'
    elif 1024*1024 <= absvalue < 1024*1024*100:
        retval = retval + format(absvalue/(1024*1024), '0.1f') + ' MB'
    elif 1024*1024*100 <= absvalue < 1024*1024*1024:
        retval = retval + format(absvalue/(1024*1024), '.0f') + ' MB'
    else:
        retval = retval + format(absvalue/(1024*1024*1024), ',.1f') + ' GB'
    return retval

def photo_list(albumno): #---------------------------------------------------<<<
    """Return list of photos for specified album.
    Return list contains tuples of (photono, filename, location, caption)
    """
    photodata = json.loads(open('static/json/photos.json').read())
    photolist = []
    for photono in photodata:
        if photodata[photono]['albumno'] == albumno:
            photolist.append((photono,
                              photodata[photono]['filename'],
                              photodata[photono]['location'],
                              photodata[photono]['caption']))
    return sorted(photolist, key=lambda _: _[1].upper()) # sort by filename

def sub_dir(searchfor, folder=None): #---------------------------------------<<<
    """Find all occurrences of files matching a specified search pattern, in
    the specified file and its subfolders.

    searchfor = filename pattern to match (for example, '*.py')
    folder = top-level folder to be searched (default is current folder)

    Returns a list of matches."""
    if not folder:
        folder = os.getcwd()
    print(folder)
    hits = []
    for path, _, files in os.walk(folder):
        for name in files:
            if fnmatch(name, searchfor):
                hits.append(os.path.join(path, name))
    return hits

