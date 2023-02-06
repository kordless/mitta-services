#!/bin/bash
source /root/config.sh
screen -dmS weaviate bash -c "docker compose up"