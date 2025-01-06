# The script of the game goes in this file.

# ini buat main menu joget2
image main_menu_animated:
    "gui/main_menu/main_menu_1.png"
    pause 0.1
    "gui/main_menu/main_menu_2.png"
    pause 0.1
    "gui/main_menu/main_menu_3.png"
    pause 0.1
    "gui/main_menu/main_menu_4.png"
    pause 0.1
    "gui/main_menu/main_menu_5.png"
    pause 0.1
    "gui/main_menu/main_menu_6.png"
    pause 0.1
    "gui/main_menu/main_menu_7.png"
    pause 0.1
    "gui/main_menu/main_menu_8.png"
    pause 0.1
    repeat

image strip_animated:
    "images/strip/Strip1.png"
    pause 0.3
    "images/strip/Strip2.png"
    pause 0.07
    "images/strip/Strip3.png"
    pause 0.07
    "images/strip/Strip4.png"
    pause 0.07
    "images/strip/Strip5.png"
    pause 0.07
    "images/strip/Strip6.png"
    pause 0.07
    "images/strip/Strip7.png"
    pause 0.07
    "images/strip/Strip8.png"


# ini buat credit
init python:
    import random
    credits = ('Project Manager', 'Thurfah Naura Qolbi (13223021)'), ('Game Designer', 'Rafi Ihsan A. (13223018)'), ('Game Designer', 'Amirul Akhyar H. (13223077)'), ('Script Writer', 'Haura Hafizha H. (18023058)'), ('Script Writer', 'M. Dzaki Farhansyah (13223034)'), ('Programmer', 'M. Luthfii Alghazali (13223097)'), ('Programmer', 'Johanna Sekar M. (13223061)'), ('Programmer', 'Gregory Salman A. (13223016)'), ('Graphic Design and UI/UX Designer', 'Zahra Faiza F. (18323002)'), ('Graphic Design and UI/UX Designer', 'Emir Rasyadi A. (18023027)'), ('Graphic Design and UI/UX Designer', 'Kiyo Lee Tiono (13223013)'), ('Sound Designer', 'Galih M. Syah Athaya (13223115)'), ('Quality Assurance', 'Lintang Suminar (18023015)'), ('Quality Assurance', 'Joyceline Audrey (18023038)'), ('Publication Specialist', 'Agita Trinanda Ilmi (13223003)')   
    credits_s = "{size=80}Credits\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=60}" + c[0] + "\n"
        credits_s += "{size=40}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=40}Engine\n{size=60}" + renpy.version() #Nevermind. It's all good. :P

init:
    image cred = Text(credits_s, font="font/ComicSansMS3.ttf", text_align=0.5) #use this if you want to use special fonts
    #image cred = Text(credits_s, text_align=0.5)
    image theend = Text("{size=80}The end\n{size=20}jangan di skip :) ", text_align=0.5)
    image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5)


# ini buat suara ketik
init python:
    def type_sound(event, interact=True, **kwargs):
        if not interact:
            return

        # Set volume for the "Typing" channel
        renpy.music.set_volume("effect", 1.0)

        # List of typing sounds (make sure to replace these with actual files in your project)
        sounds = 'audio/Typing/Typing.mp3'

        if event == "show":  # When text is being typed
            renpy.sound.play(sounds, channel="effect")

        elif event in ["slow_done", "end"]:  # When text display finishes
            renpy.sound.stop(channel="effect")  # Stop any sound on Typing channel



# ini buat minigame
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

init: ### just setting variables in advance so there are no undefined variable problems
    $ kesempatan = 0

screen caribukti():
    modal True
    text "{color=#000000}{b}Bantu Sulthan mencari Dokumen tersebut!{/b}" xpos 0.05 ypos 0.05

    frame:
        xalign 0.5
        yalign 0.9
        xmaximum 300
        ymaximum 100
        at alpha_dissolve
        bar value kesempatan range 10

    # Image buttons
    imagebutton auto "images/caribukti/Lampu_%s.png":
        xpos 648 ypos 398 focus_mask True
        hovered Play("sound", "audio/click.wav")
        action [
        Jump("lampu")]

    imagebutton auto "images/caribukti/Komputer_%s.png":
        xpos 859 ypos 430 focus_mask True
        hovered Play("sound", "audio/click.wav")
        action [
        Jump("komputer")]

    imagebutton auto "images/caribukti/Buku1_%s.png":
        xpos 1303 ypos 161 focus_mask True
        hovered Play("sound", "audio/click.wav")
        action [
        Jump("buku1")]

    imagebutton auto "images/caribukti/Buku2_%s.png":
        xpos 1470 ypos 187 focus_mask True
        hovered Play("sound", "audio/click.wav")
        action [
        Jump("buku2")]

    imagebutton auto "images/caribukti/Kertas_%s.png":
        xpos 1521 ypos 417 focus_mask True
        hovered Play("sound", "audio/click.wav")
        action [
        Jump("kertas")]

    imagebutton auto "images/caribukti/Pot_%s.png":
        xpos 1435 ypos 57 focus_mask True
        hovered Play("sound", "audio/click.wav")
        action [
        Jump("pot")]

    imagebutton auto "images/caribukti/Pensil_%s.png":
        xpos 1128 ypos 553 focus_mask True
        hovered Play("sound", "audio/click.wav")
        action [
        Jump("pensil")]


#==========================================================================================
# =================== ASSETS DECLARATION ========================
#==========================================================================================
# Definisi Character
define Sulthan = Character("Sulthan", callback=type_sound)
define Dhika = Character("Dhika", callback=type_sound)
define Serena = Character("Serena", callback=type_sound)
define Rika = Character("Mbak Rika", callback=type_sound) #sekretaris dhika
define Polisi = Character("Polisi", callback=type_sound)
define Jaksa = Character("Jaksa", callback=type_sound)
define Hakim = Character("Hakim", callback=type_sound)
define Reporter = Character("Reporter", callback=type_sound)
define Telp = Character("...", callback=type_sound)

#TATA ATURAN INPUT MUSIK
#play sound "judul" argumen // untuk play sound effect (sekali doang abistu mati)
#play music "judul" argumen // untuk play musik yang looping
#play audio "judul" argumen // untuk play beberapa suara at the same time

# Image Buat Character
#SULTHAN
image Sulthan = "Karakter/mc.png"
image Sulthan_marah = "Karakter/mc marah.png"
image Sulthan_nyengir = "Karakter/mc nyengir.png"
image Sulthan_sedih = "Karakter/mc sedih.png"
image Sulthan_senyumtipis = "Karakter/mc senyum tipis.png"
image Sulthan_ngelab = "Karakter/mc ngelab.png"
image mc_gray = "Karakter/mc_gray.png"

#SERENA
image Serena = "Karakter/ibu mc.png"
image Serena_sedih = "Karakter/ibu mc sedih.png"
image Serena_sedihbanget = "Karakter/ibu mc sedih banget.png"
image Serena_marah = "Karakter/ibu mc marah.png"

#DHIKA
image Dhika = "Karakter/bapa mc.png"
image Dhika_senyum = "Karakter/bapa mc senyum.png"
image Dhika_sedih = "Karakter/bapa mc sedih.png"
image Dhika_marah = "Karakter/bapa mc marah.png"
image Dhika_telepon = "Karakter/bapa mc telepun.png"
image Dhika_gelisah = "Karakter/bapa mc dagdigdug.png"
image Dhika_penjara = "Karakter/bapa mc dipenjara.png"

#RIKA SEKRETARIS
image Rika = "Karakter/sekretaris mc.png"

#POLISI
image Polisi = "Karakter/polisi 1.png" 
image Polisi_marah = "Karakter/polisi ngambeg.png" 
image Polisi_kaget = "Karakter/polisi wuih kaget.png" 
image Polisi_senyum_tipis = "Karakter/polisi senyum tipis.png" 

#JAKSA
image Jaksa = "Karakter/jaksa.png"

#HAKIM
image Hakim = "Karakter/hakim serius.png"

#REPORTER
image Reporter = "Karakter/reporter ganteng.png"

# Image Buat Background
image RTengah = "background/ruang tengah.JPG"
image kantor_ayah = "background/kantor dhika.png"
image desa = "background/desa.JPG"
image halaman = "background/halaman rumah.JPG"
image kantor_polisi = "background/kantor polisi.png"
image penjara = "background/penjara.JPG"
image rumah = "background/rumah.JPG"
image proyek = "background/tempat proyek.JPG"
image lab = "background/lab.JPG"
image lobby = "background/lobby kantor.JPG"
image kamar_sulthan = "background/Kamar Sulthan.JPG"
image interogasi = "background/interogasi.JPG"
image proyek_berjalan = "background/proyek berjalan.JPG"
image sel_penjara = "background/sel penjara.JPG"
image courthouse = "background/courthouse.JPG"
image courthouse_spectator = "background/courthouse spectator.JPG"
image BWhite = "background/BlankWhite.png"

#Image buat benda
image SuratIzin = "SuratIzinOperasi.png"
image HP = "HP.png"
image LogoITB = "logo_ITB.png"
image LogoGame = "LogoGame.png"
image Pass1 = "caribukti/Pass_1.png"
image Pass2 = "caribukti/Pass_2.png"

#==========================================================================================
#==========================================================================================
#==========================================================================================
#==========================================================================================
#==========================================================================================
# The game starts here.

