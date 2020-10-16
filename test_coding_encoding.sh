#!/usr/bin/env python3

echo "This script tests the encode() function of coding.py"

python3 ./text2mtf.py test00.txt
if [ $? -eq 0 ]; then 
    echo "Test 00 passed"
else
    diff test00.mtf /home/tests/test00.mtf
fi

python3 ./text2mtf.py test01.txt
if [ $? -eq 0 ]; then
    echo "Test 01 passed"
else
    diff test01.mtf /home/tests/test01.mtf
fi

python3 ./text2mtf.py test02.txt
if [ $? -eq 0 ]; then
    echo "Test 02 passed"
else
    diff test02.mtf /home/tests/test02.mtf
fi

python3 ./text2mtf.py test03.txt
if [ $? -eq 0 ]; then
    echo "Test 03 passed"
else
    diff test03.mtf /home/tests/test03.mtf
fi

python3 ./text2mtf.py test04.txt
if [ $? -eq 0 ]; then
    echo "Test 04 passed"
else
    diff test04.mtf /home/tests/test04.mtf
fi

python3 ./text2mtf.py test05.txt
if [ $? -eq 0 ]; then
    echo "Test 05 passed"
else
    diff test05.mtf /home/tests/test05.mtf
fi

python3 ./text2mtf.py test06.txt
if [ $? -eq 0 ]; then
    echo "Test 06 passed"
else
    diff test06.mtf /home/tests/test06.mtf
fi

python3 ./text2mtf.py test07.txt
if [ $? -eq 0 ]; then
    echo "Test 07 passed"
else
    diff test07.mtf /home/tests/test07.mtf
fi

python3 ./text2mtf.py test08.txt
if [ $? -eq 0 ]; then
    echo "Test 08 passed"
else
    diff test08.mtf /home/tests/test08.mtf
fi

python3 ./text2mtf.py test09.txt
if [ $? -eq 0 ]; then
    echo "Test 09 passed"
else
    diff test09.mtf /home/tests/test09.mtf
fi

python3 ./text2mtf.py test10.txt
if [ $? -eq 0 ]; then
    echo "Test 10 passed"
else
    diff test10.mtf /home/tests/test10.mtf
fi
