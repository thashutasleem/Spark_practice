import shutil
import time


def main():
    for i in range(20):
        time.sleep(5)
        file_generator(i)

def file_generator(count):
    shutil.copyfile('text_file.txt','files/file{}.txt'.format(count))
    print("generating  file  {}".format(count))

if __name__ == '__main__':
    main()
