from phBot import *
import QtBind
from threading import Timer
import struct
import random
import json
import os
import subprocess

pVersion = '1.0.6'
pName = 'TrINFO'
pUrl = 'https://raw.githubusercontent.com/TheMoB41/TrPlugins/main/TrINFO.py'

#GUI YAPILANDIRMASI
gui = QtBind.init(__name__,pName)
QtBind.createList(gui,500,40,90,180)
btnTrController = QtBind.createButton(gui,'btnTrController_clicked',"    TrController    ",505,45)
btnUTrChat = QtBind.createButton(gui,'btnTrChat_clicked',"        TrChat        ",505,70)
btnTrUpdater = QtBind.createButton(gui,'btnTrUpdater_clicked',"     TrUpdater    ",505,95)
btnTrPacketTool = QtBind.createButton(gui,'btnTrPacketTool_clicked',"   TrPacketTooL  ",505,120)
btnTrDungeon = QtBind.createButton(gui,'btnTrDungeon_clicked',"     TrDungeon    ",505,145)
btnTrItemManager = QtBind.createButton(gui,'btnTrItemManager_clicked'," TrItemManager ",505,170)
QtBind.createList(gui,605,40,90,180)
btnTrAcademy = QtBind.createButton(gui,'btnTrAcademy_clicked',"     TrAcademy    ",610,45)
btnTrItemStack = QtBind.createButton(gui,'btnTrItemStack_clicked',"    TrItemStack    ",610,70)
btnTrBOI = QtBind.createButton(gui,'btnTrBOI_clicked',"         TrBOI         ",610,95)
btnTrBalon = QtBind.createButton(gui,'btnTrBalon_clicked',"         TrBalon       ",610,120)
btnTrKonsinye = QtBind.createButton(gui,'btnTrKonsinye_clicked',"      TrKonsinye    ",610,145)
btnTrLogin = QtBind.createButton(gui,'btnTrLogin_clicked',"        TrLogin        ",610,170)
btnIletisim = QtBind.createButton(gui,'btnIletisim_clicked',"   TheMoB ILETISIM   ",547,225)
lblInfo = QtBind.createLabel(gui,"Tr PLUGINLERI HAKKINDA ACIKLAMALAR:",21,11)
lblInfo2 = QtBind.createLabel(gui,"/\ TheMoB /\ GAUCHE /\ SINCE 2006 /\ ",505,245)

