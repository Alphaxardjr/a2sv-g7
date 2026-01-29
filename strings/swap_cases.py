def swap_case(s):
    modigified = ""
    for st in s:
        if st.lower == st:
            modigified += st.upper()
        else:
            modigified += st.lower()
    return modigified

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)