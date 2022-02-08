# apysc._console.loggers docstrings

## Module summary

Definitions and interface for loggers.

## getLogger function docstring

Return a logger with the specified name, creating it if necessary. If no name is specified, return the root logger.

## get_info_logger function docstring

Get information logger.<hr>

**[Returns]**

- `logger`: Logger
  - Information logger as following settings. - Level: INFO - Format: `%Y-%m-%d %H:%M:%S. <message>`

## Formatter class docstring

Formatter instances are used to convert a LogRecord to text. Formatters need to know how a LogRecord is constructed. They are responsible for converting a LogRecord to (usually) a string which can be interpreted by either a human or an external system. The base Formatter allows a formatting string to be specified. If none is supplied, the the style-dependent default value, "%(message)s", "{message}", or "${message}", is used. The Formatter can be initialized with a format string which makes use of knowledge of the LogRecord attributes - e.g. the default value mentioned above makes use of the fact that the user's message and arguments are pre- formatted into a LogRecord's message attribute. Currently, the useful attributes in a LogRecord are described by: %(name)s Name of the logger (logging channel) %(levelno)s Numeric logging level for the message (DEBUG, INFO, WARNING, ERROR, CRITICAL) %(levelname)s Text logging level for the message ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL") %(pathname)s Full pathname of the source file where the logging call was issued (if available) %(filename)s Filename portion of pathname %(module)s Module (name portion of filename) %(lineno)d Source line number where the logging call was issued (if available) %(funcName)s Function name %(created)f Time when the LogRecord was created (time.time() return value) %(asctime)s Textual time when the LogRecord was created %(msecs)d Millisecond portion of the creation time %(relativeCreated)d Time in milliseconds when the LogRecord was created, relative to the time the logging module was loaded (typically at application startup time) %(thread)d Thread ID (if available) %(threadName)s Thread name (if available) %(process)d Process ID (if available) %(message)s The result of record.getMessage(), computed just as the record is emitted

Formatter instances are used to convert a LogRecord to text. Formatters need to know how a LogRecord is constructed. They are responsible for converting a LogRecord to (usually) a string which can be interpreted by either a human or an external system. The base Formatter allows a formatting string to be specified. If none is supplied, the the style-dependent default value, "%(message)s", "{message}", or "${message}", is used. The Formatter can be initialized with a format string which makes use of knowledge of the LogRecord attributes - e.g. the default value mentioned above makes use of the fact that the user's message and arguments are pre- formatted into a LogRecord's message attribute. Currently, the useful attributes in a LogRecord are described by: %(name)s Name of the logger (logging channel) %(levelno)s Numeric logging level for the message (DEBUG, INFO, WARNING, ERROR, CRITICAL) %(levelname)s Text logging level for the message ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL") %(pathname)s Full pathname of the source file where the logging call was issued (if available) %(filename)s Filename portion of pathname %(module)s Module (name portion of filename) %(lineno)d Source line number where the logging call was issued (if available) %(funcName)s Function name %(created)f Time when the LogRecord was created (time.time() return value) %(asctime)s Textual time when the LogRecord was created %(msecs)d Millisecond portion of the creation time %(relativeCreated)d Time in milliseconds when the LogRecord was created, relative to the time the logging module was loaded (typically at application startup time) %(thread)d Thread ID (if available) %(threadName)s Thread name (if available) %(process)d Process ID (if available) %(message)s The result of record.getMessage(), computed just as the record is emitted

### __init__ method docstring

Initialize the formatter with specified format strings. Initialize the formatter either with the specified format string, or a default as described above. Allow for specialized date formatting with the optional datefmt argument. If datefmt is omitted, you get an ISO8601-like (or RFC 3339-like) format. Use a style parameter of '%', '{' or '$' to specify that you want to use one of %-formatting, :meth:`str.format` (``{}``) formatting or :class:`string.Template` formatting in your format string. .. versionchanged:: 3.2 Added the ``style`` parameter.

### localtime method docstring

localtime([seconds]) -> (tm_year,tm_mon,tm_mday,tm_hour,tm_min, tm_sec,tm_wday,tm_yday,tm_isdst) Convert seconds since the Epoch to a time tuple expressing local time. When 'seconds' is not passed in, convert the current time instead.

### format method docstring

