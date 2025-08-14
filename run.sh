#!/bin/bash

# Dung lượng RAM tối thiểu và tối đa
MIN_RAM="2G"
MAX_RAM="4G"

# File jar của server
SERVER_JAR="paper.jar"

# Chạy server
java -Xms$MIN_RAM -Xmx$MAX_RAM -jar $SERVER_JAR nogui