label start:
    stop music
    scene black
    show LogoITB with dissolve:
        xalign 0.5
        yalign 0.5
        pause 1.0
        linear 2 ypos 0.5 xpos 0.35 xzoom 0.6 yzoom 0.6
    
    pause(3)
    show LogoGame with dissolve:
        zoom 0.4
        xalign 0.5
        yalign 0.5
        pause 1.0
        linear 2 ypos 0.5 xpos 0.6 xzoom 0.6 yzoom 0.6

    play music "tema dark.mp3" volume 0.5
    pause(3)
    hide LogoGame
    hide LogoITB
    centered "{color=#FF0000}{b}DISCLAIMER:{/color}{/b}\n Semua konten, karakter, nama, tempat, dan alur cerita dalam gim ini sepenuhnya bersifat fiksi. Kesamaan dengan kejadian, individu, atau lokasi di dunia nyata hanyalah kebetulan belaka. Gim ini tidak dimaksudkan untuk mewakili atau mencerminkan pandangan, kepercayaan, atau peristiwa apa pun di dunia nyata."


    scene black
    play audio "Petir.mp3" volume 1.5
    scene black with Fade(0.5, 0, 1, color="#fff")
    
    centered "Hujan deras menyelimuti seluruh wilayah kota. Angin berhembus kencang dan langit begitu gelap."

    centered "Sulthan duduk di meja belajarnya sembari menatap keluar melalui jendela kamarnya."

    # Teks ketiga
    centered "Tatapan kosong tanpa harapan terpampang di raut wajahnya setelah tiga minggu lalu dokter mendiagnosanya menderita penyakit kulit langka yang mengharuskannya menjalani pengobatan setiap minggunya." 
    
    centered "Semakin hari, kondisinya semakin memburuk."
    centered "Harapan hidup {p=0.5}{cps=16}semakin{/cps}{cps=9}{color=#FF0000} menipis{/color}{/cps}."
    centered "Luka bakar telah menyelimuti hampir seluruh bagian tubuhnya, menyisakan bagian wajah yang masih bersih tanpa bekas."

    # Background flashings
    play audio "Petir.mp3" volume 1.5
    play sound "Hujan.mp3" fadein 1 volume 0.3 loop
    scene black with Fade(0.5, 0, 0.5, color="#fff")

    show mc_gray at left
    with dissolve
    Sulthan "..."

    Sulthan "Apakah hidupku akan berakhir seperti ini?"

    Sulthan "Aku tidak tau lagi apa yang harus kulakukan. Tapi..."
    Sulthan "apa yang menyebabkan aku seperti ini?" 
    Sulthan "Setidaknya, aku ingin tau alasannya."

    stop music fadeout 0.3
    stop sound
    play sound "Hujan.mp3" volume 0.1 loop
    play effect "door-knocking.mp3" volume 2

    pause(2.7)
    scene kamar_sulthan with fade
    show Sulthan at left 

    pause(0.4)
    show Serena:
        xalign 1.5
        yalign 1.0
        linear 1 xpos 1.2
    with dissolve
    stop effect

    Serena "Nak, Ibu boleh minta tolong kamu jemput Ayah di kantor. Lagi hujan deras gini, takut Ayah nggak bisa balik pakai bus."

    Sulthan "Boleh, Bu. Ayah udah dikabarin, kan?"

    Serena "Sudah, Nak."

    Sulthan "Baik, Bu. Aku berangkat sekarang..."

    #di sini tambahin sesuatu yang nunjukin dia siap-siap trus nyalain mobil trus berangkats
    stop sound
    hide Sulthan with dissolve
    hide Serena with dissolve
    scene black with fade
    play effect "mobilngeng.mp3" volume 1.0
    pause(8)
    stop effect
    jump kantor

    return

## ================================================ ##
## ================================================ ##

label kantor: # scene 2
    scene lobby with fade
    play music "tema happy.mp3" volume 0.8
    #scene ruangan lobby kantor
    #play music "musik lobby" volume x
    show Sulthan at left with dissolve
    show Rika at right with dissolve

    Rika "huh??..."

    Rika "Ohh, Halo Sulthan! Mau ketemu Pak Dhika ya?"

    Sulthan "Hai Mbak Rika! Iya nih aku mau jemput Ayah. Ayah lagi di mana ya mbak?"

    Rika "Pak Dhika masih ada rapat bersama kliennya. Kamu mending tunggu aja di ruang kerjanya ya..."

    Sulthan "Ohh, baiklah. Terima kasih, Mbak. Aku tunggu di ruangan Ayah deh."

    hide Sulthan with dissolve
    hide Rika 

    #pindah scene ke ruangan ayah
    #sound effect buka pintu ruangan trus duduk
    scene kantor_ayah with fade
    show Sulthan with dissolve
    Sulthan "Huft..."
    Sulthan "{color=#D3D3D3}Kenapa aku harus hidup seperti ini? Apakah aku akan memiliki penyakit ini seumur hidupku?"
    Sulthan "{color=#D3D3D3}Apakah benar kata orang-orang, bahwa penyakit ini..."
    Sulthan "{color=#D3D3D3}efek dari proyek tambang yang baru beroperasi itu."
    Sulthan "Hmmm"
    Sulthan "..."
    Sulthan "Lama banget ini Ayah meeting."
    Sulthan "Liat-liat ruangan Ayah ahh...."

    "...Sulthan beranjak dan melihat sekeliling. Ia membaca pigura, plakat, dan apa saja yang ada di ruangan ayah. Entah mengapa Ia merasakan dorongan untuk membuka laci meja Ayah..."

    play effect "BukaLaci.mp3" volume 1
    play effect "CariKertas.mp3" volume 1

    #show sulthan bingung 
    "..."

    stop music
    play music "tema tegang.mp3" volume 1.0
    stop effect
    Sulthan "Huh..."
    Sulthan "Dokumen Apa ini..?"
    Sulthan "Hmmm..."
    Sulthan "...Teguran Kementrian Kesehatan.....Operasi Tambang Daerah XXXXXX mengeluarkan limbah cair berbahaya..."
    Sulthan "Efek samping pada manusia :"
    Sulthan "{color=#FF0000}{cps=8}Luka Bakar Sekujur Tubuh."
    Sulthan "tch.... Jadi benar, proyek sialan itu yang menjadi penyebab penyakitku ini. Memang dasar pengusaha rakus keparat"
    
    "Bersama dengan teguran Kementrian Kesehatan yang terdapat dalam dokumen tersegel, bagaikan disembunyikan, ada surat lain yang tampak resmi..."
    
    #"Sebuah surat yang menunjukkan kop surat resmi bertuliskan 'Pemerintah Daerah' dan berjudul 'Surat Izin operasi'"
    Sulthan "Apa-apaan ini! Kenapa ayah menyimpan surat seperti ini?... Jangan-jangan..."
    play audio "bombsin.mp3" volume 2
    hide Sulthan
    show Sulthan_marah:
        xalign 0.5
        yalign 1.0
        linear 0.5 xpos 0.2
    play audio "PaperGrab.mp3" volume 1.2
    show SuratIzin:
        xalign 0.5
        yalign 1.5
        linear 0.5 ypos 1.1


    Sulthan "DISETUJUI OLEH AYAH?!!" with vpunch
    Sulthan "HAH??! Bagaimana bisa?"
    Sulthan "Ternyata selama ini..."
    hide SuratIzin with dissolve
    play sound "PaperGrab.mp3" volume 1.2
    "Mata Sulthan berkaca-kaca, tubuhnya gemetar melihat tanda tangan Ayahnya di lembar persetujuan surat izin operasi tambang itu. Proyek besar yang selama ini berada di dekat rumahnya. Proyek besar yang menyebabkan ia mengidap penyakit serius."
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

## ================================================ ##
## ================================================ ##

label confront:
    scene black with fade
    centered "Confrontation..."
    scene kantor_ayah with fade
    
    show Sulthan_sedih at right with dissolve
    "(Tidak lama, Dhika membuka pintu ruangannya)"
    show Dhika at left with dissolve
    Dhika "(Berjalan menghampiri Sulthan) Ada apa nak? Kenapa kamu menangis?"
    hide Sulthan_sedih
    show Sulthan_marah at right
    Sulthan "Ini semua karena Ayah! Ayah yang bikin aku jadi sakit gini."
    Dhika "Ayah bisa jelasin, itu semua tidak seperti yang kamu pikirkan."
    Sulthan "Ga seperti apa yang aku pikirin? Jelas - jelas disini ada tanda tangan Ayah berarti Ayah menyetujui proyek besar itu dong."
    Dhika "Iya memang benar ada tanda tangan Ayah disitu, tapi Ayah tidak bisa apa-apa. Ayah terpaksa menyetujui ini semua karena diancam. Kalau Ayah tidak setuju, yang ada hidup kamu dan ibu kamu dalam bahaya. Ayah juga tidak tahu kalau efeknya bakal seperti gini."
    Sulthan "Kenapa Ayah gapernah bilang hal ini ke aku atau Ibu?"
    Dhika "Ayah cuma gamau kalian khawatir. Semenjak Ayah tau kamu sakit, Ayah menyesal sejadi-jadinya. Ayah tidak minta kamu memaafkan Ayah, tapi biarkan Ayah coba perbaiki ini semua. Ayah cuma perlu kamu percaya sama Ayah."
    Sulthan "Gimana aku bisa percaya sama Ayah kalau Ayah sendiri menutupi ini semua dari aku dan Ibu? Memang Ayah pikir penyakit aku bisa disembuhin?"
    Dhika "Iya Ayah tau Ayah salah, tolong maafkan Ayah."
    hide Sulthan_marah
    show Sulthan at right
    Sulthan "(Dalam hati) Aku tau aku yang terkena imbas dari semua ini, tapi aku sadar Ayah tidak punya pilihan lain. Apakah aku harus mempercayai Ayahku?"
    
    "Pikiran Sulthan kacau. Sulthan paham bahwa Ayahnya tidak mempunyai pilihan. Namun, di sisi lain, Sulthan merasa dikhianati karena ialah yang terkena imbasnya. Sulthan mencoba untuk mempercayai Ayahnya dengan rasa ragu." 
    
    Sulthan "Ayah bilang Ayah sedang memperbaiki ini semua, memangnya Ayah mau melakukan apa? Ayah emang bisa balikin kondisi aku kayak dulu?"
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

## ================================================ ##
## ================================================ ##

