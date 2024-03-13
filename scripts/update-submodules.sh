#!/usr/bin/env bash
set -euo pipefail

REPOS=(DMAS DroneManager frontend LLM)
changed=0

GIT_ASKPASS=$(pwd)/scripts/git-helper.sh
export GIT_ASKPASS

for repo in "${REPOS[@]}"; do
  echo "Updating $repo"
  git submodule update --remote --init --merge "$repo"
  git add "$repo"
  if git commit -m "Update $repo"; then
    changed=1
  fi
  echo "-------------------"
done

if [ $changed -eq 1 ]; then
  echo "Pushing changes"
  git push
fi
