read -p "Enter a number: " num
i=2
f=0
while [ $i -le $(expr $num / 2) ]; do
    if [ $(expr $num % $i) -eq 0 ]; then
        f=1
    fi
    i=$(expr $i + 1)
done
if [ $f -eq 1 ]; then
    echo "$num is composite (not prime)"
else
    echo "$num is Prime"
fi