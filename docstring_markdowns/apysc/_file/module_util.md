# apysc._file.module_util docstrings

## Module summary

Module related common utilities. Mainly following interfaces are defined: <br>・get_module_paths_recursively <br> ・Get all module paths under the specified directory. <br>・save_tmp_module <br> ・Save a temporary Python module. <br>・save_tmp_module_and_run_script <br> ・Save a temporary Python module and run that script. <br>・read_target_path_module <br> ・Read a module of the specified module path. <br>・read_module_or_class_from_package_path <br> ・Read a specified package path module or class.

## get_module_paths_recursively function docstring

Get all module paths under the specified directory.<hr>

**[Parameters]**

- `dir_path`: str
  - Directory path to search modules.
- `module_paths`: list of str or None
  - Current Python module paths (only used by recursive function calls).

<hr>

**[Returns]**

- `module_paths`: list of str
  - Python module paths. `__init__.py` modules will not be included.

## read_module_or_class_from_package_path function docstring

Read a specified package path module or class.<hr>

**[Parameters]**

- `module_or_class_package_path`: str
  - Target package module or class path.

<hr>

**[Returns]**

- `module_or_class`: ModuleType or Type
  - Read module or class.

## read_target_path_module function docstring

Read a module of the specified module path.<hr>

**[Parameters]**

- `module_path`: str
  - Target module path.

<hr>

**[Returns]**

- `module`: ModuleType
  - Read module.

## save_tmp_module function docstring

Save a temporary Python module.<hr>

**[Parameters]**

- `script`: str
  - Python script string.

<hr>

**[Returns]**

- `saved_module_path`: str
  - Saved temporary module path.

## save_tmp_module_and_run_script function docstring

Save a temporary Python module and run that script.<hr>

**[Parameters]**

- `script`: str
  - Python script string.

<hr>

**[Returns]**

- `stdout`: str
  - Result stdout string.

## List class docstring



### __add__ method docstring

Return self+value.

### GenericMeta method docstring

Metaclass for generic types. This is a metaclass for typing.Generic and generic ABCs defined in typing module. User defined subclasses of GenericMeta can override __new__ and invoke super().__new__. Note that GenericMeta.__new__ has strict rules on what is allowed in its bases argument: * plain Generic is disallowed in bases; * Generic[...] should appear in bases at most once; * if Generic[...] is present, then it should list all type variables that appear in other bases. In addition, type of all generic bases is erased, e.g., C[int] is stripped to plain C.

### __contains__ method docstring

Return key in self.

### __delitem__ method docstring

Delete self[key].

### list method docstring

list() -> new empty list list(iterable) -> new list initialized from iterable's items

### __getitem__ method docstring

x.__getitem__(y) <==> x[y]

### __iadd__ method docstring

Implement self+=value.

### __imul__ method docstring

Implement self*=value.

### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

### __iter__ method docstring

Implement iter(self).

### __len__ method docstring

Return len(self).

### __mul__ method docstring

Return self*value.

### object method docstring

The most base type

### __reversed__ method docstring

L.__reversed__() -- return a reverse iterator over the list

### __rmul__ method docstring

Return value*self.

### __setitem__ method docstring

Set self[key] to value.

### __sizeof__ method docstring

L.__sizeof__() -- size of L in memory, in bytes

### append method docstring

L.append(object) -> None -- append object to end

### clear method docstring

L.clear() -> None -- remove all items from L

### copy method docstring

L.copy() -> list -- a shallow copy of L

### count method docstring

L.count(value) -> integer -- return number of occurrences of value

### extend method docstring

L.extend(iterable) -> None -- extend list by appending elements from the iterable

### index method docstring

L.index(value, [start, [stop]]) -> integer -- return first index of value. Raises ValueError if the value is not present.

### insert method docstring

L.insert(index, object) -- insert object before index

### pop method docstring

L.pop([index]) -> item -- remove and return item at index (default last). Raises IndexError if list is empty or index is out of range.

### remove method docstring

L.remove(value) -> None -- remove first occurrence of value. Raises ValueError if the value is not present.

### reverse method docstring

L.reverse() -- reverse *IN PLACE*

### sort method docstring

L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*

## module class docstring

module(name[, doc]) Create a module object. The name must be a string; the optional doc argument can have any type.

module(name[, doc]) Create a module object. The name must be a string; the optional doc argument can have any type.

### __dir__ method docstring

__dir__() -> list specialized dir() implementation

### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

## datetime class docstring

datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]]) The year, month and day arguments are required. tzinfo may be None, or an instance of a tzinfo subclass. The remaining arguments may be ints.

datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]]) The year, month and day arguments are required. tzinfo may be None, or an instance of a tzinfo subclass. The remaining arguments may be ints.

### __add__ method docstring

Return self+value.

### __format__ method docstring

Formats self with strftime.

### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

### __radd__ method docstring

Return value+self.

### __reduce__ method docstring

__reduce__() -> (cls, state)

### __reduce_ex__ method docstring

__reduce_ex__(proto) -> (cls, state)

### __rsub__ method docstring

Return value-self.

### __sub__ method docstring

Return self-value.

### astimezone method docstring

tz -> convert to local time in new timezone tz

### combine method docstring

date, time -> datetime with same date and time fields

### ctime method docstring

Return ctime() style string.

### date method docstring

Return date object with same year, month and day.

### dst method docstring

Return self.tzinfo.dst(self).

### fromordinal method docstring

int -> date corresponding to a proleptic Gregorian ordinal.

### fromtimestamp method docstring

timestamp[, tz] -> tz's local time from POSIX timestamp.

### isocalendar method docstring

Return a 3-tuple containing ISO year, week number, and weekday.

### isoformat method docstring

[sep] -> string in ISO 8601 format, YYYY-MM-DDT[HH[:MM[:SS[.mmm[uuu]]]]][+HH:MM]. sep is used to separate the year from the time, and defaults to 'T'. timespec specifies what components of the time to include (allowed values are 'auto', 'hours', 'minutes', 'seconds', 'milliseconds', and 'microseconds').

### isoweekday method docstring

Return the day of the week represented by the date. Monday == 1 ... Sunday == 7

### now method docstring

Returns new datetime object representing current time local to tz. tz Timezone object. If no tz is specified, uses local timezone.

### replace method docstring

Return datetime with new specified fields.

### strftime method docstring

format -> strftime() style string.

### strptime method docstring

string, format -> new datetime parsed from a string (like time.strptime()).

### time method docstring

Return time object with same time but with tzinfo=None.

### timestamp method docstring

Return POSIX timestamp as float.

### timetuple method docstring

Return time tuple, compatible with time.localtime().

### timetz method docstring

Return time object with same time and tzinfo.

### today method docstring

Current date or datetime: same as self.__class__.fromtimestamp(time.time()).

### toordinal method docstring

Return proleptic Gregorian ordinal. January 1 of year 1 is day 1.

### tzname method docstring

Return self.tzinfo.tzname(self).

### utcfromtimestamp method docstring

Construct a naive UTC datetime from a POSIX timestamp.

### utcnow method docstring

Return a new datetime representing UTC day and time.

### utcoffset method docstring

Return self.tzinfo.utcoffset(self).

### utctimetuple method docstring

Return UTC time tuple, compatible with time.localtime().

### weekday method docstring

Return the day of the week represented by the date. Monday == 0 ... Sunday == 6