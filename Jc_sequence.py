import os.path


def booting_data():
    path = 'my_sequence.txt'
    if os.path.isfile(path):
        pass
    else:
        x = '이름\t입력값\t모듈번호\n시작\t0\t0\n'
        list = open('my_sequence.txt', 'w', encoding='UTF-8')
        list.write(x)
        list.close()

    path = 'cnt.txt'
    if os.path.isfile(path):
        pass
    else:
        x = '1'
        list = open('cnt.txt', 'w', encoding='UTF-8')
        list.write(x)
        list.close()

    path = 'cnt2.txt'
    if os.path.isfile(path):
        pass
    else:
        x = '1'
        list = open('cnt2.txt', 'w', encoding='UTF-8')
        list.write(x)
        list.close()

def reset_sequence():
    x = '이름\t입력값\t모듈번호\n시작\t0\t0\n'
    list = open('my_sequence.txt', 'w', encoding='UTF-8')
    list.write(x)
    list.close()

def save_sequence():
    file=open('cnt.txt','r',encoding='UTF-8')
    cnt=file.read()
    file.close()
    file=open('my_sequence.txt','r',encoding='UTF-8')
    datas=file.readlines()
    file.close()
    data=''
    for i in range(len(datas)):
        data+=datas[i]
    save=open('save_sequence_{}.txt'.format(cnt),'w',encoding='UTF-8')
    save.write(data)
    save.close()
    cnt=int(cnt)+1
    list = open('cnt.txt', 'w', encoding='UTF-8')
    list.write(str(cnt))
    list.close()

def import_sequence(txt):
    file=open(txt,'r',encoding='UTF-8')
    datas=file.read()
    file.close()
    file=open('my_sequence.txt','w',encoding='UTF-8')
    file.write(datas)
    file.close()

def read_my_sequence():
    file=open('my_sequence.txt','r',encoding='UTF-8')
    lines=file.readlines()
    file.close()
    for i in range(len(lines)):
        lines[i]=lines[i].strip().split('\t')
    return lines

def up_sequence(ndex):
    lines = read_my_sequence()
    lines=lines[1:]
    a=lines[ndex]
    b=lines[ndex-1]
    lines[ndex]=b
    lines[ndex-1]=a
    data=''
    for i in range(len(lines)):
        for m in range(len(lines[i])):
            data += lines[i][m]
            if m == (len(lines[i]) - 1):
                break
            else:
                data += '\t'
        data += '\n'
    file=open('my_sequence.txt','w',encoding='UTF-8')
    file.write('이름\t입력값\t모듈번호\n')
    file.write(data)
    file.close()

def dn_sequence(ndex):
    lines = read_my_sequence()
    lines=lines[1:]
    a=lines[ndex]
    b=lines[ndex+1]
    lines[ndex]=b
    lines[ndex+1]=a
    data=''
    for i in range(len(lines)):
        for m in range(len(lines[i])):
            data += lines[i][m]
            if m == (len(lines[i]) - 1):
                break
            else:
                data += '\t'
        data += '\n'
    file=open('my_sequence.txt','w',encoding='UTF-8')
    file.write('이름\t입력값\t모듈번호\n')
    file.write(data)
    file.close()

def import_txt(txt):
    path = txt
    if os.path.isfile(path):
        import_sequence(path)
        return True
    else:
        return False

def del_sequence(ndex):
    lines = read_my_sequence()
    lines = lines[1:]
    del lines[ndex]
    data=''
    for i in range(len(lines)):
        for m in range(len(lines[i])):
            data += lines[i][m]
            if m == (len(lines[i]) - 1):
                break
            else:
                data += '\t'
        data += '\n'
    file=open('my_sequence.txt','w',encoding='UTF-8')
    file.write('이름\t입력값\t모듈번호\n')
    file.write(data)
    file.close()

def add_sequence(txt,values,num):
    file=open('my_sequence.txt','a',encoding='UTF-8')
    file.write('{}\t{}\t{}\n'.format(txt,values,num))
    file.close()

def dup_sequence(ndex):
    file=open('my_sequence.txt','r',encoding='UTF-8')
    lines=file.readlines()
    file.close()
    lines=lines[1:]
    x=lines[ndex]
    file=open('my_sequence.txt','a',encoding='UTF-8')
    file.write(x)
    file.close()

if __name__ == '__main__':
    print(read_my_sequence())