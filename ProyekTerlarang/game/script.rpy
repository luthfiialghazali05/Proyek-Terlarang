# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    import random

define MC = Character("Sulthan")
define f_MC = Character("Ayah Sulthan")
define m_MC = Character("Mamah Sulthan")

# The game starts here.
define flash = Fade(.05, 0, .75, color="#fff")

label start:
    scene black

    # Teks pertama
    centered "Hujan deras menyelimuti seluruh wilayah kota. Angin berhembus kencang dan langit begitu gelap."

    # Teks kedua
    centered "Sulthan duduk di meja belajarnya sembari menatap keluar melalui jendela kamarnya."

    # Teks ketiga
    centered "Tatapan kosong tanpa harapan terpampang di raut wajahnya setelah tiga minggu lalu dokter mendiagnosanya menderita penyakit kulit langka yang mengharuskannya menjalani medical check-up. Semakin hari, kondisinya semakin memburuk. Harapan hidup menipis karena luka bakar telah menyelimuti hampir seluruh bagian tubuhnya, menyisakan bagian wajah yang masih bersih tanpa bekas."

    # Background flashings
    play audio "Petir.mp3" volume 1.5
    play audio "Hujan.mp3" fadein 1 volume 0.7
    scene black with flash

    MC "..."

    MC "Apakah hidupku akan berakhir seperti ini?"

    MC "aku tidak tau lagi apa yang harus kulakukan. Tapi, apa yang menyebabkan aku seperti ini? setidaknya, aku ingin tau alasannya."

    stop audio

    return
