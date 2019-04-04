#!/usr/bin/env bash

# bump_version.sh (show|major|minor|patch|prerelease|build)

set -o nounset
set -o errexit
set -o pipefail

VERSION_FILE=mongo_db_from_config/__init__.py

HELP_INFORMATION="bump_version.sh (show|major|minor|patch|prerelease|build|finalize)"

old_version=$(sed -n "s/^__version__ = '\(.*\)'$/\1/p" $VERSION_FILE)

if [ $# -ne 1 ]
then
   echo "$HELP_INFORMATION"
else
    case $1 in
        major|minor|patch|prerelease|build)
            new_version=$(python -c "import semver; print(semver.bump_$1('$old_version'))")
            echo Changing version from "$old_version" to "$new_version"
            sed -i "s/$old_version/$new_version/" $VERSION_FILE
            git add $VERSION_FILE
            git commit -m"Bump version from $old_version to $new_version"
            git push
            ;;
        finalize)
            new_version=$(python -c "import semver; print(semver.finalize_version('$old_version'))")
            echo Changing version from "$old_version" to "$new_version"
            sed -i "s/$old_version/$new_version/" $VERSION_FILE
            git add $VERSION_FILE
            git commit -m"Finalize version from $old_version to $new_version"
            git push
            ;;
        show)
            echo "$old_version"
            ;;
        *)
            echo "$HELP_INFORMATION"
            ;;
    esac
fi