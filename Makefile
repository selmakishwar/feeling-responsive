all : commands

## commands   : show all commands.
commands :
	@grep -E '^##' Makefile | sed -e 's/## //g'

## serve      : run a local server.
serve : 
	jekyll serve --config _config.yml,_config_dev.yml

#-------------------------------------------------------------------------------

## clean      : clean up junk files.
clean :
	rm -rf _site .sass-cache $$(find . -name '*~' -print)
