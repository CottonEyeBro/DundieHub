#!/usr/bin/env bash
set -euo pipefail

cd client
npm install
npm run build
cd ..

rm -rf public
mkdir -p public
cp -a client/build/. public/