label investigate: 
    stop music
    play music "investigate.mp3" volume 1.0
    scene black with fade
    centered "Investigation..."


    scene kantor_ayah with fade

    show Sulthan at right with dissolve
    Sulthan "Kayaknya ada suara langkah kaki mendekat. Aku harus bersikap tidak tahu apa-apa."

    show Dhika at left with dissolve
    Dhika "Eh, kamu sudah disini (melihat Sulthan yang lesu), kamu lagi kenapa Nak?"
    Sulthan "Ga kenapa-napa, langsung pulang aja yaa Yah. Aku udah lemes banget."
    hide Dhika with dissolve
    hide Sulthan with dissolve

    "Sulthan dan Ayahnya meninggalkan ruangan kerja tersebut dan menuju rumah."

    scene RTengah with fade

    show Sulthan at left with dissolve
    Sulthan "Kenapa Ayah bisa setega ini, apa yang Ayah pikirkan ketika mengambil keputusan ini?"
    Sulthan "Kenapa malah aku yang kena imbasnya?"
    Sulthan "Apa yang harus aku lakukan sekarang?"
    Sulthan "Tidak."
    Sulthan "Tidak, Aku tidak boleh kalah dengan keadaan ini. Kalau Ayah saja bisa melakukan ini, Aku juga bisa. Dia harus merasakan apa yang Aku rasakan!"
    Sulthan "Bagaimana Aku memulainya?"
    Sulthan "Sepertinya aku harus menyusun rencana dulu."
    Sulthan "Hmm, kira-kira apa ya?"

    menu :
        "Kamu ingin melakukan investigasi. Apa yang akan kamu lakukan setelah ini?"
        "Cek sampel air di rumah":
            Sulthan "Aha! Aku bisa mulai dengan mengambil sampel air dari rumah ini. Kayaknya Aku bisa pakai lab di sekolah buat meneliti ini saat jam istirahat. Aku bisa ngambil air dari wastafel di dapur."

            hide Sulthan with dissolve
            play audio "BukaLaci.mp3" volume 1.7
            play sound "nulis.mp3" volume 5.0 loop
            "Sulthan mengambil alat tulis dan kertas dari laci mejanya, menuliskan semua rencana yang berjalan di pikirannya, memastikan semua skenario berjalan sempurna."
            "Tidak peduli dengan apa yang akan dihadapinya. yang ia inginkan hanya sebuah pembalasan yang sempurna. Sulthan mulai menyusun rencana yang matang."
            stop sound 
            show Sulthan at center with dissolve
            Sulthan "Baiklah, Aku akan mulai dari mengumpulkan sampel dari air di rumahku."
            scene black with fade
            play sound "keran.mp3" volume 1.7
            centered "Sulthan berdiri dari meja belajarnya, bergerak menuju dapur. Ia melihat sekelilingnya dan berjalan mendekati wastafel yang berada tidak jauh dari kompor di sebelah kirinya. Ia membuka keran secara perlahan, memastikan air tidak mengenai bagian tubuhnya. Ia mengambil 1 botol air mentah dari keran rumahnya." 
            stop sound

            scene RTengah with fade
            show Sulthan at center with dissolve
            Sulthan "Okeh, tahap 1 selesai. Besok akan kubawa ke lab di sekolah."
            Sulthan "Saatnya tidur sebelum Ibu marah."

            scene black with fade
            centered "Keesokan harinya, di lab sekolah..."

            scene lab with fade
            show Sulthan_ngelab with dissolve
            Sulthan "Pertama aku bisa mengambil strip test reagen buat mengecek kandungan airnya."
            Sulthan "Aku tinggal masukin strip tesnya ke air. Eh, aku butuh gelas kimia sepertinya."
            hide Sulthan_ngelab with dissolve
            Sulthan "..."
            Sulthan "..."
            show Sulthan_ngelab with dissolve

            Sulthan "Okeh gelas kimia sudah, tinggal celup deh"
            '...'
            show strip_animated at right
            pause(0.7)
            play audio "bombsin.mp3" volume 2
            pause(0.3)
            'Warna strip test berubah dari kuning menjadi ungu'

            Sulthan 'Sudah kuduga, memang air ini terkontaminasi. Kira-kira mengandung apa ya?'
            Sulthan "(membuka google)"
            Sulthan 'WAY!'
            Sulthan 'Timbal konsentrasi tinggi di dalam airnya! Pantas saja tubuhku bisa jadi gini. Ayah memang sialan!'

            Sulthan 'Hmmm, oke satu bukti sudah. Tapi apakah bukti ini cukup kuat untuk membuktikan ayah terlibat?'
            Sulthan "Harus apalagi ya selanjutnya?"

            menu:
                "Cek kembali dokumen resmi semalam":
                    Sulthan "AH IYA, DOKUMEN ITU!"
                    Sulthan "Aku bisa kembali ke kantor ayah dan memfoto dokumen itu. Baiklah, akan kulakukan setelah pulang sekolah."
                    hide Sulthan_ngelab with dissolve

                    scene black with fade
                    centered "Selesai sekolah Sulthan langsung menuju kantor ayahnya"

                    scene lobby with fade
                    show Sulthan at left with dissolve
                    Sulthan "(dalam hati) Aku ngeboong apa ya biar bisa masuk ke kantor Ayah?"

                    show Rika at right with dissolve
                    Sulthan "Selamat sore, Mbak. Aku mau jemput ayah. Ayah ada dimana, ya?"
                    Rika "Pak Dhika lagi ada di ruang meeting. Kamu tunggu di ruangannya saja ya."
                    Sulthan "Baik, Mbak."
                    hide Sulthan with dissolve
                    hide Rika

                    scene kantor_ayah with fade
                    show Sulthan at left with dissolve
                    Sulthan "Aku harus segera mencari surat itu sebelum ketahuan orang-orang."
                    "Sulthan membuka laci kedua meja kerja ayahnya, tempat dimana ia menemukan surat perjanjian itu."
                    Sulthan "..."
                    play sound "BukaLaci.mp3" volume 1
                    Sulthan "..."
                    Sulthan "Waduh!"
                    Sulthan "Sudah tidak ada!"
                    Sulthan "Aku yakin surat itu masih ada disekitar sini."
                    $ kesempatan = 10 + 1
                    scene caribukti
                    
                    label caribukti:
                        if kesempatan == 0:
                            jump kesempatanhabis
                        else:
                            $ kesempatan -=1
                            call screen caribukti
                        
                    label buku1:
                        Sulthan "Ah hanya buku-buku ayah, tidak ada yang spesial."
                        Sulthan "Bukan disini berarti."
                        jump caribukti
                    
                    label buku2:
                        Sulthan "Hoo, apa ini?"
                        Sulthan "Ada robekan notes!"
                        show Pass1:
                            zoom 0.7
                            xalign 0.5
                            yalign 1.5
                            linear 2 xpos 0.5 ypos 0.5

                        Sulthan "Password?"
                        Sulthan "Hanya dua digit yang terlihat, pasti sisanya ada disekitar sini!"
                        hide Pass1
                        show Pass1:
                            zoom 0.7
                            xalign 0.5
                            yalign 1
                            linear 2 ypos 0.027 xpos 0.6 xzoom 0.5 yzoom 0.5
                        
                        jump caribukti

                    label pot:
                        Sulthan "Duh tinggi sekali"
                        Sulthan "..."
                        Sulthan "Ada robekan notes!"
                        show Pass2:
                            zoom 0.7
                            xalign 0.5
                            yalign 1.5
                            linear 2 xpos 0.5 ypos 0.5
                        Sulthan "Password?"
                        Sulthan "Hanya dua digit yang terlihat, pasti sisanya ada disekitar sini!"
                        hide Pass2
                        show Pass2:
                            zoom 0.7
                            xalign 0.5
                            yalign 1
                            linear 2 ypos 0.027 xpos 0.555 xzoom 0.5 yzoom 0.5

                        jump caribukti
                    
                    label kertas:
                        Sulthan 'Mungkin ada di tumpukan kertas ini.'
                        Sulthan '...'
                        Sulthan '...'
                        Sulthan 'Sial sudah tidak ada!'
                        Sulthan 'Aku yakin versi digitalnya masih ada di komputer ayah.'
                        jump caribukti

                    label lampu:
                        Sulthan 'Ya ini lampu.'
                        Sulthan 'Berharap apa mencari disini.'
                        jump caribukti
                    
                    label pensil:
                        Sulthan "???"
                        Sulthan "Ngapain aku mencari disini"
                        Sulthan "Aneh!"
                        jump caribukti

                    label komputer:
                        $ password = renpy.input('Password?')
                        $ password = password.strip()
                        if password == "5691":
                            'Password Benar'
                            show Sulthan at left with dissolve
                            Sulthan 'Oke bagus! Saatnya mencari file-nya'
                            Sulthan '...'
                            Sulthan '...'
                            
                            Sulthan "Ah ini dia boi!"
                            Sulthan "Saatnya difoto sebagai bukti tambahan."
                            play sound "Camera.mp3" volume 10
                            scene kantor_ayah with Fade(0.1, 0, 0.1, color="#fff")
                            show Sulthan at left

                            hide SuratIzin
                            show HP with dissolve:
                                zoom 2
                                xalign 0.5
                                yalign 0.5
                                linear 2 ypos 0.45 xpos 0.9 xzoom 0.5 yzoom 0.5

                            Sulthan "Dengan 2 bukti ini, aku yakin polisi akan mempercayai ucapanku!"
                            Sulthan "Saatnya melaporkan ke kantor polisi"
                            hide Sulthan
                            scene black with fade

                            jump ending4

                        else:
                            'password salah'
                            Sulthan "Sial! Passwordnya apa ya?"
                            jump caribukti
                    
                    label kesempatanhabis:
                        Telp "Lagi ngapain kamu Sulthan"
                        show Sulthan at left with dissolve
                        Sulthan "Eh Ayah."
                        show Dhika:
                            xalign 1.5
                            yalign 1.0
                            linear 1 xpos 1.3

                        Sulthan "Ga lagi ngapa ngapain kok cuman liat liat aja."
                        Dhika "Kenapa kok tiba-tiba ke kantor?"
                        Sulthan "Engga cuman pengen liat Ayah aja-"
                        Sulthan "Udah yah dadah."
                        hide Sulthan with dissolve
                        "Sulthan bergegas meninggalkan ruang kantor."
                        Dhika "Hmm ada yang aneh"
                        hide Dhika
                        scene black

                        jump bukti1
                        
                        

                "Lapor Polisi":
                    Sulthan "Rasanya sudah cukup deh bukti ini"
                    Sulthan "Sepulang sekolah, aku langsung ke kantor polisi saja deh"
                    scene black with fade
                    hide Sulthan_ngelab with dissolve

                    jump bukti1



        "Tidak melakukan apapun":
            Sulthan "Ah rasanya terlalu sulit untuk mencari bukti apapun, biarkan saja polisi yang melakukannya"
            hide Sulthan with dissolve
            
            scene black with fade
            "Keesokan harinya, Sulthan langsung melaporkan tindakan ayahnya ke kantor polisi"

            jump bukti0

