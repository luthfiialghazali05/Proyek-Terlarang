# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    import random

# Definisi Character
define MC = Character("Sulthan")
define Serena = Character("Serena")

# Image Buat Character
image mc_gray = "mc_gray.png"
image serena = "ibu mc.png"
image mc = "mc.png"

# Image Buat Backgroun
image RTengah = "background/Ruang tengah.jpg"

# The game starts here.
define flash = Fade(.05, 0, .75, color="#fff")



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
    MC "..."

    MC "Apakah hidupku akan berakhir seperti ini?"

    MC "aku tidak tau lagi apa yang harus kulakukan. Tapi, apa yang menyebabkan aku seperti ini? setidaknya, aku ingin tau alasannya."

    stop sound fadeout 0.1
    play sound "Hujan.mp3" volume 0.05 loop
    play audio "door-knocking.mp3" volume 2

    pause(2.7)
    scene RTengah with fade
    show mc at left 
    with dissolve

    pause(0.4)
    show serena at right
    with dissolve
    Serena "Nak, Ibu boleh minta tolong kamu jemput Ayah ya di kantor, lagi hujan deras gini takut Ayah nggak bisa balik pakai bus."

    MC "Boleh, Bu. Ayah udah dikabarin, kan?"

    Serena "Sudah, Nak."

    stop sound

    jump kantor

    return

label kantor:
    scene black

    MC "Boleh, Bu. Ayah udah dikabarin, kan?"

    Serena "Sudah, Nak."

    return

