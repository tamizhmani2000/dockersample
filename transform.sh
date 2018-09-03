NAMES="$(< output2)" #names from names.txt file

for NAME in $NAMES; do
    echo "$NAME" | cut -c 3- |rev|cut -c 3- |rev | base64 -D >>decoded.txt
    echo '' >>decoded.txt
done
echo "Program Completed"