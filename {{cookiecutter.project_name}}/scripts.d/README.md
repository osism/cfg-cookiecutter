Any other scripts can be stored in this directory and executed
one after the other as hook scripts. Like the scripts directory,
the scripts.d directory is also deleted. It is not part of the final
configuration repository.

If three scripts `001-sample.sh`, `002-sample.sh`, and `003-sample.sh`
are present, first `001-sample.sh`, then `002-sample.sh` and finally
`003-sample.sh` would be executed.

The scripts must be executable. These can be any scripts, the shebang
must be set correctly.

The use of additional hook scripts makes particular sense if you maintain
your own fork of the osism/cfg-cookiecutter repository and can then make
your own changes via these additional hook scripts.
