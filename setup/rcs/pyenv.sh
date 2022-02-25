

# pyenv
# --------------------------------------------------------------------

if command -v pyenv > /dev/null ; then
	eval "$(pyenv init --path)"  # mksh: check if present
	eval "$(pyenv init -)"
fi
