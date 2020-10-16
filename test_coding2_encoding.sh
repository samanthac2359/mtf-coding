#!/usr/bin/env python3

echo "This script tests the encode() function of coding2.py"

python3 ./encode.py test00.txt
if [ $? -eq 0 ]; then
    echo "Test 00 passed"
else
    diff test00.mtf /home/tests/test00.mtf
fi

python3 ./encode.py test01.txt
if [ $? -eq 0 ]; then
    echo "Test 01 passed"
else
    diff test01.mtf /home/tests/test01.mtf
fi

python3 ./encode.py test02.txt
if [ $? -eq 0 ]; then
    echo "Test 02 passed"
else
    diff test02.mtf /home/tests/test02.mtf
fi

python3 ./encode.py test03.txt
if [ $? -eq 0 ]; then
    echo "Test 03 passed"
else
    diff test03.mtf /home/tests/test03.mtf
fi

python3 ./encode.py test04.txt
if [ $? -eq 0 ]; then
    echo "Test 04 passed"
else
    diff test04.mtf /home/tests/test04.mtf
fi

python3 ./encode.py test05.txt
if [ $? -eq 0 ]; then
    echo "Test 05 passed"
else
    diff test05.mtf /home/tests/test05.mtf
fi

python3 ./encode.py test06.txt
if [ $? -eq 0 ]; then
    echo "Test 06 passed"
else
    diff test06.mtf /home/tests/test06.mtf
fi

python3 ./encode.py test07.txt
if [ $? -eq 0 ]; then
    echo "Test 07 passed"
else
    diff test07.mtf /home/tests/test07.mtf
fi

python3 ./encode.py test08.txt
if [ $? -eq 0 ]; then
    echo "Test 08 passed"
else
    diff test08.mtf /home/tests/test08.mtf
fi

python3 ./encode.py test09.txt
if [ $? -eq 0 ]; then
    echo "Test 09 passed"
else
    diff test09.mtf /home/tests/test09.mtf
fi

python3 ./encode.py test10.txt
if [ $? -eq 0 ]; then
    echo "Test 10 passed"
else
    diff test10.mtf /home/tests/test10.mtf
fi

python3 ./encode.py test11.txt
if [ $? -eq 0 ]; then
    echo "Test 11 passed"
else
    diff test11.mtf /home/tests/test11.mtf
fi

python3 ./encode.py test12.txt
if [ $? -eq 0 ]; then
    echo "Test 12 passed"
else
    diff test12.mtf /home/tests/test12.mtf
fi

python3 ./encode.py test13.txt
if [ $? -eq 0 ]; then
    echo "Test 13 passed"
else
    diff test13.mtf /home/tests/test13.mtf
fi

python3 ./encode.py test14.txt
if [ $? -eq 0 ]; then
    echo "Test 14 passed"
else
    diff test14.mtf /home/tests/test14.mtf
fi

python3 ./encode.py test15.txt
if [ $? -eq 0 ]; then
    echo "Test 15 passed"
else
    diff test15.mtf /home/tests/test15.mtf
fi

python3 ./encode.py test16.txt
if [ $? -eq 0 ]; then
    echo "Test 16 passed"
else
    diff test16.mtf /home/tests/test16.mtf
fi

python3 ./encode.py test17.txt
if [ $? -eq 0 ]; then
    echo "Test 17 passed"
else
    diff test17.mtf /home/tests/test17.mtf
fi

python3 ./encode.py test18.txt
if [ $? -eq 0 ]; then
    echo "Test 18 passed"
else
    diff test18.mtf /home/tests/test18.mtf
fi

python3 ./encode.py test19.txt
if [ $? -eq 0 ]; then
    echo "Test 19 passed"
else
    diff test19.mtf /home/tests/test19.mtf
fi

