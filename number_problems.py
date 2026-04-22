import streamlit as st

st.title("NUMBER PROBLEMS")

num = st.number_input("ENTER THE NUMBER", min_value=0, step=1)

st.subheader("""HERE YOU CAN CHECK:
                * SUM OF DIGITS
                * FACTORIAL
                * REVERSE NUMBER
                * PALINDROME
                * SPY NUMBER
                * PERFECT NUMBER
                * ARMSTRONG NUMBER
                * DISARIAN NUMBER
                * STRONG NUMBER
                * XYLEM OR PHLOEM
                * AUTOMORPHIC NUMBER
                * FIBONACCI SERIES
                * HAPPY NUMBER
            """)

sum_btn = st.button("SUM OF DIGITS")
fact_btn = st.button("FACTORIAL")
rev_btn = st.button("REVERSE NUMBER")
pal_btn = st.button("PALINDROME")
spy_btn = st.button("SPY NUMBER")
perfect_btn = st.button("PERFECT NUMBER")
arm_btn = st.button("ARMSTRONG NUMBER")
dis_btn = st.button("DISARIAN NUMBER")
strong_btn = st.button("STRONG NUMBER")
xylem_btn = st.button("XYLEM OR PHLOEM")
auto_btn = st.button("AUTOMORPHIC NUMBER")
fib_btn = st.button("FIBONACCI SERIES")
happy_btn = st.button("HAPPY NUMBER")

# SUM
if sum_btn:
    temp = num
    total = 0
    while temp > 0:
        rem = temp % 10
        total += rem
        temp //= 10
    st.success(total)
    st.subheader("""LOGIC:
                temp = num
                total = 0
                while temp > 0:
                    rem = temp % 10
                    total += rem
                    temp //= 10
                """)

# FACTORIAL
elif fact_btn:
    temp = num
    fact = 1
    while temp > 0:
        fact *= temp
        temp -= 1
    st.success(fact)

    st.subheader("""LOGIC:
                temp = num
                fact = 1
                while temp > 0:
                    fact *= temp
                    temp -= 1""")

# REVERSE
elif rev_btn:
    temp = num
    rev = 0
    while temp > 0:
        rem = temp % 10
        rev = rev * 10 + rem
        temp //= 10
    st.success(rev)

    st.subheader("""LOGIC:
                temp = num
                rev = 0
                while temp > 0:
                    rem = temp % 10
                    rev = rev * 10 + rem
                    temp //= 10""")

# PALINDROME
elif pal_btn:
    temp = num
    rev = 0
    while temp > 0:
        rem = temp % 10
        rev = rev * 10 + rem
        temp //= 10
    if rev == num:
        st.success("PALINDROME")
    else:
        st.error("NOT A PALINDROME")

    st.subheader("""LOGIC:
                temp = num
                rev = 0
                while temp > 0:
                    rem = temp % 10
                    rev = rev * 10 + rem
                    temp //= 10
                if rev == num:
                    st.success("PALINDROME")
                else:
                    st.error("NOT A PALINDROME")
            """)

# SPY NUMBER
elif spy_btn:
    temp = num
    total = 0
    pro = 1
    while temp > 0:
        rem = temp % 10
        total += rem
        pro *= rem
        temp //= 10
    if total == pro:
        st.success("SPY NUMBER")
    else:
        st.error("NOT A SPY NUMBER")

    st.subheader("""LOGIC:
                temp = num
                total = 0
                pro = 1
                while temp > 0:
                    rem = temp % 10
                    total += rem
                    pro *= rem
                    temp //= 10
                if total == pro:
                    st.success("SPY NUMBER")
                else:
                    st.error("NOT A SPY NUMBER")""")

# PERFECT NUMBER
elif perfect_btn:
    i = 1
    total = 0
    while i <= num // 2:
        if num % i == 0:
            total += i
        i += 1
    if total == num:
        st.success("PERFECT NUMBER")
    else:
        st.error("NOT A PERFECT NUMBER")

    st.subheader("""LOGIC:
                i = 1
                total = 0
                while i <= num // 2:
                    if num % i == 0:
                        total += i
                    i += 1
                if total == num:
                    st.success("PERFECT NUMBER")
                else:
                    st.error("NOT A PERFECT NUMBER")
            """)

