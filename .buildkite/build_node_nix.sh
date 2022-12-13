#! /usr/bin/env -S nix develop --accept-flake-config .#base -c bash
# shellcheck shell=bash

set -xeuo pipefail

TESTDIR="$PWD"

TEMPDIR="/scratch/workdir"
rm -rf "TEMPDIR"
mkdir -p "TEMPDIR"

cd $TEMPDIR
git clone https://github.com/input-output-hk/cardano-node.git
cd cardano-node
git checkout DESIRED_REVISION
nix-build -v -A cardano-node -o cardano-node-bin
nix-build -v -A cardano-cli -o cardano-cli-bin

echo "cardano-node dir content:"
ls cardano-node

echo "cardano-cli dir content:"
ls cardano-node/cardano-cli-bin/bin

echo "cardano-node dir content:"
ls cardano-node/cardano-node-bin/bin
