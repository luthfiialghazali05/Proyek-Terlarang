﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    import random

#ASSETS DECLARATION
# Definisi Character
define Sulthan = Character("Sulthan")
define Dhika = Character("Dhika")
define Serena = Character("Serena")
define Rika = Character("Mbak Rika")

# Image Buat Character
image mc_gray = "mc_gray.png"
image Serena = "ibu mc.png"
image Sulthan = "mc.png"

# Image Buat Backgroun
image RTengah = "background/Ruang tengah.jpg"
image RKantor = "background/Ruang Kantor.JPG"

#==========================================================================================
# The game starts here.
define flash = Fade(.05, 0, .75, color="#fff")

#Scene 1
label start:
    stop music
    scene white
    play audio "Petir.mp3" volume 1.5
    scene black with Fade(0.5, 0, 1, color="#fff")
    
    # Teks pertama
    centered "Hujan deras menyelimuti seluruh wilayah kota. Angin berhembus kencang dan langit begitu gelap."

    # Teks kedua
    centered "Sulthan duduk di meja belajarnya sembari menatap keluar melalui jendela kamarnya."

    # Teks ketiga
    centered "Tatapan kosong tanpa harapan terpampang di raut wajahnya setelah tiga minggu lalu dokter mendiagnosanya menderita penyakit kulit langka yang mengharuskannya menjalani medical check-up." 
    
    centered "Semakin hari, kondisinya semakin memburuk. Harapan hidup menipis karena luka bakar telah menyelimuti hampir seluruh bagian tubuhnya, menyisakan bagian wajah yang masih bersih tanpa bekas."

    # Background flashings
    play audio "Petir.mp3" volume 1.5
    play sound "Hujan.mp3" fadein 1 volume 0.6 loop
    scene black with flash

    show mc_gray at left 
    with dissolve
    Sulthan "..."

    Sulthan "Apakah hidupku akan berakhir seperti ini?"

    Sulthan "aku tidak tau lagi apa yang harus kulakukan. Tapi, apa yang menyebabkan aku seperti ini? setidaknya, aku ingin tau alasannya."

    stop sound fadeout 0.1
    play sound "Hujan.mp3" volume 0.05 loop
    play audio "door-knocking.mp3" volume 2

    pause(2.7)
    scene RTengah with fade
    show Sulthan at left 
    with dissolve

    pause(0.4)
    show Serena at right
    with dissolve
    Serena "Nak, Ibu boleh minta tolong kamu jemput Ayah ya di kantor, lagi hujan deras gini takut Ayah nggak bisa balik pakai bus."

    Sulthan "Boleh, Bu. Ayah udah dikabarin, kan?"

    Serena "Sudah, Nak."

    Sulthan "Baik bu, aku berangkat sekarang..."
    #di sini tambahin sesuatu yang nunjukin dia siap-siap trus nyalain mobil trus berangkats
    stop sound
    hide Sulthan with dissolve
    hide Serena with dissolve
    scene black with fade

    jump kantor

    return

