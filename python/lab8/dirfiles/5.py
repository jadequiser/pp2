# def write(listik):
#     with open("failik.txt", 'w') as file:
#         for item in listik:
#             file.write(str(item) + '\n')


# listik = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,22,2,2]
# write(listik)



# print(f"Listik was added in failik.")


listik = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2]
file = open('failik.txt','w')
for item in listik:
            file.write(str(item) + '\n')
file.close()
print(f"Listik was added in failik.")
