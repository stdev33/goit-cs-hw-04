#!/bin/bash

OUTPUT_DIR="./text_files"

# Number of files to generate (default: 10 if not specified)
NUM_FILES=${1:-10}

KEYWORDS=("keyword1" "keyword2" "keyword3")

if [ ! -d "$OUTPUT_DIR" ]; then
  mkdir -p "$OUTPUT_DIR"
  echo "Directory $OUTPUT_DIR has been created."
fi

for ((i=1; i<=NUM_FILES; i++)); do
  FILE_PATH="$OUTPUT_DIR/file_$i.txt"

  # Create a file with random content, including a random keyword
  echo "This is random text for testing. ${KEYWORDS[$RANDOM % ${#KEYWORDS[@]}]} is included here." > "$FILE_PATH"

  # Add additional random lines to the file
  for ((j=0; j<5; j++)); do
    RANDOM_WORD="random_text_$RANDOM"
    echo "$RANDOM_WORD" >> "$FILE_PATH"
  done

  echo "File $FILE_PATH has been generated."
done

echo "All $NUM_FILES files have been successfully created in the $OUTPUT_DIR directory."
