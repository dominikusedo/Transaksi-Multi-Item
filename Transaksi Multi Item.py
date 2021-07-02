# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 10:22:53 2021

@author: Dominikus Edo Kristian - 20083000121
"""
print("===========================================")
print(" KANTIN FAKULTAS TEKNOLOGI INFORMASI UNMER ")
print("===========================================")
print("MENU MAKANAN :")
print("-------------------------------------------")
print(" a = NASI GORENG                  Rp 15.000")
print(" b = LONTONG GORENG               Rp 14.900")
print(" c = BAKSO GORENG                 Rp 12.900")
print(" d = RUJAK GORENG                 Rp 13.000")
print(" e = RUJAK BAKSO                  Rp 15.000")
print(" f = RUJAK BAKSO PECEL            Rp 17.000")
print("-------------------------------------------")
print("MENU MINUMAN :")
print("-------------------------------------------")
print(" a = TEH DINGIN / HANGAT / PANAS   Rp 2.500")
print(" b = KOPI DINGIN                   Rp 5.000")
print(" c = KOPI TEH PANAS                Rp 6.500")
print(" d = COCA COLA DINGIN              Rp 3.500")
print(" e = COCA COLA PANAS               Rp 5.000")
print("===========================================")

kodeMakanan = ['a','b','c','d','e','f']
kodeMinuman = ['a','b','c','d','e']
namaMakanan = ['NASI GORENG','LONTONG GORENG','BAKSO GORENG','RUJAK GORENG','RUJAK BAKSO','RUJAK BAKSO PECEL']
namaMinuman = ['TEH DINGIN / HANGAT / PANAS','KOPI DINGIN','KOPI TEH PANAS','COCA COLA DINGIN','COCA COLA PANAS']
hargaMakanan = [15000,14900,12900,13000,15000,17000]
hargaMinuman = [2500,5000,6500,3500,5000]
pesanmakanan = []
pesanminuman = []
jumlahmakanan = []
jumlahminuman = []
hargamakanan = []
hargaminuman = []
jmlhargamakanan = []
jmlhargaminuman = []

ulangi = "y"
while ulangi=="y" or ulangi=="Y":
    pilihan = input(">> Pilih Makanan / Minuman? a / b = ")
    if pilihan=="a":
        pilihanMakanan  = input(">> Pilih Makanan           = ")
        qty             = input(">> Masukkan Jumlah Barang  = ")
        jumlahmakanan.append(qty)
    elif pilihan=="b":
        pilihanMinuman  = input(">> Pilih Minuman           = ")
        qty             = input(">> Masukkan Jumlah Barang  = ")
        jumlahminuman.append(qty)
    
    i = 0
    while i<len(namaMakanan) and pilihan =="a":
        if pilihanMakanan == kodeMakanan[i]:
            nm_mkn = namaMakanan[i]
            hrg_mkn = hargaMakanan[i]
            jml_mkn = hrg_mkn * int(qty)
            pesanmakanan.append(nm_mkn)
            hargamakanan.append(hrg_mkn)
            jmlhargamakanan.append(jml_mkn)
            print(">>> NAMA MAKANAN     : " + nm_mkn)
            print(">>> HARGA SATUAN     : " + str(hrg_mkn))
            print(">>> JUMLAH           : " + qty)
        i+=1
    while i<len(namaMinuman) and pilihan =="b":
        if pilihanMinuman == kodeMinuman[i]:
            nm_mnm = namaMinuman[i]
            hrg_mnm = hargaMinuman[i]
            jml_mnm = hrg_mnm * int(qty)
            pesanminuman.append(nm_mnm)
            hargaminuman.append(hrg_mnm)
            jmlhargaminuman.append(jml_mnm)
            print(">>> NAMA MINUMAN     : " + nm_mnm)
            print(">>> HARGA SATUAN     : " + str(hrg_mnm))
            print(">>> JUMLAH           : " + qty)
        i+=1
    ulangi = input(">> Tambah Lagi ? y/t = ")
    if ulangi== "t" or ulangi =="T":
        print("===========================================")
        print(" KANTIN FAKULTAS TEKNOLOGI INFORMASI UNMER ")
        print("===========================================")
        print("RINCIAN PEMBAYARAN :")
        print("-------------------------------------------")
        print("MAKANAN :")
        print("-------------------------------------------")
        print("NAMA BARANG"+" - "+"HARGA SATUAN"+" - "+"JUMLAH")
        print("-------------------------------------------")
        p=0
        while p<len(pesanmakanan):
            print(pesanmakanan[p]+" - "+str(hargamakanan[p])+" - "+str(jumlahmakanan[p]))
            p+=1
        tothargamakanan = sum(jmlhargamakanan)
        print("-------------------------------------------")
        print("TOTAL HARGA MAKANAN = " + str(tothargamakanan))
        print("-------------------------------------------")
        print("MINUMAN :")
        print("-------------------------------------------")
        print("NAMA BARANG"+" - "+"HARGA SATUAN"+" - "+"JUMLAH")
        print("-------------------------------------------")
        p=0
        while p<len(pesanminuman):
            print(pesanminuman[p]+" - "+str(hargaminuman[p])+" - "+str(jumlahminuman[p]))
            p+=1
        tothargaminuman = sum(jmlhargaminuman)
        print("-------------------------------------------")
        print("TOTAL HARGA MINUMAN = " + str(tothargaminuman))
        print("-------------------------------------------")
        totharga = tothargamakanan + tothargaminuman
        print(">>> TOTAL TAGIHAN = " + str(totharga))
        bayar = input(">>> UANG DIBAYARKAN   = ")
        kembali = int(bayar) - totharga
        print(">>> TOTAL KEMBALIAN = " + str(kembali))
        break
