state = 0
NOTHING,FIRST,MIDDLE,LAST,LAST2 = 0,1,2,3,4
string = input()

cons = {'r','R','s','e','E','f','a','q','Q','t','T','d','w','W','c','z','x','v','g'}
vowels = {'k','o','i','O','j','p','u','P','h','y','n','b','m','l'}
cons_mix = {'rt','sw','sg','fr','fa','fq','ft','fx','fv','fg','qt'}
cons_first = {'E','Q','W'}
ans = 0

for i in range(len(string)):
    s = string[i]
    if state == NOTHING and s != ' ':
        state = FIRST

    elif state == FIRST:
        state = MIDDLE

    elif state == MIDDLE:
        if s in vowels:
            state = MIDDLE
        elif s in cons_first:
            state = FIRST
        elif s in cons:
            state = LAST
        elif s == ' ':
            state = NOTHING

    elif state == LAST:
        if s == ' ':
            state = NOTHING
        elif string[i-1]+s in cons_mix:
            state = LAST2
        elif s in vowels:
            ans += 1
            state = MIDDLE
        elif s in cons:
            state = FIRST

    elif state == LAST2:
        if s == ' ':
            state = NOTHING
        elif s in cons:
            state = FIRST
        elif s in vowels:
            ans += 1
            state = MIDDLE

print(ans)
