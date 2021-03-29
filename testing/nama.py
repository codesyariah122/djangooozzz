def panggil():
	nama = input("Siapa nama kamu ? ")
	jawaban = "Hai, {} ... Selamat datang ! ".format(nama) if nama != "" else "Nama harus di isi"

	print(jawaban)