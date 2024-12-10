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



# Image Buat Background
image RTengah = "background/ruang tengah.JPG"
image kantor_ayah = "background/kantor dhika.JPG"
image desa = "background/desa.JPG"
image halaman = "background/halaman rumah.JPG"
image kantor_polisi = "background/kantor polisi.JPG"
image penjara = "background/penjara.JPG"
image rumah = "background/rumah.JPG"
image proyek = "background/tempat proyek.JPG"

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
    centered "Confrontation..."
    scene RKantor with fade
    
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
    Sulthan "(Dalam hati) Aku tau aku yang terkena imbas dari semua ini, tapi aku sadar Ayah tidak punya pilihan lain. Apakah aku harus mempercayai Ayahku?"
    
    centered "Pikiran Sulthan kacau. Sulthan paham bahwa Ayahnya tidak mempunyai pilihan. Namun, di sisi lain, Sulthan merasa dikhianati karena ialah yang terkena imbasnya. Sulthan mencoba untuk mempercayai Ayahnya dengan rasa ragu."
    
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

label investigate: 
    scene black with fade
    centered "Investigation..."

    scene RKantor with fade

    show Sulthan at right with dissolve
    Sulthan "Kayaknya ada suara langkah kaki mendekat. Aku harus bersikap tidak tahu apa-apa."

    show Dhika at left with dissolve
    Dhika "Eh, kamu sudah disini (melihat Sulthan yang lesu), kamu lagi kenapa nak?"
    Sulthan "Ga kenapa-napa, langsung pulang aja yaa yah. Aku udah lemes banget."
    hide Dhika with dissolve
    hide Sulthan with dissolve

    "Sulthan dan Ayahnya meninggalkan ruangan kerja tersebut dan menuju rumah."

    scene RTengah with fade

    show Sulthan at left with dissolve
    Sulthan  "Kenapa ayah bisa setega ini, apa yang ayah pikirkan ketika mengambil keputusan ini? Kenapa malah aku yang kena imbasnya? Apa yang harus aku lakukan sekarang? Apakah semua yang ku lihat benar-benar kenyataannya?"
    Sulthan "Tidak, aku tidak boleh kalah dengan keadaan ini. Kalau ayah saja bisa melakukan ini, aku juga bisa. dia harus merasakan apa yang aku rasakan."
    Sulthan "Bagaimana aku memulainya? Sepertinya aku harus menyusun rencana dulu. Hmm, kira-kira apa ya?"

    menu :
        "Kamu ingin melakukan investigasi, Apa yang akan kamu lakukan setelah ini?"
        "Cek sample air di rumah":
            Sulthan "Aha! aku bisa mulai dengan mengambil sampel air dari rumah ini. Kayaknya aku bisa pakai lab di sekolah buat meneliti ini pas jam istirahat. Aku bisa ngambil air dari wastafel di dapur."

            hide Sulthan with dissolve
            "Sulthan mengambil alat tulis dan kertas dari laci mejanya, menuliskan semua rencana yang berjalan di pikirannya, memastikan semua skenario berjalan sempurna."
            "Tidak peduli dengan apa yang akan dihadapinya. yang ia inginkan hanya sebuah pembalasan yang sempurna. Sulthan mulai menyusun rencana yang sempurna."
            show Sulthan at center with dissolve
            Sulthan "Baiklah, aku akan mulai dari mengumpulkan sampel dari air di rumahku."
            scene black with fade
            centered "Sulthan berdiri dari meja belajarnya, membuka pintu dan mulai berjalan menuruni anak tangga, berbelok ke kanan mengikuti lorong panjang yang mengarahkannya menuju dapur. Ia melihat sekelilingnya dan berjalan mendekati wastafel yang berada tidak jauh dari kompor di sebelah kirinya. Ia membuka keran secara perlahan, memastikan air tidak mengenai bagian tubuhnya. ia mengambil 1 botol air mentah dari keran rumahnya." 
            
            scene RTengah with fade
            show Sulthan at center with dissolve
            Sulthan "Okeh, tahap 1 selesai. Besok akan kubawa ke lab di sekolah."
            Sulthan "Saatnya tidur sebelum Ibu marah."

            scene black with fade
            "keesokan harinya, di lab sekolah..."

            # scene nya ganti ke lab anjay tapi belom ada lab cuki
            Sulthan "Pertama aku bisa mengambil strip test reagen buat mengecek kandungan airnya. Dimana strip tes nya. Kayaknya ada di rak alat-alat kimia."
            Sulthan "Aku tinggal masukin strip tesnya ke air. Eh, aku butuh gelas kimia sepertinya."
            Sulthan "..."
            Sulthan "..."

            Sulthan "okeh gelas kimia sudah, tinggal celup deh"
            '...'
            'Warna strip test berubah dari kuning menjadi ungu'

            Sulthan 'Sudah kuduga, memang air ini terkontaminasi. Kira-kira mengandung apa ya?'
            Sulthan '(membuka google)'
            Sulthan 'WAY, Timbal konsentrasi tinggi di dalam airnya! Pantas saja tubuhku bisa jadi gini. Ayah memang sialan!'

            Sulthan 'Hmmm, oke satu bukti sudah. Tapi apakah bukti ini cukup kuat untuk membuktikan ayah terlibat?'
            Sulthan "Harus apalagi ya selanjutnya?"

            menu:
                "Cek kembali dokumen resmi semalam":
                    Sulthan "AH IYA, PROPOSAL ITU! Aku bisa kembali ke kantor ayah dan memfoto proposalnya. Baiklah, akan kulakukan setelah pulang sekolah."
                    hide Sulthan with dissolve

                    "Selesai sekolah Sulthan langsung ke kantor ayahnya"
                    scene black with fade

                    scene RKantor with fade
                    show Sulthan at left with dissolve
                    Sulthan "(dalam hati) Aku ngeboong apa ya biar bisa masuk ke kantor ayah?"

                    show Serena at right with dissolve
                    Sulthan "Selamat sore, Mbak. Aku mau jemput ayah. Ayah ada dimana, ya?"
                    Serena "Pak Dhika lagi ada di ruang meeting. Kamu tunggu di ruangannya saja ya."
                    Sulthan "Baik, Mbak."
                    hide Serena


                    Sulthan "Aku harus segera mencari surat itu sebelum ketahuan orang-orang."
                    "Sulthan membuka laci kedua meja kerja ayahnya, tempat dimana ia menemukan surat perjanjian itu."
                    Sulthan "..."
                    Sulthan "..."
                    Sulthan "Ah ini dia boi"
                    Sulthan "saatnya difoto sebagai bukti tambahan"
                    "Cekrek!"

                    Sulthan "Dengan 2 bukti ini, aku yakin polisi akan mempercayai ucapanku!"
                    Sulthan "Saatnya melaporkan ke kantor polisi"
                    hide Sulthan

                    jump ending4


                "Lapor Polisi":
                    Sulthan "Rasanya sudah cukup deh bukti ini"
                    Sulthan "Sepulang sekolah, aku langsung ke kantor polisi saja deh"

                    jump ending3



        "Tidak melakukan apapun":
            Sulthan "Ah rasanya terlalu sulit untuk mencari bukti apapun, biarkan saja polisi yang melakukannya"
            hide Sulthan with dissolve
            
            scene black with fade
            "Keesokan harinya, Sulthan langsung melaporkan tindakan ayahnya ke kantor polisi"

            jump ending3

    

