# apysc._jupyter.jupyter_util docstrings

## Module summary

The module that is implemented each Jupyter interface and definition. Mainly the following interfaces are defined: <br>・display_on_jupyter Save the overall HTML and display it on the Jupyter. <br>・display_on_colaboratory Save the overall HTML and display it on the Google Colaboratory.

## _save_overall_html function docstring

Save the overall HTML file.<hr>

**[Parameters]**

- `html_file_name`: str, default 'index.html'
  - The output HTML file name.
- `minify`: bool, default True
  - Boolean value whether minify a HTML or not.

## display_on_colaboratory function docstring

Save the overall HTML and display it on the Google Colaboratory.<hr>

**[Parameters]**

- `html_file_name`: str, default 'index.html'
  - The output HTML file name.
- `minify`: bool, default True
  - Boolean value whether minify a HTML or not. False setting is useful when debugging.

<hr>

**[References]**

- [display_on_colaboratory interface document](https://simon-ritchie.github.io/apysc/display_on_colaboratory.html)

## display_on_jupyter function docstring

Save the overall HTML and display it on the Jupyter.<hr>

**[Parameters]**

- `html_file_name`: str, default 'index.html'
  - The output HTML file name.
- `minify`: bool, default True
  - Boolean value whether minify a HTML or not. False setting is useful when debugging.

<hr>

**[Notes]**

Currently, this interface does not support Jupyter on the VS Code. This interface requires the Jupyter library (e.g., `notebook` package).<hr>

**[References]**

- [display_on_jupyter interface document](https://simon-ritchie.github.io/apysc/display_on_jupyter.html)

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