lstInfo = QtBind.createList(gui,21,30,470,250)
#BUTON ISLEVLERI	
def btnTrController_clicked():
	QtBind.clear(gui,lstInfo)
	QtBind.append(gui,lstInfo,'TrController:\n   # BU PLUGIN LIDER LISTESINE EKLENMIS CHARLARIN CHAT EKRANINDAN DIGER\nCHARLARA CESITLI ISLEMLER YAPTIRIR.\n   # DESTEK KOMUTLARI: \n- BAŞLAT : BOTU BASLAT.\n- DURDUR : BOTU DURDUR.\n- TRACE #OYUNCU : LIDERE YADA YAZDIGIN CHARA TRACE AT.\n- NOTRACE : TRACE DURDUR.\n- FOLLOW : OYUN TAKIP SISTEMI.\n- NOFOLLOW : OYUN TAKIP SISTEMI DURDURMA.\n- KORKUR #PosX? #PosY? #Range? #PosZ? : KOORDINAT KURMAK.\n- KORAL : CHARIN MEVCUT KOORDINATLARINI PM OLARAK ALMAK.\n- RANGE #Radius? : RANGE DEGISTIR.\n(VARSAYILAN 35, OZEL DEGER GIRMEK ICIN BASINA 0000 KOYULMALIDIR.\n- SCKUR #DOSYA YOLU : YAZDIGINIZ DOSYA YOLUNDAKI SCRIPTI TANIMLAR.')
	QtBind.append(gui,lstInfo,'- ALANKUR #ISIM : YAZILAN ISIMDEKI KASILMA ALANINI AKTIF EDER.\n- PROFIL #ISIM : YAZDIGINIZ ISIMDEKI PROFILI YUKLER.\n- INJECT #Opcode #Encrypted? #Data? : PAKET ENJEKTE ET.\n- RECALL #TOWN ISMI : YAZDIGIN TOWNA KAYIT YAPAR.# REVERSE KOMUTLARI :\n- REVERSE RETURN : SON RETURN NOKTASINA REVERSE.\n- REVERSE OLUM : SON OLUM NOKTASINA REVERSE.\n- REVERSE ALAN #ALAN ADI : YAZDIGINIZ ALAN ADINA REVERSE.\n- REVERSE PLAYER #NICK : YAZDIGINIZ PT UYESINE REVERSE.\n- GIY #ITEM ISMI : CHARA ITEM GIYDIRMEK.\n- CIKART #ITEM : CHARDAN ITEM CIKARTMAK.\n- RETURN : RETURN SCROLL KULLAN.\n- ZERK : ZERK HAZIRSA KULLAN.\n- DAGIL #RANGE : SECILEN RANGEDE HERHANGI KOORDINATA GIDER.\n- TP #A #B : A-B ARASI TELEPORT.\n- DISMOUNT #CESIT : SECTIGINIZ CESITTE PETI KAPATIR.')
	QtBind.append(gui,lstInfo,'- DC : OYUN BAGLANTISINI KESER.\n- PTAYRIL : PTDEN AYRIL.\n- CHAT #CESIT #MESAJ : MESAJ GONDER.\n- CAPE #RENK? : PVP MODU.\n- SIT : OTUR - KALK.\n- JUMP JUMP : YATIR EFEKTI\n- COME : MEYDAN OKUMA EFEKTI.\n- MERHABA : SELAMLAMA EFEKTI.\n- WALK : YURUME EFEKTINE GECIS.\n- RUN : KOSMA EFEKTINE GECIS.\n   # SCRIPTE EKLENEBILIR ÖZEL KOMUTLAR :\n- Notification,title,message : BİR WİNDOWS BİLDİRİMİ GÖSTER.\n(BOT SİMGE DURUMUNA KÜÇÜLTÜLMELİDİR.)\n- NotifyList,message : LİSTEDE BİR BİLDİRİM OLUŞTURUR.\n- PlaySound,ding.wav : WAV DOSYASI PHBOT KLASÖRÜNÜN İÇİNDE OLMALIDIR.')
	QtBind.append(gui,lstInfo,'- SetScript,Mobs103.txt : SCRİPT PHBOT KLASÖRÜNDE OLMALIDIR.\n- CloseBot : BOTU HEMEN KAPATIR.\n- CloseBot,in,5 : 5 DAKIKA SONRA BOTU KAPATIR.\n- CloseBot,at,05:30 : BILGISAYAR SAATINE GORE BOTU KAPATIR. (24 SAAT FORMATI)\n- GoClientless : CLIENTLESS MODUNA GECIR.\n- StartBot,in,5 : 5 DAKIKA SONRA BOTU BASLAT.\n- StartBot,at,05:30 : BILGISAYAR SAATINE GORE BOT BASLATILIR. (24 SAAT FORMATI)\n- StopStart : BOTU DURDURUP 1 SANIYE SONRA TEKRAR BAŞLATIR.\n- StartTrace,player : NICKI YAZILI PLAYERA TRACE BASLATIR.\n- RemoveSkill,skillname : EĞER SKİLL AKTİFSE İPTAL ET.\n- Drop,itemname : YAZILI ITEMIN ILK STACKINI YERE ATAR.\n- OpenphBot,commandlinearguments : SEÇILEBİLİR ARGÜMANLARLA YENİ BİR \n                                                                                                                         BOT AÇAR.\n- LeaveParty : PTDEN AYRIL.\n- CustomNPC,savedname : KAYIT EDİLEN ÖZEL KOMUT DOSYASINI YÜRÜTÜR.')
	QtBind.append(gui,lstInfo,'   # TARGET MODU KOMUTLARI:\n - TARGETON : TARGET MODUNU ETKİNLEŞTİRİR.\n - TARGETOFF : TARGET MODUNU KAPATIR.\n - DEFFON: DEFANS MODUNU ETKİNLEŞTİRİR.\n - DEFFOFF: DEFANS MODUNU KAPATIR.\n # KALE TELEPORT KODLARI :\n HOTAN FORTRESS KODLARI :\n- H11/H12/H13/H14/H21/H22/H23/H24/H31/H32/H33/H34\n JANGAN FORTRESS KODLARI :\n- J11/J12/J13/J21/J22/J23/J31/J32/J33\n FORTRESS KOMUTLARININ MANTIĞI :\nHARF = KALENİN BAŞ HARFİ\nBİRİNCİ RAKAM = BULUNDUĞU TP NUMARASI\nİKİNCİ RAKAM = GİDECEĞİN TP NUMARASI')