label believe:
    scene black with fade
    scene RKantor with fade

    show Sulthan at right with dissolve
    show Dhika at left with dissolve
    Sulthan "Aku ingin percaya pada Ayah tapi apakah Ayah bisa berjanji padaku untuk mencari solusinya?"
    Dhika "Bisa, Ayah selama ini juga selalu mencari cara buat menyembuhkan kamu."
    Sulthan "(Dalam hati) Mungkin Ayah ada benarnya. Sepertinya aku bisa mempercayainya. Lagipula dia juga Ayahku."
    centered "Sulthan pun percaya pada Ayahnya dan bertekad untuk mendukung apapun yang Ayahnya lakukan. Sulthan dan Ayahnya mulai mengumpulkan semua bukti yang bisa menutup proyek tersebut dan mengakhiri semua penderitaan yang dialami."
    Sulthan "Apa yang bisa aku bantu, yah?"
    Dhika "Kita bisa mulai dengan meninjau seisi rumah dengan air yang terkontaminasi."
    hide Sulthan
    show Sulthan_senyumtipis at right
    Sulthan "Baiklah! Ayo kita pulang dan segera mencari bukti-buktinya!"
    # tambahin musik
    hide Dhika with dissolve
    Sulthan "(Dalam hati sambil menuruni tangga) Aku tidak percaya semua ini terjadi. 10 menit lalu aku sangat ingin menyerah dan saat ini Aku merasa sangat bahagia karena dapat menemukan penyebab masalah ini dan akan menyelesaikannya. Aku ingin cepat-cepat pulang."
    hide Sulthan_senyumtipis with dissolve  
    scene black with fade
    pause(2.0)
    scene RTengah with fade

    centered "Mereka sampai di rumah. dengan cepat keluar dari mobil dan berjalan menuju pintu."

    show Sulthan at right with dissolve
    show Dhika at left with dissolve
    Dhika "Maaf, nak. Tampaknya hari sudah larut. Kita bisa memulainya esok hari karena Ayah harus bekerja."
    hide Sulthan_senyumtipis
    show Sulthan_sedih
    Sulthan "Yah, oke deh. Selamat tidur Ayah."
    hide Dhika with dissolve
    Sulthan "Ah padahal aku sudah sangat bersemangat. Gapapa deh aku bisa mulai esok hari."
    hide Sulthan_sedih with dissolve
    scene black with fade

    centered "Selang beberapa hari..."
    scene RTengah with Fade
    show Sulthan_sedih with dissolve
    Sulthan "Kok gak ada info apa-apa dari Ayah. Kapan bakal dimulai, ya? Apa aku inisiatif ya buat mulai? Gak deh, aku nunggu Ayah aja."
    hide Sulthan_sedih with dissolve
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
    show Sulthan_sedih at left with dissolve
    show Dhika at right with dissolve
    Sulthan "Ayah… Ayah bilang akan melakukan sesuatu untuk menghentikan proyek itu… Sudah berbulan-bulan… Apa yang sudah Ayah lakukan?" 
    #tambahin musik
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
    scene black with fade
    pause (2.0)

    centered "Beberapa hari kemudian, Sulthan meninggal karena penyakitnya udah menyebar ke seluruh badan"

    scene RTengah with fade
    show Serena_sedihbanget at left with dissolve
    show Dhika_sedih at right with dissolve
    Serena "Kenapa, Pak? Kenapa kita tidak melakukan apa pun? Kenapa kita biarkan Sulthan pergi seperti ini?"
    Dhika "Aku… Aku tidak tahu… Aku hanya ingin melindungi kalian… Aku pikir aku punya waktu lebih banyak…"
    hide Serena_sedihbanget
    show Serena_marah
    Serena "Melindungi? Melindungi dari apa? Kau hanya melindungi dirimu sendiri, Dhika! Sulthan pergi karena kau terlalu takut untuk bertindak!"
    Dhika "Aku… Aku menyesal…"
    hide Serena_marah with dissolve
    hide Dhika_sedih with dissolve
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