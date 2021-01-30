.PHONY: all build

all: build

build:
	@poetry install --no-root
	@poetry run proto
	@poetry build
