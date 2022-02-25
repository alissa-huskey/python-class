

# gnu coreutils
# --------------------------------------------------------------------

if read -r coreutils < <(brew --prefix coreutils 2> /dev/null) \
  && [[ -d "${gnubin}/libexec/gnubin" ]] ; then
  PATH="${coreutils}/libexec/gnubin:$PATH"  # mksh: check if present
  alias ls='ls --literal --human-readable --color=always'
fi

unset coreutils