## ================================================ ##
## ================================================ ##

label believe:
    scene black with fade
    scene kantor_ayah with fade

    show Sulthan at right with dissolve
    show Dhika at left with dissolve
    Sulthan "Aku ingin percaya pada Ayah tapi apakah Ayah bisa berjanji padaku untuk mencari solusinya?"
    Dhika "Bisa, Ayah selama ini juga selalu mencari cara buat menyembuhkan kamu."
    Sulthan "(Dalam hati) Mungkin Ayah ada benarnya. Sepertinya aku bisa mempercayainya. Lagipula dia juga Ayahku."
    "Sulthan pun percaya pada Ayahnya dan bertekad untuk mendukung apapun yang Ayahnya lakukan. Sulthan dan Ayahnya mulai mengumpulkan semua bukti yang bisa menutup proyek tersebut dan mengakhiri semua penderitaan yang dialami."
    Sulthan "Apa yang bisa aku bantu, yah?"
    Dhika "Kita bisa mulai dengan meninjau seisi rumah dengan air yang terkontaminasi."
    hide Sulthan
    show Sulthan_senyumtipis at right
    Sulthan "Baiklah! Ayo kita pulang dan segera mencari bukti-buktinya!"
    play music "tema happy.mp3" volume 1.7
    hide Dhika with dissolve
    Sulthan "(Dalam hati sambil menuruni tangga) Aku tidak percaya semua ini terjadi. 10 menit lalu aku sangat ingin menyerah dan saat ini Aku merasa sangat bahagia karena dapat menemukan penyebab masalah ini dan akan menyelesaikannya. Aku ingin cepat-cepat pulang."
    hide Sulthan_senyumtipis with dissolve  
    stop music
    scene black with fade
    play sound "mobilngeng.mp3" volume 1.2
    pause(2.0)
    scene RTengah with fade

    "Mereka sampai di rumah. dengan cepat keluar dari mobil dan berjalan menuju pintu."

    show Sulthan at right with dissolve
    show Dhika at left with dissolve
    Dhika "Maaf, nak. Tampaknya hari sudah larut. Kita bisa memulainya esok hari karena Ayah harus bekerja."
    hide Sulthan
    show Sulthan_sedih
    Sulthan "Yah, oke deh. Selamat tidur Ayah."
    hide Dhika with dissolve
    Sulthan "Ah padahal aku sudah sangat bersemangat. Gapapa deh aku bisa mulai esok hari."
    hide Sulthan_sedih with dissolve
    scene black with fade
    
    centered "Selang beberapa hari..."
    scene RTengah with fade
    show Sulthan_sedih with dissolve
    Sulthan "Kok gak ada info apa-apa dari Ayah. Kapan bakal dimulai, ya? Apa aku inisiatif ya buat mulai? Gak deh, aku nunggu Ayah aja."
    hide Sulthan_sedih with dissolve
    scene black with fade
    pause (2.0)
    
    centered "Seminggu kemudian..."
    scene kamar_sulthan with fade
    show Serena at right with dissolve
    show Sulthan at left with dissolve
    Serena "Nak, obatnya diminum dulu ya, kondisimu sudah semakin buruk. Aktivitasmu dikurangi, ya."
    Sulthan "Ayah gimana, bu? Ayah sudah pulang?"
    Serena "Belum, nanti Ibu kabarin ya. Ibu turun dulu"
    hide Serena with dissolve
    hide Sulthan
    show Sulthan_sedih at left
    Sulthan "Apa yang Ayah katakan cuma janji kosong, ya? sebenarnya Ayah tidak melakukan apa-apa. Tapi, hanya meyakinkanku agar aku percaya padanya."
    hide Sulthan_sedih with dissolve
    scene black with fade
    pause (2.0)

    centered "Kondisi Sulthan semakin memburuk. Ia sering terbaring lemah di tempat tidur, tubuhnya semakin lemah dan sulit digerakkan. Di sisi lain, Dhika, Ayahnya, belum juga menunjukkan tindakan nyata. Semua yang dikatakannya kepada Sulthan hanyalah janji kosong."

    scene kamar_sulthan with fade
    show Sulthan_sedih at left with dissolve
    show Dhika at right with dissolve
    Sulthan "Ayah… Ayah bilang akan melakukan sesuatu untuk menghentikan proyek itu… Sudah berbulan-bulan… Apa yang sudah Ayah lakukan?" 
    play music "tema horror.mp3" volume 1.7
    hide Dhika
    show Dhika_sedih at right
    Dhika "Nak, Ayah masih mencari cara. Ini tidak mudah. Orang-orang di belakang proyek ini sangat kuat, dan Ayah harus berhati-hati."
    Sulthan "Berhati-hati? Ayah, aku tidak punya waktu lagi… Setiap hari, rasa sakit ini semakin parah. Apa gunanya berhati-hati kalau aku tidak akan ada di sini untuk melihat hasilnya?"
    Dhika "Sulthan, Ayah berusaha. Ayah benar-benar berusaha. Ayah hanya ingin memastikan kita semua tetap aman."
    Sulthan "Aman? Apa artinya aman kalau aku seperti ini? Ayah… Ayah hanya bicara… Semua hanya janji… Aku tidak pernah melihat Ayah melakukan apapun."
    Dhika "Nak, tolong jangan seperti ini. Ayah… Ayah akan segera bertindak. Ayah janji."
    Sulthan "Janji? Ayah tahu aku tidak akan sempat melihat Ayah menepati janji itu…"
    Sulthan "(Dalam hati) Ah, percuma saja, aku hanya menghabiskan tenagaku untuk berdebat dengannya. Lebih baik aku tidur saja."
    hide Sulthan_sedih with dissolve
    hide Dhika_sedih with dissolve
    stop music
    scene black with fade
    pause (2.0)

    centered "Beberapa hari kemudian, Sulthan meninggal karena penyakitnya udah menyebar ke seluruh badan"

    scene RTengah with fade
    show Serena_sedihbanget at left with dissolve
    show Dhika_sedih at right with dissolve
    Serena "Kenapa, Pak? Kenapa kita tidak melakukan apa pun? Kenapa kita biarkan Sulthan pergi seperti ini?"
    Dhika "Aku… Aku tidak tahu… Aku hanya ingin melindungi kalian… Aku pikir aku punya waktu lebih banyak…"
    hide Serena_sedihbanget
    show Serena_marah at left
    Serena "Melindungi? Melindungi dari apa? Kau hanya melindungi dirimu sendiri, Dhika! Sulthan pergi karena kau terlalu takut untuk bertindak!"
    Dhika "Aku… Aku menyesal…"
    hide Serena_marah with dissolve
    hide Dhika_sedih with dissolve
    scene black with fade
    pause (2.0)

    centered "Beberapa minggu kemudian, Dhika duduk sendirian di kantornya. Proyek besar di dekat rumahnya tetap berjalan. Korban lain mulai bermunculan, namun tidak ada yang berani melawan. Dhika terus dihantui oleh bayangan Sulthan."
    centered "Dhika hanya bisa menyesali tindakannya yang tidak pernah ia lakukan. Janji-janji yang ia berikan kepada Sulthan hanyalah kata-kata kosong. Proyek besar itu tetap berjalan, membawa lebih banyak penderitaan, sementara Dhika hidup dalam bayang-bayang rasa bersalah yang tak terhapuskan."
    centered "TAMAT."

    jump end_credit

## ================================================ ##
## ================================================ ##

label report:
    hide Sulthan_marah
    show Sulthan at left with dissolve 
    show Dhika at right with dissolve
    Dhika   "(berjalan menghampiri Sulthan)"
    Dhika   "Ada apa, nak? kenapa kamu menangis?"
    Sulthan "Ini semua karena Ayah, Ayah yang bikin aku jadi sakit gini."
    Dhika   "Ayah bisa jelasin, itu semua tidak seperti apa yang kamu pikirkan." 
    Sulthan "Ga seperti apa yang aku pikirin? Jelas - jelas disini ada tanda tangan ayah berarti ayah sama aja setujuin proyek besar itu dong."
    Dhika   "Iya memang benar ada tanda tangan ayah disitu, tapi ayah tidak bisa apa-apa. Ayah terpaksa menyetujui ini semua karena diancam. Kalau Ayah tidak setuju, yang ada hidup kamu dan ibu kamu dalam bahaya. Ayah juga tidak tahu kalau efeknya bakal seperti gini."
    Sulthan "Kenapa ayah gapernah bilang hal ini ke aku atau ibu?"
    Dhika   "Ayah cuma gamau kalian khawatir. Semenjak ayah tau kamu sakit, ayah menyesal sejadi-jadinya. Ayah tidak minta kamu memaafkan Ayah, tapi biarkan ayah coba perbaiki ini semua. Ayah cuma perlu kamu percaya sama Ayah."
    Sulthan "Gimana mau percaya sama Ayah kalau Ayah sendiri tutup-tutupin ini semua dari aku sama Ibu. Emang ayah pikir penyakit aku bisa disembuhin?"
    Dhika   "Iya Ayah tau Ayah salah, maafin Ayah. "
    Sulthan "Aku tau aku yang terkena imbas dari semua ini, tapi aku sadar ayah tidak punya pilihan lain. Apakah aku harus mempercayai ayahku?"


    Sulthan "Ayah bilang Ayah lagi memperbaiki ini semua, memangnya ayah mau melakukan apa? Ayah emang bisa balikin kondisi aku kayak dulu?"
    Dhika "Ayah lagi mengumpulkan bukti yang bisa mempercepat proses penutupan proyek ini. Nanti setelah proyek ini ditutup, ayah akan fokus mencari cara buat sembuhin kamu."
    
    hide Dhika with dissolve
    hide Sulthan with dissolve
    scene black with fade
    centered "Setelah konfrontasi dengan ayahnya, Sulthan merasa tidak mendapat jawaban yang memuaskan. Ia memutuskan untuk melapor ke polisi meskipun tidak memiliki bukti yang kuat."

    show mc_gray at left
    Sulthan "Ah, ayah terlalu banyak basa-basi. Lebih baik aku segera pergi dari sini dan melaporkannya ke polisi. Tapi, aku membawa bukti apa? Aku bahkan tidak tahu akan melaporkan apa. Urusan nanti deh, yang penting aku harus melaporkan hal tersebut."
    hide mc_gray at left
    jump ending2
    return