Format the specified record as text. The record's attribute dictionary is used as the operand to a string formatting operation which yields the returned string. Before formatting the dictionary, a couple of preparatory steps are carried out. The message attribute of the record is computed using LogRecord.getMessage(). If the formatting string uses the time (as determined by a call to usesTime(), formatTime() is called to format the event time. If there is exception information, it is formatted using formatException() and appended to the message.

### formatException method docstring

Format and return the specified exception information as a string. This default implementation just uses traceback.print_exception()

### formatStack method docstring

This method is provided as an extension point for specialized formatting of stack information. The input data is a string as returned from a call to :func:`traceback.print_stack`, but with the last trailing newline removed. The base implementation just returns the value passed in.

### formatTime method docstring

Return the creation time of the specified LogRecord as formatted text. This method should be called from format() by a formatter which wants to make use of a formatted time. This method can be overridden in formatters to provide for any specific requirement, but the basic behaviour is as follows: if datefmt (a string) is specified, it is used with time.strftime() to format the creation time of the record. Otherwise, an ISO8601-like (or RFC 3339-like) format is used. The resulting string is returned. This function uses a user-configurable function to convert the creation time to a tuple. By default, time.localtime() is used; to change this for a particular formatter instance, set the 'converter' attribute to a function with the same signature as time.localtime() or time.gmtime(). To change it for all formatters, for example if you want all logging times to be shown in GMT, set the 'converter' attribute in the Formatter class.

### usesTime method docstring

Check if the format uses the creation time of the record.

## Logger class docstring

Instances of the Logger class represent a single logging channel. A "logging channel" indicates an area of an application. Exactly how an "area" is defined is up to the application developer. Since an application can have any number of areas, logging channels are identified by a unique string. Application areas can be nested (e.g. an area of "input processing" might include sub-areas "read CSV files", "read XLS files" and "read Gnumeric files"). To cater for this natural nesting, channel names are organized into a namespace hierarchy where levels are separated by periods, much like the Java or Python package namespace. So in the instance given above, channel names might be "input" for the upper level, and "input.csv", "input.xls" and "input.gnu" for the sub-levels. There is no arbitrary limit to the depth of nesting.

Instances of the Logger class represent a single logging channel. A "logging channel" indicates an area of an application. Exactly how an "area" is defined is up to the application developer. Since an application can have any number of areas, logging channels are identified by a unique string. Application areas can be nested (e.g. an area of "input processing" might include sub-areas "read CSV files", "read XLS files" and "read Gnumeric files"). To cater for this natural nesting, channel names are organized into a namespace hierarchy where levels are separated by periods, much like the Java or Python package namespace. So in the instance given above, channel names might be "input" for the upper level, and "input.csv", "input.xls" and "input.gnu" for the sub-levels. There is no arbitrary limit to the depth of nesting.

### __init__ method docstring

Initialize the logger with a name and an optional level.

### _log method docstring

Low-level logging routine which creates a LogRecord and then calls all the handlers of this logger to handle the record.

### addFilter method docstring

Add the specified filter to this handler.

### addHandler method docstring

Add the specified handler to this logger.

### callHandlers method docstring

Pass a record to all relevant handlers. Loop through all handlers for this logger and its parents in the logger hierarchy. If no handler was found, output a one-off error message to sys.stderr. Stop searching up the hierarchy whenever a logger with the "propagate" attribute set to zero is found - that will be the last logger whose handlers are called.

### critical method docstring

Log 'msg % args' with severity 'CRITICAL'. To pass exception information, use the keyword argument exc_info with a true value, e.g. logger.critical("Houston, we have a %s", "major disaster", exc_info=1)

### debug method docstring

Log 'msg % args' with severity 'DEBUG'. To pass exception information, use the keyword argument exc_info with a true value, e.g. logger.debug("Houston, we have a %s", "thorny problem", exc_info=1)

### error method docstring

Log 'msg % args' with severity 'ERROR'. To pass exception information, use the keyword argument exc_info with a true value, e.g. logger.error("Houston, we have a %s", "major problem", exc_info=1)

### exception method docstring

Convenience method for logging an ERROR with exception information.

### critical method docstring

Log 'msg % args' with severity 'CRITICAL'. To pass exception information, use the keyword argument exc_info with a true value, e.g. logger.critical("Houston, we have a %s", "major disaster", exc_info=1)

### filter method docstring

Determine if a record is loggable by consulting all the filters. The default is to allow the record to be logged; any filter can veto this and the record is then dropped. Returns a zero value if a record is to be dropped, else non-zero. .. versionchanged:: 3.2 Allow filters to be just callables.

