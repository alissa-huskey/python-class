"""Contains the Logger class"""

from datetime import datetime
import logging
from pathlib import Path
from sys import stderr, stdout

class Logger():
    """Logging class"""

    """Width of decorative lines"""
    WIDTH: int = 75

    """Directory to write logfiles"""
    LOGDIR = Path(__file__).parents[2].joinpath("tmp")

    """Default log record format"""
    FMT: str = "%(asctime)s [%(levelname)s] %(message)s"

    """Default date format"""
    DATEFMT: str = "%Y-%m-%dT%H:%M:%S"

    """Long date format"""
    LONG_DATE: str = "%a, %b %d, %Y @ %I:%M%p %Z"

    """Log levels"""
    LEVELS: dict = {
        'NOTSET': 0,
        'DEBUG': 10,
        'INFO': 20,
        'WARNING': 30,
        'WARN': 30,
        'ERROR': 40,
        'CRITICAL': 50,
        'FATAL': 50,
    }

    """Available outputs"""
    OUTPUTS: tuple = ("file", "stderr", "stdout", "null")

    """logger interface"""
    logger: logging.Logger

    """logger name"""
    name: str

    """logging status"""
    enabled: bool

    """where to write log output
       determines handler
       see: OUTPUTS
      """
    output: str

    """Maximum log messages to emit
       see: LEVELS
    """
    level: int

    """Ouput format strings
       logging.Formatter, datefmt
       see: FMT: DATEFMT, LONGDATE
    """
    format: tuple

    """Output handler
       set through output
    """
    handler: logging.Handler

    def __init__(self, name: str, output: str="file",
                 enabled: bool=True, level=logging.DEBUG):
        """Initializer
        Params
        ------
        * name (str)                              : log name
        * output (str, default: "file")           : used to determine handler
                                                    (see Logger.OUTPUTS)
        * level (int|str, default: logging.debug) : log level
                                                    (see Logger.LEVELS)
        * enabled (bool, default: True)           : enable logging

        Examples
        --------
        >>> log("lexicon", enabled=False)
        >>> log("lexicon", output="stderr")
        >>> log("lexicon")
        """
        if not enabled:
            level, output = 0, "null"

        self._init_attrs_()
        self.logger = logging.getLogger(__file__)
        self.name = name
        self.enabled = enabled
        self.output = output
        self.level = level
        self.format = self.FMT, self.DATEFMT

        self._init_methods_()
        self._init_log_()

    def _init_attrs_(self):
        """Initialize internal property attributes"""
        for attr in ("nh", "fh", "eh", "sh", "handler", "format",
                     "date_format", "enabled", "level"):
            setattr(self, f"_{attr}", None)

    def _init_methods_(self):
        """Create logging methods for levels"""
        for lvl in list(self.LEVELS.keys())[1:]:
            level= getattr(logging, lvl)
            name = lvl.lower()
            method = self.mklog_fn(name, level)
            setattr(self, name, method)

    def _init_log_(self):
        """Write startup messages to log stream"""
        num, level = self._lvl_(self.level)
        output, handler = self.output, repr(self.handler)
        plain, line = " %(message)s", "="*self.WIDTH
        status = ("DISABLED", "ENABLED")[self.enabled]

        self.write(f"\n{line}")
        self.write(datetime.today().strftime(self.LONG_DATE), fmt=plain)
        self.write(f"Initializing {self.name} log: {status}", fmt=plain)
        self.write(f"Level {num}: {level}", fmt=plain)
        self.write(f"Output {output}: {handler}", fmt=plain)
        self.write(f"{line}\n")

    def __call__(self, *args, **kwargs):
        """Log using default log level when called"""
        self.log(*args, **kwargs)

    def _lvl_(self, lvl) -> tuple:
        """Normalize level, Return int, str"""
        if isinstance(lvl, str):
            level = lvl.upper()
            num = self._lvl_to_num_(lvl)
        elif isinstance(lvl, int):
            level = self._lvl_to_str_(lvl)
            num = lvl
        return num, level

    def _lvl_to_num_(self, level) -> int:
        """Return int for level str"""
        return self.LEVELS.get(str(level).upper(), level)

    def _lvl_to_str_(self, lvl) -> str:
        """Return str for level int"""
        mapping = dict(zip(self.LEVELS.values(), self.LEVELS.keys()))
        return mapping.get(lvl)

    def mkmsg(self, *args, **kwargs) -> str:
        """Return log message for args"""
        return " ".join(map(str, args))

    def write(self, *args, fmt="%(message)s", **kwargs):
        """write info message, with temp changes to output, level, and format
           as follows:

           * output: if null, switch to stdout
           * level: set to info
           * format: switch to fmt argument
        """
        output = "stdout" if self.output == "null" else self.output
        revert = self.level, self.output, self.format
        self.level, self.output, self.format = "info", output, fmt
        self.info(*args, **kwargs)
        self.level, self.output, self.format = revert

    def log(self, *args, **kwargs):
        """Write message to log stream
        Params
        ------
        * args: message
        * level (str|int, default: logging.DEBUG): level of log message
        """
        level = kwargs.get("level", logging.DEBUG)
        msg = self.mkmsg(*args, **kwargs)
        self.logger.log(level, msg)

    def mklog_fn(self, name: str, level: int):
        """Generage log function named name for log level level"""
        def log_fn(*args, **kwargs):
            """write log message"""
            kwargs['level'] = level
            self.log(*args, **kwargs)
        log_fn.__name__ = name
        return log_fn

    @property
    def null(self) -> logging.NullHandler:
        """Return log handler to disable printing log messages"""
        if not self._nh:
            self._nh = logging.NullHandler()
        return self._nh

    @property
    def stdout(self) -> logging.StreamHandler:
        """Return log handler to print to stdout"""
        if not self._sh:
            self._sh = logging.StreamHandler(stream=stdout)
        return self._sh

    @property
    def stderr(self) -> logging.StreamHandler:
        """Return handler to print to stderr"""
        if not self._eh:
            self._eh = logging.StreamHandler(stream=stderr)
        return self._eh

    @property
    def file(self) -> logging.FileHandler:
        """Return handler to print to file"""
        if not self._fh:
            self._fh = logging.FileHandler(self.LOGDIR.joinpath(f"{self.name}.log"))
        return self._fh

    @property
    def output(self) -> str:
        """output property"""
        return self._output

    @output.setter
    def output(self, value):
        """Set self._output and set handler to matching handler property
           see Logger.OUTPUTS for valid output strings
        """
        if value not in self.OUTPUTS:
            msg = f"No handler found for output: '{value}'\n"
            msg += "Must be one of: {self.outputs}"
            raise NameError(msg)
        self._output = value
        self.handler = getattr(self, self._output)

    @property
    def enabled(self) -> bool:
        """enabled property"""
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """set self._enabled
           setting to False sets level and output
        """
        self._enabled = enabled
        if not self._enabled:
            self.output = "null"
            self.level = 0

    @property
    def handler(self) -> logging.Handler:
        """handler property"""
        return self._handler

    @handler.setter
    def handler(self, handler):
        """set self._handler, add to logger, and remove old handler"""
        if self._handler and self.logger.handlers:
            self.logger.removeHandler(self._handler)
        self._handler = handler
        self.logger.addHandler(self._handler)

    @property
    def format(self) -> tuple:
        """format property
           tuple with two format strings:
           * logging.Formatter fmt
           * time.strftime fmt
        """
        return self._format, self._date_format

    @format.setter
    def format(self, fmts):
        """set _format and self._date_format and set the handler format
           if a single format string is passed, datefmt will default to
           self.DATEFMT"""
        if isinstance(fmts, str):
            fmts = (fmts, self.DATEFMT)
        self._format, self._date_format = fmts
        formatter = logging.Formatter(*fmts)
        self.handler.setFormatter(formatter)

    @property
    def level(self):
        """level property"""
        return self._level

    @level.setter
    def level(self, lvl):
        """set self._level and update logger and handler"""
        self._level, _ = self._lvl_(lvl)
        self.logger.setLevel(self._level)
        self.handler.setLevel(self._level)

