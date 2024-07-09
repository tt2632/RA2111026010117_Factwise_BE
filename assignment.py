def num(n):
    if n==0:
        return "zero"
    if n<20:
        return["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","ninetten"][n]
    if n<100:
        return["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"][n//10]+ ("" if n% 10==0 else num(n%10))
    if n<1000:
        return num(n//100)+"hundred"+("" if n%100==0 else "and" + num(n%100))
    if n==1000:
        return "onethousand"

words_sum= sum(len(num(i).replace(" ","").replace("-","")) for i in range(1,1001))
print(words_sum)
