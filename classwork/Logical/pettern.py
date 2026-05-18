# for i in range(5):
#     for j in range(5):
#         print('*', end=" ")
#     print()

# *
# **
# ***
# ****
# *****

# for j in range(5):
#     for i in range(j+1):
#         print('*', end=" ")
#     print()

# for j in range(5):
#     print("*"*(j + 1))

# *****
# ****
# ***
# **
# *

# lines = 5
# for j in range(lines):
#     for i in range( lines - j ):
#         print("*", end=" ")
#     print()

# * * * * *
# * * * *
# * * *
# * *
# *

# lines = 5
# for j in range(lines):
#     for k in range(j):
#         print(" ", end=" ")
#     for i in range(lines - j):
#         print("*", end=" ")
#     print()

#     *
#    * *
#   * * *
#  * * * *
# * * * * *

# lines = 5
# for j in range(lines):
#     for k in range(lines - j):
#         print(" ", end="")
#     for i in range(j + 1):
#         print("* ", end="")
#     print()

# * * * * *
#  * * * *
#   * * *
#    * *
#     *

# lines = 5
# for j in range(lines):
#     for k in range(j + 1):
#         print(" ", end="")
#     for i in range(lines - j):
#         print("* ", end="")
#     print()

# Home work Dimond pettern and whole dimond border on show star
# Home work

# k = 1
# lines = 5
# for j in range(lines):
#     for i in range(j + 1):
#         print(k, end="")
#         k += 1
#     print()

# 0
# 10
# 010
# 1010
# 01010

# lines = 5
# for j in range(lines):
#     for i in range(j + 1):
#         print((i + j)%2, end="")
#     print()


#Python Project
# ----Class Practice
# ----Project
# ----Assignment

# Home Work
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

# lines = 10
# for j in range(lines):
#     if j < 5:
#         k_condition = lines - j
#         i_condition = j + 1
#     else:
#         k_condition = j + 1
#         i_condition = lines - j

#     for k in range(k_condition):
#         print(" ", end="")
#     for i in range(i_condition):
#         print("* ", end="")
#     print()

#      *
#     * *
#    *   *
#   *     *
#  *       *
#  *       *
#   *     *
#    *   *
#     * *
#      *

# lines = 5
# mid = lines // 2
# for j in range(lines):
#     if j < mid:
#         space = lines - j
#         stars = j + 1
#     else:
#         space = j + 1
#         stars = lines - j
#     for k in range(space):
#         print(" ", end="")
#     for i in range(stars):
#         if i == 0 or i == stars - 1:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()

# k = 1
# lines = 5
# for j in range(lines):
#     for i in range(j + 1):
#         print(k, end="")
#         k += 1
#     print()  

# 5
# 45
# 345
# 2345
# 12345

k = 5
lines = 5
for j in range(lines):
    for i in range(j + 1):
        print(k -  (j - i), end="")
        # k -= 1
    print()