## ================================================ ##
## ================================================ ##

label ending2:
    scene kantor_polisi
    show Sulthan at left with dissolve
    # ganti scene ke kantor polisi
    Sulthan "Apa aku akan benar-benar melaporkan ayahku? Biar gimana pun, dia adalah ayahku. Apakah aku terlalu gila?"
    Sulthan "..."
    Sulthan "Tidak..."
    Sulthan "Aku tidak gila sama sekali. Ayah jauh lebih gila karena membiarkanku sakit."

    #ini polisi
    show polisi at right with dissolve
    Polisi "Selamat sore anak muda! Apa yang bisa kami bantu?"

    Sulthan "Pak, saya ingin melaporkan sebuah kejahatan. Proyek besar di dekat rumah saya menyebabkan kerusakan lingkungan, dan saya yakin itu penyebab penyakit saya. Ayah saya terlibat dalam proyek itu."

    play sound "PaperGrab.mp3" volume 1.2 
    Polisi "(mengambil catatan)"
    Polisi "Baik, Nak. Bisa dijelaskan lebih rinci? Apa yang membuat Anda yakin ayah Anda terlibat?"

    Sulthan "Saya menemukan dokumen di ruang kerja ayah saya. Ada tanda tangannya di kontrak proyek besar itu. Tapi... saya tidak sempat membawa dokumen itu ke sini."

    Polisi "Jadi Anda melaporkan tanpa membawa bukti?"

    Sulthan "(Suaranya memelas, matanya berkaca-kaca) Iya, Pak. Tapi saya yakin sekali! Saya bisa tunjukkan lokasi proyeknya dan ceritakan apa yang terjadi!"

    Polisi "..."
    Polisi "Baiklah, kami akan mencatat laporan ini dan memanggil ayah Anda untuk dimintai keterangan. Tapi perlu diingat, tanpa bukti konkret, akan sulit untuk melanjutkan kasus ini. Saat ini, kau boleh kembali."
    
    Sulthan "Terimakasih pak telah mendengarkanku!"

    hide Sulthan with dissolve
    hide polisi with dissolve
    scene black with fade

    scene kantor_ayah with fade
    show Dhika at left with dissolve
    Dhika "Kemana anak ini? Bukannya menjemputku malah kabur entah kemana. Teleponnya tidak diangkat lagi. Kira-kira apa yang dia lakukan?"
    "(Kring…. kring…. *Suara telepon berbunyi)"
    Dhika "Halo, dengan Dhika disini. Dengan siapa dimana?"

    Telp "Selamat sore. Apa benar dengan pak Dhika? "
    Dhika "Ya, benar."
    Telp "Kami dari kepolisian Wilayah Semeleketeha memanggil bapak untuk melakukan pemeriksaan lebih lanjut terkait laporan yang baru saja masuk beberapa jam lalu. Kami tunggu kehadirannya pada pukul 7 Malam."

    Dhika "Siap pak, saya segera kesana (mematikan telepon)."
    Dhika "Ish. Apa yang telah bocah tengil itu lakukan. Bisa-bisanya dia melaporkanku ke polisi. Memang anak gak tau diri. Aku akan memberinya pelajaran."
    "(Dhika segera menuju kantor kepolisian)"
    hide Dhika with dissolve
    
    scene black with fade

    centered "(Dhika tiba di kantor polisi setelah mendapat panggilan. Ia tampak tenang namun waspada. Sulthan duduk di kursi sebelah, menunduk, tidak berani menatap ayahnya.)"


    # masukin scene di kantor polisi
    scene kantor_polisi with fade
    show Dhika at left with dissolve
    show Polisi at right with dissolve

    Polisi "Pak Dhika, kami menerima laporan dari putra Anda bahwa Anda terlibat dalam sebuah proyek besar yang diduga menyebabkan kerusakan lingkungan dan membahayakan kesehatan warga, termasuk putra Anda sendiri. Apa tanggapan Anda?"

    Dhika   "Pak, saya rasa ini hanya kesalahpahaman. Sulthan anak saya, dia sedang sakit, dan mungkin pikirannya terganggu."

    hide Polisi
    show Sulthan_marah at right with dissolve
    Sulthan "Ayah! Jangan bilang seperti itu! Aku tahu apa yang aku lihat!"

    Dhika   "Nak, Ayah tidak tahu apa yang kamu lihat. Tapi Ayah yakin itu hanya salah paham. Ayah bekerja keras untuk keluarga kita, dan Ayah tidak mungkin melakukan hal-hal yang merugikan kita."

    hide Sulthan_marah
    show Polisi at right with dissolve
    Polisi "Pak Dhika, anak Anda mengklaim ada dokumen yang menunjukkan tanda tangan Anda pada proyek tersebut. Apa tanggapan Anda?"

    
    Dhika   "Pak, saya bisa pastikan, tidak ada dokumen seperti itu. Kalau ada, tolong tunjukkan kepada saya sekarang."

    hide Dhika
    show Sulthan_sedih at left with dissolve
    Sulthan "Aku… Aku tidak punya dokumen itu di sini, tapi aku bisa bawa nanti!"

    Polisi "Sulthan, tanpa bukti konkret, kami tidak bisa melanjutkan penyelidikan ini."

    Sulthan "Pak, tolong percaya sama saya…"

    hide Sulthan_sedih
    show Dhika at left with dissolve
    Dhika  "Pak Polisi, saya paham kekhawatiran anak saya. Saya juga sedih melihat kondisinya sekarang. Tapi ini semua hanya spekulasi. Jika memang ada bukti, saya siap bekerja sama."
    
    Polisi "Nak, kami harus menutup laporan ini sampai ada bukti yang kuat. Kalau nanti Anda memiliki dokumen yang bisa mendukung laporan Anda, silakan datang lagi ke sini."
    hide Dhika
    show Sulthan_sedih at left with dissolve
    Sulthan "(monolog) Mau gimana lagi, aku tidak memiliki bukti apapun. Seharusnya aku foto saja surat izin tadi."

    hide Sulthan_sedih
    scene black with fade

    scene RTengah with fade
    show Dhika at left with dissolve
    show Sulthan_sedih at right with dissolve
    Dhika "Aku tahu kamu ingin keadilanmu. Tapi bukan begitu caranya. Kau hanya membuat dirimu terlihat bodoh di depan orang lain."

    hide Sulthan_sedih
    show Sulthan_marah at right
    Sulthan "Kau sangat jahat! Kau dengan mudah melupakan semua perkataan manismu sebelumnya. Begitu mudahnya kau memutarbalikkan fakta. Bahkan kau sepertinya tidak peduli denganku."
    Sulthan "Apa kau benar-benar ayahku? Kau tidak pantas ku panggil ayah!"
    Dhika   "Ayah menawarkan solusi kepadamu, Nak, tapi kau tidak mendengarkanku. Bagaimana ayah membantumu jika kamu melakukan itu ke ayah? Tidak perlu lepas kendali, nak. Kita bisa bicarakan ini baik-baik"
    Sulthan "Sudah cukup omong kosongmu! Ucapanmu bahkan tidak jauh beda dengan koruptor-koruptor negeri ini"
    hide Dhika
    show Dhika_marah at left
    Dhika   "Lancang sekali bicaramu, Nak! Apakah begitu tata krama berbicara kepada ayahmu?"
    Sulthan  "Tidak ada ayah yang ingin mencelakakan anaknya sendiri demi keuntungannya."

    hide Sulthan_marah
    hide Dhika_marah
    scene black with fade
    centered "Setelah kejadian itu, Sulthan tidak berbicara sepatah kata pun kepada ayahnya. Hubungan mereka semakin renggang. Sementara itu, kondisi kesehatan Sulthan semakin memburuk dari hari ke hari."

    stop music
    play music "tema dark.mp3" volume 1.0
    show mc_gray
    Sulthan "(Sambil berbaring di tempat tidur, suaranya hampir tidak terdengar)"
    Sulthan "Aku sudah mencoba… Aku sudah berusaha… Tapi semua sia-sia. Lebih baik tidak tahu apa-apa daripada mati dengan kenyataan ini."

    hide mc_gray
    centered "Beberapa minggu kemudian, Sulthan meninggal dunia. Serena menangis tersedu di samping jenazah putranya, sementara Dhika..."
    centered "hanya duduk diam...."
    centered "menyesal."
    centered "Proyek besar itu terus berjalan, memakan lebih banyak korban."
    centered "..."

    centered "Sulthan pergi meninggalkan dunia tanpa pernah melihat keadilan yang ia perjuangkan. Ayahnya, Dhika, terus hidup dengan rasa bersalah yang membebani, namun tetap tidak pernah benar-benar bertindak. Proyek besar itu menjadi simbol ketidakadilan, dan Sulthan hanyalah satu dari sekian banyak korban yang tidak pernah mendapat keadilan."
    centered "{color=#FF0000}{b}-Tamat-{/b}{/color}"

    jump end_credit

## ================================================ ##
## ================================================ ##

