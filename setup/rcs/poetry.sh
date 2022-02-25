

# poetry
# --------------------------------------------------------------------

if [[ -d $HOME/.poetry/bin ]]; then
	PATH="$HOME/.poetry/bin:$PATH" # mksh: check if present
  export PATH
fi

poetry_activate() {
	local venv

	if ! command -v poetry > /dev/null; then
		return
	fi

	if [[ $PWD/pyproject.toml ]] && [[ -z "${VIRTUAL_ENV}" ]]; then
		venv="$(poetry env info -p)"
		if [[ -n "${venv}" ]]; then
			source "${venv}/bin/activate"
		fi
	fi
}
