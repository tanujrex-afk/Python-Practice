amount= float(input("enter the amount:"))
if amount >= 10000:
    discount=20
elif amount >=5000:
    discount=10
elif amount>=2000:
    discount=5
else: 
    discount=0 
discount_amount=amount*discount/100
final_amount= amount-discount_amount
print("Original amount :", amount)
print("Discount :",discount,"%")
print("discount amount:",discount_amount)
print("final amount:", final_amount)