label bukti1:
    hide All
    scene black with fade
    "Sulthan pergi ke kantor polisi"

    #ADEGAN KANTOR POLISI
    scene kantor_polisi with fade
    show Polisi at left with dissolve
    Polisi "Selamat siang, Nak. Ada yang bisa kami bantu?"
    show Sulthan at right with dissolve
    Sulthan "(Menelan ludah, suaranya pelan) Selamat siang, Pak. Saya... saya ingin melapor. "
    Polisi "(Memperhatikan ekspresi Sulthan dengan cermat)"
    Polisi "Tentu. Apa yang ingin kamu laporkan?"
    Sulthan "(Terlihat ragu, memegang map lebih erat)\n
    Ini... tentang sebuah proyek besar di dekat tempat tinggal saya. Saya pikir proyek itu mencemari lingkungan kami... dan mungkin menyebabkan penyakit seperti yang saya alami."
    Polisi "(Mengangguk dan mengisyaratkan Sulthan untuk duduk)\n Baik, mari duduk dulu. Ceritakan semuanya dari awal."
    "(Sulthan duduk dan menarik nafas panjang)"
    Sulthan "(Terlihat gelisah)\n Beberapa bulan setelah proyek itu dimulai, saya mulai sakit. Kulit saya gatal, ruam muncul di beberapa bagian tubuh. Awalnya kami pikir ini hanya alergi biasa, tapi semakin lama semakin parah."
    hide Sulthan
    show Sulthan_sedih at right
    Polisi "(Mendengarkan dengan serius)\nDan apa yang membuatmu yakin ini berkaitan dengan proyek tersebut?"
    Sulthan "(Sambil membuka map dan menunjukkan hasil sample air)\n
    Saya sempat menemui dokter, dan beliau bilang penyakit saya mungkin disebabkan oleh air yang terkontaminasi limbah dari proyek itu. Saya mulai mencari tahu lebih jauh… saya sempat menganalisa kandungan air yang ada di lingkungan saya dan hasilnya menunjukkan bahwa air tersebut sudah terkontaminasi oleh timbal."
    Sulthan "Lebih parahnya lagi, saya… Saya menemukan proposal proyek besar tersebut di kantor ayah saya. Ayah saya... dia salah satu penandatangan proyek itu."
    hide Polisi
    show Polisi_kaget at left
    Polisi "(Polisi mengangkat alis, terkejut, tapi tetap menjaga ketenangan.)\n Jadi, ayahmu terlibat dalam proyek ini?"
    Sulthan "(Menunduk, suara mulai bergetar)\n
    Saya tidak ingin mempercayainya, Pak. Tapi dokumen ini jelas menunjukkan bahwa ia tahu soal limbah itu. Saya tidak tahu harus bagaimana..."
    Polisi "Apakah proposal tersebut berada di tanganmu sekarang?"
    Sulthan "(Menggeleng)\n
    Tidak pak, saya takut Ayah saya mengetahui kalau saya yang mengambil proposal tersebut."
    Polisi "(Polisi terheran, namun tetap mencoba meminta bukti lain)\n 
    Apakah kamu memiliki bukti lain?"
    Sulthan "(Sulthan menggeleng kembali)"
    Polisi "Baiklah, Ini langkah besar yang kamu ambil dengan melapor. Kami akan memeriksa lebih lanjut. Tapi kamu harus tahu, melibatkan keluarga dalam masalah ini tidak akan mudah."
    jump ending3

## ================================================ ##
## ================================================ ##

label bukti0: 
    hide All
    scene black with fade
    "Sulthan pergi ke kantor polisi"

    #ADEGAN KANTOR POLISI
    scene kantor_polisi with fade
    show Polisi at left with dissolve
    Polisi "Selamat siang, Nak. Ada yang bisa kami bantu?"
    show Sulthan at right with dissolve
    Sulthan "(Menelan ludah, suaranya pelan) Selamat siang, Pak. Saya... saya ingin melapor. "
    Polisi "(Memperhatikan ekspresi Sulthan dengan cermat)"
    Polisi "Tentu. Apa yang ingin kamu laporkan?"
    Sulthan "(Terlihat ragu)\n Ini... tentang sebuah proyek besar di dekat tempat tinggal saya. Saya pikir proyek itu mencemari lingkungan kami... dan mungkin menyebabkan penyakit seperti yang saya alami."
    Polisi "(Mengangguk dan mengisyaratkan Sulthan untuk duduk)\n Baik, mari duduk dulu. Ceritakan semuanya dari awal."
    "(Sulthan duduk dan menarik nafas panjang)"
    Sulthan "(Terlihat gelisah)\n Beberapa bulan setelah proyek itu dimulai, saya mulai sakit. Kulit saya gatal, ruam muncul di beberapa bagian tubuh. Awalnya kami pikir ini hanya alergi biasa, tapi semakin lama semakin parah."
    hide Sulthan
    show Sulthan_sedih at right
    Polisi "(Mendengarkan dengan serius)\nDan apa yang membuatmu yakin ini berkaitan dengan proyek tersebut?"
    Sulthan "Saya sempat menemui dokter, dan beliau bilang penyakit saya mungkin disebabkan oleh air yang terkontaminasi limbah dari proyek itu. Sejak saat itu, Saya mulai mencari tahu lebih jauh…"
    Sulthan "Lalu, saya… Saya menemukan proposal proyek besar tersebut di kantor ayah saya. Ayah saya... dia salah satu penandatangan proyek itu."
    hide Polisi
    show Polisi_kaget at left
    Polisi "(Polisi mengangkat alis, terkejut, tapi tetap menjaga ketenangan.)\n Jadi, ayahmu terlibat dalam proyek ini?"
    Sulthan "(Menunduk, suara mulai bergetar)\n
    Saya tidak ingin mempercayainya, Pak. Tapi dokumen ini jelas menunjukkan bahwa ia tahu soal limbah itu. Saya tidak tahu harus bagaimana..."
    Polisi "Apakah proposal tersebut berada di tanganmu sekarang?"
    Sulthan "(Menggeleng)\n Tidak pak, saya takut Ayah saya mengetahui kalau saya yang mengambil proposal tersebut."
    Polisi "(Polisi terheran, namun tetap mencoba meminta bukti lain)\n 
    Apakah kamu memiliki bukti lain?"
    Sulthan "(Sulthan menggeleng kembali)"
    Polisi "Baiklah, Ini langkah besar yang kamu ambil dengan melapor. Kami akan memeriksa lebih lanjut. Tapi kamu harus tahu, melibatkan keluarga dalam masalah ini tidak akan mudah."
    jump ending3

## ================================================ ##
## ================================================ ##

