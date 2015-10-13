PY=python3

all : commands

## commands   : show all commands.
commands :
	@grep -E '^##' Makefile | sed -e 's/## //g'

## amy        : update workshop and other data from AMY.
amy :
	${PY} bin/get-amy.py https://amy.software-carpentry.org/api/v1/ _data/amy.yml

## dashboard  : update data about status of projects.
dashboard :
	${PY} bin/get-dashboard.py ./git-token.txt _data/dashboard.yml

## includes   : update include file listing from disk.
includes :
	${PY} bin/get-includes.py _data/includes.yml

## serve      : run a local server.
serve : 
	jekyll serve --config _config.yml,_config_dev.yml

## build      : build files but do not run a server.
build : 
	jekyll build

#-------------------------------------------------------------------------------

## clean      : clean up junk files.
clean :
	rm -rf _site .sass-cache $$(find . -name '*~' -print) $$(find . -name .DS_Store -print)
