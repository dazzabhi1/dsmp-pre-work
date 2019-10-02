# --------------
##File path for the file 
file_path 
def read_file(path):
    file = open(path , 'r')
    sentence = file.readline()
    file.close()
    return sentence

sample_message=read_file(file_path)


#Code starts here


# --------------
#Code starts here
file_path_1
file_path_2

def read_file(path1,path2):
    file1=open(path1 , 'r')
    file2=open(path2 , 'r')
    
    cod_1 = file1.readline()
    cod_2=file2.readline()
    return(cod_1,cod_2)
    file1.close()
    file2.close()

message_1, message_2=read_file(file_path_1,file_path_2)
print(message_1,message_2)

def fuse_msg(message_a , message_b):
    quotient= int(message_b) // int(message_a)
    return(str(quotient))

secret_msg_1=fuse_msg(message_1,message_2)
print(secret_msg_1)





# --------------
#Code starts here
file_path_3

def read_file(path):
    file=open(path,'r')
    file_1=file.readline()

    file.close()
    return file_1

message_3=read_file(file_path_3)
print(message_3)
def substitute_msg(message_c):
      if(message_c=='Red'):
            sub="Army General"
            return sub
      elif(message_c=='Green'):
            sub="Data Scientist"
            return sub
      else:
            sub="Marine Biologist"
            return sub

secret_msg_2=substitute_msg(message_3)
print(secret_msg_2)


# --------------
# File path for message 4  and message 5
file_path_4
file_path_5

def read_file(path1,path2):
    file4=open(path1,'r')
    file5=open(path2,'r')

    mess_4=file4.readline()
    mess_5=file5.readline()

    file4.close()
    file5.close()
    return (mess_4,mess_5)

message_4,message_5=read_file(file_path_4,file_path_5)
print(message_4,message_5)

def compare_msg(message_d,message_e):
    a_list=message_d.split()
    b_list=message_e.split()
    c_list=[x for x in a_list if not x in b_list]
    final_msg=" ".join(c_list)
    return final_msg

secret_msg_3=compare_msg(message_4,message_5)
print(secret_msg_3)

#Code starts here







# --------------
#Code starts here
file_path_6

def read_file(path):
    file=open(path,'r')

    mess=file.readline()
    file.close()
    return (mess)

message_6=read_file(file_path_6)
print(message_6)

def extract_msg(message_f):
    a_list=message_f.split()
    #even_word=lambda x:(len(x)%2==0)
    #print(even_word(a_list))
    b_list=list(filter(lambda x:len(x)%2==0,a_list))
    final_msg=" ".join(b_list)
    print(a_list)
    print(final_msg)
    return final_msg

secret_msg_4=str(extract_msg(message_6))
print(secret_msg_4)



# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]


final_path= user_data_dir + '/secret_message.txt'

#Code starts here
secret_msg=" ".join(message_parts)
print(secret_msg)

def write_file(secret_msg,path):
    file=open(path,'a+')
    file.write(secret_msg)
    file.close()

finalcode=write_file(secret_msg,final_path)