label ending3:
    Sulthan "(Mengangguk pelan, matanya berkaca-kaca)\nSaya tahu, Pak. Tapi saya tidak bisa diam saja. Orang-orang di sekitar saya... mereka mungkin terkena dampak yang sama. Ini bukan hanya tentang saya."
    hide Polisi_kaget
    show Polisi_senyum_tipis at left
    Polisi "(Sambil tersenyum tipis, nada suaranya meyakinkan)\nKamu melakukan hal yang benar. Kami akan mulai menyelidiki ini secepatnya. Apakah kamu bersedia bekerja sama lebih lanjut jika diperlukan?"
    hide Sulthan_sedih
    show Sulthan at right
    Sulthan "(Menatap polisi dengan tatapan tegas meskipun ada sedikit ketakutan di matanya)\nSaya siap, Pak. Apa pun yang diperlukan untuk memastikan ini tidak terus terjadi."
    Polisi "hmmm... baiklah. Kami akan memulai penyelidikan. Terima kasih atas keberanianmu, Sulthan. Jika ada perkembangan, kami akan segera menghubungimu."
    hide sulthan with dissolve
    hide Polisi_senyum_tipis with dissolve

    scene black with fade
    centered "Polisi setuju memulai investigasi \n Sulthan berdiri, mengangguk pelan, dan meninggalkan kantor polisi dengan langkah berat namun hati yang lebih lega."
    centered "Sementara itu di rumah..."

    #ADEGAN DI RUMAH
    scene rumah with fade
    show Dhika at left with dissolve
    Dhika "Sulthan kemana ya, kok belum pulang-pulang. Apa lagi ada kerja kelompok ya makanya bisa lama"
    play sound "TELEPON IPHONE SOUND EFFECT.mp3" volume 0.7
    "(Telepon berbunyi...)"
    hide Dhika
    show Dhika_telepon at left
    stop sound
    Dhika "Halo, dengan Dhika disini. Dengan siapa dimana?"
    Polisi "(Dari telepon) Selamat sore. Apa benar dengan pak Dhika?"
    Dhika "Ya, benar."
    Polisi "(Dari telepon) Kami dari kepolisian Wilayah Semeleketeha memanggil bapak untuk melakukan pemeriksaan lebih lanjut terkait laporan yang baru saja masuk beberapa jam lalu. Kami tunggu kehadirannya pada pukul 7 Malam."
    Dhika "Ada masalah apa ini pak? Mengapa saya tiba-tiba diperiksa seperti ini? saya tidak melakukan kesalahan apapun pak!"
    Polisi "(Dari telepon) Bapak penuhi saja panggilan ini. Kami akan jelaskan nanti. Saya harap bapak menerima panggilan ini dengan serius!"
    Dhika "Siap pak, saya segera kesana (mematikan telepon)."
    hide Dhika_telepon with dissolve

    scene black with fade
    centered "Sesampainya di kantor polisi, Dhika dibawa ke ruang pemeriksaan dan diinterogasi"

    #ADEGAN INTEROGASI
    centered"Pak Dhika duduk di ruang interogasi. Wajahnya tetap tenang, meskipun pertanyaan tajam terus dilontarkan oleh polisi."
    scene interogasi with fade
    show Dhika at left with dissolve
    show Polisi at right with dissolve
    Polisi "Pak Dhika, Anda adalah salah satu penandatangan utama proyek besar ini. Bukti-bukti yang kami miliki menunjukkan adanya pelanggaran pengelolaan limbah yang menyebabkan kerusakan lingkungan."
    Polisi "Kami juga memiliki laporan transaksi keuangan mencurigakan yang melibatkan Anda. Apa penjelasan Anda?"
    hide Dhika
    show Dhika_senyum at left
    Dhika "(Tersenyum kecil, tetap tenang)\nSaya rasa Anda salah paham. Semua yang saya lakukan sesuai prosedur. Tanggung jawab utama ada pada pihak lain."
    Polisi "(Tatapannya tajam)\nTapi Anda tahu soal limbah ini sebelum proyek dimulai, bukan? Kami juga punya bukti bahwa dana yang seharusnya digunakan untuk pengelolaan limbah tidak sampai ke tempatnya."
    hide Dhika_senyum
    show Dhika at left
    Dhika "(Suara tenang, namun dengan nada manipulatif)\nSemua pengeluaran sudah dilaporkan ke departemen keuangan. Kalau ada yang salah, itu di luar kendali saya. Lagipula, saya hanya mengikuti instruksi atasan."
    "Polisi terus menekan, namun Pak Dhika tidak kehilangan kendali. Dia mulai berbicara dengan lebih lembut, mencoba menggiring suasana."
    hide Dhika
    show Dhika_senyum at left
    Dhika "(Sambil tersenyum tipis)\nSaya tahu ini pekerjaan Anda, Pak Polisi. Tapi Anda tahu bagaimana dunia ini berjalan, bukan? Tidak semuanya sehitam-putih itu."
    "Dhika mengeluarkan amplop tebal dari tasnya dan meletakkannya di meja."
    Dhika "(Suara rendah)\nMungkin kita bisa menyelesaikan ini dengan cara yang lebih... efisien. Anda mengerti maksud saya, kan?"
    "Polisi Terlihat ragu. Setelah beberapa saat, dia mengambil amplop itu dengan wajah datar."
    Polisi "(Sambil berdiri)\nKami akan meninjau kembali kasus ini. Untuk saat ini, Anda boleh pulang, Pak Dhika."
    "Pak Dhika tersenyum puas, bangkit, dan meninggalkan ruangan."
    hide Dhika_senyum with dissolve
    hide Polisi with dissolve

    scene black with fade
    centered "Sulthan menunggu berhari-hari, berminggu-minggu, tetapi tidak mendapat kabar lebih lanjut dari Polisi."
    centered "Ia merasa janggal karena Ia merasa semua bukti yang ia temukan sangat amat kuat untuk menjatuhkan ayahnya ke balik jeruji besi."
    centered "Ia berinisiatif untuk kembali ke kantor polisi dan menanyakan hal tersebut."

    #ADEGAN FOLLOW UP KASUS
    scene kantor_polisi with fade
    show Sulthan at right with dissolve
    show Polisi at left with dissolve
    Polisi "Selamat siang. Ada yang bisa kami bantu?"
    Sulthan "Siang. Saya ingin menanyakan progress dari bukti yang saya laporkan mengenai pencemaran lingkungan beberapa minggu lalu."
    Polisi "Baik, mohon tunggu sebentar. Kami akan mencari laporan tersebut."
    hide Polisi with dissolve
    "(Sulthan duduk, menunggu polisi kembali memanggilnya)"
    show Polisi at left with dissolve
    Polisi "Saya telah menemukan laporan kasus ini. Mengenai laporan tersebut telah diselesaikan dan kasus telah ditutup."
    hide Sulthan
    show Sulthan_marah at right
    Sulthan "(Tercengang dan terkejut mendengar hal tersebut)\nHAH, Bagaimana bisa? Kenapa diselesaikan? Bukankah kasus ini bisa memakan banyak korban setelahku?"
    Sulthan "Siapa dibalik semua ini? Mengapa Anda bisa menyelesaikannya?"
    Polisi "Terkait hal ini, kami telah memanggil Pak Dhika selaku orang yang Anda laporkan. Setelah interogasi yang kami lakukan, kami menyimpulkan Pak Dhika tidak bersalah atas kasus ini, karena bukti yang diperoleh tidak valid."
    Sulthan "(Di dalam hati) \nAku yakin ayah ada dibalik semua ini!"
    hide Sulthan_marah
    hide Polisi 
    
    scene black with fade
    centered "Sulthan tampak kesal dan sangat frustasi mendengar hal tersebut."
    centered "Ia meninggalkan kantor polisi dengan wajah seakan tidak percaya semua bukti yang telah dikumpulkan hanya berakhir seperti ini."
    centered "Di rumah, Sulthan menghadapi ayahnya setelah mengetahui bahwa kasusnya tidak dilanjutkan."
    
    #ADEGAN RUMAH
    scene rumah with fade
    show Dhika at left with dissolve
    show Sulthan_marah at right with dissolve
    Sulthan "(Suara penuh emosi)\nAyah! Kenapa Ayah melakukan itu? Aku tahu Ayah membayar polisi untuk menutup kasus ini!"
    Dhika "(Suaranya dingin)\n
    Jaga bicaramu, Sulthan. Ayah hanya melakukan apa yang perlu dilakukan untuk melindungi keluarga kita."
    Sulthan "(Terus menekan)\nMelindungi? Ayah melindungi diri sendiri, bukan kita! Proyek itu sudah menghancurkan banyak orang, termasuk aku! Ayah tahu penyakitku disebabkan oleh limbah itu, kan?"
    hide Dhika
    show Dhika_marah at left
    Dhika "(Suaranya semakin tegas)\nDan apa yang bisa kita lakukan? Menghentikan proyek itu? Itu tidak akan terjadi. Dunia ini kejam, Sulthan. Kalau kita tidak bertahan, kita akan diinjak-injak."
    hide Sulthan_marah
    show Sulthan_sedih at right
    Sulthan "(Suara bergetar, hampir menangis)\nKalau begitu, Ayah rela mengorbankan semua orang, termasuk anak ayah sendiri, hanya demi uang?"
    hide Dhika_marah
    show Dhika at left
    Dhika "(Mencoba meredakan suasana, tapi tetap manipulatif)\nNak, kamu harus mengerti. Semua yang Ayah lakukan ini untuk masa depan kita. Proyek ini memberi kita kehidupan yang lebih baik. Jangan terlalu emosional."
    hide Sulthan_sedih
    show Sulthan_marah at right
    Sulthan "(Suara penuh amarah)\nMasa depan yang seperti apa, Ayah? Hidup lebih baik dengan mengorbankan nyawa orang lain? Aku muak, Ayah. Aku tidak bisa tinggal di sini lagi."
    hide Sulthan_marah with dissolve
    Dhika "..."
    hide dhika with dissolve
    
    scene black with fade
    centered "Sulthan berjalan pergi ke kamarnya, meninggalkan ayahnya yang terlihat marah tapi tetap tenang."
    centered "Beberapa hari kemudian, Sulthan berbicara dengan ibunya di ruang tamu. Wajahnya terlihat pucat karena penyakitnya semakin parah."

    #ADEGAN HUBUNGAN YANG MEMBURUK
    scene rumah with fade
    show Sulthan_sedih at left with dissolve
    show Serena_sedih at right with dissolve
    Serena "(Sambil menyentuh bahu Sulthan)\nSulthan, Ayahmu hanya mencoba melindungi keluarga ini. Jangan terlalu keras padanya."
    Sulthan "(Suaranya lemah, namun penuh tekad)\nBu, Ayah tidak melindungi siapa pun. Dia hanya melindungi dirinya sendiri. Proyek itu tetap berjalan, dan korban terus berjatuhan. Aku sudah tidak tahu lagi harus bicara apa dengannya."
    hide Serena_sedih
    show Serena_sedihbanget
    Serena "(Menangis pelan)\nNak, kita tidak punya pilihan. Ayahmu punya banyak tekanan."
    Sulthan "(Memandang ibunya dengan mata penuh rasa sakit)\nTidak ada yang memaksa Ayah untuk memilih jalan ini, Bu. Dia yang memutuskan untuk korupsi, untuk menutup mata terhadap penderitaan orang lain."
    hide Sulthan_sedih with dissolve
    hide Serena_sedihbanget with dissolve

    #ADEGAN SULTHAN LIAT PROYEK MASIH BERJALAN
    scene proyek_berjalan with fade
    play sound "sound effect suasana proyek bangunan.mp3" volume 0.5
    "Sulthan berdiri di depan proyek besar yang masih beroperasi. Truk-truk besar dan mesin berat terus bekerja. Ia merasa kecewa dan marah."
    show Sulthan_sedih
    Sulthan "..."
    "Proyek besar itu terus berjalan, memakan lebih banyak korban tanpa ada yang bisa menghentikannya."
    "Sulthan hanya bisa melihat dari kejauhan, tubuhnya semakin lemah akibat penyakit yang ia derita."
    hide Sulthan_sedih
    
    scene black with fade
    centered "Sulthan hanya bisa terduduk di tanah, menatap proyek tersebut dengan air mata mengalir di pipinya."
    centered "Tamat"

    jump end_credit

## ================================================ ##
## ================================================ ##

