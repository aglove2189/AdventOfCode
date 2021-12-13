for FILE in *.py; do printf '%s ' $FILE  && (time python $FILE) 2>&1 > /dev/null | grep real | awk '{print $2}'; done
