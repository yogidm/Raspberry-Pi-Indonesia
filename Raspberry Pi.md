


```
sudo apt install gdebi-core

```
## Daftar isi

1. Apa itu Raspberry Pi?
    + Raspberry Pi 3b+
    + Jenis dan spesifikasinya
    + Konfigurasi pin dan modul perangkat keras
2. Sistem Operasi pendukung Raspbery Pi
3. Apa saja yang dapat kita lakukan dengan Raspberry Pi?
4. Akses GPIO pada Raspberry Pi
4. Menggunakan GUI
5. Yuk membuat game kecil-kecilan
6. Komunikasi dengan Arduino
7. Welcome to Internet of Things
8. Kamera pada Raspberry Pi
9. Apa selanjutnya?


# 1. Apa itu Raspberry Pi?

**`Raspberry Pi`** merupakan salah satu jenis komputer mini (mini-PC) yang sering digunakan untuk pembelajaran pemograman sistem tertanam di sekolah ataupun universitas. Raspberry Pi juga sering digunakan pada kasus jaringan, [IoT (Internet of Things)](https://id.wikipedia.org/wiki/Internet_untuk_Segala), dan [Robotika](https://en.wikipedia.org/wiki/Robot) dengan keunggulannya yang berbentuk mini. Dengan fitur yang lengkap, memungkinkan mini-PC ini mudah terhubung dengan beberapa perangkat lainnya seperti [Arduino](http://arduno.cc), Android, maupun web server. Selain itu, Raspberry Pi ini juga sudah mendukung [ROS (Robot Operating System)](http://wiki.ros.org/) sebagai perpustakaan dan alat untuk kontrol robot lanjutan. Untuk referensi tentang Raspberry lebih lanjut, klik di [Wikipedia Reference](https://en.wikipedia.org/wiki/Raspberry_Pi#Model_B).


## Raspberry Pi 3b+

Versi berapa kah Raspberry Pi yang kita akan gunakan? Yups, untuk mengetahuinya, dapat kita lihat pada papan Raspberry Pi bagian atas. Disitu sudah dituliskan jenis dan tahun pembuatannya. Atau kurang lebih akan tampak pada gambar dibawah ini:


<img src="GambarPi/RasPi-Crop-1.png">[Gambar dari www.raspberrypi.org](https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/)

---

## Jenis dan Spesifikasinya 

Raspberry Pi 3b+ merupakan produk termuhtakhir dari jenis Raspberry Pi 3. Jenis ini memiliki spesifikasi sebagai berikut:

+ Broadcom BCM2837B0, Cortex-A53 (ARMv8) 64-bit SoC @ 1.4GHz 
+ 1GB LPDDR2 SDRAM
+ 2.4GHz and 5GHz IEEE 802.11.b/g/n/ac wireless LAN, Bluetooth 4.2, BLE
+ Gigabit Ethernet over USB 2.0 (maximum throughput 300 Mbps)
+ Extended 40-pin GPIO header
+ Full-size HDMI
+ 4 USB 2.0 ports
+ CSI camera port for connecting a Raspberry Pi camera
+ DSI display port for connecting a Raspberry Pi touchscreen display
+ 4-pole stereo output and composite video port
+ Micro SD port for loading your operating system and storing data
+ 5V/2.5A DC power input
+ Power-over-Ethernet (PoE) support (requires separate PoE HAT)

atau apabila kita komparasi dengan beberapa jenis Raspberry Pi lainnya:

<img src="GambarPi/Specifications.png">[Sumber](https://image.ibb.co/bweuCz/Specifications.png)

lalu, berapa harga kisaran sebuah Raspberry Pi yang dijual dipasaran? (estimasi harga dari website resmi)

- Raspberry Pi 1, Model A & Model B (2012, discontinued)
- [Raspberry Pi 1, Model B+](https://www.raspberrypi.org/products/raspberry-pi-1-model-b-plus/) (July, 2014)
- [Raspberry Pi 1, Model A+](https://www.raspberrypi.org/products/raspberry-pi-1-model-a-plus/) (November, 2014)
- [Raspberry Pi 2, Model B](https://www.raspberrypi.org/products/raspberry-pi-2-model-b/) (February, 2015)
- [Raspberry Pi Zero](https://www.raspberrypi.org/products/raspberry-pi-zero/) (November, 2015)
- [Raspberry Pi 3, Model B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/) (March, 2016)
- [Raspberry Pi Zero W](https://www.raspberrypi.org/products/raspberry-pi-zero-w/) (February, 2017)
- [Raspberry Pi 3, Model B+](https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/) (March, 2018)
- [Raspberry Pi 3, Model A+](https://www.raspberrypi.org/products/raspberry-pi-3-model-a-plus/) (November, 2018)



Bagi Anda ingin mengembangakan Raspberry Pi lebih lanjut, berikut beberapa referensi lanjutan:

+ [Schematic Raspberry Pi 3B+](https://www.raspberrypi.org/documentation/hardware/raspberrypi/schematics/rpi_SCH_3bplus_1p0_reduced.pdf)
+ [Mechanical Drawing (Board)](https://www.raspberrypi.org/documentation/hardware/raspberrypi/mechanical/rpi_MECH_3bplus.pdf)
+ [Mechanical Drawing (Case)](https://www.raspberrypi.org/documentation/hardware/raspberrypi/mechanical/rpi_MECH_3bplus_case.pdf)
+ [Basic Guides to Configuring Raspberry Pi](https://github.com/raspberrypi/documentation/tree/master/configuration)
+ [Techincal FAQ](https://github.com/raspberrypi/documentation/tree/master/faqs)

---

## Konfigurasi Pin dan Modul Perangkat Keras

GPIO (General Purpose Input/Output) pin merupakan sebuah fitur dari Raspberry Pi untuk melakukan interaksi dengan perangkat-perangkat lainnya diluar Raspberry Pi. Semisal kita ingin menyala-matikan sebuah lampu LED, kita dapat menggunakan pin `GPIO` untuk memberikan perintah atau isyarat kepada rangkaian kontrol lampu LED. Perintah atau isyarat tersebut biasaya dituliskan pada sebuah program dengan bahasa Python dengan menggunakan pustaka `RPi.GPIO` yang dapat dengan mudah diunduh menggunakan perintah `pip install RPi.GPIO` pada terminal Linux OS based yang digunakan pada Raspberry Pi kalian. 

Perangkat keras Raspberry Pi 3b+ merupakan fitur-fitur pendukung Raspberry Pi yang dapat digunakan atau tidak atau sesuai kebutuhan penggunannya. Fitur tersebut dapat digunakan dengan menghubungkan perangkat tambahan sesuai dengan jenis peghubungnya. Semisal untuk 4xUSB yang tersedia, dapat dihubungkan dengan USB Keyboard dan USB Mouse sebagai perangkat masukan pada sistem operasi didalamnya. Atau CSI camera port yang digunakan untuk menghubungkan Raspberry Pi camera yang dijual terpisah. Namun kita juga bisa menggunakan USB Webcam untuk mengganti Raspberry Pi camera untuk kebutuhan kita. Oleh karenanya, penggunaan fitur-fitur yang tersedia tidaklah harus kesemuanya disediakan dan digunakan. **Bergantung pada kebutuhan kita.** 

**Akan tetapi**, ada satu yang perlu dan harus kita butuhkan agar Raspberry Pi kita dapat bekerja, yaitu catu daya. Ya, catu daya yang dibutuhkan adalah `5V/2.5A DC` dengan port `universal micro USB`, atau apabila kalian kesusahan untuk mencari sumber catu dayanya, kalian dapat menggunakan `charger smartphone` kalian. :D

![RaspberryPi3B+](https://image.ibb.co/bsrfkK/raspberry_pi_circuit_note.png)

---



# 2. Sistem Operasi pendukung Raspberry Pi

Ada banyak sistem operasi pendukung Raspberry Pi yang bergantung pada kebutuhannya masing-masing. Pada umumnya, sistem operasi Raspberry Pi yang digunakan adalah `Raspbian`, yaitu sistem operasi resmi berbasis Debian. Untuk sistem operasi lainnya yang sering digunakan yang berbasis Ubuntu, dapat menggunakan `Ubuntu MATE`. Ketika kita tidak menggunakan sistem operasi yang resmi, kita menyalahi aturan penggunaan Raspberry Pi. Kebanyakan sumber yang digunakan pada Rapberry Pi bersifat `Creative Common` atau `open-source` yang memungkinkan kita dapat merubah dan mengembangkan sesuai kebutuhan kita sesuai keinginan kita. Yups, sama halnya dengan sistem operasi Linux based, yang open-source. `Kita bisa memodifikasi sesuai keinginan kita. :D`

Berikut adalah daftar sistem operasi yang mendukung Raspberry Pi :


- [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) - The official supported Raspberry Pi OS, based on Debian and available as a lite version.
- [NOOBS](https://www.raspberrypi.org/downloads/noobs/) - New Out Of the Box Software, an easy OS installer for beginners.
- [Ubuntu MATE](https://ubuntu-mate.org/raspberry-pi/) - Ubuntu distribution for the Raspberry Pi based on MATE desktop. `Supports Raspberry Pi 2+`
- [Snappy Ubuntu Core](https://developer.ubuntu.com/core/get-started/raspberry-pi-2-3) - Official (minimal) Ubuntu distribution for IoT. `Supports Raspberry Pi 2+`
- [Windows 10 IoT Core](https://docs.microsoft.com/nl-nl/windows/iot-core/downloads) - Windows 10 distribution for IoT. `Supports Raspberry Pi 2+`
- [OSMC](https://osmc.tv/) - Open Source Media Centre, based on Kodi.
- [PiNet](http://pinet.org.uk/) - System to manage Raspberry Pi classrooms.
- [Risc OS](https://www.riscosopen.org/content/downloads/raspberry-pi) - Non-Linux OS originated from the group that developed the ARM microprocessor.
- [RuneAudio](http://www.runeaudio.com/) - Free and open source OS that turns embedded hardware into Hi-Fi music players.
- [OpenELEC](http://openelec.tv/) - Open Embedded Linux Entertainment Center, a very lightweight Kodi build.
- [HypriotOS](http://blog.hypriot.com/about/) - Minimal Debian-based operating system, optimized to run Docker.
- [Kali Linux](https://www.offensive-security.com/kali-linux-arm-images/) - Penetration Testing & Ethical Hacking Linux distro for ARM devices.
- [RetroPie](https://retropie.org.uk/) - Retro-gaming on the Raspberry Pi.
- [Alpine Linux](https://wiki.alpinelinux.org/wiki/Raspberry_Pi) - Security-oriented, lightweight Linux distribution based on musl libc and busybox.
- [Arch Linux ARM](https://archlinuxarm.org/) - Lightweight and flexible Linux distribution that tries to Keep It Simple.
- [Volumio](https://volumio.org/) - Headless audiophile music player, designed to play music with the highest possible fidelity.
- [Recalbox](https://www.recalbox.com) - Drag & drop light-weight retro-gaming and media center on the Raspberry Pi.
- [Lakka](http://lakka.tv) - Retro-gaming on the Raspberry Pi built entirely on RetroArch.
- [RasPlex](http://www.rasplex.com/) - Plex client for the Raspberry Pi.
- [chilipie-kiosk](https://github.com/futurice/chilipie-kiosk) - Image which boots directly into full-screen Chrome, perfect for dashboards and build monitors. `Supports Raspberry Pi 2+`
- [DietPi](https://github.com/Fourdee/DietPi) - Minimal image designed to fit on a 2GB SD card, with tons of configurable settings and scripts.
- [CentOS](https://wiki.centos.org/SpecialInterestGroup/AltArch/Arm32/RaspberryPi3) - CentOS on the Raspberry Pi. *Supports Raspberry Pi 2+*
- [Minibian](https://minibianpi.wordpress.com/) - Minimal Raspbian (lighter than Jessie Lite).
- [BerryBoot](http://www.berryterminal.com/doku.php/berryboot) - Bootloader/universal OS installer, with support to VNC and HDMI-CEC.
- [PirateBox](https://piratebox.cc/raspberry_pi:diy) - Anonymous offline mobile file-sharing and communications system.
- [OctoPi](https://octopi.octoprint.org/) - Distribution for 3d printers.
- [Kano OS](http://developers.kano.me/downloads/) - Open-source OS for exploration, creation, and play – free for Raspberry Pi and the new Pi 3.
- [balenaOS](https://www.balena.io/os/) - open source OS to run Docker containers on embedded devices that's been designed for reliability and proven in production.
- [Fedora](https://fedoraproject.org/wiki/Raspberry_Pi#Preparing_the_SD_card) - Linux Fedora distribution built for the Pi. `Supports Raspberry Pi 2+`
- [motionEyeOS](https://github.com/ccrisan/motioneyeos/wiki) - Linux distribution that turns a single-board computer into a video surveillance system.
- [NextCloudPi](https://ownyourbits.com/2017/02/13/nextcloud-ready-raspberry-pi-image/) - Nextcloud ready image based on Raspbian. Features Nextcloud 11 running on Raspbian 8, with PHP 7 and HTTP2 enabled Apache server.
- [PiDeck](http://pideck.com/) - Small form factor DVS system allowing you to control digital music files with timecode vinyl.
- [OpenWRT](https://wiki.openwrt.org/toh/raspberry_pi_foundation/raspberry_pi) - OpenWrt is described as a Linux distribution for embedded devices for network management.
- [FreeBSD](https://wiki.freebsd.org/FreeBSD/arm/Raspberry%20Pi) - FreeBSD is an advanced computer operating system used to power modern servers, desktops, and embedded platforms.
- [NetBSD](https://wiki.netbsd.org/ports/evbarm/raspberry_pi/) - NetBSD is a free, fast, secure, and highly portable Unix-like Open Source operating system.
- [Hass.io](https://home-assistant.io/hassio/installation/) - Home automation operating system/application for embedded device, also available standalone.
- [Android Things](https://developer.android.com/things/hardware/raspberrypi.html) - Build connected devices for a wide variety of consumer, retail, and industrial applications. `Supports Raspberry Pi 3`
- [Gladys Project](https://gladysproject.com/en/) - Gladys, Your home assistant. `Supports Raspberry Pi 3`
- [OpenMediaVault](https://www.openmediavault.org/) - OpenMediaVault is the next generation network attached storage (NAS) solution based on Debian Linux containing services like SSH, (S)FTP, SMB/CIFS, DAAP media server, RSync, BitTorrent client and many more. `Supports Raspberry Pi 3`
- [EZ-WifiBroadcast](https://github.com/bortek/EZ-WifiBroadcast/wiki) - Affordable Wireless Digital HD Video Transmission made easy. `Supports Raspberry Pi 3` `Supports Raspberry Pi Zero`
- [DroneBridge](https://github.com/seeul8er/DroneBridge) - A WifiBroadcast extension to make for a real alternative to DJI Lightbridge and other similar systems. `Supports Raspberry Pi 3`
- [TrueOS](https://www.trueos.org/handbook/pico.html) - FreeBSD-based thin client solution. `Supports Raspberry Pi 2+`
- [OpenHABian](https://docs.openhab.org/installation/openhabian.html) - A preconfigured version of the OpenHAB home automation software. `Supports Raspberry Pi 2+]`
- [FabScanPi](https://mariolukas.github.io/FabScanPi-Server/) - FabScanPi is an open source 3D laser scanner using the Raspberry Pi Camera Module. `Supports Raspberry Pi 2+`
- [Rocket Show](https://rocketshow.net) - Play synced backing tracks, videos and DMX light-sequences live on stage. `Supports Raspberry Pi 3`
- [SamplerBox](http://www.samplerbox.org/makeitsoftware) - Drop'n'play sampler: drop .WAV samples on the SD card, and play!
- [SARPi](http://sarpi.fatdog.nl/index.php?p=sarpi) - Stands for the Slackware ARM on Raspberry Pi.
- [Gentoo](https://wiki.gentoo.org/wiki/Raspberry_Pi) - Gentoo Stage 3 tarball for Raspberry Pi.
- [MoodleBox](https://moodlebox.net/) - The MoodleBox provides a Moodle learning management system on Raspberry Pi. `Supports Raspberry Pi 3`

# 3. Apa saja yang dapat kita lakukan dengan Raspberry Pi?

Pada bagian ini, kita akan memulai untuk membayangkan apa saja yang akan bisa kita buat dari satu papan yang berisi sistem tertanam sebesar kartu ATM. Semisal kita akan membuat sebuah [Smart TV ](https://www.hackster.io/apugog/raspberry-pi-smart-tv-d886de) yang hanya membutuhkan beberapa komponen pendukung seperti layar monitor dan kabel HDMI to VGA, atau kita juga dapat membuat sebuah sistem otomasi yang biasanya disebut [Smart Home](https://www.electromaker.io/blog/article/9-best-raspberry-pi-smart-home-software-options) untuk melakukan banyak hal pada rumah kita terutama ketika kita memiliki mobilitas tinggi dan harus mengurus rumah dari kejauhan dimana sistem ini sudah terintegrasi dengan internet. Ya, kurang lebih sistem tersebut sudah melekat dengan IoT atau [Internet of Things](https://medium.com/@paliwalmanu99/internet-of-things-raspberry-pi-home-automation-system-based-on-iot-a5862fdb4d58). 

Kadang kita sebagai penikmat kemajuan teknologi, kita tidak akan terus berdiam dalam berfikir untuk terus ber-**inovasi**. Dengan semangat itulah, mendorong kita untuk terus belajar. Akan tetapi, budaya untuk membaca kadang menjadi halangan. Belum lagi membaca artikel berbahasa Inggris. Ya, semua berawal dari terbiasa. Agar terbiasa, berawal dari memaksa. Memaksa diri sendiri untuk segera belajar. Agar kita terbiasa `Belajar` dimanapun dalam situasi apapun. Awal untuk belajar adalah `MEMBACA`. Membaca semua keadaan sekitar yang dapat kita gapai sesuai dengan porsi masing-masing. Ketika semua proses belajar sudah menjadi kebiasaan, `ILMU` yang muncul dihadapan kita, akan dengan mudah diterima. Mengambil `MAKNA` dan `KESAN` darinya (apapun itu) sebagai satu titik dimana kita sudah belajar. **Melakukan - Merasakan - Mengingat - Menprinsipkannya**. 

Oleh karenanya, sebagai bahan lanjutan yang dapat kalian lakukan sendiri, dengan kemauan sendiri, setelah selesai membaca referensi ini, ada beberapa proyek yang sudah dilakukan banyak orang sebelumnya. Untuk mempermudah pembacaan referensi berbahasa Inggris, dapat menggunakan fitur Google Translate dengan menempel alamat sebuah website pada terjemahannya. Seperti pada [tautan berikut](https://translate.google.com/translate?hl=en&sl=en&tl=id&u=https%3A%2F%2Fopensource.com%2Fresources%2Fraspberry-pi). 

Berikut beberapa daftar rujukan proyek yang dapat kalian baca:


- [Mini OONTZ](https://cdn-learn.adafruit.com/downloads/pdf/mini-oontz-3d-printed-midi-controller.pdf) - 3D printed mini MIDI controller.
- [Power Sniffing Strip](https://hackaday.com/2012/10/04/malicious-raspberry-pi-power-strip-looks-a-bit-scary/) - Enclosure in a power strip, sniffing network data.
- [Raspberry Pi Erlang Cluster](https://medium.com/@pieterjan_m/erlang-pi2-arm-cluster-vs-xeon-vm-40871d35d356#.bpao66cm8) - Erlang cluster on a Raspberry Pi 2.
- [NTP driven Nixie Clock](http://www.mjoldfield.com/atelier/2012/08/ntp-nixie.html) - Nixie Tube Clock powered by a Raspberry Pi.
- [40-node Raspberry Pi Cluster](http://hackaday.com/2014/02/17/40-node-raspi-cluster/) - Cluster aimed to be under the size of full tower desktop.
- [Raspberry PI Hadoop Cluster](http://www.widriksson.com/raspberry-pi-hadoop-cluster/) - Big Data cluster running on the Raspberry Pi.
- [Multi-Datacenter Cassandra on 32 Raspberry Pi’s](http://www.datastax.com/dev/blog/32-node-raspberry-pi-cassandra-cluster) - Showcase for the always on, fault tolerant nature of Cassandra using a Raspberry Pi cluster board.
- [Building a Ceph Cluster on Raspberry Pi](http://bryanapperson.com/blog/the-definitive-guide-ceph-cluster-on-raspberry-pi/) - Highly redundant and low power usage RADOS home storage solution.
- [Smart Mirror](https://github.com/evancohen/smart-mirror) - Voice controlled smart mirror with IoT integration. `Supports Raspberry Pi 2+`
- [Magic Mirror](http://magicmirror.builders) - The original open source modular smart mirror platform. `Supports Raspberry Pi 2+`
- [Chromebook Charger Kiosk](https://www.reddit.com/r/raspberry_pi/comments/53nj1z/chromebook_charger_kiosk_last_minute_charge_for/) - Timed charging station for students using Chromebooks at school.
- [Jasper](https://jasperproject.github.io/) - Flexible open source personal assistant.
- [Lightberry](https://lightberry.eu) - Led lighting solution dedicated for raspberry pi and your TV.
- [SecPi](https://github.com/SecPi/SecPi) - Raspberry Pi based home alarm system.
- [PiClock](https://github.com/n0bel/PiClock) - Fancy Clock built around a monitor and a Raspberry Pi.
- [Garage Door Opener](https://github.com/benjefferies/gogo-garage-opener) - Garage door opener using the [Garage Opener](https://play.google.com/store/apps/details?id=com.ionicframework.gogogarageopenerui416115&hl=en) app to control garage door.
- [Movel](https://github.com/stevelacy/movel) - Raspberry Pi car computer.
- [PiFanTuner](https://github.com/winkidney/PIFanTuner) - CPU-fan-tuner daemon, just enables your fan as necessary. `Supports Raspberry Pi 3`
- [SkyJack](https://samy.pl/skyjack/) - Take over and allow full control over any Parrot AR Drone within wireless distance.
- [Nerves Project](https://github.com/nerves-project) - Craft and deploy bulletproof embedded software in Elixir.
- [Wordpress using Docker](https://github.com/rothgar/rpi-wordpress) - Run a Wordpress site in containers with dynamic DNS.
- [Pi-hole](https://pi-hole.net/) - Black hole for internet ads.
- [Planning lunch with a Slackbot on resin.io](https://resin.io/blog/planning-lunch-with-a-slackbot-on-resin-io/) - Node.js Slackbot (lunchbot), hosted on Resin.
- [Sonus](https://github.com/evancohen/sonus) - Node.js voice control for your Pi (and everything else) with customizable offline hotword detection.
- [Sonic Pi](https://github.com/samaaron/sonic-pi) - The Live Coding Music Synth for Everyone.
- [Pi4j Project](http://pi4j.com) - Java I/O library the Raspberry Pi.
- [Harry Potter and the real life Daily Prophet](https://www.raspberrypi.org/blog/harry-potter-and-the-real-life-daily-prophet/) - Display mimicking the Daily Prophet from Harry Potter using a 7" Raspberry Pi display.
- [PiScan](http://denis.papathanasiou.org/posts/2015.05.30.post.html) - Makeshift Amazon Dash orders using a Raspberry PI + EAN scanner.
- [PiE-Ink](http://www.htxt.co.za/2017/02/07/pie-ink-is-a-raspberry-pi-name-tag-that-uses-an-e-ink-display/) - E-ink nametag display running on a Pi Zero. `Supports Raspberry Pi Zero`
- [Whispering Mirror](http://whisperingwallproject.com/whisperingmirror/) - Interactive soundart installation using the Hifiberry DAC.
- [clockOS](https://github.com/iGerli/clockOS) - simple smart desktop clock using a Raspberry Pi display.
- [Zelda Home Automation](https://www.raspberrypi.org/blog/zelda-home-automation/) - Home automation based on sound recognition from notes played on an ocarina.
- [Looper/synth/drum thing](https://github.com/otem/Raspberry-Pi-Looper-synth-drum-thing) - Sequencer/Drumpad, like Native Instruments' Maschine for the Pi.
- [Waves](https://github.com/euniceylee/waves) - Transforming the transience of the spoken word into something concrete and physical through a microphone, waveform and thermal printer.
- [DIY USB Rubber Ducky](https://hackaday.io/project/17598-diy-usb-rubber-ducky) - Raspberry Pi Zero Rubber Ducky recognized as a USB HID by just about anything with a USB port, thus allowing you to run custom scripts as if it were a keyboard. `Supports Raspberry Pi Zero`
- [Kubernetes on ARM](https://github.com/luxas/kubernetes-on-arm) - Get your ARM device up and running Kubernetes in less than ten minutes.
- [Lumos](https://www.instructables.com/id/LUMOS-Smart-Lamp-for-Better-Health/) - Smart Lamp for Better Sleep. `Supports Raspberry Pi 3 Supports Raspberry Pi Zero`
- [Vinyl Shelf Finder](https://valentingalea.github.io/vinyl-shelf-finder/) - Uses a tilt & pan laser to find a record in a record collection.
- [Building Timelapse with Resin](https://steveedson.co.uk/project-matilda/) - Remotely deploying timelapse camera using Docker, Resin, and 3G internet.
- [NALIVATOR-9000](https://github.com/fote/nalivator9000) - Robot bartender for making cocktails with Telegram-bot interface and speech synthesis on Golang.
- [Stratux](https://github.com/cyoung/stratux) - Open source ADS-B reciever which feeds weather, traffic, GPS, and AHRS data to electronic flight bag software via wifi.
- [Voice Kit](https://aiyprojects.withgoogle.com/voice) - AIY Voice Kit from Google, to build a standalone voice recognition system using the Google Assistant, or add voice recognition and natural language processing to your Raspberry Pi-based projects.
- [speed-camera](https://github.com/pageauc/speed-camera) - Object Motion Tracking uses python, openCV, USB Cam or picamera module to record speed data.
- [pi-timolo](https://github.com/pageauc/pi-timolo) - Remote Headless multi feature PiCamera Operation from Rclone Remote Storage Service and More.
- [Hearing aid prototoype](https://github.com/m-r-s/hearingaid-prototype) - A Raspberry Pi powered prototype of a hearing aid. `Supports Raspberry Pi 3`
- [RPI tempmon](https://github.com/gavinlyonsrepo/raspberrypi_tempmon) - CPU GPU temperature monitor with various functions such as LED GPIO, Graph output, email, alarm limit, notifications and logging.
- [RPi Motor Library](https://github.com/gavinlyonsrepo/RpiMotorLib) - Python 3 library to connect various motors & servos to the Pi.
- [Circle](https://github.com/rsta2/circle) - A C++ bare metal environment for Raspberry Pi.
- [Project MyHouse](https://maxoffsky.com/research-progress/project-myhouse-a-smart-dollhouse-with-gesture-recognition/) - Smart Doll House with Gesture Recognition, using Raspberry Pi 3 or Pi Zero and PSMove motion controller.
- [Skate-o-Meter](http://www.instructables.com/id/Skate-o-Meter/) - Skateboard odometer and speedometer with RFID user system.
- [Occu-Pi](https://github.com/bww/occu-pi) - Controller software for the Occu-pi, a totally awesome bathroom door sensor.
- [docsis-cable-load-monitor](https://github.com/sp4rkie/docsis-cable-load-monitor) - Tool to monitor downstream load on DOCSIS cable networks.
- [BeeMonitor](https://beemonitor.org/setup/) - Honey beehive monitoring project.
- [pi_payments](https://github.com/anshulahuja98/pi_payments) - Payment module based on RFID.
- [RaspiBolt](https://github.com/Stadicus/guides/tree/master/raspibolt) - Beginner’s Guide to ️⚡Lightning️⚡ on a Raspberry Pi.
- [RaspiBlitz](https://github.com/rootzoll/raspiblitz) - Fastest and cheapest way to get your own Lightning Node running.
- [FistBump BLE Edition](https://github.com/eliddell1/Project-Blue-Fist/blob/master/README.md) - WPA Hash Grabbing Bluetooth Peripheral / Android App.
- [Pi Image Capturer](https://github.com/rajeshkumarkhadka/Pi-Image-Capturer) - Captures images, integrated with the Google IOT Cloud Platform ecosystem.
- [Bitcoin Tracker](https://github.com/jonathanrjpereira/Bitcoin-Bar) - A Physical Dashboard that displays Bitcoin stats in real time. `Supports Raspberry Pi  Supports Raspberry Pi Zero`


# 4. Akses GPIO pada Raspberry Pi

`GPIO` merupakan kumpulan pin yang memiliki fungsi untuk berinterksi dengan komponen diluar Raspberry Pi kita. Kumpulan pin-pin tersebut disebut dengan istilah `Broadcom` atau (BCM). Sejumlah 40 pin yang disediakan oleh Raspberry Pi, hanya saja tidak semua pin dapat dijadikan sebagai `GPIO`. Jika kita klasifikasikan kedalam 3 buah kelas berdasarkan penggunaan GPIOnya, maka akan menjadi, Bukan GPIO (Merah), Bisa Jadi GPIO (Cyan), dan GPIO (Hijau) sebagaimana pada gambar dibawah ini.

<img src="GambarPi/g8988.png">

Pada pin warna `Cyan`, pin dapat berfungsi ganda, bisa untuk `I2C/GPIO` dan `serial/GPIO`. Pada kasus ini, kita bisa merubahnya dengan menerapkan kondisi tersebut. Jika fitur `I2C` pada pin `I2C/GPIO` dimatikan, maka pin tersebut berfungsi sebagai `GPIO` atau sama dengan pin warna hijau lainnya. Akan tetapi, jika fitur `I2C` diaktifkan, maka pin tersebut berfungsi sebagai fitur `I2C` pada Raspberry Pi dan tidak sebagai `GPIO`. Kondisi ini juga berlaku pada pin `serial/GPIO`. Untuk menggunakan dan menerapkan kedua fitur tersebut, dapat diakses pada ternimal kalian dengan `CTRL + ALT + T` dan ketikkan `raspi-config` lalu masuk pada `Interface Option` dan pilih fitur yang akan digunakan. Kurang lebih akan muncul layar seperti berikut.

<img src="GambarPi/menu.png">

Semisal pilih fitur `I2C`

<img src="GambarPi/I2C.png">

maka akan muncul layar konfirmasi setelan fitur I2C. Pilih `<yes>` untuk mengaktifkan fitur, dan `<no>` untuk mematikan fitur.

<img src="GambarPi/I2C-2.png">

## Dasar rangkaian listrik

Hanya mengingat ulang tentang yang sudah dipelajari tentang rangkaian listrik.

### Breadboard / Project Board

Breadboard merupakan sebuah papan dengan banyak lobang yang digunakan untuk menghubungkan kaki-kaki komponen elektronik menjadi satu sesuai dengan arah hubung tiap lobangnya. Untuk jumlah kolom, bergantung pada besar kecil Breadboardnya. `baris` diberi tanda dalam bentuk `angka`, dan `kolom` diberi tanda dalam bentuk `huruf`. Baris dan kolom tersebut, saling terhubung tiap 5 `kolom`nya tiap `baris`nya Semisal untuk `baris` ke-5, `kolom` A-B-C-D-E saling terhubung, juga pada `kolom` F-G-H-I-J saling terhubung. Akan tetapi, kedua kelompok `kolom` yang terhubung tersebut, tidak saling terhubung satu sama lain. Terdapat jarak antara kolom E dengan F yang memisahkan kedua kelompoknya. Seperti pada warna kuning pada gambar di bawah ini.

<img src="GambarPi/Atas.png">

Selain itu, ada juga komposisi lobang pada Breadboard yang terhubung secara `horizontal`, yaitu pada garis `biru` dan `merah` yang mengapit lobang `vertikal`. Pada lobang ini, semua lobang tehubung hingga ada jarak yang memisahkan keduanya. Letak pemisahnya berada tepat ditengah-tengah. Pada lobang `horizontal` biru dan merah ini, biasanya digunakan untuk pengunaan `VCC/5V` dan `GND`. Biasanya, warna `merah` menandakan bahwa `VCC/5V` dan warna `biru` menandakan `GND`. Lihat gambar di bawah ini.

<img src="GambarPi/Samping.png">

Apabila kalian sudah faham akan konsep Breadbroad, selanjutnya kita akan membahas tentang LED. 

### LED (Light Emmiting Diode)

LED memiliki `polaritas` atau kutub `( + dan - )` yang salah satunya dapat diketahui dengan dilihat / diterawang. Ciri-ciri LED dengan kutub `positif` adalah memiliki kaki yang lebih panjang daripada kaki satunya. Juga jika diterawang dari samping pada inti LEDnya, maka ada dua buah kepala LED yang saling berhadapan dan terpisah. Kepala inti LED yang lebih `kecil` merupakan kutub `positif` dari LED tersebut. Coba sekarang cek LED kalian yang kurang lebih akan seperti gambar berikut.

<img src="GambarPi/led-resistor.png">
<img src="GambarPi/LED-resistor.png">

Pada dasarnya, LED dapat nyala dengan baik, jika kutub `positif` diberi tegangan dan kutub lainya diberi `GND`. Pada pemberian tegangan ini, posisinya tidak boleh terbalik, karena jika terbalik, LED akan rusak. Selain itu, jika tegangan yang diberikan terlalu besar, LED akan terbakar. Oleh karenanya, sebelum tegangan yang masuk ke LED, LED harus dihubungkan dengan `resistor` atau `hambatan`. Nilai hambatan yang digunakan pada LED untuk tegangan 5V, biasanya sebesar 220 Ohm atau 330 Ohm. Penggunaan nilai hambatan tersebut hanya bersifat `kebiasaan penulis` dalam memilih resistor untuk LED yang bekerja pada 5V. Untuk penjelasan tentang nilai hambatan optimal yang digunakan pada LED pada tegangan tertentu, dapat dilihat pada [tautan berikut](https://www.evilmadscientist.com/2012/resistors-for-leds/).

Nilai hambatan dapat diperoleh dengan membaca warna gelangnya sesuai dengan jumlah gelang yang ada. Resistor juga memiliki ukuran masing-masing sesuai dengan kebutuhannya. Berbeda dengan LED yang memiliki kutub, resistor tidak memiliki kutub yang memungkinkan dapat digunakan pada posisi bebas tanpa memperdulikan kutub positif atau sebaliknya. Berikut contoh rangkaian untuk menyalakan sebuah LED dengan resistor dan sumber tegangan. 

<img src="GambarPi/RangkaianLED.png">

<img src="GambarPi/rangkaian-led.png">




## Percobaan 1 (Blink LED)

Mari kita mulai Percobaan 1 tentang Output. Pada kasus ini, kita akan mencoba menyalakan dan mematikan lampu LED. Lalu, apa saja yang kita butuhkan?

### Alat dan bahan

+ Breadboard / Project Board
+ Raspberry Pi (kita menggunakan MOdel 3b+)
+ Resistor 220 Ohm
+ Lampu LED (warna bebas)
+ Kabel jumper secukupnya (F2M dan M2M)


### Langkah kerja

1. Persiapkan alat dan bahan yang akan digunakan
2. Nyalakan Raspberry Pi hingga siap digunakan
3. Rangkailah LED dan Resistor sesuai dengan gambar rangkaian berikut. Pin `GPIO` yang digunakan adalah pin `GPIO23`.

<img src="GambarPi/gambar-rangkaian-1.png">
<img src="GambarPi/gambar-rangkaian-1-foto.jpg">

4. Buat sebuah dokumen Python baru pada `Desktop` kalian atau folder lain sesuai keinginan kalian dengan nama `led.py`. 
5. Tulis kode berikut didalamnya. Jangan lupa untuk menyimpannya. 

```python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)

while True:
    GPIO.output(23, GPIO.HIGH)
    time.sleep(0.5)

    GPIO.output(23, GPIO.LOW)
    time.sleep(1)
```
6. Kalian bisa menggunakan `F5` untuk `run` pada editor Python kalian, atau bisa menggunakan terminal apabila kalian menggunakan fitur `remote` terminal Raspberry Pi kalian dengan menuliskan `python led.py` setelah kalian masuk pada direktori dokumen berada. **) Jika muncul peringatan, abaikan saja.*

7. Coba amati apa yang terjadi, lalu coba kalian ubah nilai x pada `time.sleep(x)` sesuai keinginan kalian. Amati apa perbedaannya. 

8. Tekan `Ctrl + C` untuk keluar dari proses yang sedang dijalankan pada terminal atau console.

Untuk mengetahui hasil dari percobaan ini, dapat dilihat pada video berikut:

[![Hasil Percobaan 1 - Blink LED](https://img.youtube.com/vi/QvgoyTG5KZk/0.jpg)](https://www.youtube.com/watch?v=QvgoyTG5KZk)


## Percobaan 2 (Input dan Output)

Pada percobaan ini, tidak jauh berbeda dengan Percobaan 1, yang hanya menambahkan sebuah tombol tekan (push-button) pada rangkaiannya. Sehingga akan terjadi proses masukan dan keluaran pada programnya. 

### Alat dan bahan

+ Breadboard / Project Board
+ Raspberry Pi (kita menggunakan MOdel 3b+)
+ Resistor 220 Ohm
+ Lampu LED (warna bebas)
+ Kabel jumper secukupnya (F2M dan M2M)
+ Push-button

### Langkah kerja

1. Persiapkan alat dan bahan yang akan digunakan
2. Nyalakan Raspberry Pi hingga siap digunakan
3. Rangkailah push-button, LED dan Resistor sesuai dengan gambar rangkaian berikut. Pin `GPIO` yang digunakan adalah pin `GPIO23` untuk keluaran menuju LED dan `GPIO22` untuk masukan dari push-button.

<img src="GambarPi/gambar-rangkaian-2.png">

<img src="GambarPi/gambar-rangkaian-2-foto.jpg">

4. Buat sebuah dokumen Python baru pada `Desktop` kalian atau folder lain sesuai keinginan kalian dengan nama `tombol.py`. 
5. Tulis kode berikut didalamnya menggunakan editor kalian. Jangan lupa untuk menyimpannya. 


```python
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while True:
    tombol = GPIO.input(22)
    if tombol == False:
        GPIO.output(23, GPIO.HIGH)
        print ("Tertekan")
    else:
        GPIO.output(23, GPIO.LOW)
        print ("Bebas")
```

6. Kalian bisa menggunakan `F5` untuk `run` pada editor Python kalian, atau bisa menggunakan terminal apabila kalian menggunakan fitur `remote` terminal Raspberry Pi kalian dengan menuliskan `python led.py` setelah kalian masuk pada direktori dokumen berada.

7. Coba tekan tombol push-button nya, dan amati apa yang akan terjadi. Coba ubah kode diatas dengan penggunaan logika, jika tombol ditekan sekali, maka LED akan berkedip secara cepat dan setelah dilepas, LED akan menyala terus. 

8. Tekan `Ctrl + C` untuk keluar dari proses yang sedang dijalankan pada terminal atau console.

Sebagai patokan, kurang lebih hasil percobaan 2 ini seperti pada video berikut. 

[![Hasil Percobaan 2 - Input dan Output](https://img.youtube.com/vi/9z8uqpZ-F-4/0.jpg)](https://www.youtube.com/watch?v=9z8uqpZ-F-4)


# 5. Menggunakan GUI untuk antar-muka

Grapchical User Interface (GUI) merupakan suatu tampilan pada layar komputer yang dapat terhubung dengan perangkat keras diluar komputer tersebut. Dengan asumsi, Raspberry Pi merupakan komputer dengan bentuk mini. 

# 8. IoT

## Mengirim data pada cloud

Pada bab kali ini, kita akan mencoba mengirim data pada cloud untuk IoT. Singkatnya, kita akan mengirimkan data temperatur pada CPU di dalam Raspberry Pi kita. Lalu, apa yang dibutuhkan?

## Alat dan Bahan

+ Raspberrry Pi
+ Akun thingspeak.com (membutuhkan email aktif untuk mendaftar)
+ Sambungan internet

## Langkah Kerja

1. Siapkan alat dan bahan yang dibutuhkan
2. Buat akun thingspeak kalian [disini](http://thingspeak.com). Kurang lebih seperti tampilan di bawah ini.

<img src="GambarPi/Thingspeak-daftar.png">

3. Lengkapi persyaratan pendaftaran akun baru. 
4. Setelah sukses mendaftar, masuklah pada menu, `Channels` > `My Channels`. Create `New Channel`. 
5. Lengkapi kolom isian sesuai dengan kebutuhan. Semisal seperti gambar berikut ini. Lalu `Save Channel`.

<img src="GambarPi/channel-baru.png">

6. Lalu akan muncul menu-menu fitur dari channel kita yang sudah dibuat, seperti berikut ini. 

<img src="GambarPi/Tampilan-channel-1.png">

7. Dari menu terebut, kita akan mengambil `API Keys` dari channel tersebut. Klik tab `API Keys`. 

<img src="GambarPi/ApiKeys.png">

8. Buat sebuah dokumen baru pada direktotri yang biasa anda gunakan atap pada `/Desktop` dengan nama `suhu.py` dan tuliskan kode dibawah ini di dalamnya. Jangan lupa untuk menyimpan setelah Anda menuliskannya. Untuk variabel `key` pada kode dibawah, dapat diisikan dengan `Write API Key` dari channel thingspeak kalian. 

```python
import httplib
import urllib
import time
key = "ABCD"  # Masukkan API Keys kalian disini

def kirim():
    while True:
        # Baca suhu CPU
        temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 
        params = urllib.urlencode({'field1': temp, 'key':key }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print temp
            print response.status, response.reason
            data = response.read()
            conn.close()
        except:
            print "connection failed"
        break
        
if __name__ == "__main__":
        while True:
                kirim()
```

9. Coba jalankan program yang telah dibuat, jika pustaka `httplib` dan `urllib` belum terinstall, coba gunakan perintah berikut pada terminal. Setelah sukses, coba jalankan kembali program yang telah kita buat. 

```
sudo apt-get install httplib
sudo apt-get install urllib
```

10. Untuk mengetahui status dari pengiriman data suhu dan `ping` dari sambungan serta status respon server, dapat dilihat dari console atau terminal dimana program tersebut dijalankan, seperti gambar berikut ini.

<img src="GambarPi/status-kirim-thingspeak.png">

Ketika status pengiriman sudah berhasil dan server sudah memberikan respon `OK`, maka pada channel thingspeak kita, akan menampilkan grafik perubahan suhu dari CPU kita, seperti gambar dibawah ini. 

<img src="GambarPi/grafik-suhu.png">

## Membaca Data dari Cloud 

Setelah kita dapat mengirim data menuju cloud atau server kita di thingspeak.com, kita juga dapat membaca hasi kiriman tadi dalam format notasi `json` yang telah disediakan. Agar kita dapat melihat tautan data `JSON` kita, dapat dibuka pada tab API Key kita. Semisal pada tautan berikut ini dengan merubah `(channel_id)` dengan channel id milik kita. `https://api.thingspeak.com/channels/(channel_id)/feeds.json?results=2`

<img src="GambarPi/api-request.png">
<img src="GambarPi/json-format.png">


Dari tautan data `json` kita, kita dapat langsung mengambil data tersebut dengan kode python kita dan menggunakan data tersebut untuk keperluan yang kita inginkan. Semisal pada kasus pembacaan LED dari tombol yang sebelumnya data status tombol tersebut sudah dikirimkan kepada server melalui internet. 

## Alat dan Bahan

+ Raspberrry Pi
+ Akun thingspeak.com (membutuhkan email aktif untuk mendaftar)
+ Sambungan internet
+ LED
+ Push-button
+ Kabel jumper secukupnya

## Langkah Kerja

1. Siapkan alat dan bahan yang dibutuhkan
2. Hubungkan rangkaian seperti gambar beirkut ini


3. kode berikut

```python
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while True:
    tombol = GPIO.input(22)
    if tombol == False:
        GPIO.output(23, GPIO.HIGH)
        print ("Tertekan")
    else:
        GPIO.output(23, GPIO.LOW)
        print ("Bebas")
```






Thanks for [Awesome Raspberry Pi](https://github.com/thibmaek/awesome-raspberry-pi/blob/master/README.md)
