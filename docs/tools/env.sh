#!/bin/zsh
#
# .env file for python-class -- this file is automatically sourced by vs code every time
#                               a terminal is started
#
# can be found at:
# https://raw.githubusercontent.com/alissa-huskey/python-class/master/docs/tools/env.sh
#


# set your project version of python
PYENV_VERSION="3.8.11"
export PYENV_VERSION

# ----------------------------------------------------------------------------------------
# You should not need to change anything below this line.
# ----------------------------------------------------------------------------------------

# ensure that python can find your package/modules
if ! [[ "${PWD}" =~ "${PYTHONPATH}" ]]; then
  PYTHONPATH="${PYTHONPATH}:${PWD}"
  export PYTHONPATH
fi

# if poetry is installed and used in this projgect
if command -v poetry > /dev/null \
  && [[ -f $PWD/pyproject.toml ]] \
  && [[ -z "${VIRTUAL_ENV}" ]]; then

  # get the path to your virtual environment
  venv="$(poetry env info -p)"

  # if there is a virtual env, activate it
  #
  if [[ -n "${venv}" ]]; then
    source "${venv}/bin/activate"
  fi
fi
