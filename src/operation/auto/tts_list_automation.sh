#!/bin/bash

tts --list_models > ../out/models_list.txt

python3 ../src/operation/tts_lists_process.py