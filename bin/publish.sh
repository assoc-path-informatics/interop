#!/bin/bash

remote_repo="git@github.com:nhoffman/pelicandemo.git"
remote_branch=gh-pages

echo 'Publishing to GitHub Pages 📤 '
pushd output
git init
git remote add deploy "$remote_repo"
git checkout $remote_branch || git checkout --orphan $remote_branch
# git config user.name "${GITHUB_ACTOR}"
# git config user.email "${GITHUB_ACTOR}@users.noreply.github.com"
# if [ "$GH_PAGES_CNAME" != "none" ]
# then
#     echo "$GH_PAGES_CNAME" > CNAME
# fi
git add .

echo -n 'Files to Commit:' && ls -l | wc -l
git commit -m "[ci skip] Automated deployment to GitHub Pages on $(date +%s%3N)"
git push deploy $remote_branch --force
rm -fr .git
popd
