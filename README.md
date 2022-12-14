## 4. While loops (while)
1. Write a program that uses a `while` loop to print out all numbers divisible by three in the range of 1-1000.
```python
n = 3
while n <= 1000:
    if n % 3 == 0:
        print(n)
    n += 3
```
Output console:
```
3
6
9
12
15
18
21
24
27
30
33
36
39
42
45
48
51
54
57
60
63
66
69
72
75
78
81
84
87
90
93
96
99
102
105
108
111
114
117
120
123
126
129
132
135
138
141
144
147
150
153
156
159
162
165
168
171
174
177
180
183
186
189
192
195
198
201
204
207
210
213
216
219
222
225
228
231
234
237
240
243
246
249
252
255
258
261
264
267
270
273
276
279
282
285
288
291
294
297
300
303
306
309
312
315
318
321
324
327
330
333
336
339
342
345
348
351
354
357
360
363
366
369
372
375
378
381
384
387
390
393
396
399
402
405
408
411
414
417
420
423
426
429
432
435
438
441
444
447
450
453
456
459
462
465
468
471
474
477
480
483
486
489
492
495
498
501
504
507
510
513
516
519
522
525
528
531
534
537
540
543
546
549
552
555
558
561
564
567
570
573
576
579
582
585
588
591
594
597
600
603
606
609
612
615
618
621
624
627
630
633
636
639
642
645
648
651
654
657
660
663
666
669
672
675
678
681
684
687
690
693
696
699
702
705
708
711
714
717
720
723
726
729
732
735
738
741
744
747
750
753
756
759
762
765
768
771
774
777
780
783
786
789
792
795
798
801
804
807
810
813
816
819
822
825
828
831
834
837
840
843
846
849
852
855
858
861
864
867
870
873
876
879
882
885
888
891
894
897
900
903
906
909
912
915
918
921
924
927
930
933
936
939
942
945
948
951
954
957
960
963
966
969
972
975
978
981
984
987
990
993
996
999
```
2. Write a program that converts inches to centimeters until the user inputs a negative value. Then the program ends.
```python
getInput = input("Input any number (negative number to exit): ")
numIn = float(getInput)
while numIn >= 0:
    numCm = numIn * 2.54
    print(getInput, "in =", numCm, "cm")
    getInput = input("Input any number (negative number to exit): ")
    numIn = float(getInput)
```
Output console:
```
Input any number (negative number to exit): 3
3 in = 7.62 cm
Input any number (negative number to exit): 3
3 in = 7.62 cm
Input any number (negative number to exit): 45
45 in = 114.3 cm
Input any number (negative number to exit): 2.5
2.5 in = 6.35 cm
Input any number (negative number to exit): -2
```
3. Write a program that asks the user to enter numbers until they enter an empty string to quit. Finally, the program
prints out the smallest and largest number from the numbers it received.
```python
numMax = 0
num = input("Enter a number (Enter blank to exit): ")
if num != "":
    numMin = float(num)
else:
    numMin = 0
while num != "":
    if float(num) < numMin:
        numMin = float(num)
    elif float(num) > numMax:
        numMax = float(num)
    num = input("Enter a number (Enter blank to exit): ")
numMinStr = str(numMin)
numMaxStr = str(numMax)
if numMinStr[len(numMinStr)-1:] == "0":
    numMin = int(numMin)
if numMaxStr[len(numMaxStr)-1:] == "0":
    numMax = int(numMax)
print("The smallest number is: ", numMin)
print("The largest number is: ", numMax)
```
Output console:
```
Enter a number (Enter blank to exit): 4
Enter a number (Enter blank to exit): 5
Enter a number (Enter blank to exit): 63
Enter a number (Enter blank to exit): 
The smallest number is:  4
The largest number is:  63
```
4. Write a game where the computer draws a random integer between 1 and 10. The user tries to guess the number until
they guess the right number. After each guess the program prints out a text: `Too high`, `Too low` or `Correct`. 
Notice that the computer must not change the number between guesses.
```python
import random
ranNum = random.randint(1,10)
numGuess = int(input("Guess the number from 1-10: "))
while numGuess != ranNum:
    if numGuess < ranNum:
        print("Too low. Try again")
    else:
        print("Too high. Try again")
    numGuess = int(input("Guess the number from 1-10: "))
print("Correct!")
```
Output console:
```
Guess the number from 1-10: 3
Too low. Try again
Guess the number from 1-10: 5
Correct!
```
5. Write a program that asks the user for a username and password. If either or both are incorrect, the program 
ask the user to enter the username and password again. This continues until the login information is correct or
wrong credentials have been entered five times. If the information is correct, the program prints out `Welcome`.
After five failed attempts the program prints out `Access denied`. The correct username is **python** and password 
**rules**.
```python
userOK = "python"
passOK = "rules"
username = input("Username: ")
password = input("Password: ")
time = 1
while (username != userOK or password != passOK) and time < 5:
    print("Login failed. Try again")
    username = input("Username: ")
    password = input("Password: ")
    time += 1
if username != userOK or password != passOK:
    print("Access denied")
else:
    print("Welcome")
```
Output console:
```
Username: python
Password: rules
Welcome
```
6. Implement an algorithm for calculating an approximation for the value of pi (??). Let's assume that A is a unit
circle. A unit circle has the radius of one and it is centered at the origin (0,0). Smallest possible square B
is drawn around the unit circle so that circle A is completely inside the square. The corners of the square are now 
(-1,-1), (1, -1), (1, 1), and (-1, 1). If a large number of random points are scattered inside the square, the fraction
of points that fall inside the circle A correlates with the fraction of the area of circle A compared to the area of 
square B: ??r^2/4 = ??*1^2/4 = ??/4. This can be used as a simple method for calculating an approximation of the value 
of pi: Let's generate a large number of random points, such as one million, inside square B. Let N be the total number
of random points. Each point inside the square is tested for whether it resides inside circle A. Let n be the total 
number of points that fall inside circle A. Now we have n/N?????/4, and from that we get ?????4n/N. Write a program that
asks the user how many random points to generate, and then calculates the approximate value of pi using the method 
explained above. At the end, the program prints out the approximation of pi to the user. (Notice that it is easy to
test if a point falls inside circle A by testing if it fulfills the inequation x^2+y^2<1.).
```python
import random
count = 0
insidePoints = 0
totalPoints = int(input("How many points to generate for calculating pi value: "))
while count < totalPoints:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if x*x + y*y < 1:
        insidePoints += 1
    count += 1
print("Value of pi is: ", 4*insidePoints/totalPoints)
```
Output console:
```
How many points to generate for calculating pi value: 1000000
Value of pi is:  3.139976

Process finished with exit code 0
```
