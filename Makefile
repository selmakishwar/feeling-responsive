PY=python3

all : commands

## commands   : show all commands.
commands :
	@grep -E '^##' Makefile | sed -e 's/## //g'

## update     : update data from the web.
update :
	${PY} bin/make-dashboard.py ./git-token.txt _data/dashboard.yml

## serve      : run a local server.
serve : 
	jekyll serve --config _config.yml,_config_dev.yml

#-------------------------------------------------------------------------------

## clean      : clean up junk files.
clean :
	rm -rf _site .sass-cache $$(find . -name '*~' -print)
