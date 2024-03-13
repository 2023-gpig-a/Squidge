#!/usr/bin/env bash
set -euo pipefail

REPOS=(DMAS DroneManager frontend LLM)
changed=0

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
  git checkout -b "update-$(date +%Y%m%d%H%M%S)"
  git push

  gh pr create --title "Update submodules" --body "Update submodules" --base master --head "update-$(date +%Y%m%d%H%M%S)"
fi
