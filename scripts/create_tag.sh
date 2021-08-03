#!/usr/bin/env bash

sed="sed";
uname=$(uname);
case "$uname" in
    (*Darwin*) sed='gsed'; ;;
esac;


if [[ "$(git status --porcelain)" ]]; then
  printf "Working directory not clean:\n\n"
  git status
else
  echo Current tags:
  git tag

  echo Commits since last tag:
  git log "$(git describe --tags --abbrev=0)"..HEAD --oneline
  echo "Please enter next version (x.y.z):"
  read version
  npm version "$version" -m "Update version to %s"
fi
