import streamlit as st
st.title("NUMBER PROBLEMES")

num = st.number_input("ENTER THE NUMBER ",min_value=0)

st.subheader("""HERE YOU CAN RUN THE CHECK THE 
                 SUM OF NUMBERS
                FACTORIAL OF NUMBERS
                REVERSE THE GIVEN NUMBER
                PALINDROME OR NOT
                SPY NUMBER OR NOT
                PERFECT NUMBER OR NOT
                ARMSTRONG NUMBER OR NOT
                DISARIUM NUMBER OR NOT
                STRONG NUMBER OR NOT
                XYLEM OR PHLOEM
                AUTOMORPHIC NUMBER OR NOT
                FIBONACCI SERIES
                HAPPY NUMBER OR NOT
            """)
sum = st.button(" SUM OF GIVEN NUMBER ")
factioral = st.button("FACTORIAL OF GIVEN NUMBER ")
reverse = st.button("REVERSE THE NUMBER ")
palindrome = st.button("PALINDROME OR NOT")
spy = st.button("SPY NUMBER OR NOT")
perfectnum = st.button("PERFECT NUMBER OR NOT")
armstrongnum = st.button("ARMSTRONG NUMBER OR NOT")
disariannum = st.button("DISARIAN NUMBER OR NOT")
strongnum = st.button("STRONG NUMBER OR NOT ")
xylemphonum = st.button("XYLEM NUMER OR PHONUM NUMBER")
automorphicnum = st.button("AUTOMORPHIC NUMBER OR NOT ")
fibnocciseries = st.button("FIBNOCCI SERIES ")
happynum = st.button("HAPPY NUMBER ")

if sum:
    st.subheader("SUM OF GIVEN NUMBER PROBLEM IS :  ")
    i=0
    sum = 0
    while num >0:
        rem = num % 10
        sum += rem
        num = num//10
    st.success(sum)

elif factioral:
    st.subheader("FACTORIAL OF A GIVEN NUMBER IS :  ")
    pro=1
    while num > 0:
        pro = pro *num
        num-=1
    st.success(pro)

elif reverse:
    st.subheader("REVERSE OF A GIVEN NUMBER IS :  ")
    sum = 0
    while num >0:
        rem = num % 10
        sum =rem+sum*10
        num = num//10
    st.success(sum)

elif palindrome:
    temp = num
    sum = 0
    while num >0:
        rem = num %10
        sum = rem+sum*10
        num = num //10
    if temp == sum:
        st.success("GIVEN NUMBER IS A PALINDROME")
    else:
        st.error("GIVEN NUMBER IS NOT A PALINDROME")


elif spy:
    sum=0
    pro=1
    while num > 0:
        rem = num % 10
        sum += rem
        pro *= rem
        num = num//10
    if sum == pro:
        st.success("GIVEN NUMBER IS A SPY NUMBER ")
    else:
        st.error("GIVEN NUMBER IS NOT A SPY NUMBER ")
    
elif perfectnum:
    i=1
    sum=0
    temp=num
    while i <= num//2:
        if num%i == 0:
            sum+=i
        i+=1
    if sum == temp:
        st.success("GIVEN NUMBER IS A PERFECT NUMBER ")
    else:
        st.error("GIVEN NUMBER IS NOT A PERFECT NUMBER ")

elif armstrongnum:
    temp = num
    temp1 = num
    count = 0
    while temp >0:
        count+=1
        temp //=10
    while temp1 > 0:
        rem = temp1 % 10
        sum = sum+(rem**count)
        temp1 = temp1//10
    if num == sum:
        st.success("GIVEN NUMBER IS AN ARMSTRONG NUMBER ")
    else:
        st.error("GIVEN NUMBER IS NOT AN ARMSTRONG NUMBER ")

elif disariannum:
    temp = num
    temp1 = num
    count=0
    sum=0
    while temp > 0:
        count+=1
        temp = temp//10
    while temp1 > 0:
        rem = temp1 % 10
        sum += (rem**count)
        count-=1
        temp1 //=10
    if num == sum:
        st.success("GIVEN NUMBER IS A DISARIAN NUMBER ")
    else:
        st.error("GIVEN NUMBER IS NOT A DISARIAN NUMBER ")
    
elif strongnum:
    temp = num
    total = 0
    while temp > 0:
        rem = temp % 10
        fact = 1
        i = 1
        while i <= rem:
            fact *= i
            i += 1
        total += fact
        temp = temp // 10
    if total == num:
        st.success("THE GIVEN NUMBER IS A STRONG NUMBER")
    else:
        st.error("GIVEN NUMBER IS NOT A STRONG NUMBER")

elif xylemphonum:
    temp = num
    sum_of_endelements = 0
    sum_of_remelements = 0
    while temp > 0:
        rem = temp % 10
        if temp == num or temp < 10:
            sum_of_endelements+=rem
        else:
            sum_of_remelements+=rem
        temp //=10
    if sum_of_endelements == sum_of_remelements:
        st.success("GIVEN NUMBER IS A XYLEM NUMBER ")
    else:
        st.success("GIVEN NUMBER IS A PHONUM NUMBER")
    
elif automorphicnum:
    temp = num
    square = num * num
    count = 0
    while temp > 0:
        count += 1
        temp = temp // 10
    last_digits = square % (10 ** count)
    if last_digits == num:
        st.success("GIVEN NUMBER IS AN AUTOMORPHIC NUMBER")
    else:
        st.error("GIVEN NUMBER IS NOT AN AUTOMORPHIC NUMBER")

elif fibnocciseries:
    st.subheader("FIBONACCI SERIES")
    a = 0
    b = 1
    i = 0
    lst = []  
    while num > 0:
        lst.append(a)
        c = a + b
        a = b
        b = c
        num -= 1
    st.success(lst)

else :
    no = int(input("Enter the number: "))

lst = []

while no != 1 and no not in lst:
    lst.append(no)

    total = 0
    temp = no

    while temp > 0:
        rem = temp % 10
        total += rem * rem
        temp = temp // 10

    no = total

if no == 1:
    st.success("Happy Number")
else:
    st.error("Not a Happy Number")


    

        














