# ☕️ Loyalty Points Engine Challenge
#
# RULES:
# • Each whole dollar spent earns 3 points
# • Tiers:
#     < 100 pts   →  Bronze
#     100-499 pts → Silver
#     ≥ 500 pts   →  Gold
#
# STEPS:
# 1. Define earn_points(price) → returns points for one purchase
# 2. Define tier_label(points) → returns "Bronze" / "Silver" / "Gold"
# 3. Given the hard-coded list `purchases`,
#    loop through it, call earn_points() for each amount,
#    and add the result to total_points.
# 4. After the loop, call tier_label(total_points)
# 5. Print 'Loyalty Summary':
#       • Total dollars spent
#       • Total points earned
#       • Final tier

# Purchase history (e.g., 3.75, 7.20, etc.)
purchases = [12.3,35.5,34,6.7,34.7,3.2,5.8,16.9,18.7,28.7]
total_Doller_spent=0.00
total_points=0
tier=[
    (0,100,"Bronze"),
    (100,500,"Silver"),
    (500,float('inf'),"Gold")
]

def earn_points(price):
    if price>1:
        wholedoller=int(price)
        return wholedoller*3
    else :
        print("Spended money is not enough to earn points !")
        return 0
        
def tier_label(points):
    for low,high,label in tier:
        if low <= points < high:
            return label

for amt in purchases:
    total_Doller_spent+=amt
    total_points+=earn_points(amt)

finaltier=tier_label(total_points)

print("\n===Loyalty Summary===")
print(f"\nTotal amount Spent : {total_Doller_spent}")
print(f"\nTotal Points earned : {total_points}")
print(f"final Tier Earned : {finaltier}")







# tier_label(501)
        
        
        
        
        
        
        