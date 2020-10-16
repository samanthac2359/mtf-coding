#!/usr/bin/env python3

echo "This script tests the decode() function of coding2.py"

python3 ./decode.py test00.mtf
if [ $? -eq 0 ]; then
    echo "Test 00 passed"
else
    diff test00.txt /home/tests/test00.txt
fi

python3 ./decode.py test01.mtf
if [ $? -eq 0 ]; then
    echo "Test 01 passed"
else
    diff test01.txt /home/tests/test01.txt
fi

python3 ./decode.py test02.mtf
if [ $? -eq 0 ]; then
    echo "Test 02 passed"
else
    diff test02.txt /home/tests/test02.txt
fi

python3 ./decode.py test03.mtf
if [ $? -eq 0 ]; then
    echo "Test 03 passed"
else
    diff test03.txt /home/tests/test03.txt
fi

python3 ./decode.py test04.mtf
if [ $? -eq 0 ]; then
    echo "Test 04 passed"
else
    diff test04.txt /home/tests/test04.txt
fi

python3 ./decode.py test05.mtf
if [ $? -eq 0 ]; then
    echo "Test 05 passed"
else
    diff test05.txt /home/tests/test05.txt
fi

python3 ./decode.py test06.mtf
if [ $? -eq 0 ]; then
    echo "Test 06 passed"
else
    diff test06.txt /home/tests/test06.txt
fi

python3 ./decode.py test07.mtf
if [ $? -eq 0 ]; then
    echo "Test 07 passed"
else
    diff test07.txt /home/tests/test07.txt
fi

python3 ./decode.py test08.mtf
if [ $? -eq 0 ]; then
    echo "Test 08 passed"
else
    diff test08.txt /home/tests/test08.txt
fi

python3 ./decode.py test09.mtf
if [ $? -eq 0 ]; then
    echo "Test 09 passed"
else
    diff test09.txt /home/tests/test09.txt
fi

python3 ./decode.py test10.mtf
if [ $? -eq 0 ]; then
    echo "Test 10 passed"
else
    diff test10.txt /home/tests/test10.txt
fi

python3 ./decode.py test11.mtf
if [ $? -eq 0 ]; then
    echo "Test 11 passed"
else
    diff test11.txt /home/tests/test11.txt
fi

python3 ./decode.py test12.mtf
if [ $? -eq 0 ]; then
    echo "Test 12 passed"
else
    diff test12.txt /home/tests/test12.txt
fi

python3 ./decode.py test13.mtf
if [ $? -eq 0 ]; then
    echo "Test 13 passed"
else
    diff test13.txt /home/tests/test13.txt
fi

python3 ./decode.py test14.mtf
if [ $? -eq 0 ]; then
    echo "Test 14 passed"
else
    diff test14.txt /home/tests/test14.txt
fi

python3 ./decode.py test15.mtf
if [ $? -eq 0 ]; then
    echo "Test 15 passed"
else
    diff test15.txt /home/tests/test15.txt
fi

python3 ./decode.py test16.mtf
if [ $? -eq 0 ]; then
    echo "Test 16 passed"
else
    diff test16.txt /home/tests/test16.txt
fi

python3 ./decode.py test17.mtf
if [ $? -eq 0 ]; then
    echo "Test 17 passed"
else
    diff test17.txt /home/tests/test17.txt
fi

python3 ./decode.py test18.mtf
if [ $? -eq 0 ]; then
    echo "Test 18 passed"
else
    diff test18.txt /home/tests/test18.txt
fi

python3 ./decode.py test19.mtf
if [ $? -eq 0 ]; then
    echo "Test 19 passed"
else
    diff test19.txt /home/tests/test19.txt
fi