def btnTrChat_clicked():
	QtBind.clear(gui,lstInfo)
	QtBind.append(gui,lstInfo,'TrChat:\n   # BU PLUGIN ILE 10 SANIYEDE BIR SPAM MESAJ ATILABILIR, SECILEN KOSULA GORE\nISTEDIGINIZ CHAT EKRANINA MESAJ GONDEREBILIRSINIZ.\n   # BUNA EK OLARAK SCRIPTE EKLEYECEGINIZ BASIT BIR KODLA SCRIPT ESNASINDA\nOTO MESAJ ATTIRABILIRSINIZ..\n   # ORNEK: "chat,all,SELAM" VEYA "chat,private,TheMoB,SELAM"')
def btnTrPacketTool_clicked():
	QtBind.clear(gui,lstInfo)
	QtBind.append(gui,lstInfo,'TrPacketTooL:\n    # BU PLUGIN CLIENTTEN SERVERA GONDERILEN OPCODE PAKETLERINI VEYA\nSERVERDAN CLIENTE GELEN OPCODE PAKETLERINI GOSTERMEKTEDIR.\n    # EK OLARAK CLIENTTEN SERVERA OPCODE ENEJEKTE EDEBILIR VE CEVRENIZDEKI\nNPCLERIN DATALARINA ULASABILIRSINIZ.')
def btnTrUpdater_clicked():
	QtBind.clear(gui,lstInfo)
	QtBind.append(gui,lstInfo,'TrUpdater:\n    # BU PLUGIN BILGSAYARINIZDA GITHUB.COM UZERINDEN YAYINLANAN\nHERHANGI BIR YAZILIMCININ PLUGININI BULDUGU TAKTIRDE GUNCELLER..\n KULLANIMI:\n"GUNCELLEMELERI KONTROL ET" BUTONUNA BASTIKTAN SONRA;\n LISTEDE "GUNCELLEME BULUNDU" YAZAN PLUGINLERIN UZERINE TIKLAYIP,\n"SECILEN PLUGINI GUNCELLE" BUTONUNA BASINIZ.\n    # ISLEM BITIMINDE BOTUNUZU YENIDEN BASLATIRSANIZ VEYA "PLUGIN"\nSEKMESINDE "YENIDEN YUKLE" BUTONUNA TIKLARSANIZ PLUGININ SON\nVERSIYONUNU KULLANMAYA BASLAYABILIRSINIZ..')
def btnTrItemStack_clicked():
	QtBind.clear(gui,lstInfo)
	QtBind.append(gui,lstInfo,'TrItemStack:\n    # BU PLUGIN ILE ENVATER/DEPO/GUILD DEPOSUNU OTOMATIK STACKLEYEBILIR. \n DEPO VE GUILD DEPOSUNA GOLD GONDEREBILIR VE ENVANTERE GOLD ALABILIRSINIZ\n DEBUG MODU SECENEKLERI ILE LAGLI SERVERLARDA ZAMAN ASIMI UYGULAMALI \n ISLEM YAPTIRABILIRSINIZ.')
def btnTrAcademy_clicked():
	QtBind.clear(gui,lstInfo)
	QtBind.append(gui,lstInfo,'TrAcademy:\n    # BU PLUGIN ILE;\n - CHAR OLUSTURMA (ISTEDIGINIZ IRKTA, NICKLE VE SIRAYLA),\n - CHAR SILME (40-100 LVL ARASI),\n - AKADEMIDE OLAN CHARLARI SILMEDEN TEKRAR OYUNA GIRME (40-50 LVL ARASI)\nISLEVLERINI YAPTIRABILIRSINIZ.\n    # ID ICERISINDE CHAR ALANI KALMADIGINDA;\n - BOTU KAPATMA,\n - PHBOT BILDIRIMLERINDE GOSTERME,\n - DOSYA YOLUNU BELIRTTIGINIZ SESI CALMA (.waw UZANTILI),\n - LOG DOSYASI OLUSTURMA\nOZELLIKLERI BULUNMAKTADIR. ')
def btnIletisim_clicked():
	QtBind.clear(gui,lstInfo)
	QtBind.append(gui,lstInfo,'- ILETISIM:\n   # DISCORD: "TheMoB#8710"\n   # E-MAIL: "can.berk.cetin@hotmail.com.tr"\n\n- SOSYAL MEDYA:\n    # INSTAGRAM: "can.berk.cetin"\n    # YOUTUBE: "TRSRO MYRA TheMoB" ')
