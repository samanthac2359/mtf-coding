#!/usr/bin/env python3

echo "This script tests the decode() function of coding.py"

python3 ./mtf2text.py test00.mtf
if [ $? -eq 0 ]; then
    echo "Test 00 passed"
else
    diff test00.txt /home/tests/test00.txt
fi

python3 ./mtf2text.py test01.mtf
if [ $? -eq 0 ]; then
    echo "Test 01 passed"
else
    diff test01.txt /home/tests/test01.txt
fi

python3 ./mtf2text.py test02.mtf
if [ $? -eq 0 ]; then
    echo "Test 02 passed"
else
    diff test02.txt /home/tests/test02.txt
fi

python3 ./mtf2text.py test03.mtf
if [ $? -eq 0 ]; then
    echo "Test 03 passed"
else
    diff test03.txt /home/tests/test03.txt
fi

python3 ./mtf2text.py test04.mtf
if [ $? -eq 0 ]; then
    echo "Test 04 passed"
else
    diff test04.txt /home/tests/test04.txt
fi

python3 ./mtf2text.py test05.mtf
if [ $? -eq 0 ]; then
    echo "Test 05 passed"
else
    diff test05.txt /home/tests/test05.txt
fi

python3 ./mtf2text.py test06.mtf
if [ $? -eq 0 ]; then
    echo "Test 06 passed"
else
    diff test06.txt /home/tests/test06.txt
fi

python3 ./mtf2text.py test07.mtf
if [ $? -eq 0 ]; then
    echo "Test 07 passed"
else
    diff test07.txt /home/tests/test07.txt
fi

python3 ./mtf2text.py test08.mtf
if [ $? -eq 0 ]; then
    echo "Test 08 passed"
else
    diff test08.txt /home/tests/test08.txt
fi

python3 ./mtf2text.py test09.mtf
if [ $? -eq 0 ]; then
    echo "Test 09 passed"
else
    diff test09.txt /home/tests/test09.txt
fi

python3 ./mtf2text.py test10.mtf
if [ $? -eq 0 ]; then
    echo "Test 10 passed"
else
    diff test10.txt /home/tests/test10.txt
fi