label kantor:
    scene black
    #scene ruangan lobby kantor
    #play music "musik lobby" volume x
    show Sulthan at left with dissolve
    show Serena at right with dissolve

    Rika "huh??..."

    Rika "Ohh, Halo Sulthan! Mau ketemu Pak Dhika ya?"

    Sulthan "Hai Mbak Rika! Iya nih aku mau jemput Ayah. Ayah lagi di mana ya mbak?"

    Rika "Pak Dhika masih ada rapat bersama kliennya. Kamu mending tunggu aja di ruang kerjanya ya..."

    Sulthan "ohh, baiklah. Terima kasih mbak, aku tunggu di ruangan Ayah deh"

    hide Sulthan with dissolve
    hide Serena 

    #pindah scene ke ruangan ayah
    #sound effect buka pintu ruangan trus duduk
    scene RKantor with fade
    show Sulthan with dissolve
    Sulthan "Huft..."
    Sulthan "(dalam hati) Kenapa aku harus hidup seperti ini? Apakah aku akan memiliki penyakit ini seumur hidupku?"
    Sulthan "(dalam hati) Apakah benar kata orang-orang, bahwa penyakit ini... adalah efek dari proyek tambang yang baru beroperasi itu...."
    # kasih jeda kalo bisa sulthan meren dulu trus melek lagi
    Sulthan "lama banget ini ayah meeting... liat liat ruangan ayah ahh"
    "Sulthan beranjak dan melihat sekeliling. Ia membaca pigura, plakat, dan apa saja yang ada di ruangan ayah. Entah mengapa Ia merasakan dorongan untuk membuka laci meja Ayah"
    #play sound geser geser kertas, mainin kertas, buka laci
    #show sulthan bingung 
    "Sulthan membuka-buka dokumen dan laci meja ayah. Lalu pada salah satu laci di meja ayah, Sulthan menemukan kumpulan dokumen bersegel yang sudah terbuka. Ia pun membukanya"

    Sulthan "huh..."
    Sulthan "dokumen Apa ini..?"
    Sulthan "Hmmm..."
    Sulthan "(Membaca dokumen tersebut)...Teguran Kementrian Kesehatan........Operasi tambang daerah XXXXXX mengeluarkan limbah cair berbahaya.............Efek samping yang dirasakan manusia yang terpapar limbah tersebut adalah.....Luka...Bakar...Sekujur...Tubuh......."
    Sulthan "tch.... Jadi benar, proyek sialan itu yang menjadi penyebab penyakitku ini. Memang dasar pengusaha rakus keparat"
    "Anehnya, bersama dengan teguran Kementrian Kesehatan yang terdapat dalam dokumen yang disegel, bagaikan disembunyikan, ada surat lain yang tampak resmi"
    "Sebuah surat yang menunjukkan kop surat resmi bertuliskan 'Pemerintah Daerah' dan berjudul 'Surat Izin operasi'"
    Sulthan "Apa-apaan ini! Kenapa ayah menyimpan surat seperti ini?... Jangan-jangan..."
    "Surat Izin Operasi
    Dengan ini memberikan izin operasi kepada tambang di daerah XXXXXXX sampai waktu yang tidak ditentukan...
    .
    .
    .
    Disetujui oleh: Dhika Arduianto."
    Sulthan "HAH??! Bagaimana bisa? Ternyata selama ini..."
    "Mata Sulthan berkaca-kaca, tubuhnya gemetar melihat tanda tangan Ayahnya di lembar persetujuan surat izin operasi tambang itu. Proyek besar yang selama ini berada di dekat rumahnya. Proyek besar yang menyebabkan ia mengidap penyakit langka."
    Sulthan "Selama ini... Ayah sudah tau... Ayah sudah tau penyebab penderitaanku. Penderitaan yang mengancam masa depanku dan merusak masa mudaku. Ayah tau dan tetap membiarkan hal ini..."
    Sulthan "Ayah, Teganya kau... Semua ini... Karena Ayah..."
    hide Sulthan with dissolve
    pause(2.0)

    menu:
        "Apa yang akan kamu lakukan setelah ini?"
        "Konfrontasi langsung dengan ayah":
            jump confront
        "Pura-pura tidak tahu dan lakukan investigasi sendiri":
            jump investigate

label confront:
    scene black with fade
    scene RKantor with fade
    
    show Sulthan at right with dissolve
    "(Tidak lama, Dhika membuka pintu ruangannya)"
    show Dhika at left with dissolve
    Dhika "(Berjalan menghampiri Sulthan) Ada apa nak? Kenapa kamu menangis?"
    Sulthan "Ini semua karena Ayah! Ayah yang bikin aku jadi sakit gini."
    Dhika "Ayah bisa jelasin, itu semua tidak seperti yang kamu pikirkan."
    Sulthan "Ga seperti apa yang aku pikirin? Jelas - jelas disini ada tanda tangan Ayah berarti Ayah menyetujui proyek besar itu dong."
    Dhika "Iya memang benar ada tanda tangan Ayah disitu, tapi Ayah tidak bisa apa-apa. Ayah terpaksa menyetujui ini semua karena diancam. Kalau Ayah tidak setuju, yang ada hidup kamu dan ibu kamu dalam bahaya. Ayah juga tidak tahu kalau efeknya bakal seperti gini."
    Sulthan "Kenapa Ayah gapernah bilang hal ini ke aku atau Ibu?"
    Dhika "Ayah cuma gamau kalian khawatir. Semenjak Ayah tau kamu sakit, Ayah menyesal sejadi-jadinya. Ayah tidak minta kamu memaafkan Ayah, tapi biarkan Ayah coba perbaiki ini semua. Ayah cuma perlu kamu percaya sama Ayah."
    Sulthan "Gimana aku bisa percaya sama Ayah kalau Ayah sendiri menutupi ini semua dari aku dan Ibu? Memang Ayah pikir penyakit aku bisa disembuhin?"
    Dhika "Iya Ayah tau Ayah salah, tolong maafkan Ayah."
    Sulthan "(Dalam hati) Aku tau aku yang terkena imbas dari semua ini, tapi aku sadar Ayah tidak punya pilihan lain. Apakah aku harus mempercayai Ayahku?"
    
    centered "Pikiran Sulthan kacau. Sulthan paham bahwa Ayahnya tidak mempunyai pilihan. Namun, di sisi lain, Sulthan merasa dikhianati karena ialah yang terkena imbasnya. Sulthan mencoba untuk mempercayai Ayahnya dengan rasa ragu."
    
    sulthan "Ayah bilang Ayah sedang memperbaiki ini semua, memangnya Ayah mau melakukan apa? Ayah emang bisa balikin kondisi aku kayak dulu?"
    Dhika "Ayah sedang mengumpulkan bukti yang bisa mempercepat proses penutupan proyek ini. Nanti setelah proyek ini ditutup, Ayah akan fokus mencari cara untuk menyembuhkan kamu."
    hide Dhika with dissolve
    hide Sulthan with dissolve
    pause(2.0)

    menu:
        "Ayah telah dikonfrontasi, Apa yang akan kamu lakukan setelah ini?"
        "Percaya pada Ayah":
            jump believe
        "Lapor ke polisi":
            jump report