# ARMSTRONG
elif arm_btn:
    temp = num
    count = 0
    total = 0

    while temp > 0:
        count += 1
        temp //= 10

    temp = num
    while temp > 0:
        rem = temp % 10
        total += rem ** count
        temp //= 10

    if total == num:
        st.success("ARMSTRONG NUMBER")
    else:
        st.error("NOT AN ARMSTRONG NUMBER")

    st.subheader("""LOGIC:
                temp = num
                count = 0
                total = 0

                while temp > 0:
                    count += 1
                    temp //= 10

                temp = num
                while temp > 0:
                    rem = temp % 10
                    total += rem ** count
                    temp //= 10

                if total == num:
                    st.success("ARMSTRONG NUMBER")
                else:
                    st.error("NOT AN ARMSTRONG NUMBER")""")

# DISARIAN
elif dis_btn:
    temp = num
    count = 0
    total = 0

    while temp > 0:
        count += 1
        temp //= 10

    temp = num
    while temp > 0:
        rem = temp % 10
        total += rem ** count
        count -= 1
        temp //= 10

    if total == num:
        st.success("DISARIAN NUMBER")
    else:
        st.error("NOT A DISARIAN NUMBER")
    
    st.subheader("""LOGIC:
                temp = num
                count = 0
                total = 0

                while temp > 0:
                    count += 1
                    temp //= 10

                temp = num
                while temp > 0:
                    rem = temp % 10
                    total += rem ** count
                    count -= 1
                    temp //= 10

                if total == num:
                    st.success("DISARIAN NUMBER")
                else:
                    st.error("NOT A DISARIAN NUMBER")""")

# STRONG NUMBER
elif strong_btn:
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
        temp //= 10

    if total == num:
        st.success("STRONG NUMBER")
    else:
        st.error("NOT A STRONG NUMBER")

    st.subheader("""LOGIC:
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
                    temp //= 10

                if total == num:
                    st.success("STRONG NUMBER")
                else:
                    st.error("NOT A STRONG NUMBER")""")

# XYLEM / PHLOEM
elif xylem_btn:
    temp = num
    sum_end = 0
    sum_mid = 0

    while temp > 0:
        rem = temp % 10
        if temp == num or temp < 10:
            sum_end += rem
        else:
            sum_mid += rem
        temp //= 10

    if sum_end == sum_mid:
        st.success("XYLEM NUMBER")
    else:
        st.success("PHLOEM NUMBER")

    st.subheader("""LOGIC:
                temp = num
                sum_end = 0
                sum_mid = 0

                while temp > 0:
                    rem = temp % 10
                    if temp == num or temp < 10:
                        sum_end += rem
                    else:
                        sum_mid += rem
                    temp //= 10

                if sum_end == sum_mid:
                    st.success("XYLEM NUMBER")
                else:
                    st.success("PHLOEM NUMBER")""")

# AUTOMORPHIC
elif auto_btn:
    square = num * num
    temp = num
    count = 0

    while temp > 0:
        count += 1
        temp //= 10

    if square % (10 ** count) == num:
        st.success("AUTOMORPHIC NUMBER")
    else:
        st.error("NOT AN AUTOMORPHIC NUMBER")

    st.subheader("""LOGIC:
                square = num * num
                temp = num
                count = 0

                while temp > 0:
                    count += 1
                    temp //= 10

                if square % (10 ** count) == num:
                    st.success("AUTOMORPHIC NUMBER")
                else:
                    st.error("NOT AN AUTOMORPHIC NUMBER")""")

# FIBONACCI
elif fib_btn:
    a, b = 0, 1
    count = num
    series = []

    while count > 0:
        series.append(a)
        a, b = b, a + b
        count -= 1

    st.success(series)

    st.subheader("""LOGIC:
                a, b = 0, 1
                count = num
                series = []

                while count > 0:
                    series.append(a)
                    a, b = b, a + b
                    count -= 1

                st.success(series)""")

# HAPPY NUMBER
elif happy_btn:
    no = num
    visited = set()

    while no != 1 and no not in visited:
        visited.add(no)
        total = 0

        while no > 0:
            rem = no % 10
            total += rem * rem
            no //= 10

        no = total

    if no == 1:
        st.success("HAPPY NUMBER")
    else:
        st.error("NOT A HAPPY NUMBER")

    st.subheader("""LOGIC:
                no = num
                visited = set()

                while no != 1 and no not in visited:
                    visited.add(no)
                    total = 0

                    while no > 0:
                        rem = no % 10
                        total += rem * rem
                        no //= 10

                    no = total

                if no == 1:
                    st.success("HAPPY NUMBER")
                else:
                    st.error("NOT A HAPPY NUMBER")""")

    

        














