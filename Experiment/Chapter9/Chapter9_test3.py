def copy(src_file, dst_file):
        fr = open(src_file, 'rb')
        fw = open(dst_file, 'wb')
        while True:
            b = fr.read()
            if not b:
                break
            fw.write(b)
        fw.close()
copy('test.txt','test2.txt')