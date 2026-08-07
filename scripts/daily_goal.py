TARGET = 76

def remaining(done):
    return max(TARGET - done, 0)

if __name__ == '__main__':
    print('contributions left today:', remaining(54))
