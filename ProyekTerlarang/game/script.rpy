# The script of the game goes in this file.

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
    
    "Confrontation..."
    "Coming soon"
    menu:
        "ayah udah diconfront, Apa yang akan kamu lakukan setelah ini?"
        "Percaya sama ayah":
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

    "You Believed"
    "ending"
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