label ending4:
    hide All
    scene black with fade
    "Sulthan pergi ke kantor polisi"

    #ADEGAN KANTOR POLISI
    scene kantor_polisi with fade
    show Polisi at left with dissolve
    Polisi "Selamat siang, Nak. Ada yang bisa kami bantu?"
    show Sulthan at right with dissolve
    Sulthan "(Menelan ludah, suaranya pelan) Selamat siang, Pak. Saya... saya ingin melapor. "
    Polisi "(Memperhatikan ekspresi Sulthan dengan cermat)"
    Polisi "Tentu. Apa yang ingin kamu laporkan?"
    Sulthan "(Terlihat ragu, memegang map lebih erat)\nIni... tentang sebuah proyek besar di dekat tempat tinggal saya. Saya pikir proyek itu mencemari lingkungan kami... dan mungkin menyebabkan penyakit seperti yang saya alami."
    Polisi "(Mengangguk dan mengisyaratkan Sulthan untuk duduk)\n Baik, mari duduk dulu. Ceritakan semuanya dari awal."
    "(Sulthan duduk dan menarik nafas panjang)"
    Sulthan "(Terlihat gelisah)\n Beberapa bulan setelah proyek itu dimulai, saya mulai sakit. Kulit saya gatal, ruam muncul di beberapa bagian tubuh. Awalnya kami pikir ini hanya alergi biasa, tapi semakin lama semakin parah."
    hide Sulthan
    show Sulthan_sedih at right
    Polisi "(Mendengarkan dengan serius)\nDan apa yang membuatmu yakin ini berkaitan dengan proyek tersebut?"
    Sulthan "(Sambil membuka map dan menunjukkan dokumen)\nSaya sempat menemui dokter, dan beliau bilang penyakit saya mungkin disebabkan karena proyek ini, karena dalam proposal ini diterangkan bahwa terdapat beberapa kerugian yang disebabkan proyek ini apabila proyek ini dijalankan."
    hide Polisi
    show Polisi_kaget at left
    Polisi "(Polisi mengangkat alis, terkejut, tapi tetap menjaga ketenangan.)\n Jadi, ayahmu terlibat dalam proyek ini?"
    Sulthan "(Menunduk, suara mulai bergetar)\n
    Saya tidak ingin mempercayainya, Pak. Tapi dokumen ini jelas menunjukkan bahwa ia tahu soal limbah itu. Saya tidak tahu harus bagaimana..."
    Polisi "(Sambil melihat dokumen dan mencatat)\nIni langkah besar yang kamu ambil dengan melapor. Kami akan memeriksa dokumen ini. Tapi kamu harus tahu, melibatkan keluarga dalam masalah ini tidak akan mudah."
    Sulthan "(Mengangguk pelan, matanya berkaca-kaca)\nSaya tahu, Pak. Tapi saya tidak bisa diam saja. Orang-orang di sekitar saya... mereka mungkin terkena dampak yang sama. Ini bukan hanya tentang saya."
    hide Polisi_kaget
    show Polisi_senyum_tipis at left 
    Polisi "(Sambil tersenyum tipis, nada suaranya meyakinkan)\nKamu melakukan hal yang benar. Kami akan mulai menyelidiki ini secepatnya. Apakah kamu bersedia bekerja sama lebih lanjut jika diperlukan?"
    hide Sulthan_sedih
    show Sulthan at right
    Sulthan "(Menatap polisi dengan tatapan tegas meskipun ada sedikit ketakutan di matanya)\nSaya siap, Pak. Apa pun yang diperlukan untuk memastikan ini tidak terus terjadi."
    Polisi "hmmm... baiklah. Kami akan memulai penyelidikan. Terima kasih atas keberanianmu, Sulthan. Jika ada perkembangan, kami akan segera menghubungimu."
    hide sulthan with dissolve
    hide Polisi_senyum_tipis with dissolve

    scene black with fade
    centered "Polisi setuju memulai investigasi \n Sulthan berdiri, mengangguk pelan, dan meninggalkan kantor polisi dengan langkah berat namun hati yang lebih lega."
    centered "Sementara itu di rumah..."

    #ADEGAN DI RUMAH
    scene rumah with fade
    show Dhika at left with dissolve
    Dhika "Sulthan kemana ya, kok belum pulang-pulang. Apa lagi ada kerja kelompok ya makanya bisa lama"
    play sound "TELEPON IPHONE SOUND EFFECT.mp3" volume 0.7
    "(Telepon berbunyi...)"
    hide Dhika
    show Dhika_telepon at left
    stop sound
    Dhika "Halo, dengan Dhika disini. Dengan siapa dimana?"
    Polisi "(Dari telepon) Selamat sore. Apa benar dengan pak Dhika?"
    Dhika "Ya, benar."
    Polisi "(Dari telepon) Kami dari kepolisian Wilayah Semeleketeha memanggil bapak untuk melakukan pemeriksaan lebih lanjut terkait laporan yang baru saja masuk beberapa jam lalu. Kami tunggu kehadirannya pada pukul 7 Malam."
    Dhika "Ada masalah apa ini pak? Mengapa saya tiba-tiba diperiksa seperti ini? saya tidak melakukan kesalahan apapun pak!"
    Polisi "(Dari telepon) Bapak penuhi saja panggilan ini. Kami akan jelaskan nanti. Saya harap bapak menerima panggilan ini dengan serius!"
    Dhika "Siap pak, saya segera kesana (mematikan telepon)."
    hide Dhika_telepon

    scene black with fade
    centered "Sesampainya di kantor polisi, Dhika dibawa ke ruang pemeriksaan dan diinterogasi"

    #ADEGAN INTEROGASI
    scene interogasi with fade
    show Dhika at left with dissolve
    show Polisi at right with dissolve
    Polisi "Pak Dhika, dokumen ini menunjukkan bahwa Anda menerima laporan tentang limbah beracun sebelum proyek dimulai. Tapi Anda tetap menandatangani persetujuan."
    Polisi "Ada juga bukti bahwa beberapa dana yang seharusnya digunakan untuk pengelolaan limbah tidak sesuai penggunaannya. Bisa Anda jelaskan?"
    Dhika "(Suaranya bergetar)\nSaya tidak tahu apa-apa soal itu! Saya hanya bertanggung jawab pada bagian administrasi dan operasional. Bagian keuangan dan lingkungan yang mengatur alokasi dana."
    Polisi "(Sambil mengetuk meja dengan pena)\nTapi tanda tangan Anda ada di dokumen anggaran ini, Pak Dhika. Kami juga menemukan transfer mencurigakan ke rekening pribadi Anda dari salah satu subkontraktor proyek. Bagaimana Anda menjelaskan hal ini?"
    hide Dhika
    show Dhika_gelisah at left
    Dhika "(Terlihat semakin panik\nItu hanya bonus... itu... itu bagian dari insentif proyek! Tidak ada yang ilegal!"
    hide Polisi
    show Polisi_marah at right
    Polisi "(Menatap tajam)\nBonus? Atau Anda menutup mata terhadap pelanggaran lingkungan sebagai gantinya? Karena, dari semua bukti ini, tampaknya Anda menerima pembayaran untuk membiarkan pengelolaan limbah ini diabaikan."
    hide Dhika_gelisah
    show Dhika_marah at left
    Dhika "(Mulai kehilangan ketenangan, suaranya meninggi)\nSaya tidak tahu kalau ini akan berdampak separah ini! Saya hanya melakukan apa yang disuruh oleh atasan saya."
    Polisi "(Tenang namun tegas) \nPak Dhika, ini bukan hanya tentang Anda. Ini soal ratusan orang yang terkena dampak pencemaran ini. Dan dari semua bukti yang kami miliki, Anda terlibat dalam korupsi yang menyebabkan dampak besar pada kesehatan masyarakat dan lingkungan."
    hide Dhika_marah
    show Dhika_sedih at left
    Dhika "..."
    hide Dhika_sedih
    hide Polisi_marah

    scene black with fade
    centered "Kasus berlanjut hingga tahap persidangan"
    centered "Di ruang sidang, Pak Dhika berdiri sebagai terdakwa. Jaksa memaparkan argumennya."

    #ADEGAN SIDANG
    scene courthouse with fade
    show Dhika_sedih at left  with dissolve
    show Jaksa at right with dissolve:
        zoom 0.6
    show Hakim at center with dissolve
    Jaksa "Yang Mulia, terdakwa, Pak Dhika, tidak hanya lalai dalam tanggung jawabnya sebagai manajer proyek, tetapi juga menerima suap untuk mengabaikan pelanggaran pengelolaan limbah."
    Jaksa "Bukti transfer dana ilegal dan dokumen proyek menunjukkan bahwa terdakwa secara sadar menempatkan keuntungan pribadi di atas kepentingan masyarakat dan lingkungan."
    play sound "gavel-of-justice-124029.mp3"
    Hakim "(mengetuk palu)\nTerdakwa dinyatakan bersalah atas kelalaian yang menyebabkan pencemaran lingkungan, serta tindak pidana korupsi."
    Hakim "Pengadilan menjatuhkan hukuman lima tahun penjara dan denda sebesar 1,5 miliar rupiah, yang sebagian akan diberikan sebagai kompensasi kepada korban pencemaran."
    hide Dhika_sedih
    hide Jaksa
    hide Hakim
    scene courthouse_spectator with fade
    show Sulthan_senyumtipis with dissolve
    "Sulthan duduk di kursi penonton, menunduk mendengar putusan hakim. Ada rasa sakit bercampur kelegaan di wajahnya."
    hide Sulthan_senyumtipis with dissolve

    #Adegan masuk Penjara
    scene penjara with fade
    "Dhika dikurung di dalam penjara akibat tindak pidana korupsi yang dilakukannya"
    scene sel_penjara with fade
    show Dhika_penjara at center with dissolve:
        zoom 1.5
    "Dhika sedih dan kecewa terhadap dirinya sendiri. Ia menyesal telah mencuri uang rakyat hanya karena ketamakannya"
    hide Dhika_penjara with dissolve
    
    scene proyek with fade
    show Sulthan at left with dissolve
    "Sulthan berdiri di depan lokasi proyek yang sekarang ditutup. Seorang reporter mendekatinya."
    show Reporter at right with dissolve
    Reporter "Sulthan, apa pendapat Anda tentang penutupan proyek ini dan pengungkapan kasus korupsi yang melibatkan beberapa pejabat?"
    hide Sulthan
    show Sulthan_senyumtipis at left
    Sulthan "(Menatap lokasi proyek yang kosong)\n
    Proyek ini seharusnya membawa manfaat, bukan kerusakan. Tapi karena keserakahan dan korupsi, semuanya hancur. Saya berharap ini menjadi pengingat bahwa uang tidak sebanding dengan nyawa dan lingkungan."
    "Reporter mengangguk, lalu meninggalkan Sulthan yang berdiri diam, merenungi semua yang telah terjadi."
    hide Reporter with dissolve
    "Sulthan merenungkan apakah yang Ia lakukan adalah langkah yang tepat. Ia tahu, untuk kebaikan orang banyak, Ia harus melakukan hal ini\n
    Tetapi... Sekarang ayah yang Ia sayangi berakhir di penjara"
    "Namun, Ia yakin bahwa yang Ia lakukan adalah hal yang tepat. Pengorbanan yang Ia lakukan adalah langkah yang mulia untuk menyelamatkan orang banyak. Kalau bukan ia yang melakukannya, siapa lagi?"
    
    scene black with fade
    centered "Dhika dipenjara, Proyek berhenti beroperasi.\nSulthan dan warga sekitar pun kian membaik dan menjadi sehat kembali"
    centered "Tamat"
    jump end_credit

## ================================================ ##
## ================================================ ##

label end_credit:
    scene black
    centered "Kamu telah menamatkan game ini"
    centered "Korupsi menghancurkan keadilan dan merampas hak-hak rakyat.\nJangan membiarkan korupsi merusak masa depan generasi penerus kita. \n \n end credit incoming..."
    call credits
    return

label credits:
    $ credits_speed = 25 #scrolling speed in seconds
    scene black #replace this with a fancy background
    with dissolve
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(1)
    hide theend
    show cred at Move((0.5, 3.3), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(1)
    hide thanks
    return

