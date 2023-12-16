import os
from os.path import join, dirname
from dotenv import load_dotenv

from pymongo import MongoClient
import hashlib #untuk enkripsi, sudah bawaan

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME =  os.environ.get("DB_NAME")

client = MongoClient(MONGODB_URI)

db = client[DB_NAME]


# filename = True

# if filename:
#     nama = 'arif'

# doc = {'nama' : nama}
# print(doc)


# name ='test'
# twins1 = list(db.users.find({'profile_info' : {'$regex' : name, '$options': 'i'}}))
# twins2 = list(db.users.find({'username' : {'$regex' : name, '$options': 'i'}}))

# if twins1 : print(twins1[1]['profile_info'])

# elif twins2 : print(twins2[1]['username'])

# else : print('tidak ada')


# if os.path.exists('./static/gunung_pics/test123.jpg'):
#     os.remove('./static/gunung_pics/test123.jpg')
#     print('file dihapus')
# else:
    # print('file tidak ditemukan')

# list_nama = [{'nama' : 'arif'},{'nama' : 'brody'},{'nama' : 'coyy'}]
# for nama in list_nama : 
#     nama['status'] = 'jomblo'

# print(list_nama)

# list_nama = [{'nama' : 'arif', 'umur' : '20'},{'nama' : 'brody', 'umur' : '25'},{'nama' : 'coyy', 'umur' : '21'}]
# jumlah_item = len(list_nama)
# print(jumlah_item)

# sorted_list = sorted(list_nama, key=lambda x: x['umur'], reverse=True)

# for item in sorted_list:
#     print(item)


# nama = 'arif'
# try:
#     namaBaru = nama.split(' ')[1]
#     print(namaBaru+"hai")
# except :
#     namaBaru = nama.split(' ')[0]
#     print(namaBaru+"halo")

# nama='arif'
# namaSplit=nama.split(' ')
# for nama in namaSplit: print(nama)





# pw_hash = hashlib.sha256("puncak123".encode("utf-8")).hexdigest()
# doc = {
#         "useremail" : "arifdwiprasetya14@gmail.com",
#         "username"  : "Arif Dwi Prasetya",
#         "password"  : pw_hash,
#         "role"      : "admin"
#     }
# db.users.insert_one(doc)

# my_list = [
#     {"nama": "John", "umur": 20},
#     {"nama": "Jane", "umur": 25},
#     {"nama": "Bob", "umur": 10},
#     {"nama": "Alice", "umur": 30},
#     {"nama": "Charlie", "umur": 10},
# ]

# # Menggunakan list comprehension untuk membuat list baru tanpa dictionary yang memiliki umur 10
# filtered_list = [person for person in my_list if person["umur"] != 10]

# # Memodifikasi list awal dengan menggantinya dengan list yang sudah difilter
# my_list = filtered_list

# print(my_list)



# doc = {
#             'nama_gunung' : 'Gunung Cubu Cubu',
#             'provinsi_gunung' : 'Sumatera Barat',
#             'ketinggian_gunung' : '1200 mdpl',
#             'gambar_gunung' : 'bg_gunung.jpg',
#             'link_gmaps' : '',
#             'link_iframe' : '',
#             'deskripsi_umum' : 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Odit cupiditate tempora, molestiae earum facilis fugit libero doloremque illo necessitatibus dolorum soluta ipsum provident, reiciendis at dolore rem et nisi nesciunt!',
#             'deskripsi_perlengkapan' : '',
#             'deskripsi_peringatan' : ''
#         }

# db.gunung.insert_one(doc)


# doc = {
#     'id_gunung' : "657a60c7ad94931ea9d005d0",
#     'useremail' : "arifdwiprasetya@gmail.com"
# }

# db.likes.insert_one(doc)


query_result = bool(db.likes.find_one({
    'id_gunung' : "657a60c7ad94931ea9d005d0",
    'useremail' : "arifdwiprasetya@gmail.com",
    }))

print(query_result)