def btnTrItemManager_clicked():
	QtBind.clear(gui,lstInfo)
	QtBind.append(gui,lstInfo,'TrItemManager:\n    # BU PLUGININ CIFT ISLEVI VARDIR.\n1. ISLEV:\n # PLUGIN UZERINDEN CHARINIZDA MEVCUT OLAN STONE, ELIXIR VE COINLERI\nGOREBILIRSINIZ.(ENVANTER - STORAGE - GUILD STORAGE)\n2.ISLEV:\n # PLUGINDE BELIRLEDIGINIZ MAIN CHAR,SIFRE VE DEGREE NUMARASI ILE DIGER\nCHARLARINIZDAKI STONE,ELIXIR VE COIN MIKTARLARINI PM OLARAK ALABILIRSINIZ.\n YAPMANIZ GEREKEN TEK SEY YAN CHARINIZI GORMEK ISTEDIGINIZ YERIN VE\nITEMIN KODUNU YAZMAK..\n # YER KODLARI:\n i = ENVANTER | s = STORAGE | g = GUILD SORAGE\n # ITEM KODLARI:\n Stone | Elixir | Coin\n # ORNEK: STORAGEDEKI COIN MIKTARINI PM OLARAK ALMAK ICIN "sCoin" YAZILIR. ')
def btnTrDungeon_clicked():
	QtBind.clear(gui,lstInfo)
	QtBind.append(gui,lstInfo,'TrDungeon:\n    # BU PLUGIN ILE FORGOTTEN WORLD - HOLW WATER TEMPLE GIBI DUNGEONLARI\nSCRIPTE EKLENEN 2 KOMUT SAYESINDE OTO YAPTIRABILIRSINIZ.\n1. KOMUT:\n "AtackArea,x,y"\n # x = RANGE (YAZILMAZSA VARSAYILAN = 75)\n # y = YENIDEN CANAVAR TANIMLAMA SURESI (SANIYE)\n2. KOMUT:\n "GoDimensional"\n      VEYA\n "GoDimensional,Dimension Hole (Flame Mountain-3 stars)" \n            = DIMENSION ACIP FGW GIRMESI ICIN.')
def btnTrBOI_clicked():
	QtBind.clear(gui,lstInfo)
	QtBind.append(gui,lstInfo, 'TrBOI:\n    # BU PLUGIN ILE BATTLE OF INIFINITY ARENASINA MÜDAHELE ETMEDEN GİRİŞ\nYAPILIP, TAMAMLANIP, ÇIKIŞ YAPILABİLİR.\n # SCRIPTE EKLENEBİLECEK ÖZEL BİR KOMUTLA SCRİPT İLE ARENA TAMAMLANABİLİR.\n - KOD: BOI,type,morph\n - ÖRN1: BOI,solo,A\n - ÖRN2: BOI,party,B')
def btnTrBalon_clicked():
	QtBind.clear(gui,lstInfo)
	QtBind.append(gui,lstInfo,'TrBalon:\n    # BU PLUGIN ILE KARNAVAL BALON EVENTLERİNDE OTOMATİK BALON\nAÇTIRABİLİRSİNİZ. PASİF BİR PLUGİNDİR.YANİ HERHANGİ BİR ARAYÜZÜ YOKTUR.\n TOWNA DÖNDÜĞÜNDE ÜZERİNDE BALON VARSA KULLANMAYA BAŞLAR.\n BİTİŞTE RETURN SCROLL KULLANIR VE BOTU BAŞLATIR.')
def btnTrKonsinye_clicked():
	QtBind.clear(gui,lstInfo)
	QtBind.append(gui,lstInfo,'TrKonsinye:\n    # BU PLUGIN ILE CLIENTLESS MODDA KONSİNYEDE SATILAN ÜRÜNLERİ\nGÖREBİLİRSİNİZ. LİSTEYE EKLEDİĞİNİZ ITEMLERİ MAX FİYAT VE MİN ADET YAZARAK\nSATIN ALDIRABİLİRSİNİZ.\nNOT: CHARIN NPCNİN YAKININDA OLMASI GEREKMEKTEDİR.')
def btnTrLogin_clicked():
	QtBind.clear(gui,lstInfo)
	QtBind.append(gui,lstInfo,'TrLogin:\n    # BU PLUGIN ILE HERHANGİ BİR CHARIN GÜN İÇERİSİNDE HANGİ SAAT\nARALIKLARINDA OYUNDA KALMASINI İSTEDİĞİNİZİ BELİRLEYEBİLİRSİNİZ.\n BELİRTİLEN SAATLER HARİCİ BOT AÇIK KALIR CHAR OFFLİNE KALIR.\n NOT: HER CHAR İÇİN AYRI CONFİG KAYDI VARDIR.')
log('Plugin: '+pName+' v'+pVersion+' BASARIYLA YUKLENDI')
