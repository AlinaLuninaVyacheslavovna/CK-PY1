def delete(list_, index=None):
    if index==None or index==-1:
        return list_[:-1]
    elif index < 0:
        return list_[index - 1::-1][::-1] +list_[-1:index:-1][::-1]
    return list_[:index] + list_[index + 1:]

print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
