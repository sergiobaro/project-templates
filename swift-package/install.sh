#!/usr/bin/env bash

swift build -c release || exit 1
cp .build/release/{{name.lowercase}} /usr/local/bin/{{name.lowercase}}