### findCaller method docstring

Find the stack frame of the caller so that we can note the source file name, line number and function name.

### getChild method docstring

Get a logger which is a descendant to this one. This is a convenience method, such that logging.getLogger('abc').getChild('def.ghi') is the same as logging.getLogger('abc.def.ghi') It's useful, for example, when the parent logger is named using __name__ rather than a literal string.

### getEffectiveLevel method docstring

Get the effective level for this logger. Loop through this logger and its parents in the logger hierarchy, looking for a non-zero logging level. Return the first one found.

### handle method docstring

Call the handlers for the specified record. This method is used for unpickled records received from a socket, as well as those created locally. Logger-level filtering is applied.

### hasHandlers method docstring

See if this logger has any handlers configured. Loop through all handlers for this logger and its parents in the logger hierarchy. Return True if a handler was found, else False. Stop searching up the hierarchy whenever a logger with the "propagate" attribute set to zero is found - that will be the last logger which is checked for the existence of handlers.

### info method docstring

Log 'msg % args' with severity 'INFO'. To pass exception information, use the keyword argument exc_info with a true value, e.g. logger.info("Houston, we have a %s", "interesting problem", exc_info=1)

### isEnabledFor method docstring

Is this logger enabled for level 'level'?

### log method docstring

Log 'msg % args' with the integer severity 'level'. To pass exception information, use the keyword argument exc_info with a true value, e.g. logger.log(level, "We have a %s", "mysterious problem", exc_info=1)

### makeRecord method docstring

A factory method which can be overridden in subclasses to create specialized LogRecords.

### removeFilter method docstring

Remove the specified filter from this handler.

### removeHandler method docstring

Remove the specified handler from this logger.

### setLevel method docstring

Set the logging level of this logger. level must be an int or a str.

### warning method docstring

Log 'msg % args' with severity 'WARNING'. To pass exception information, use the keyword argument exc_info with a true value, e.g. logger.warning("Houston, we have a %s", "bit of a problem", exc_info=1)

## StreamHandler class docstring

A handler class which writes logging records, appropriately formatted, to a stream. Note that this class does not close the stream, as sys.stdout or sys.stderr may be used.

A handler class which writes logging records, appropriately formatted, to a stream. Note that this class does not close the stream, as sys.stdout or sys.stderr may be used.

### __init__ method docstring

Initialize the handler. If stream is not specified, sys.stderr is used.

### acquire method docstring

Acquire the I/O thread lock.

### addFilter method docstring

Add the specified filter to this handler.

### close method docstring

Tidy up any resources used by the handler. This version removes the handler from an internal map of handlers, _handlers, which is used for handler lookup by name. Subclasses should ensure that this gets called from overridden close() methods.

### createLock method docstring

Acquire a thread lock for serializing access to the underlying I/O.

### emit method docstring

Emit a record. If a formatter is specified, it is used to format the record. The record is then written to the stream with a trailing newline. If exception information is present, it is formatted using traceback.print_exception and appended to the stream. If the stream has an 'encoding' attribute, it is used to determine how to do the output to the stream.

### filter method docstring

Determine if a record is loggable by consulting all the filters. The default is to allow the record to be logged; any filter can veto this and the record is then dropped. Returns a zero value if a record is to be dropped, else non-zero. .. versionchanged:: 3.2 Allow filters to be just callables.

### flush method docstring

Flushes the stream.

### format method docstring

Format the specified record. If a formatter is set, use it. Otherwise, use the default formatter for the module.

### handle method docstring

Conditionally emit the specified logging record. Emission depends on filters which may have been added to the handler. Wrap the actual emission of the record with acquisition/release of the I/O thread lock. Returns whether the filter passed the record for emission.

### handleError method docstring

Handle errors which occur during an emit() call. This method should be called from handlers when an exception is encountered during an emit() call. If raiseExceptions is false, exceptions get silently ignored. This is what is mostly wanted for a logging system - most users will not care about errors in the logging system, they are more interested in application errors. You could, however, replace this with a custom handler if you wish. The record which was being processed is passed in to this method.

### release method docstring

Release the I/O thread lock.

### removeFilter method docstring

Remove the specified filter from this handler.

### setFormatter method docstring

Set the formatter for this handler.

### setLevel method docstring

Set the logging level of this handler. level must be an int or a str.