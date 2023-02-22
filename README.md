# CSharp-Smart-Home
Smart Home Project 

##Projenin Amacı

Bu projenin amacı C# ile Akıllı Ev kontrolü sağlamaktı. 
- Hareket algılandığında uyarı verip fotoğraf çekmek isteyip istemediğinizi soruyor. Bu interaktifte amaçladığımız şey evin güvenliği.
- RFID ile şifreli bir güvenlik sistemi koyduk. Tanımlı kullancılar giriş yapabiliyor ve istenirse yeni kullanıcı tanımlanabiliyor.
- RFID ile kayıtlı kullanıcı giriş yaptığında kapıyı açıyoruz. 
- LDR sensörü ile ortamın ışık şiddetini anlık olarak kontrol edip ampüllerimizin şiddetini oda bazlı olarak değiştirebiliyoruz. Bu interaktife amaçladığımız şey kullanıcıya konfor sağalamak.<br/>
## Kullanılan Malzemeler

- Rasperry Pi 4
- Rasperry Pi Camera Module 
- LDR Module
- PIR Module
- RFID
- Servo Motor
- L298 Motor Driver Module

## Bağlantılar

Firebase ile haberleştirdim. Fotoğrafların kaydedilmesi için Firebase Storage kullandım ve diğer veriler için Realtime Database üzerinden verilerimi yönlendirdim.




