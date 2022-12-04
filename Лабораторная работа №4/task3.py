def delete(list_, index=None):
    return list_[:index] + list_[-1:index:-1][::-1]

print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2], index=2))  # [0, 1]
