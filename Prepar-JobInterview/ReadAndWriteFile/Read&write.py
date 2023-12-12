try:
    readFile = open('demoFile.txt')
    try:
        readFile.write("my Name is not Hasibullah Aman now")
    except:
        print("you can't write in file")
    finally:
        readFile.close()
except:
    print('some error in reading file')
