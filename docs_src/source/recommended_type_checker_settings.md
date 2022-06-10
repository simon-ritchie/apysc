# Recommended type-annotation checker settings

This page explains the type-annotation checker libraries settings, such as the mypy and Pylance (Pyright).

## Recommended type-annotation checker libraries

The apysc library uses the mypy and Pylance (Pyright) checker libraries. So if you want to use the type-annotation checker libraries on the apysc project, these two libraries probably become comfortable.

## Mypy's ignoring error code

The apysc library ignores the mypy misc (miscellaneous) errors with the `--disable-error-code misc` option.

This error code causes many mypy errors on the apysc library, but most are harmless, so the apysc ignores them.
