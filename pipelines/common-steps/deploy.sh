#!/bin/bash

set -x
du -hs * | sort -hgit commit
sam deploy template.yaml --config-env ${ENVIRONMENT} --no-confirm-changeset --force-upload --no-fail-on-empty-changeset --no-progressbar