label investigate: 
    scene black with fade
    "Investigation..."
    "Coming soon"
    menu:
        "Kamu udah investigasi, Apa yang akan kamu lakukan setelah ini?"
        "Ayah menang":
            jump ending3
        "Sulthan menang":
            jump ending4

label believe:
    scene black with fade

    show Sulthan at right with dissolve
    show Dhika at left with dissolve
    Sulthan "Aku ingin percaya pada Ayah tapi apakah Ayah bisa berjanji padaku untuk mencari solusinya?"
    Dhika "Bisa, Ayah selama ini juga selalu mencari cara buat menyembuhkan kamu."
    Sulthan "(Dalam hati) Mungkin Ayah ada benarnya. Sepertinya aku bisa mempercayainya. Lagipula dia juga Ayahku."
    centered "Sulthan pun percaya pada Ayahnya dan bertekad untuk mendukung apapun yang Ayahnya lakukan. Sulthan dan Ayahnya mulai mengumpulkan semua bukti yang bisa menutup proyek tersebut dan mengakhiri semua penderitaan yang dialami."
    Sulthan "Apa yang bisa aku bantu, yah?"
    Dhika "Kita bisa mulai dengan meninjau seisi rumah dengan air yang terkontaminasi."
    Sulthan "Baiklah! Ayo kita pulang dan segera mencari bukti-buktinya!"
    # tambahin musik
    hide Dhika with dissolve
    Sulthan "(Dalam hati sambil menuruni tangga) Aku tidak percaya semua ini terjadi. 10 menit lalu aku sangat ingin menyerah dan saat ini Aku merasa sangat bahagia karena dapat menemukan penyebab masalah ini dan akan menyelesaikannya. Aku ingin cepat-cepat pulang."
    hide Sulthan with dissolve  
    scene black with fade
    pause(2.7)
    scene RTengah with fade

    centered "Mereka sampai di rumah. dengan cepat keluar dari mobil dan berjalan menuju pintu."

    show Sulthan at right with dissolve
    show Dhika at left with dissolve
    Dhika "Maaf, nak. Tampaknya hari sudah larut. Kita bisa memulainya esok hari karena Ayah harus bekerja."
    Sulthan "Yah, oke deh. Selamat tidur Ayah."
    hide Dhika with dissolve
    Sulthan "Ah padahal aku sudah sangat bersemangat. Gapapa deh aku bisa mulai esok hari."
    hide Dhika with dissolve
    scene black with fade
    pause (2.0)
    
    centered "Selang beberapa hari..."
    scene RTengah with Fade
    show Sulthan with dissolve
    Sulthan "Kok gak ada info apa-apa dari Ayah. Kapan bakal dimulai, ya? Apa aku inisiatif ya buat mulai? Gak deh, aku nunggu Ayah aja."
    hide Sulthan with dissolve
    scene black with fade
    pause (2.0)
    
    centered "Seminggu kemudian..."
    scene RTengah with fade
    show Serena at right with dissolve
    show Sulthan at left with dissolve
    Serena "Nak, obatnya diminum dulu ya, kondisimu sudah semakin buruk. Aktivitasmu dikurangi, ya."
    Sulthan "Ayah gimana, bu? Ayah sudah pulang?"
    Serena "Belum, nanti Ibu kabarin ya. Ibu turun dulu"
    hide Serena with dissolve
    Sulthan "Apa yang Ayah katakan cuma janji kosong, ya? sebenarnya Ayah tidak melakukan apa-apa. Tapi, hanya meyakinkanku agar aku percaya padanya."
    hide Sulthan with dissolve
    scene black with fade
    pause (2.0)

    centered "Kondisi Sulthan semakin memburuk. Ia sering terbaring lemah di tempat tidur, tubuhnya semakin lemah dan sulit digerakkan. Di sisi lain, Dhika, Ayahnya, belum juga menunjukkan tindakan nyata. Semua yang dikatakannya kepada Sulthan hanyalah janji kosong."

    scene RTengah with fade
    show Sulthan at left with dissolve
    show Dhika at right with dissolve
    Sulthan "Ayah… Ayah bilang akan melakukan sesuatu untuk menghentikan proyek itu… Sudah berbulan-bulan… Apa yang sudah Ayah lakukan?" 
    #tambahin musik
    Dhika "Nak, Ayah masih mencari cara. Ini tidak mudah. Orang-orang di belakang proyek ini sangat kuat, dan Ayah harus berhati-hati."
    Sulthan "Berhati-hati? Ayah, aku tidak punya waktu lagi… Setiap hari, rasa sakit ini semakin parah. Apa gunanya berhati-hati kalau aku tidak akan ada di sini untuk melihat hasilnya?"
    Dhika "Sulthan, Ayah berusaha. Ayah benar-benar berusaha. Ayah hanya ingin memastikan kita semua tetap aman."
    Sulthan "Aman? Apa artinya aman kalau aku seperti ini? Ayah… Ayah hanya bicara… Semua hanya janji… Aku tidak pernah melihat Ayah melakukan apapun."
    Dhika "Nak, tolong jangan seperti ini. Ayah… Ayah akan segera bertindak. Ayah janji."
    Sulthan "Janji? Ayah tahu aku tidak akan sempat melihat Ayah menepati janji itu…"
    Sulthan "(Dalam hati) Ah, percuma saja, aku hanya menghabiskan tenagaku untuk berdebat dengannya. Lebih baik aku tidur saja."
    hide Sulthan with dissolve
    hide Dhika with dissolve
    scene black with fade
    pause (2.0)

    centered "Beberapa hari kemudian, Sulthan meninggal karena penyakitnya udah menyebar ke seluruh badan"

    scene RTengah with fade
    show Serena at left with dissolve
    show Dhika at right with dissolve
    Serena "Kenapa, Pak? Kenapa kita tidak melakukan apa pun? Kenapa kita biarkan Sulthan pergi seperti ini?"
    Dhika "Aku… Aku tidak tahu… Aku hanya ingin melindungi kalian… Aku pikir aku punya waktu lebih banyak…"
    #ganti gambar serena jdi marah
    Serena "Melindungi? Melindungi dari apa? Kau hanya melindungi dirimu sendiri, Dhika! Sulthan pergi karena kau terlalu takut untuk bertindak!"
    Dhika "Aku… Aku menyesal…"
    hide Serena with dissolve
    hide Dhika with dissolve
    scene black with fade
    pause (2.0)

    centered "Beberapa minggu kemudian, Dhika duduk sendirian di kantornya. Proyek besar di dekat rumahnya tetap berjalan. Korban lain mulai bermunculan, namun tidak ada yang berani melawan. Dhika terus dihantui oleh bayangan Sulthan."
    centered "Dhika hanya bisa menyesali tindakannya yang tidak pernah ia lakukan. Janji-janji yang ia berikan kepada Sulthan hanyalah kata-kata kosong. Proyek besar itu tetap berjalan, membawa lebih banyak penderitaan, sementara Dhika hidup dalam bayang-bayang rasa bersalah yang tak terhapuskan."
    centered "TAMAT."

    return

label report:
    scene black with fade

    "You report it"
    "ending"
    return

label ending3:
    scene black with fade

    "You ending 3"
    "ending"
    return

label ending4:
    scene black with fade

    "You ending 4"
    "ending"
    return