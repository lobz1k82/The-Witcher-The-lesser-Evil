 # Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define v = Character('Войт', color="#290a08")
define config.mouse = {'default':[("cursor.gif", 0, 0)]}
define g = Character('Геральт', color="#290a08")
define n = Character('Носикамень', color="#290a08")
define k = Character ('Колотушка', color="#290a08")
define i = Character ('Ирион', color="#290a08")
define s = Character ('Стрегобор', color="#290a08")
define ren = Character ('Ренфри', color="#290a08")
define r1 = Character ('Ногорн', color="#290a08")
define r2 = Character ('Десятка', color="#290a08")
define r3 = Character ('Киврил', color="#290a08")
define r4 = Character ('Тавик', color="#290a08")
define r5 = Character ('Выр', color="#290a08")
define r6 = Character ('Нимир', color="#290a08")
define t = Character ('Сотник', color="#290a08")
init:
    image bg road = "road.jpg"

    $ flash = Fade(.25, 0, .75, color="#fff")


# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
    scene begin1

    stop music

    play music "music2.mp3"

    "Первыми, как обычно, на него обратили внимание кошки и дети."
    "Ведьмак ехал медленно, не пытаясь опередить воз с сеном, занимавший всю ширину улицы."

    scene donkey
    
    "За ведьмаком, вытянув шею и то и дело сильно натягивая веревку, трусил привязанный к луке седла навьюченный осел."

    scene donkey2

    "Кроме обычного груза, длинноухий трудяга тащил на спину большую штуковину, обернутую попоной. "

    "Серо-белый бок осла покрывали черные полоски запекшейся крови."

    scene begin

    "Наконец воз свернул в боковую улочку, ведущую к амбарам и пристани, от которой веяло бризом и несло смолой."

    "Геральт поторопил лошадь."
    scene scene 5


    "Ведьмак остановился у дома войта, главного человека в городе. "

    show house

    with fade

    show geralt1 with dissolve:

        xalign 0.0

        yalign 1.0



    show kaldsheets1 with dissolve:

        xalign 1.0

        yalign 1.0

    "Геральт вошел внутрь и обратил взгляд на перебиравшего бумаги Кальдемейна."
    
    hide geralt1

    show geralt:

        xalign 0.0

        yalign 1.0 

    hide kaldsheets1
    
    show kaldsheets:

        xalign 1.0

        yalign 1.0

    v "Кто там еще?!"

    "Проворчал войт." 

    show kaldsheets:
        "kaldsheets.png" 
        pause 0.5
        "kaldsheets2.png" with dissolve
        pause 0.75
        "kaldogo.png" with dissolve

    "Тяжело вздохнув, мужчина обернулся и увидел своего старого товарища."

    
    v "О, привет, Геральт!"

    

    show geralttalk:
        xalign 0.0

        yalign 1.0 
    
    hide geralt
    
    

    show kaldmolch:

        xalign 1.0

        yalign 1.0
   
    hide kaldsheets
    

    g "Привет, Кальдемейн."

    hide geralttalk 
    
    show geralt:
        xalign 0.0

        yalign 1.0 
    
    hide kaldmolch
    
    show kaldtalk:

        xalign 1.0

        yalign 1.0
    
    v "Ты тут не бывал, почитай, года два!"
    v "Откуда занесло?"
    v "А, черт с ним, не все равно откуда!"
    v "У нас тут, понимаешь, черт-те что творится, потому что как завтра ярмарка. "
    v "Ну, что там у тебя, выкладывай!"
    hide geralt 
    show geralttalk:
        xalign 0.0

        yalign 1.0 
    g "Потом. Давай выйдем."

    scene scene 3

    with fade

    show kik with dissolve:

        xalign 1.0

        yalign 1.0

    show kaldogo2 with dissolve:

        xalign 0.25

        yalign 1.0    
    show geralthands with dissolve:

        xalign 0.0

        yalign 1.0



    stop music

    play music "kikimora.mp3"
    "Они вышли на улицу, и Геральт отвернул попону. Кальдемейн широко раскрыл рот."

    v "Господи, Геральт? Это что такое?"
    show geralthandstalk:
        xalign 0.0

        yalign 1.0 
    
    hide geralthands
    g "Кикимора."
    g "Не будет ли за нее какой-нибудь награды, милсдарь войт?"
    show geralthands:
        xalign 0.0

        yalign 1.0 
    
    hide geralthandstalk
    show kaldogo2:
        "kaldogo2.png" 
        pause 0.5
        "kaldthink.png" with dissolve

    
    
    "Кальдемейн переступил с ноги на ногу, глядя на паучье, обтянутое черной высохшей кожей тело, на остекленевший глаз с вертикальным зрачком, на иглоподобные в окровавленной пасти."
    
    show kaldthink:
        "kaldthink.png"
        xalign 0.25
        yalign 1.0
        pause 0.5
        "kaldtalk1.png" with dissolve
    hide kaldogo2

    
    v "Где..."
    v "Откуда это..."
    show geralthandstalk:
        xalign 0.0

        yalign 1.0 
    
    hide geralthands
    show kaldright:
        xalign 0.25

        yalign 1.0 
    
    hide kaldthink
    
    g "На плотине, верстах в четырех отсюда."
    g "На болотах."
    show geralthiptalk:
        "geralthandstalk.png"
        xalign 0.0
        yalign 1.0
        pause 0.5
        "geralthiptalk.png" with dissolve
    hide geralthandstalk
    g "Кальдемейн, кажется, гибли люди. "

    g "Дети."
    show geralthip:
        xalign 0.0

        yalign 1.0 
    
    hide geralthiptalk
    show kaldhandssleep:
        xalign 0.25

        yalign 1.0 
    hide kaldmolch1
    hide kaldtalk1
    hide kaldogo2
    hide kaldright
    v "Награды не будет."
    "Угрюмо сказал войт."
    show kaldtalkhands:
        xalign 0.25

        yalign 1.0 
    hide kaldhandssleep

    

    show geralt:
        xalign 0.0

        yalign 1.0 
    
    hide geralthip
    v "Никто и не думал, что такая..."
    v "Такой..."
    v "Cидит на соленых болотах."
    v "Факт, несколько человек пропало в тамошних местах, но..."
    v "Мало кто лазил по тем трясинам. "
    show kaldtalk1:
        "kaldtalkhands.png"
        xalign 0.25
        yalign 1.0
        pause 0.5
        "kaldtalk1.png" with dissolve
    hide kaldtalkhands
    v "А ты-то как там очутился? "
    v "Почему не ехал большаком?"
    show geralttalk:
        xalign 0.0

        yalign 1.0 
    
    hide geralt
    show kaldmolch1:
        xalign 0.25

        yalign 1.0 
    
    hide kaldtalk1
    g "На большаках не заработаешь, Кальдемейн."
    show geralthands:
        xalign 0.0

        yalign 1.0 
    
    hide geralttalk
    show kaldthinktalk:
        "kaldmolch1.png"
        xalign 0.25
        yalign 1.0
        pause 0.5
        "kaldthinktalk.png" with dissolve
    hide kaldmolch1
    v "Я забыл. "
    v "У нас даже домовые появляются редко."
    show kaldtalk1:
        "kaldthinktalk.png"
        xalign 0.25
        yalign 1.0
        pause 0.5
        "kaldtalk1.png" with dissolve
    hide kaldthinktalk
    v "Потому как заплатить – не заплачу."
    v "Фондов нету. На награды-то."
    show geralttalk:
        xalign 0.0

        yalign 1.0 
    
    hide geralthands
    show kaldmolch1:
        xalign 0.25

        yalign 1.0 
    
    hide kaldtalk1
    g "Скверно."
    g "Немного наличных мне б не помешали, чтобы перезимовать."
    g "Отправляюсь в Испанден, да не знаю, успею ли до снега. "
    g "Могу застрять в каком-нибудь городишке вдоль Лутонского тракта."
    show geralt:
        xalign 0.0

        yalign 1.0 
    
    hide geralttalk
    show kaldtalkhands:
        xalign 0.25

        yalign 1.0 
    
    hide kaldmolch1
    v "Надолго к нам, в Блавикен?"
    show geralttalk:
        xalign 0.0

        yalign 1.0 
    
    hide geralt
    show kaldmolchhands:
        xalign 0.25

        yalign 1.0 
    
    hide kaldtalkhands
    g "Нет."
    g "Нельзя засиживаться. Зима подпирает."
    show geralthands:
        xalign 0.0

        yalign 1.0 
    
    hide geralttalk
    show kaldtalk1:
        xalign 0.25

        yalign 1.0 
    
    hide kaldmolchhands
    v "Где остановишься? Может, у меня?"
    v "На мансарде есть свободная комната. На кой тебе к трактирщикам переться?"
    v "Обдерут как липку, разбойники. Поболтаем, расскажешь, что в мире слыхать."
    show geralthandstalk:
        xalign 0.0

        yalign 1.0 
    
    hide geralthands
    show kaldmolch1:
        xalign 0.25

        yalign 1.0 
    
    hide kaldtalk1
    g "Охотно. "
    show geralthiptalk:
        "geralthandstalk.png"
        xalign 0.0
        yalign 1.0
        pause 0.5
        "geralthiptalk.png" with dissolve
    hide geralthandstalk
    g "А как на это твоя жена? Последний раз я заметил, она не очень-то меня жалует."
    show geralthip:
        xalign 0.0

        yalign 1.0 
    
    hide geralthiptalk
    show kaldhandssleep:
        xalign 0.25

        yalign 1.0 
    
    hide kaldmolch1
    
    v "В моем доме бабы не гугу. Но так, между нами, постарайся не делать при ней того, что недавно выкинул за ужином."
    show geralthiptalk:
        xalign 0.0

        yalign 1.0 
    
    hide geralthip
    show kaldmolch1:
        xalign 0.25

        yalign 1.0 
    
    hide kaldhandssleep
    g "Ты имеешь в виду, когда я запустил вилкой в крысу?"
    show geralthip:
        xalign 0.0

        yalign 1.0 
    
    hide geralthiptalk
    show kaldtalk1:
        xalign 0.25

        yalign 1.0 
    
    hide kaldmolch1
    v "Нет. Я имею в виду, что ты в нее попал, хотя было темно."
    show geralttalk:
        "geralthip.png"
        xalign 0.0
        yalign 1.0
        pause 0.5
        "geralttalk.png" with dissolve
    hide geralthip
    show kaldmolch1:
        xalign 0.25

        yalign 1.0 
    
    hide kaldtalk1
    g "Я думал, будет забавно."
    show geralt:
        xalign 0.0

        yalign 1.0 
    
    hide geralttalk
    show kaldrighttalk:
        xalign 0.25

        yalign 1.0 
    
    hide kaldmolch1
    v "Оно и было. Только не делай этого при Либуше. "
    v "Слушай, а эта... как там ее... Куки..."
    show geralthandstalk:
        xalign 0.0

        yalign 1.0 
    
    hide geralt
    show kaldmolch1:
        xalign 0.25

        yalign 1.0 
    
    hide kaldtalk1
    hide kaldrighttalk
    g "Кикимора."
    show geralthands:
        xalign 0.0

        yalign 1.0 
    
    hide geralthandstalk
    show kaldtalk1:
        xalign 0.25

        yalign 1.0 
    
    hide kaldmolch1
    v "Она тебе для чего-то нужна?"
    show geralthandstalk:
        xalign 0.0

        yalign 1.0 
    
    hide geralthands
    show kaldmolch1:
        xalign 0.25

        yalign 1.0 
    
    hide kaldtalk1
    g "Интересно, для чего бы? Если награды не будет, можешь выкинуть ее на помойку."
    show geralthands:
        xalign 0.0

        yalign 1.0 
    
    hide geralthandstalk
    show kaldthinktalk:
        "kaldmolch1.png"
        xalign 0.25
        yalign 1.0
        pause 0.5
        "kaldthinktalk.png" with dissolve
    hide kaldmolch1
    v "А знаешь, это мысль. "
    show kaldshout:
        "kaldthinktalk.png"
        xalign 0.25
        yalign 1.0
        pause 0.5
        "kaldshout.png" with dissolve
    hide kaldthinktalk
    v "Эй, Карэлька, Борг, Носикамень!"
    v "Есть там кто? "
    scene scene 3

    with fade
    show guard with dissolve:
        xalign 0.0

        yalign 1.0 
    
    show kik with dissolve:
        xalign 1.25
        yalign 1.0
    show geralt with dissolve:
        xalign 0.5

        yalign 1.0 
    
    hide geralthandstalk
    show kaldturn with dissolve:
        xalign 0.75

        yalign 1.0 
    
    hide kaldtalk1
    hide kaldthink


    "Вошел городской стражник с алебардой на плече."
    show kaldshout:
        xalign 0.75

        yalign 1.0 
    
    hide kaldturn
    
    v "Носикамень, прихвати кого-нибудь в помощь, забери от хаты осла вместе с той дрянью, что покрыта попоной, отведи за хлевы и утопи в навозной яме."
    v "Усек?"
    show kaldshoutmolch:
        xalign 0.75

        yalign 1.0 
    
    hide kaldshout
    show guardtalk:
        xalign 0.0

        yalign 1.0 
    hide guard
    n "Угу... Слушаюсь..."
    n "Только, милсдарь войт..."
    show kaldtalk2:
        xalign 0.75

        yalign 1.0 
    hide kaldshoutmolch
    hide kaldturn
    show guardmolch:
        xalign 0.0

        yalign 1.0 
    hide guardtalk
    v "Чего еще?"
    show kaldturn:
        xalign 0.75

        yalign 1.0 
    
    hide kaldtalk2
    show guardtalk:
        xalign 0.0

        yalign 1.0 
    hide guardmolch
    n "Может прежде чем утопить..."
    show geralthands:
        xalign 0.5

        yalign 1.0 
    hide geralt
    show kaldtalk2:
        xalign 0.75

        yalign 1.0 
    
    hide kaldturn
    show guardmolch:
        xalign 0.0

        yalign 1.0 
    hide guardtalk
    v "Ну?"
    show kaldturn:
        xalign 0.75

        yalign 1.0 
    
    hide kaldtalk2
    show guardtalk:
        xalign 0.0

        yalign 1.0 
    hide guardmolch
    n "Показать ее мэтру Ириону? А вруг ему куда-нито сгодится?"
    show guardmolch:
        xalign 0.0

        yalign 1.0 
    hide guardtalk
    show kaldshout:
        xalign 0.75

        yalign 1.0 
    
    hide kaldturn
    v "А ты не дурак, Носикамень."
    v "Слушай, Геральт, может, наш городской колдун отвалит тебе чего за эту падаль?"
    v "Рыбаки приносят разных чудовищ, восьминогов там, крабаллонов, каракатов, на этом многие заработали."
    v "А ну пошли в башню."
    show kaldshoutmolch:
        xalign 0.75

        yalign 1.0 
    
    hide kaldshout
    show geralthandstalk:
        xalign 0.5

        yalign 1.0 
    
    hide geralthands
    g "Разбогатели? Собственного колдуна завели? Навсегда или временно?"
    show kaldtalk2:
        xalign 0.75

        yalign 1.0 
    
    hide kaldshoutmolch
    show geralthands:
        xalign 0.5

        yalign 1.0 
    
    hide geralthandstalk
    v "Навсегда."
    v "Мэтр Ирион уже год как в Блавикене. "
    v "Сильный маг, Геральт, сразу видно. "
    show kaldturn:
        xalign 0.75

        yalign 1.0 
    
    hide kaldtalk2
    show geralthandstalk:
        xalign 0.5

        yalign 1.0 
    
    hide geralthands
    g "Не думаю, чтобы ваш сильный маг заплатил бы за кикимору."
    show geralthands1:
        xalign 0.5

        yalign 1.0 
    
    hide geralthandstalk
    "Поморщился Геральт."
    show geralthandstalk:
        xalign 0.5

        yalign 1.0 
    
    hide geralthands1
    g "Насколько мне известно, она на эликсиры не годится."
    g "Думаю, Ирион только отчитает меня."
    g "Мы, ведьмаки, не очень-то дружим с волшебниками."
    show kaldtalk2:
        xalign 0.75

        yalign 1.0 
    
    hide kaldturn
    show geralthands:
        xalign 0.5

        yalign 1.0 
    
    hide geralthandstalk
    v "Никогда не слышал, чтобы мэтр Ирион кого-нибудь обругал."
    v "Заплатит ли, не обещаю, но попытка не пытка."
    v "На болотах таких куки... это, кикимор, может быть, много. "
    v "И что тогда?"
    v "Пусть колдун осмотрит ее и в случае чего наведет на топи какие-нибудь чары или чего там еще."
    show geralt1:
        xalign 0.5

        yalign 1.0 
    
    hide geralthands
    "Ведьмак ненадолго задумался."
    show kaldturn:
        xalign 0.75

        yalign 1.0 
    
    hide kaldtalk2
    show geralttalk:
        xalign 0.5

        yalign 1.0 
    
    hide geralt1
    g "Ну что ж, один-ноль в твою пользу, Кальдемейн."
    scene tower
    with fade
    "Башня, сложенная из гладко отесанных гранитных блоков, увенчанная каменными зубцами, выглядела вполне представительно."
    "Она возвышалась над побитыми крышами домов и полуразвалившимися кровлями халуп."
    scene door
    with dissolve
    # show guardmolch:
    #     xalign 0.0

    #     yalign 1.0 
    # show kik:
    #     xalign 1.25

    #     yalign 1.0 
    # show geralttalk with dissolve:
    #     xalign 0.25

    #     yalign 1.0
    # show kaldturn with dissolve:
    #     xalign 0.75

    #     yalign 1.0 
    

    g "Вижу, подновил. Волшебством или вас на работы согнал?"
    # show geralthands:
    #     xalign 0.25

    #     yalign 1.0
    # hide geralttalk
    # show kaldtalk2:
    #     xalign 0.75

    #     yalign 1.0
    # hide kaldturn
    # v "В основном чарами."
    # show geralthandstalk:
    #     xalign 0.25

    #     yalign 1.0
    # hide geralthands
    # show kaldturn:
    #     xalign 0.75

    #     yalign 1.0
    # hide kaldtalk2
    v "Вполне нормальный. Людям помогает."
    v "Но отшельник, молчун. Почти не вылазит из башни."
    scene plain
    with dissolve
    show kolotushkamolch:
        xalign 0.0

        yalign 1.0
    show kaldtalk1 with dissolve:
        xalign 0.0
        yalign 1.0
    v "Приветствует войт Кальдемейн, явившийся к мэтру Ириону по делу."
    v "С ним приветствует также ведьмак Геральт из Ривии, также явившийся по делу."
    show kolotushka:
        xalign 0.0

        yalign 1.0
    hide kolotushkamolch
    
    show kaldmolch1:
        xalign 0.0
        yalign 1.0
    hide kaldtalk1
    k "Мэтр Ирион не принимает. Уходите, добрые..."
    show kolotushkamolch:
        xalign 0.0

        yalign 1.0
    hide kolotushka
    hide kaldmolch1
    show geraltustalk:
        xalign 0.0
        yalign 1.0
    
    g "Я не добрый человек."
    g "Я ведьмак."
    
    show geraltushandstalk:
        "geraltustalk.png"
        xalign 0.0
        yalign 1.0
        pause 0.5
        "geraltushandstalk.png" with dissolve
    hide geraltustalk
    g "А вон там, на осле, лежит кикимора, которую я убил недалеко от городка."
    g "Любой волшебник-резидент обязан заботиться о безопасности района."
    g "Мэтру Ириону ни к чему оказывать мне честь беседой, и он не обязан меня принимать, ежели такова его воля."
    show geraltustalk:
        "geraltushandstalk.png"
        xalign 0.0
        yalign 1.0
        pause 0.5
        "geraltushandstalk.png" with dissolve
    hide geraltushandstalk
    g "Но кикимору пусть осмотрит и сделает соответствующие выводы."
    g "Носикамень, раскрой кикимору и свали ее здесь, у самых дверей."
    hide geraltustalk
    show kaldtalk1:
        xalign 0.0
        yalign 1.0
    v "Геральт, ты-то уедешь, а мне тут придется..."
    hide kaldtalk1
    show geraltustalk:
        xalign 0.0
        yalign 1.0
    g "Пошли, Кальдемейн."
    g "Носикамень, вынь палец из носа и делай что велят."
    show geraltus:
        xalign 0.0
        yalign 1.0
    hide geraltustalk

    show kolotushka:
        xalign 0.0

        yalign 1.0
    hide kolotushkamolch
    k "Сейчас, Геральт, это верно ты?"
    show geraltustalk:
        xalign 0.0
        yalign 1.0
    hide geraltus
    
    "Ведьмак тихо выругался."
    show kolotushkamolch:
        xalign 0.0

        yalign 1.0
    hide kolotushka
    g "Ну, зануда!"
    g "Да, верно я. Ну и что с того, что это верно я?"
    show geraltus:
        xalign 0.0
        yalign 1.0
    hide geraltustalk
    show kolotushka:
        xalign 0.0

        yalign 1.0
    hide kolotushkamolch
    k "Подойди ближе к двери, один. Я тебя впущу."
    show geraltustalk:
        xalign 0.0
        yalign 1.0
    hide geraltus
    show kolotushkamolch:
        xalign 0.0

        yalign 1.0
    hide kolotushka
    g "А как с кикиморой?"
    show geraltus:
        xalign 0.0
        yalign 1.0
    hide geraltustalk
    show kolotushka:
        xalign 0.0

        yalign 1.0
    hide kolotushkamolch
    k "Черт с ней. Я хочу поговорить с тобой, Геральт."
    k "Только с тобой."
    k "Извините, войт."
    hide geraltus
    show kaldtalk1:
        xalign 0.0
        yalign 1.0
    v "Да чего уж там, мэтр Ирион."
    v "Бывай, Геральт. Увидимся позже."
    v "Носикамень! Уродину в жижу!"
    hide kaldtalk1
    show guardtalk:
        xalign 0.0
        yalign 1.0
    n "Слушаюсь!"
    scene door
    with dissolve
    "Ведьмак подошел к двери."
    scene doorflash
    with dissolve
    "Она слегка приоткрылась, ровно настолько, чтобы он мог протиснуться."
    scene garden
    with flash
    stop music

    play music "garden.mp3"
    "За ней оказался сад."
    "Он цвел белым и розовым, воздух был напоен ароматом дождя."
    "Небо пересекала многоцветная радуга, связывая кроны с далекой голубоватой цепью гор."
    "Домик посреди сада, маленький и скромный, утопал в мальвах."
    show geralt1 with dissolve:
        xalign 0.25
        yalign 1.0
    "Геральт глянул под ноги и увидел, что стоит по колено в тимьяне."
    show stregobortalk with dissolve:
        xalign 1.0
        yalign 1.0
    i "Ну, иди же, Геральт. Я у дома."
    i "Наконец-то. Приветствую тебя, ведьмак."
    show stregobor with dissolve:
        xalign 1.0
        yalign 1.0
    hide stregobortalk
    show geralttalk:
        xalign 0.25
        yalign 1.0
    hide geralt1
    g "Стрегобор!"
    "Удивился решивший не удивляться Геральт."
    show geralt:
        xalign 0.25
        yalign 1.0
    hide geralttalk
    
    show stregobortalk with dissolve:
        xalign 1.0
        yalign 1.0
    hide stregobor

    s "Что поделываешь здесь, Геральт? По-прежнему трудишься, за деньги истребляя представителей вымирающих видов?"
    s "Что получил за кикимору? Наверное -  ничего, иначе б не пришел сюда."
    s "Подумать только, есть люди, не верящие в Предназначение."
    s "Разве что знал обо мне."
    show stregoborhappytalk:
        xalign 1.0
        yalign 1.0
    hide stregobortalk
    s "Знал?"
    show stregobor1:
        xalign 1.0
        yalign 1.0
    hide stregoborhappytalk
    show geralttalk:
        xalign 0.25
        yalign 1.0
    hide geralt
    g "Не знал."
    g "Уж если я где не ожидал тебя встретить, так именно здесь. "
    g "Если мне память не изменяет, раньше ты жил в Ковире, в такой же башне."
    show geralt:
        xalign 0.25
        yalign 1.0
    hide geralttalk
    show stregobortalk:
        xalign 1.0
        yalign 1.0
    hide stregoborhappy
    s "Много изменилось с тех пор."
    show stregobor1:
        xalign 1.0
        yalign 1.0
    hide stregobortalk
    show geralthandstalk:
        xalign 0.25
        yalign 1.0
    hide geralt
    g "Хотя бы твое имя. Теперь ты вроде бы зовешься мэтром Ирионом?"
    show stregobortalk:
        xalign 1.0
        yalign 1.0
    hide stregobor1
    show geralthands:
        xalign 0.25
        yalign 1.0
    hide geralthandstalk
    s "Так звали строителя этой башни, он скончался лет двадцать назад. Я решил, что его надо как-то почтить, ну и занял его обитель. "
    s "Я тут сижу за резидента."
    s "Большинство горожан живут дарами моря, а, как тебе известно, моя специальность - кроме иллюзий, разумеется, - это погода."
    s "Порой шторм пригашу, порой вызову, то западным ветром пригоню ближе к берегу косяк мерлангов или угрей."
    s "Жить можно."
    s "То есть..."
    s "Можно бы жить."
    "Грустно добавил чародей."
    show geralthiptalk:
        xalign 0.25
        yalign 1.0
    hide geralthands
    show stregobor1:
        xalign 1.0
        yalign 1.0
    hide stregobortalk
    g "Почему «можно бы»?"
    g "И зачем ты сменил имя?"
    show geralthip:
        xalign 0.25
        yalign 1.0
    hide geralthiptalk
    show stregobortalk:
        xalign 1.0
        yalign 1.0
    hide stregobor1
    s "У Предназначения масса обличий."
    s "Мое прекрасно снаружи и отвратительно внутри."
    s "Оно протянуло ко мне свои окровавленные когти..."
    show geralttalk:
        xalign 0.25
        yalign 1.0
    hide geralthip
    show stregobor1:
        xalign 1.0
        yalign 1.0
    hide stregobortalk
    g "Ты ничуть не изменился, Стрегобор. "
    g "Плетешь ерунду и при этом строишь умные и многозначительные мины."
    g "Не можешь говорить нормально?"
    scene garden2
    show stregorich
    s "Могу."
    s "Если это доставит тебе удовольствие, могу. "
    s "Я забрался сюда, сбежав от жуткого существа, которое собралось меня прикончить. Бегство ничего не дало, оно меня нашло."
    s "По всей вероятности, попытается убить завтра, в крайнем случае - послезавтра."
    show gerich
    hide stregorich
    g "Та-а-ак."
    g "Теперь понимаю."
    scene garden
    show stregoborangrytalk:
        xalign 1.0
        yalign 1.0

    show geralthands:
        xalign 0.25
        yalign 1.0
    s "Что-то мне сдается, моя возможная смерть не очень-то тебя волнует."
    show stregoborangry:
        xalign 1.0
        yalign 1.0
    hide stregoborangrytalk
    show geralthandstalk:
        xalign 0.25
        yalign 1.0
    hide geralthands
    g "Стрегобор, таков мир."
    show geralthands:
        xalign 0.25
        yalign 1.0
    hide geralthandstalk
    show stregobortalk:
        xalign 1.0
        yalign 1.0
    hide stregoborangry
    s "А я-то считал тебя другом. Надеялся на твою помощь."
    show stregobor1:
        xalign 1.0
        yalign 1.0
    hide stregoborhappybeardtalk
    hide stregobortalk
    hide stregoborhappy
    hide stregoborhappytalk
    hide stregoborhappybeardtalk
    show geralthandstalk:
        xalign 0.25
        yalign 1.0
    hide geralthands
    g "Наша последняя встреча имела место при дворе короля Иди в Ковире."
    g "Я пришел получить плату за уничтожение амфисбены, которая терроризировала всю округу."
    g "Тогда ты и твой собрат Завист наперебой обзывали меня шарлатаном, бездумной машиной для убийств и, если мне память не изменяет, трупоедом."
    g "В результате Иди не только не заплатил мне ни шелонга, но еще велел за двенадцать часов убраться из Ковира."
    g "А поскольку клепсидра у него была испорчена, я едва-едва успел."
    g "А теперь ты говоришь, что рассчитываешь на мою помощь. "
    g "Говоришь, что тебя преследует чудовище."
    g "Чего ты боишься, Стрегобор? "
    g "Если оно на тебя нападет, скажи ему, что обожаешь чудовищ, оберегаешь их и следишь за тем, чтобы ни один трупоедский ведьмак не нарушил их покоя. "
    g "Ну а уж если и после этого чудовище выпотрошит тебя и сожрет, значит, оно чудовищно неблагодарное чудовище."
    hide geralthandstalk
    show geralthands:
        xalign 0.25
        yalign 1.0
    hide stregobor1
    show stregoborangrybeard:
        "stregobor1.png"
        xalign 1.0
        yalign 1.0
        pause 0.5
        "stregoborangrybeard.png" with dissolve
    # show stregoborangrybeard with dissolve:
    #     xalign 1.0
    #     yalign 1.0
    # hide stregobor1 with dissolve
    "Колдун, отвернувшись, молчал."
    hide geralthands
    show geralthappy:
        "geralthands.png"
        xalign 0.25
        yalign 1.0
        pause 0.5
        "geralthappy.png" with dissolve
    "Геральт рассмеялся."
    hide geralthappy
    show geralthappytalk:
        xalign 0.25
        yalign 1.0
    g "Не надувайся как жаба, маг."
    g "Говори, что тебе угрожает. Посмотрим, что можно сделать."
    hide geralthappytalk
    show geralthands1:
        xalign 0.25
        yalign 1.0
    hide stregoborangrybeard
    show stregobortalk:
        "stregoborangrybeard.png"
        xalign 1.0
        yalign 1.0
        pause 0.5
        "stregobortalk.png" with dissolve
    # hide stregoborangrybeard
    # show stregobortalk with dissolve:
    #     xalign 1.0
    #     yalign 1.0
    s "Ты слышал о Проклятии Черного Солнца?"
    hide geralthands1
    show geralthandstalk:
        xalign 0.25
        yalign 1.0
    hide stregobortalk
    show stregobor1:
        xalign 1.0
        yalign 1.0
    g "А как же. Слышал. "
    g "Только под названием Мании Сумасшедшего Эльтибальда."
    g "Так звали мага, который устроил бузу, в результате которой перебили или заточили в башни несколько десятков высокородных девиц."
    g "Даже королевских кровей."
    g "Якобы они были одержимы дьяволом, прокляты, порчены Черным Солнцем, как на вашем напыщенном жаргоне вы окрестили обыкновеннейшее солнечное затмение. "
    hide geralthandstalk
    show geralthands:
        xalign 0.25
        yalign 1.0
    hide stregobor1
    show stregobortalk:
        xalign 1.0
        yalign 1.0
    s "Эльтибальд, который вовсе не был сумасшедшим, расшифровал надписи на менгирах дауков, на надгробных плитах в некрополях вожгоров, проанализировал легенды и мифы детолаков."
    s "Никаких сомнений быть не могло."
    s "Черное Солнце должно было предвещать скорое возвращение Лилиты, почитаемой на Востоке под именем Нийями, и гибель человечества. "
    s "Дорогу для Лилиты должны были проложить «шестьдесят дев в златых коронах, кои кровью заполнят русла рек»."
    scene garden2
    show gerich
    # show geralthiptalk:
    #     "geralthands.png"
    #     xalign 0.0
    #     yalign 1.0
    #     pause 0.5
    #     "geralthiptalk.png" with dissolve
    g "Бред."
    g "И вдобавок нерифмованный."
    g "Все приличные предсказания бывают в стихах."
    g "Всем известно, что имел в виду Эльтибальд и Совет Чародеев."
    g "Вы воспользовались бредом сумасшедшего, чтобы укрепить свою власть, разрушить союзы, не допустить родственных связей."
    g "И устроить неразбериху в династиях словом, как следует подергать за веревочки, подвязанные к марионеткам в коронах."
    g "А ты мне мозги пудришь какими-то предсказаниями, которых постыдился бы даже кривой старик на ярмарке."
    hide gerich
    show stregorich
    s "Можно скептически относиться к теории Эльтибальда, к интерпретациям предсказателей. "
    s "Но нельзя отрицать того факта, что у девушек, родившихся после затмения, наблюдаются чудовищные мутации."
    hide stregorich
    show gerich
    g "Почему же нельзя?"
    g "Я слышал нечто диаметрально противоположное."
    hide gerich
    show stregorich
    s "Я присутствовал при вскрытии одной из них."
    s "Геральт, то, что мы обнаружили внутри черепа и спинного мозга, невозможно было однозначно определить."
    s "Какая-то красная губка."
    s "Внутренние органы смещены, перемешаны, некоторых вообще нет."
    s "Все покрыто подвижными жгутиками, сине-розовыми лоскутиками.  "
    s "Сердце с шестью камерами."
    s "Две практически атрофированы, но тем не менее. "
    s "Что ты на это скажешь?"
    hide stregorich
    show gerich
    g "Я видел людей, у которых вместо рук орлиные когти, людей с волчьими клыками."
    g "Людей с дополнительными суставами, дополнительными органами и дополнительными чувствами."
    g "Все это были результаты вашей возни с магией."
    scene garden
    show stregoborangrytalk:
        xalign 1.0
        yalign 1.0
    hide geralthandstalk
    show geralthands:
        xalign 0.25
        yalign 1.0
    s "Говоришь, видел различные мутации?"
    s "А скольких из них ты угробил за деньги в соответствии со своим ведьмачьим призванием? "
    s "А?"
    s "Потому как можно иметь волчьи клыки и ограничиться тем, что их показываешь девкам в хлеву, а можно иметь волчью натуру и нападать на детей."
    s "Именно так было с рожденными после затмения девочками, у которых обнаружились необъяснимая склонность к жестокости, агрессивность, бурные вспышки гнева и чрезмерный темперамент."
    hide stregoborangrytalk
    show stregobor1:
        xalign 1.0
        yalign 1.0
    hide geralthands
    show geralthandstalk:
        xalign 0.25
        yalign 1.0
    g "У любой бабы при желании можно отыскать подобное."
    g "Что ты плетешь?"
    g "Выпытываешь, сколько мутантов я убил, а почему тебя не интересует, скольких я расколдовал, освободил от сглаза?"
    g "Я, ведьмак, которого вы презираете."
    g "А что сделали вы, могущественные чернокнижники?"
    hide stregobor1
    show stregoborbeardtalk:
        xalign 1.0
        yalign 1.0
    hide geralthandstalk
    show geralthands:
        xalign 0.25
        yalign 1.0
    s "Применили высшую магию."
    s "Нашу и священническую в различных храмах."
    s "Все испытания окончились смертью девушек."
    hide stregoborbeardtalk
    show stregobor1:
        xalign 1.0
        yalign 1.0
    hide geralthands
    show geralthiptalk:
        xalign 0.25
        yalign 1.0
    g "Это плохо говорит о вас, а не о девушках."
    g "Итак, первые трупы."
    g "Насколько я понимаю, вскрывали только их?"
    hide stregobor1
    show stregobortalk:
        xalign 1.0
        yalign 1.0
    hide geralthiptalk
    show geralthip:
        xalign 0.25
        yalign 1.0
    s "Не только."
    s "Не смотри на меня так, сам прекрасно знаешь, что были и еще трупы."
    s "Сначала решили было ликвидировать всех."
    s "Но потом передумали..."
    s "Тех же, которых все-таки...убирали, вскрывали."
    s "Одну подвергли вивисекции."
    hide stregobortalk
    show stregobor1:
        xalign 1.0
        yalign 1.0
    hide geralthip
    show geraltangrytalk:
        xalign 0.25
        yalign 1.0
    g "И вы, сукины дети, еще осмеливаетесь критиковать ведьмаков?"
    g "Эх, Стрегобор, Стрегобор, придет день, люди поумнеют и возьмутся за вас."
    hide stregobor1
    show stregobortalk:
        xalign 1.0
        yalign 1.0
    hide geraltangrytalk
    show geralt:
        xalign 0.25
        yalign 1.0
    s "Не думаю, чтобы это случилось очень скоро."
    "Кисло заметил чародей. "
    hide stregobortalk
    show stregobor1:
        xalign 1.0
        yalign 1.0
    hide geralt
    show geraltangrytalk:
        xalign 0.25
        yalign 1.0
    g "Так утверждаете вы, колдуны, задрав носы выше своего нимба непогрешимости."
    g "Коли уж об этом зашла речь, ты, вероятно, не станешь утверждать, что якобы, охотясь на так называемых мутантов, вы ни разу не ошиблись?"
    hide stregobor1
    show stregobortalk:
        xalign 1.0
        yalign 1.0
    hide geraltangrytalk
    show geralt:
        xalign 0.25
        yalign 1.0
    s "Ладно."
    s "Буду откровенен, хотя в собственных интересах и не следовало бы. "
    s "Ошиблись, и к тому же не раз."
    s "Разделить их по группам оказалось весьма трудным делом."
    s "Поэтому мы перестали их убивать, а стали изолировать."
    hide stregobortalk
    show stregobor1:
        xalign 1.0
        yalign 1.0
    hide geralt
    show geralthandstalk:
        xalign 0.25
        yalign 1.0
    g "Ну да, ваши знаменитые башни."
    hide stregobor1
    show stregobortalk:
        xalign 1.0
        yalign 1.0
    hide geralthandstalk
    show geralthands:
        xalign 0.25
        yalign 1.0
    s "Да, наши башни."
    s "Однако это была очередная ошибка."
    s "Мы недооценили их, и многие сбежали."
    s "Среди принцев, особенно тех, что помоложе, которым нечего было делать, а еще меньше - терять, распространилась какая-то идиотская мода освобождать заключенных красоток."
    s "К счастью, большинство свернули себе шеи."
    hide stregobortalk
    show stregobor1:
        xalign 1.0
        yalign 1.0
    hide geralthands
    show geralthandstalk:
        xalign 0.25
        yalign 1.0
    g "Насколько мне известно, заточенные в башнях девушки быстро умирали. "
    g "Поговаривают, не без вашей помощи."
    hide stregobor1
    show stregoborbeardtalk:
        xalign 1.0
        yalign 1.0
    hide geralthandstalk
    show geralthands:
        xalign 0.25
        yalign 1.0
    s "Наглая ложь."
    s "Однако действительно они быстро погружались в апатию, отказывались от пищи..."
    s "Что интересно, незадолго до смерти у них прорезывался дар ясновидения."
    s "Очередное доказательство мутации."
    hide stregoborbeardtalk
    show stregobor1:
        xalign 1.0
        yalign 1.0
    hide geralthands
    show geralthandstalk:
        xalign 0.25
        yalign 1.0
    g "Что ни доказательство, то все менее убедительное."
    g "Ты не убедишь меня в своей правоте и тем более в том, что Эльтибальд не был сумасшедшим разбойником."
    g "Вернемся к чудовищу, которое тебе якобы угрожает."
    g "Я выслушал тебя и должен сказать: рассказанная тобою история мне не нравится."
    g "Но я дослушаю ее до конца."
    hide stregobor1
    show stregobortalk:
        xalign 1.0
        yalign 1.0
    hide geralthandstalk
    show geralthands:
        xalign 0.25
        yalign 1.0
    s "Не перебивая ехидными замечаниями?"
    hide stregobortalk
    show stregobor1:
        xalign 1.0
        yalign 1.0
    hide geralthands
    show geralthappytalk:
        xalign 0.25
        yalign 1.0
    g "Обещать не могу."
    hide stregobor1
    show stregobortalk:
        xalign 1.0
        yalign 1.0
    hide geralthappytalk
    show geralthands:
        xalign 0.25
        yalign 1.0
    s "Ну что ж тем больше это займет времени."
    show grey with dissolve
    show misli1 with dissolve
    s "Итак, история началась в Крейдене, маленьком северном княжестве."
    hide misli1 with dissolve
    show misli2 with dissolve
    
    s "Женой Фредефалька, княжившего в Крейдене, была Аридея, умная, образованная женщина."
    hide misli2 with dissolve
    show misli3 with dissolve
    s "В роду у нее было множество последователей искусства чернокнижников, и, вероятно, по наследству ей достался довольно редкий и могущественный артефакт, Зеркало Нехалены."
    hide misli3 with dissolve
    show misli6 with dissolve
    s "Как известно, Зеркалами Нехалены в основном пользовались пророки и ясновидцы, потому что они безошибочно, хоть и путано, предсказывали будущее."
    s "Аридея довольно часто обращалась к Зеркалу..."
    hide misli6 with dissolve
    hide grey with dissolve
    hide stregobortalk
    show stregobor1:
        xalign 1.0
        yalign 1.0
    hide geralthands
    show geralthandstalk:
        xalign 0.25
        yalign 1.0
     
    g "С обычным, как я думаю, вопросом: «Кто на свете всех милее?»."
    g "Насколько мне известно, Зеркала Нехалены подразделяются на льстивые и разбитые."
    hide stregobor1
    show stregobortalk:
        xalign 1.0
        yalign 1.0
    hide geralthandstalk
    show geralthands:
        xalign 0.25
        yalign 1.0
     
    s "Ошибаешься."
    s "Аридею больше интересовала судьба страны."
    s "А отвечая на ее вопросы, Зеркало предсказало мучительную смерть ее самой и множества ее подданных от руки либо по вине дочери Фредефалька от первого брака."
    hide stregobortalk
    show stregobor1:
        xalign 1.0
        yalign 1.0
    hide geralthands
    show geralthandstalk:
        xalign 0.25
        yalign 1.0
    g "Ясно, и надо думать, не шибко любила падчерицу."
    g "Предпочитала, чтобы трон наследовали ее собственные дети."
    hide stregobor1
    show stregobortalk:
        xalign 1.0
        yalign 1.0
    hide geralthandstalk
    show geralthands:
        xalign 0.25
        yalign 1.0
    s "Я стоял за то, чтобы ее только изолировать, но княгиня решила иначе."
    show grey with dissolve
    show misli4 with dissolve
    s "Наняла егеря-бандита и отослала с ним малышку в лес."
    hide misli4 with dissolve
    show misli5 with dissolve
    s "Позже мы нашли его в зарослях мертвым."
    hide misli5 with dissolve
    hide grey with dissolve
    hide stregobortalk
    show stregobor1:
        xalign 1.0
        yalign 1.0
    hide geralthands
    show geralttalk:
        xalign 0.25
        yalign 1.0
    g "Если ты думаешь, что мне его жаль, то ошибаешься."
    hide stregobor1
    show stregobortalk:
        xalign 1.0
        yalign 1.0
    hide geralttalk
    show geralt:
        xalign 0.25
        yalign 1.0
    show grey with dissolve
    show misli7 with dissolve
    s "Мы устроили облаву, но девчонка как сквозь землю провалилась."
    s "А мне пришлось срочно ретироваться из Крейдена, потому что Фредефальк начал что-то подозревать."
    s "Лишь спустя четыре года я получил известие от Аридеи."
    hide misli7 with dissolve
    show misli8 with dissolve
    s "Она выследила девку, та жила в Махакаме."
    s "Аридея несколько раз нанимала убийц, но ни один не вернулся."
    s "А потом уж трудно было найти желающих, слух о девке прошел повсюду."
    hide misli8 with dissolve
    show misli9 with dissolve
    s "Мечом научилась работать так, что мало какой мужик мог с ней сравняться."
    hide misli9 with dissolve
    show misli10 with dissolve
    s "Меня снова вызвали, я тайком явился в Крейден и тут узнал, что Аридею отравили."
    s "Все считали, что это работа самого Фредефалька, который высмотрел себе наложницу помоложе и поядренее, но я думаю, без Ренфри тут не обошлось."
    hide misli10 with dissolve
    hide grey with dissolve
    hide stregobortalk
    show stregobor1:
        xalign 1.0
        yalign 1.0
    hide geralt
    show geralttalk:
        xalign 0.25
        yalign 1.0
    g "Ренфри?"
    hide stregobor1
    show stregobortalk:
        xalign 1.0
        yalign 1.0
    hide geralttalk
    show geralt:
        xalign 0.25
        yalign 1.0
    s "Так звали Сорокопутку."
    s "Когда я был в Махакаме, мы встретились нос к носу, она мгновенно узнала меня и тут же сообразила, какова была моя роль тогда в Крейдене."
    s "Уверяю тебя, Геральт, я едва успел выговорить заклинание, а руки тряслись у меня страшно, когда эта дикая кошка кинулась на меня, размахивая мечом."
    show grey with dissolve
    show misli11 with dissolve
    s "Я заточил ее в изящную глыбу горного хрусталя, шесть локтей на девять. "
    s "Когда она погрузилась в летаргию, я кинул глыбу в гномовскую шахту и завалил ствол."
    
    hide misli11 with dissolve
    hide grey with dissolve
    hide stregobortalk
    show stregobor1:
        xalign 1.0
        yalign 1.0
    hide geralt
    show geralthandstalk:
        xalign 0.25
        yalign 1.0
    g "Халтурная работа."
    g "Легко расколдовать. Нельзя было, что ли, превратить в пепел?"
    g "Ведь у вас столько исключительно милых заклинаний."
    hide stregobor1
    show stregobortalk:
        xalign 1.0
        yalign 1.0
    hide geralthandstalk
    show geralthands:
        xalign 0.25
        yalign 1.0
    s "Не у меня. Не моя специальность."
    s "Но ты прав я схалтурил. "
    s "Отыскался какой-то идиот-королевич, истратил уйму денег на контрзаклинание, расколдовал ее и с триумфом привез к себе домой, в какое-то замызганное королевство на Востоке."
    hide stregobortalk
    show stregobor1:
        xalign 1.0
        yalign 1.0
    hide geralthands
    show geralthandstalk:
        xalign 0.25
        yalign 1.0
    g "Стало быть, не уродина."
    hide stregobor1
    show stregobortalk:
        xalign 1.0
        yalign 1.0
    hide geralthandstalk
    show geralthands:
        xalign 0.25
        yalign 1.0
    s "Дело вкуса."
    s "Вскоре оказалось, что она не забыла обо мне."
    s "В Ковире организовала на меня три покушения из-за угла."
    s "Я решил не рисковать и переждать в Понтаре."
    s "Она снова нашла меня. "
    s "Тогда я сбежал в Ангрен, но она и тут меня прищучила."
    s "Не знаю, как это у нее получается, следы я заметал хорошо. Наверно, свойство ее мутации."
    hide stregobortalk
    show stregobor1:
        xalign 1.0
        yalign 1.0
    hide geralthands
    show geralthandstalk:
        xalign 0.25
        yalign 1.0
    g "А что ж ты снова-то ее в хрусталь не заключил?"
    g "Угрызения совести?"
    hide stregobor1
    show stregobortalk:
        xalign 1.0
        yalign 1.0
    hide geralthandstalk
    show geralthands:
        xalign 0.25
        yalign 1.0
    s "Нет. Таковых не было."
    s "Однако оказалось, что она приобрела иммунитет против магии."
    hide stregobortalk
    show stregobor1:
        xalign 1.0
        yalign 1.0
    hide geralthands
    show geralttalk:
        xalign 0.25
        yalign 1.0
    g "Невозможно!"
    hide stregobor1
    show stregobortalk:
        xalign 1.0
        yalign 1.0
    hide geralttalk
    show geralt:
        xalign 0.25
        yalign 1.0
    s "Возможно."
    s "Достаточно заполучить соответствующий артефакт или обзавестись аурой."
    s "Это опять же могло быть следствием ее прогрессирующей мутации."
    s "Я сбежал из Ангрена и спрятался здесь, на Лукоморье, в Блавикене."
    s "Год прожил спокойно, но она снова меня вынюхала."
    hide stregobortalk
    show stregobor1:
        xalign 1.0
        yalign 1.0
    hide geralt
    show geralttalk:
        xalign 0.25
        yalign 1.0
    g "Откуда знаешь? Она уже здесь?"
    hide stregobor1
    show stregobortalk:
        xalign 1.0
        yalign 1.0
    hide geralttalk
    show geralt:
        xalign 0.25
        yalign 1.0
    s "Да. Я видел ее в кристалле."
    s "Она не одна, руководит бандой, а значит, замыслила что-то серьезное."
    s "Геральт, больше мне бежать некуда, я не знаю такого места, где бы можно было укрыться."
    s "Да. То, что ты прибыл сюда именно сейчас, не случайность."
    s "Это Предназначение."
    s "Судьба."
    s "Рок."
    hide stregobortalk
    show stregobor1:
        xalign 1.0
        yalign 1.0
    hide geralt
    show geralttalk:
        xalign 0.25
        yalign 1.0
    g "Что ты имеешь в виду?"
    hide stregobor1
    show stregobortalk:
        xalign 1.0
        yalign 1.0
    hide geralttalk
    show geralt:
        xalign 0.25
        yalign 1.0
    s "Я думаю, это ясно. Ты убьешь ее."
    show grey
    menu:

        "Согласиться с предложением":
            jump choice1_yes

        "Отказаться от его предложения":
            jump choice1_no

    
    label choice1_yes:

        $ menu_flag = True

        hide grey
        "После долгой паузы в разговоре Геральт все же ответил, с некоторым презрением в голосе."
        hide stregobortalk
        show stregobor1:
            xalign 1.0
            yalign 1.0
        hide geralt
        show geralthandstalk:
            xalign 0.0
            yalign 1.0
        g "Допустим, я соглашусь."
        g "Но ты же понимаешь, что это не по доброте душевной?"
        hide stregobor1
        show stregoborhappytalk:
            xalign 1.0
            yalign 1.0
        hide geralthandstalk
        show geralthands:
            xalign 0.0
            yalign 1.0
        s "Конечно, конечно! Сколько скажешь, столько и дам."
        hide stregoborhappytalk
        show stregobor1:
            xalign 1.0
            yalign 1.0
        hide geralthands
        show geralthandstalk:
            xalign 0.0
            yalign 1.0
        g "Три сотни крон и пару ингредиентов для эликсиров."
        hide stregobor1
        show stregoborhappytalk:
            xalign 1.0
            yalign 1.0
        hide geralthandstalk
        show geralthands:
            xalign 0.0
            yalign 1.0
        s "Договорились!"
        s "Хочешь я тебе сразу половину дам?"
        s "Только, умоляю, расправься с этим чудовищем, как можно быстрее!"
        scene hands
        with dissolve
        "И тут в руках волшебника материализовался мешочек с золотом."
        "После тяжелого вздоха, ведьмак аккуратно взял деньги и покинул колдуна, не попрощавшись."
        scene tavern
        with dissolve
        stop music

        play music "tavernmusic.mp3"
        "На следующий день Геральт вместе с Кальдемейном отправились в таверну «Золотой двор»."
        scene intavern
        show geralt1:
            xalign 0.25
            yalign 1.0
        show kaldustalk:
            xalign 0.75
            yalign 1.0
        show table:
            xalign 0.0
            yalign 0.25
        v "Напряги память, Сотник."
        v "Шесть парней и девка, одетые в черные, украшенные серебром, кожей по новиградской моде."
        v "Я видел их на заставе."
        v "Они остановились у тебя или «Под Альбакаром»."
        hide geralt1
        show geraltus:
            xalign 0.25
            yalign 1.0
        hide kaldustalk
        show kaldusmolch:
            xalign 0.75
            yalign 1.0
        hide table
        show table:
            xalign 0.0
            yalign 0.25

        t "Здесь они, войт."
        t "Говорят, приехали на ярмарку, а все при мечах, даже девка."
        hide kaldusmolch
        show kaldushandstalk:
            xalign 0.75
            yalign 1.0
        hide table
        show table:
            xalign 0.0
            yalign 0.25

        v "Угу. Где они сейчас? "
        v "Что-то их не видно."
        hide kaldushandstalk
        show kaldshoutmolch:
            xalign 0.75
            yalign 1.0
        hide table
        show table:
            xalign 0.0
            yalign 0.25

        t "В маленьком закутке. Золотом платили."
        hide geraltus
        show geraltustalk:
            xalign 0.25
            yalign 1.0
        hide table
        show table:
            xalign 0.0
            yalign 0.25
        g "Схожу один."
        g "Не надо превращать это в официальное посещение, во всяком случае, пока."
        g "Приведу ее сюда."
        hide geraltustalk
        show geraltus:
            xalign 0.25
            yalign 1.0
        hide kaldshoutmolch
        show kaldushandstalk:
            xalign 0.75
            yalign 1.0
        hide table
        show table:
            xalign 0.0
            yalign 0.25
        v "Может, и верно."
        v "Но поосторожней. Мне тут драки ни к чему."
        hide geralt
        show geralttalk:
            xalign 0.25
            yalign 1.0
        hide kaldushandstalk
        show kaldshoutmolch:
            xalign 0.75
            yalign 1.0
        hide table
        show table:
            xalign 0.0
            yalign 0.25
        g "Посмотрим."
        scene room
        with dissolve
        stop music

        play music "badboys.mp3"
        "За столом сидели шестеро мужчин. "
        "Той, которую он ожидал увидеть, среди них не было."
        scene nogorn
        r1 "Ну чего!?!"
        "Рявкнул тот, который заметил его первым."
        g "Хочу увидеться с Сорокопуткой."
        scene twins
        with dissolve
        scene twins2
        with dissolve
        scene door2
        show geraltus:
            xalign 0.25
            yalign 1.0
        show twin1:
            xalign 1.0
            yalign 1.0
        show twin2:
            xalign 0.75
            yalign 1.0
        "От стола поднялись две одинаковые фигуры."
        scene nogorn2
        r1 "Спокойно, парни."
        r1 "С кем, говоришь, хочешь встретиться, братец?"
        r1 "Кто такая Сорокопутка?"
        scene desatka
        r2 "Что за тип? Ты его знаешь?"
        scene nogorn2
        r1 "Нет."
        scene kivril
        r3 "Альбинос какой-то."
        r3 "И надо же, впускают таких в шинки к порядочным людям."
        scene tavik
        r4 "Я его где-то уже видел."
        scene nogorn2
        r1 "Не важно, где ты его видел."
        r1 "Послушай, братец, мой друг только што тебя страшно обидел."
        r1 "Ты его не вызовешь? Такой скушный вечер!"
        scene door2
        show geraltustalk:
            xalign 0.25
            yalign 1.0
        show twin1:
            xalign 1.0
            yalign 1.0
        show twin2:
            xalign 0.75
            yalign 1.0
        g "Нет, не вызову."
        "Спокойно сказал ведьмак."
        scene desatka
        r2 "А меня, если вылью на тебя эту рыбную похлебку?"
        scene nogorn2
        r1 "Спокойно!"
        r1 "Раз он сказал нет, значит нет. "
        r1 "Пока."
        r1 "Ну, брат, говори, што хочешь сказать, и выматывайся. "
        r1 "Имеешь возможность выйти сам."
        r1 "Если не воспользуешься, тебя вынесут половые."
        scene door2
        show geraltushandstalk:
            xalign 0.25
            yalign 1.0
        show twin1:
            xalign 1.0
            yalign 1.0
        show twin2:
            xalign 0.75
            yalign 1.0
        g "Тебе мне сказать нечего."
        g "Хочу увидеться с Сорокопуткой."
        g "С Ренфри."
        scene nogorn2
        r1 "Слышали, парни? Он хочет видеться с Ренфри. "
        r1 "А зачем, братец, позволь узнать?"
        scene door2
        show geraltushandstalk:
            xalign 0.25
            yalign 1.0
        show twin1:
            xalign 1.0
            yalign 1.0
        show twin2:
            xalign 0.75
            yalign 1.0
        g "Не позволю."
        scene nogorn2
        "Ногорн поднял голову и глянул на близнецов."
        scene door2
        show geraltus:
            xalign 0.25
            yalign 1.0
        show twin1:
            xalign 0.75
            yalign 1.0
        show twin2:
            xalign 0.5
            yalign 1.0
        "Те тут же сделали шаг вперед, бренча серебряными застежками высоких ботинок."
        scene tavik
        r4 "Знаю! Вспомнил, где я его видел!"
        scene nogorn2
        r1 "Чего ты там бормочешь?"
        scene desatka
        r2 "Перед домом войта."
        r2 "Он привез какого-то дракона на продажу, этакую помесь паука с крокодилом."
        r2 "Люди болтали, будто он ведьмак."
        scene kivril
        r3 "Что такое ведьмак?"
        scene tavik
        r4 "Наемный колдун. Фокусник."
        r4 "Фокусы кажет за горсть сребреников."
        r4 "Я же сказал – шутка природы."
        r4 "Оскорбление человеческих и божеских законов. "
        r4 "Таких надобно сжигать."
        scene desatka
        r2 "Мы не очень обожаем колдунов."
        r2 "Что-то мне сдается, что в тутошней дыре у нас будет работы поболее, чем думалось."
        r2 "Их здесь не один, а ведомо, они держатся разом."
        scene kivril
        r3 "Свояк свояка видит издалека."
        "Зловеще усмехнулся полуэльф."
        r3 "И как только земля таких носит?"
        r3 "Кто вас плодит, уродцев?"
        scene geraltandren
        with dissolve
        g "Будь добр, повежливее."
        scene geraltandren2
        with dissolve
        "Спокойно ответил Геральт."
        scene geraltandren3
        with dissolve
        ren "Что здесь происходит, черт побери?!"
        ren "Нельзя на минуту одних оставить?"
        show renindoor:
            xanchor 0 yanchor 0
            xpos -350 ypos -300
            linear 3.0 xpos -350 ypos 0
    
        "Геральт очень медленно обернулся и встретился взглядом с глазами цвета морской волны."
        "Она была почти одного с ним роста."
        "Соломенные волосы были подстрижены неровно, немного ниже ушей."
        "Она стояла в облегающем бархатном кафтанчике, перетянутом нарядным поясом."
        "Юбка была неровной, асимметричной – с левой стороны доходила до лодыжки, а с правой приоткрывала крепкое бедро над голенищем высокого сапога из лосиной кожи."
        "На левом боку висел меч, на правом – кинжал с большим рубином в оголовье."
        scene renindoor2
        with dissolve
        ren "Онемели?"
        scene renindoor4
        r1 "Это ведьмак."
        scene renindoor2
        ren "Ну и что?"
        scene renindoor4
        r1 "Он хочет поговорить с тобой."
        scene renindoor2
        ren "Ну и что?"
        ren "Спокойно, парни. Он хочет со мной поговорить, это не преступление."
        ren "Продолжайте свои дела. И без скандалов. "
        ren "Завтра торговый день. Думаю, вы не хотите, чтобы ваши фокусы испортили ярмарку – столь важное событие в жизни этого милого городка?"
        scene kivril
        show twin1:
            xalign 1.0
            yalign 1.0
        show twin2:
            xalign 0.75
            yalign 1.0
        r3 "Да ну тебя, Ренфри."
        r3 "Важное... событие!"
        scene twins2
        with dissolve
        scene twins
        with dissolve
        scene renindoor3
        ren "Заткнись, Киврил!"
        ren "Немедленно."
        scene room
        "Киврил перестал смеяться."
        "Немедленно."
        "Геральт не удивился."
        "В голосе Ренфри прозвучало нечто очень странное."
        "Нечто такое, что ассоциировалось с красным отблеском пожара на клинках, стонами убиваемых, ржанием коней и запахом крови."
        "Видимо, у остальных тоже возникли подобные ассоциации."
        scene renindoor5
        show geralt1:
            xalign 0.0
            yalign 1.0
        ren "Ну, белоголовый, выйдем в большую залу, присоединимся к войту, с которым ты сюда пришел."
        ren "Он, верно, тоже хочет со мной потолковать."
        scene intavern
        show kaldhandstalk:
            xalign 0.75
            yalign 1.0
        show table
        stop music

        play music "tavernmusic.mp3"
        "Кальдемейн, ожидавший у стойки, увидев их, прервал тихую беседу с трактирщиком, выпрямился, скрестил руки на груди."
        hide kaldhandstalk
        show kaldhandstalk:
            xalign 0.75
            yalign 1.0
        show geralt:
            xalign 0.5
            yalign 1.0
        show renmolch:
            xalign 0.25
            yalign 1.0
        hide table
        show table
        v "Послушайте, мазель."
        "Твердо сказан он, не тратя времени на обмен ненужными учтивостями."
        v "Я знаю от этого вот ведьмака из Ривии, что привело вас в Блавикен. "
        v "Похоже, вы в обиде на нашего колдуна."
        hide kaldhandstalk
        show kaldshoutmolch:
            xalign 0.75
            yalign 1.0
        hide renmolch
        show ren:
            xalign 0.25
            yalign 1.0
        hide table
        show table
        ren "Возможно. Ну и что?"
        hide kaldshoutmolch
        show kaldhandstalk:
            xalign 0.75
            yalign 1.0
        hide ren
        show renmolch:
            xalign 0.25
            yalign 1.0
        hide table
        show table
        v "А то, что на такие обиды есть городские или кастелянские суды."
        v "Кто у нас на Лукоморье, собирается мстить за обиду железом, тот считается самым обыкновенным разбойником."
        v "А еще то, что либо завтра поутру вы вымететесь из Блавикена вместе со своей черной компашкой, либо я вас упрячу в яму, пре..."
        v "Как это называется, Геральт?"
        hide kaldhandstalk
        show kaldshoutmolch:
            xalign 0.75
            yalign 1.0
        hide geralt
        show geralttalk:
            xalign 0.5
            yalign 1.0
        hide table
        show table
        g "Превентивно."
        hide kaldshoutmolch
        show kaldhandstalk:
            xalign 0.75
            yalign 1.0
        hide geralttalk
        show geralt:
            xalign 0.5
            yalign 1.0
        hide table
        show table
        v "Именно."
        v "Вы поняли, мазель?"
        hide kaldhandstalk
        show kaldshoutmolch:
            xalign 0.75
            yalign 1.0
        hide renmolch
        show rensheet:
            xalign 0.25
            yalign 1.0
        hide table
        show table
        "Ренфри сунула руку в мешочек на поясе, достала сложенный в несколько раз пергамент."
        hide rensheet
        show rensheettalk:
            xalign 0.25
            yalign 1.0
        hide table
        show table
        ren "Прочтите, войт, если грамотный. И больше не называйте меня мазелью."
        hide rensheettalk
        show renmolch:
            xalign 0.25
            yalign 1.0
        hide kaldshoutmolch
        show kaldread:
            xalign 0.75
            yalign 1.0
        hide table
        show table
        "Кальдемейн взял пергамент."
        hide kaldread
        show kaldread2:
            xalign 0.75
            yalign 1.0
        hide table
        show table
        "Читал долго."
        hide kaldread2
        show kaldturn:
            xalign 0.75
            yalign 1.0
        hide geralt
        show geraltsheet2:
            xalign 0.5
            yalign 1.0
        hide table
        show table
        "Потом молча подал Геральту."
        scene sheet
        g "«Моим комесам, вассалам и свободным подданным..."
        g "Всех и каждого извещаю, поелику Ренфри, крейденская княжна, пребывает на нашей службе и мила нам... "
        g "То гнев наш падает на голову тому, кто ей чинить припятствия вознамерится. Аудоен, король...»"
        g "Слово «препятствия» пишется через «е». "
        g "Но печать, похоже, подлинная."
        scene intavern
        show geralt:
            xalign 0.5
            yalign 1.0
        show rensheettalk:
            xalign 0.25
            yalign 1.0
        
        show kaldturn:
            xalign 0.75
            yalign 1.0
        
        hide table
        show table
        ren "Потому что подлинная и есть."
        hide rensheettalk
        show ren:
            xalign 0.25
            yalign 1.0
        hide table
        show table
        ren "Поставил ее Аудоен, ваш милостивый государь. "
        ren "Потому не советую чинить мне препятствия."
        ren "Независимо от того, как это пишется, последствия для вас могут быть печальными."
        ren "Не удастся вам, уважаемый войт, упрятать меня в яму.  "
        ren "И не называйте меня мазелью. Я не нарушила ни одного закона."
        ren "Пока что."
        hide ren
        show renmolch:
            xalign 0.25
            yalign 1.0
        hide kaldturn
        show kaldshout:
            xalign 0.75
            yalign 1.0
        hide table
        show table
        v "Если нарушишь хоть на пядь."
        "Кальдемейн выглядел так, словно собирался сплюнуть."
        v "Брошу в яму разом с твоим пергаментом. Клянусь всеми богами, мазель."
        v "Пошли, Геральт."
        hide renmolch
        show ren:
            xalign 0.25
            yalign 1.0
        hide kaldshout
        show kaldturn:
            xalign 0.75
            yalign 1.0
        hide table
        show table
        ren "А с тобой, ведьмак, еще пару слов."
        hide kaldturn
        hide ren
        show renmolch:
            xalign 0.25
            yalign 1.0
        hide kaldshout
        hide table
        show table
        v "Не опоздай на ужин."
        "Бросил войт через плечо."
        hide table
        hide geralt
        show rentalk
        show geralt3
        stop music

        play music "renfri.mp3"
        g "Не опоздаю."
        hide rentalk
        show rentalk2
        show geralt2
        hide geralt3
    
        ren "Я слышала о тебе."
        ren "Ты – Геральт из Ривии, белоголовый ведьмак."
        ren "Стрегобор – твой друг?"
        hide rentalk2
        show rentalk
        show geralt3
        hide geralt2
        g "Нет."
        hide rentalk
        show rentalk4
        show geralt2
        hide geralt3
        ren "Это упрощает дело."
        hide rentalk4
        show rentalk
        show geralt3
        hide geralt2
        g "Не думаю. Я не намерен оставаться в стороне."
        hide rentalk
        show rentalk3
        show geralt2
        hide geralt3
        ren "Стрегобор завтра умрет."
        "Проговорила она тихо, отбрасывая со лба прядку неровно подстриженных волос."
        ren "Зло было бы меньше, если б умер только он."
        hide rentalk3
        show rentalk
        show geralt3
        hide geralt2
        g "Если, а вернее, прежде чем Стрегобор умрет, умрут еще несколько человек."
        g "Другой возможности я не вижу."
        hide rentalk
        show rentalk2
        show geralt2
        hide geralt3
        ren "Скромно сказано – несколько."
        hide rentalk2
        show rentalk
        show geralt3
        hide geralt2
        g "Чтоб меня напугать, требуется нечто большее, чем слова, Сорокопутка."
        hide rentalk
        show rentalk4
        show geralt2
        hide geralt3
        ren "Не называй меня Сорокопуткой, не люблю."
        ren "Дело в том, что я вижу другие возможности. Стоило бы их обсудить."
        hide rentalk4
        show rentalk
        show geralt3
        hide geralt2
        g "Это все, что ты имела мне сказать?"
        hide rentalk
        show rentalk2
        show geralt2
        hide geralt3
        ren "Нет. Но теперь иди."
        hide rentalk2
        show rentalk
        show geralt3
        hide geralt2
        show grey
        with dissolve
        menu:
            
            "Убить":
                jump choice_kill

            "Подождать следующей встречи":
                jump choice_killafter

        label choice_kill:

            $ menu_flag = True

        
            hide grey
            with dissolve 
            g "А я думаю, да."

    
            scene kill
            stop music
            play sound "knife.mp3"
            "После этой фразы Геральт в ту же секунду достает из-за голени свой кинжал и пронзает сердце Ренфри. "
            "Сорокопутка издала свой последний всхлип. "
            scene black
            with fade
            play music "fight.mp3"
            "Услышав это, головорезы подоспели на источник звука."
            "Пока банда пыталась понять, что к чему, Геральт, не мешкаясь, напал на них."
            "Началась бойня, и как любая потасовка, она не обошлась без невинных жертв."
            stop music
            "Спустя некоторое время стражники прибежали на место преступления."
            scene geraltwithsword
            with fade
            "Но было уже поздно, посреди трактира стоял окровавленный Геральт, окруженный телами."
            scene black
            with fade
            n "Обед!"
            scene jail
            show geraltjailsleep:
                xalign 0.0
                yalign 1.0
            show cross
            show guardkashamolch:
                xalign 1.0
                yalign 1.0
            play music "jail.mp3"
            "Через ржавую решетку Носикамень протянул тарелку с непонятной кашеобразной субстанцией."
            hide geraltjailsleep
            show geraltjail:
                xalign 0.0
                yalign 1.0
            hide cross
            show cross
            hide guardkashamolch
            show guardkasha:
                xalign 1.0
                yalign 1.0
            n "Не надо смотреть на это с отвращением, это твоя последняя трапеза."
            hide cross
            show cross
            hide guardkasha
            show guardwatch:
                xalign 1.0
                yalign 1.0
            play sound "kolokol.mp3"
            "И в этот момент прозвенел колокол."
            hide cross
            show cross
            hide guardwatch
            show guardtalk2:
                xalign 1.0
                yalign 1.0
            n "Слышишь колокол?"
            n "Тебе таких осталось 12, а потом будешь висеть на шибенице!"

            jump choice1_done
        

        label choice_killafter:

            $ menu_flag = False
            stop music
            scene door3light
            show geraltlight:
                xalign 0.5
                yalign 1.0
            "В его каморке на мансарде кто-то был."
            "Геральт знал об этом еще прежде, чем подошел к двери, и понял по едва ощутимой вибрации медальона."
            scene door3
            show geraltwithoutlight:
                xalign 0.5
                yalign 1.0
            "Он задул каганец, которым освещал себе ступени, вынул кинжал из-за голенища, сунул его сзади за пояс."
            scene door4
            with dissolve
            "Приоткрыл дверь"
            scene black
            with fade
            "Он, умышленно не торопясь, как бы сонно, переступил порог, прикрыл за собой дверь."
            play audio "fall.mp3"
            "В следующий момент, сильно оттолкнувшись, прыгнул ласточкой, навалился на человека, сидевшего на его лежанке."
            scene dushit
            "Прижал того к постели, левое предплечье сунул ему под подбородок, потянулся за кинжалом."
            "Но не вынул. Что-то было не так. "
            scene dushitmolch
            with dissolve
            ren "Недурно для начала."
            "Глухо проговорила Ренфри, неподвижно лежа под ним."
            ren "Я рассчитывала на это, но не думала, что мы так скоро окажемся в постели. "
            ren "Убери руки с моего горла, будь любезен."
            scene dushittalk
            with dissolve
            g "Это ты?"
            scene dushitmolch
            with dissolve
            ren "Это я."
            ren "Слушай, есть два выхода. "
            ren "Первый: ты слезешь с меня, и мы побеседуем."
            ren "Второй: все остается как есть, но хотелось бы все же скинуть сапоги. "
            ren "Как минимум."
            scene dushitdolban
            with dissolve
            g "Есть и третий: я тебя просто убью."
            scene nedushit
            with dissolve
            "Геральт потянулся за кинжалом, ослабив хват."

            scene black
            with fade
            play audio "drop.mp3"
            "Ренфри воспользовалась моментом и столкнула его с себя."
            "Она хотела убежать, но ведьмак оказался быстрее."
            "Геральт, лежавший секунду ранее, уже загораживал дверной проем."
            scene kill2
            play sound "knife.mp3"
            "Сорокопутка, не успев среагировать, почувствовала острую боль в груди."
            "Это был кинжал, воткнутый прямо ей в сердце."

            show nowindow with dissolve:
                "nowindow.jpg"
                xalign 0.0
                yalign 1.0
                pause 2.0
                "window.jpg" with dissolve
            
            "Смотря на бездыханное тело девушки, ривиец не придумал ничего лучше, чем сбежать из города, оставив все как есть. "
            scene black
            with fade
            "Прошел месяц."
            scene tavern2
            "Геральт, проезжая мимо Блавикена, решил повидаться со своим старым другом."
            "Ведьмак остановился в трактире. "
            scene intavern
            show geralt1:
                xalign 0.5
                yalign 1.0
            show table2
            "Заказав выпивку, он поинтересовался у Сотника про войта."
            hide geralt1
            hide table2
            show geraltushandstalk:
                xalign 0.5
                yalign 1.0
            show table2
            g "Что-то я не видел Кальдемейна на площади."
            g "Что с ним?"
            hide geraltushandstalk
            hide table2
            show geraltushands:
                xalign 0.5
                yalign 1.0
            show table2
            t "Так убили его! "
            hide geraltushands
            hide table2
            show geraltangrytalk:
                xalign 0.5
                yalign 1.0
            show table2
            g "Кто?!"
            hide geraltangrytalk
            hide table2
            show geraltus:
                xalign 0.5
                yalign 1.0
            show table2
            t "Да были тут какие-то головорезы, с бабой во главе."
            t "Она как раз и была найдена мертвой в доме у войта. "
            t "Ну вот отморозки решили, что это Кальдемейн убил ее."
            t "А дальше ты догадываешься, что произошло."
            hide geraltus
            hide table2
            show geralt1:
                xalign 0.5
                yalign 1.0
            show table2
            g "..."
            scene table3
            with dissolve
            "Геральт, не допив свое пойло, положил пару крон на стол и молча вышел из трактира."
            jump choice1_done
    label choice1_done:
            $ renpy.movie_cutscene("titri6.webm", delay=30, loops=0, stop_music=True)
            return
    jump choice1_done

    label choice1_no:

        $ menu_flag = False
        hide grey
        hide stregobortalk
        show stregobor1:
            xalign 1.0
            yalign 1.0
        hide geralt
        show geralttalk:
            xalign 0.0
            yalign 1.0
        g "Я не наемный убийца, Стрегобор."
        hide stregobor1
        show stregobortalk:
            xalign 1.0
            yalign 1.0
        hide geralttalk
        show geralt:
            xalign 0.0
            yalign 1.0
        s "Согласен, ты не убийца."
        hide stregobortalk
        show stregobor1:
            xalign 1.0
            yalign 1.0
        hide geralt
        show geralthandstalk:
            xalign 0.0
            yalign 1.0
        g "За деньги я истребляю чудовищ."
        g "Бестий, угрожающих людям."
        g "Кошмариков и страховидл, созданных чарами и заклинаниями таких типов, как ты."
        g "Но не людей."
        hide stregobor1
        show stregobortalk:
            xalign 1.0
            yalign 1.0
        hide geralthandstalk
        show geralthands:
            xalign 0.0
            yalign 1.0
        s "Она не человек."
        s "Она – чудовище."
        s "Ты привез кикимору."
        s "Сорокопутка хуже кикиморы."
        s "Кикимора убивает от голода, а Сорокопутка удовольствия ради."
        s "Убей ее, и я заплачу столько, сколько ты пожелаешь."
        s "Я прошу тебя, Геральт."
        hide stregobortalk
        show stregobor1:
            xalign 1.0
            yalign 1.0
        hide geralt
        show geralthandstalk:
            xalign 0.0
            yalign 1.0
        g "Нет, Стрегобор."
        hide stregobor1
        show stregobortalk:
            xalign 1.0
            yalign 1.0
        hide geralthandstalk
        show geralthands:
            xalign 0.0
            yalign 1.0
        s "Геральт, когда мы слушали Эльтибальда, у многих из нас возникли сомнения."
        s "Но мы решили выбрать меньшее зло."
        s "Теперь я прошу тебя о том же."
        hide stregobortalk
        show stregobor1:
            xalign 1.0
            yalign 1.0
        hide geralt
        show geralthandstalk:
            xalign 0.0
            yalign 1.0
        g "Зло – это зло, Стрегобор."
        g "Меньшее, большее, среднее – все едино, пропорции условны, а границы размыты."
        g "Я не святой отшельник, не только одно добро творил в жизни."
        g "Но если приходится выбирать меду одним злом и другим, я предпочитаю не выбирать вообще."
        hide geralthandstalk
        show geralttalk:
            xalign 0.0
            yalign 1.0
        g "Мне пора."
        g "Увидимся завтра."
        hide stregobor1
        show stregobortalk:
            xalign 1.0
            yalign 1.0
        hide geralthandstalk
        show geralthands:
            xalign 0.0
            yalign 1.0
        s "Возможно."
        s "Если успеешь."
        scene tavern
        with dissolve
        stop music

        play music "tavernmusic.mp3"
        "На следующий день Геральт вместе с Кальдемейном отправились в таверну «Золотой двор»."
        scene intavern
        show geralt1:
            xalign 0.25
            yalign 1.0
        show kaldustalk:
            xalign 0.75
            yalign 1.0
        show table:
            xalign 0.0
            yalign 0.25
        v "Напряги память, Сотник."
        v "Шесть парней и девка, одетые в черные, украшенные серебром, кожей по новиградской моде."
        v "Я видел их на заставе."
        v "Они остановились у тебя или «Под Альбакаром»."
        hide geralt1
        show geraltus:
            xalign 0.25
            yalign 1.0
        hide kaldustalk
        show kaldusmolch:
            xalign 0.75
            yalign 1.0
        hide table
        show table:
            xalign 0.0
            yalign 0.25

        t "Здесь они, войт."
        t "Говорят, приехали на ярмарку, а все при мечах, даже девка."
        hide kaldusmolch
        show kaldushandstalk:
            xalign 0.75
            yalign 1.0
        hide table
        show table:
            xalign 0.0
            yalign 0.25

        v "Угу. Где они сейчас? "
        v "Что-то их не видно."
        hide kaldushandstalk
        show kaldshoutmolch:
            xalign 0.75
            yalign 1.0
        hide table
        show table:
            xalign 0.0
            yalign 0.25

        t "В маленьком закутке. Золотом платили."
        hide geraltus
        show geraltustalk:
            xalign 0.25
            yalign 1.0
        hide table
        show table:
            xalign 0.0
            yalign 0.25
        g "Схожу один."
        g "Не надо превращать это в официальное посещение, во всяком случае, пока."
        g "Приведу ее сюда."
        hide geraltustalk
        show geraltus:
            xalign 0.25
            yalign 1.0
        hide kaldshoutmolch
        show kaldushandstalk:
            xalign 0.75
            yalign 1.0
        hide table
        show table:
            xalign 0.0
            yalign 0.25
        v "Может, и верно."
        v "Но поосторожней. Мне тут драки ни к чему."
        hide geralt
        show geralttalk:
            xalign 0.25
            yalign 1.0
        hide kaldushandstalk
        show kaldshoutmolch:
            xalign 0.75
            yalign 1.0
        hide table
        show table:
            xalign 0.0
            yalign 0.25
        g "Посмотрим."
        scene room
        with dissolve
        stop music

        play music "badboys.mp3"
        "За столом сидели шестеро мужчин. "
        "Той, которую он ожидал увидеть, среди них не было."
        scene nogorn
        r1 "Ну чего!?!"
        "Рявкнул тот, который заметил его первым."
        g "Хочу увидеться с Сорокопуткой."
        scene twins
        with dissolve
        scene twins2
        with dissolve
        scene door2
        show geraltus:
            xalign 0.25
            yalign 1.0
        show twin1:
            xalign 1.0
            yalign 1.0
        show twin2:
            xalign 0.75
            yalign 1.0
        "От стола поднялись две одинаковые фигуры."
        scene nogorn2
        r1 "Спокойно, парни."
        r1 "С кем, говоришь, хочешь встретиться, братец?"
        r1 "Кто такая Сорокопутка?"
        scene desatka
        r2 "Что за тип? Ты его знаешь?"
        scene nogorn2
        r1 "Нет."
        scene kivril
        r3 "Альбинос какой-то."
        r3 "И надо же, впускают таких в шинки к порядочным людям."
        scene tavik
        r4 "Я его где-то уже видел."
        scene nogorn2
        r1 "Не важно, где ты его видел."
        r1 "Послушай, братец, мой друг только што тебя страшно обидел."
        r1 "Ты его не вызовешь? Такой скушный вечер!"
        scene door2
        show geraltustalk:
            xalign 0.25
            yalign 1.0
        show twin1:
            xalign 1.0
            yalign 1.0
        show twin2:
            xalign 0.75
            yalign 1.0
        g "Нет, не вызову."
        "Спокойно сказал ведьмак."
        scene desatka
        r2 "А меня, если вылью на тебя эту рыбную похлебку?"
        scene nogorn2
        r1 "Спокойно!"
        r1 "Раз он сказал нет, значит нет. "
        r1 "Пока."
        r1 "Ну, брат, говори, што хочешь сказать, и выматывайся. "
        r1 "Имеешь возможность выйти сам."
        r1 "Если не воспользуешься, тебя вынесут половые."
        scene door2
        show geraltushandstalk:
            xalign 0.25
            yalign 1.0
        show twin1:
            xalign 1.0
            yalign 1.0
        show twin2:
            xalign 0.75
            yalign 1.0
        g "Тебе мне сказать нечего."
        g "Хочу увидеться с Сорокопуткой."
        g "С Ренфри."
        scene nogorn2
        r1 "Слышали, парни? Он хочет видеться с Ренфри. "
        r1 "А зачем, братец, позволь узнать?"
        scene door2
        show geraltushandstalk:
            xalign 0.25
            yalign 1.0
        show twin1:
            xalign 1.0
            yalign 1.0
        show twin2:
            xalign 0.75
            yalign 1.0
        g "Не позволю."
        scene nogorn2
        "Ногорн поднял голову и глянул на близнецов."
        scene door2
        show geraltus:
            xalign 0.25
            yalign 1.0
        show twin1:
            xalign 0.75
            yalign 1.0
        show twin2:
            xalign 0.5
            yalign 1.0
        "Те тут же сделали шаг вперед, бренча серебряными застежками высоких ботинок."
        scene tavik
        r4 "Знаю! Вспомнил, где я его видел!"
        scene nogorn2
        r1 "Чего ты там бормочешь?"
        scene desatka
        r2 "Перед домом войта."
        r2 "Он привез какого-то дракона на продажу, этакую помесь паука с крокодилом."
        r2 "Люди болтали, будто он ведьмак."
        scene kivril
        r3 "Что такое ведьмак?"
        scene tavik
        r4 "Наемный колдун. Фокусник."
        r4 "Фокусы кажет за горсть сребреников."
        r4 "Я же сказал – шутка природы."
        r4 "Оскорбление человеческих и божеских законов. "
        r4 "Таких надобно сжигать."
        scene desatka
        r2 "Мы не очень обожаем колдунов."
        r2 "Что-то мне сдается, что в тутошней дыре у нас будет работы поболее, чем думалось."
        r2 "Их здесь не один, а ведомо, они держатся разом."
        scene kivril
        r3 "Свояк свояка видит издалека."
        "Зловеще усмехнулся полуэльф."
        r3 "И как только земля таких носит?"
        r3 "Кто вас плодит, уродцев?"
        scene geraltandren
        with dissolve
        g "Будь добр, повежливее."
        scene geraltandren2
        with dissolve
        "Спокойно ответил Геральт."
        scene geraltandren3
        with dissolve
        ren "Что здесь происходит, черт побери?!"
        ren "Нельзя на минуту одних оставить?"
        show renindoor:
            xanchor 0 yanchor 0
            xpos -350 ypos -300
            linear 3.0 xpos -350 ypos 0
    
        "Геральт очень медленно обернулся и встретился взглядом с глазами цвета морской волны."
        "Она была почти одного с ним роста."
        "Соломенные волосы были подстрижены неровно, немного ниже ушей."
        "Она стояла в облегающем бархатном кафтанчике, перетянутом нарядным поясом."
        "Юбка была неровной, асимметричной – с левой стороны доходила до лодыжки, а с правой приоткрывала крепкое бедро над голенищем высокого сапога из лосиной кожи."
        "На левом боку висел меч, на правом – кинжал с большим рубином в оголовье."
        scene renindoor2
        with dissolve
        ren "Онемели?"
        scene renindoor4
        r1 "Это ведьмак."
        scene renindoor2
        ren "Ну и что?"
        scene renindoor4
        r1 "Он хочет поговорить с тобой."
        scene renindoor2
        ren "Ну и что?"
        ren "Спокойно, парни. Он хочет со мной поговорить, это не преступление."
        ren "Продолжайте свои дела. И без скандалов. "
        ren "Завтра торговый день. Думаю, вы не хотите, чтобы ваши фокусы испортили ярмарку – столь важное событие в жизни этого милого городка?"
        scene kivril
        show twin1:
            xalign 1.0
            yalign 1.0
        show twin2:
            xalign 0.75
            yalign 1.0
        r3 "Да ну тебя, Ренфри."
        r3 "Важное... событие!"
        scene twins2
        with dissolve
        scene twins
        with dissolve
        scene renindoor3
        ren "Заткнись, Киврил!"
        ren "Немедленно."
        scene room
        "Киврил перестал смеяться."
        "Немедленно."
        "Геральт не удивился."
        "В голосе Ренфри прозвучало нечто очень странное."
        "Нечто такое, что ассоциировалось с красным отблеском пожара на клинках, стонами убиваемых, ржанием коней и запахом крови."
        "Видимо, у остальных тоже возникли подобные ассоциации."
        scene renindoor5
        show geralt1:
            xalign 0.0
            yalign 1.0
        ren "Ну, белоголовый, выйдем в большую залу, присоединимся к войту, с которым ты сюда пришел."
        ren "Он, верно, тоже хочет со мной потолковать."
        scene intavern
        show kaldhandstalk:
            xalign 0.75
            yalign 1.0
        show table
        stop music

        play music "tavernmusic.mp3"
        "Кальдемейн, ожидавший у стойки, увидев их, прервал тихую беседу с трактирщиком, выпрямился, скрестил руки на груди."
        hide kaldhandstalk
        show kaldhandstalk:
            xalign 0.75
            yalign 1.0
        show geralt:
            xalign 0.5
            yalign 1.0
        show renmolch:
            xalign 0.25
            yalign 1.0
        hide table
        show table
        v "Послушайте, мазель."
        "Твердо сказан он, не тратя времени на обмен ненужными учтивостями."
        v "Я знаю от этого вот ведьмака из Ривии, что привело вас в Блавикен. "
        v "Похоже, вы в обиде на нашего колдуна."
        hide kaldhandstalk
        show kaldshoutmolch:
            xalign 0.75
            yalign 1.0
        hide renmolch
        show ren:
            xalign 0.25
            yalign 1.0
        hide table
        show table
        ren "Возможно. Ну и что?"
        hide kaldshoutmolch
        show kaldhandstalk:
            xalign 0.75
            yalign 1.0
        hide ren
        show renmolch:
            xalign 0.25
            yalign 1.0
        hide table
        show table
        v "А то, что на такие обиды есть городские или кастелянские суды."
        v "Кто у нас на Лукоморье, собирается мстить за обиду железом, тот считается самым обыкновенным разбойником."
        v "А еще то, что либо завтра поутру вы вымететесь из Блавикена вместе со своей черной компашкой, либо я вас упрячу в яму, пре..."
        v "Как это называется, Геральт?"
        hide kaldhandstalk
        show kaldshoutmolch:
            xalign 0.75
            yalign 1.0
        hide geralt
        show geralttalk:
            xalign 0.5
            yalign 1.0
        hide table
        show table
        g "Превентивно."
        hide kaldshoutmolch
        show kaldhandstalk:
            xalign 0.75
            yalign 1.0
        hide geralttalk
        show geralt:
            xalign 0.5
            yalign 1.0
        hide table
        show table
        v "Именно."
        v "Вы поняли, мазель?"
        hide kaldhandstalk
        show kaldshoutmolch:
            xalign 0.75
            yalign 1.0
        hide renmolch
        show rensheet:
            xalign 0.25
            yalign 1.0
        hide table
        show table
        "Ренфри сунула руку в мешочек на поясе, достала сложенный в несколько раз пергамент."
        hide rensheet
        show rensheettalk:
            xalign 0.25
            yalign 1.0
        hide table
        show table
        ren "Прочтите, войт, если грамотный. И больше не называйте меня мазелью."
        hide rensheettalk
        show renmolch:
            xalign 0.25
            yalign 1.0
        hide kaldshoutmolch
        show kaldread:
            xalign 0.75
            yalign 1.0
        hide table
        show table
        "Кальдемейн взял пергамент."
        hide kaldread
        show kaldread2:
            xalign 0.75
            yalign 1.0
        hide table
        show table
        "Читал долго."
        hide kaldread2
        show kaldturn:
            xalign 0.75
            yalign 1.0
        hide geralt
        show geraltsheet2:
            xalign 0.5
            yalign 1.0
        hide table
        show table
        "Потом молча подал Геральту."
        scene sheet
        g "«Моим комесам, вассалам и свободным подданным..."
        g "Всех и каждого извещаю, поелику Ренфри, крейденская княжна, пребывает на нашей службе и мила нам... "
        g "То гнев наш падает на голову тому, кто ей чинить припятствия вознамерится. Аудоен, король...»"
        g "Слово «препятствия» пишется через «е». "
        g "Но печать, похоже, подлинная."
        scene intavern
        show geralt:
            xalign 0.5
            yalign 1.0
        show rensheettalk:
            xalign 0.25
            yalign 1.0
        
        show kaldturn:
            xalign 0.75
            yalign 1.0
        
        hide table
        show table
        ren "Потому что подлинная и есть."
        hide rensheettalk
        show ren:
            xalign 0.25
            yalign 1.0
        hide table
        show table
        ren "Поставил ее Аудоен, ваш милостивый государь. "
        ren "Потому не советую чинить мне препятствия."
        ren "Независимо от того, как это пишется, последствия для вас могут быть печальными"
        ren "Не удастся вам, уважаемый войт, упрятать меня в яму.  "
        ren "И не называйте меня мазелью. Я не нарушила ни одного закона."
        ren "Пока что."
        hide ren
        show renmolch:
            xalign 0.25
            yalign 1.0
        hide kaldturn
        show kaldshout:
            xalign 0.75
            yalign 1.0
        hide table
        show table
        v "Если нарушишь хоть на пядь."
        "Кальдемейн выглядел так, словно собирался сплюнуть."
        v "Брошу в яму разом с твоим пергаментом. Клянусь всеми богами, мазель."
        v "Пошли, Геральт."
        hide renmolch
        show ren:
            xalign 0.25
            yalign 1.0
        hide kaldshout
        show kaldturn:
            xalign 0.75
            yalign 1.0
        hide table
        show table
        ren "А с тобой, ведьмак, еще пару слов."
        hide kaldturn
        hide ren
        show renmolch:
            xalign 0.25
            yalign 1.0
        hide kaldshout
        hide table
        show table
        v "Не опоздай на ужин."
        "Бросил войт через плечо."
        hide table
        hide geralt
        show rentalk
        show geralt3
        stop music

        play music "renfri.mp3"
        g "Не опоздаю."
        hide rentalk
        show rentalk2
        show geralt2
        hide geralt3
    
        ren "Я слышала о тебе."
        ren "Ты – Геральт из Ривии, белоголовый ведьмак."
        ren "Стрегобор – твой друг?"
        hide rentalk2
        show rentalk
        show geralt3
        hide geralt2
        g "Нет."
        hide rentalk
        show rentalk4
        show geralt2
        hide geralt3
        ren "Это упрощает дело."
        hide rentalk4
        show rentalk
        show geralt3
        hide geralt2
        g "Не думаю. Я не намерен оставаться в стороне."
        hide rentalk
        show rentalk3
        show geralt2
        hide geralt3
        ren "Стрегобор завтра умрет."
        "Проговорила она тихо, отбрасывая со лба прядку неровно подстриженных волос."
        ren "Зло было бы меньше, если б умер только он."
        hide rentalk3
        show rentalk
        show geralt3
        hide geralt2
        g "Если, а вернее, прежде чем Стрегобор умрет, умрут еще несколько человек."
        g "Другой возможности я не вижу."
        hide rentalk
        show rentalk2
        show geralt2
        hide geralt3
        ren "Скромно сказано – несколько."
        hide rentalk2
        show rentalk
        show geralt3
        hide geralt2
        g "Чтоб меня напугать, требуется нечто большее, чем слова, Сорокопутка."
        hide rentalk
        show rentalk4
        show geralt2
        hide geralt3
        ren "Не называй меня Сорокопуткой, не люблю."
        ren "Дело в том, что я вижу другие возможности. Стоило бы их обсудить."
        hide rentalk4
        show rentalk
        show geralt3
        hide geralt2
        g "Это все, что ты имела мне сказать?"
        hide rentalk
        show rentalk2
        show geralt2
        hide geralt3
        ren "Нет. Но теперь иди."
        stop music
        scene door3light
        show geraltlight:
            xalign 0.5
            yalign 1.0
        "В его каморке на мансарде кто-то был."
        "Геральт знал об этом еще прежде, чем подошел к двери, и понял по едва ощутимой вибрации медальона."
        scene door3
        show geraltwithoutlight:
            xalign 0.5
            yalign 1.0
        "Он задул каганец, которым освещал себе ступени, вынул кинжал из-за голенища, сунул его сзади за пояс."
        scene door4
        with dissolve
        "Приоткрыл дверь"
        scene black
        with fade
        "Он, умышленно не торопясь, как бы сонно, переступил порог, прикрыл за собой дверь."
        play audio "fall.mp3"
        "В следующий момент, сильно оттолкнувшись, прыгнул ласточкой, навалился на человека, сидевшего на его лежанке."
        scene dushit
        "Прижал того к постели, левое предплечье сунул ему под подбородок, потянулся за кинжалом."
        "Но не вынул. Что-то было не так. "
        scene dushitmolch
        with dissolve
        ren "Недурно для начала."
        "Глухо проговорила Ренфри, неподвижно лежа под ним."
        ren "Я рассчитывала на это, но не думала, что мы так скоро окажемся в постели. "
        ren "Убери руки с моего горла, будь любезен."
        scene dushittalk
        with dissolve
        g "Это ты?"
        scene dushitmolch
        with dissolve
        ren "Это я."
        ren "Слушай, есть два выхода. "
        ren "Первый: ты слезешь с меня, и мы побеседуем."
        ren "Второй: все остается как есть, но хотелось бы все же скинуть сапоги. "
        ren "Как минимум."
        "Ведьмак выбрал первый выход."
        scene yubka
        with dissolve
        "Девушка вздохнула, встала, поправила волосы и юбку."
        scene room2
        show geraltsit
        show rensit
        show table4
        play music "romantic.mp3"
        "Она подошла к столу, высокая, худощавая, гибкая, села, вытянув ноги в сапогах."
        "Оружия вроде бы у нее не было."
        hide geraltsit
        hide rensit
        hide table4
        show geraltsit2
        show rensittalk
        show table4
        ren "Выпить есть?"
        hide geraltsit2
        hide rensittalk
        hide table4
        show geraltsittalk
        show rensit
        show table4
        g "Нет."
        hide geraltsittalk
        hide rensit
        hide table4
        show geraltsit3
        show rensitbottle
        show table4
        ren "В таком случае хорошо, что я прихватила."
        hide rensitbottle
        hide table4
        hide geraltsit3
        play audio "wine.mp3"
        show geraltsittalk2
        show rendrink
        with dissolve
        g "Почти полночь."
        hide geraltsittalk2
        hide rendrink
        show geraltsit3
        show rendrink

        "Холодно сказал Геральт."
        hide geraltsit3
        hide rendrink
        show geraltsittalk2
        show rendrink

        g "Может, перейдем к делу?"
        hide rendrink
        # show rendrink2
        # with dissolve
        play audio "wine.mp3"
        hide geraltsittalk2
        show geraltsit3
        show rendrink3:
            "rendrink.png"
            pause 0.25
            "rendrink2.png" with dissolve
            pause 1.0
            "rendrink3.png" with dissolve

        ren "Минутку."
        hide geraltsit3
        show geraltsit
        hide rendrink3
        show rendrink4
        with dissolve
        ren "Пей."
        scene buhaut
        with dissolve
        ren "Твое здоровье, Геральт."
        scene buhaut2
        with dissolve
        g "Взаимно, Сорокопутка!"
        scene buhautzloy

        ren "Меня зовут Ренфри, черт побери."
        ren "Разрешаю упускать княжий титул, но перестань именовать меня Сорокопуткой."
        scene room2
        show geraltsitdrink2
        show rensitdrink2
        show table5
        g "Тише, разбудишь весь дом."
        hide rensitdrink2
        show renbuhaet:
            "rensitdrink2.png"
            pause 0.5
            "renbuhaet.png" with dissolve
        hide rensitdrink2
        hide table5
        show table5
        g "Могу я наконец узнать, чего ради ты влезла сюда через окно?"
        hide geraltsitdrink2
        show rensitdrink3:
            "renbuhaet.png"
            pause 0.5
            "rensitdrink3.png" with dissolve
        hide renbuhaet
        hide table5
        show geraltsitdrink3
        show table5
        ren "Какой догадливый!"
        show geraltbuhaet:
            "geraltsitdrink3.png"
            pause 0.5
            "geraltbuhaet.png" with dissolve
        hide geraltsitdrink3
        hide table5
        show table5
        ren "Я хочу спасти Блавикен от резни. "
        
        show geraltsitdrink3:
            "geraltbuhaet.png"
            pause 0.5
            "geraltsitdrink3.png" with dissolve
        hide geraltbuhaet
        hide table5
        show table5
        ren "Чтобы обсудить это с тобой, я лазила по крышам, словно мартовский кот."
        show geraltsit3:
            "geraltsitdrink3.png"
            pause 0.1
            "geraltsit3.png" with dissolve
        hide geraltsitdrink3
        hide table6
        show table6
        ren "Цени."
        hide rensitdrink3
        hide geraltsit3
        show geraltsittalk2
        show rensitdrink4
        hide table6
        show table6
        g "Ценю."
        g "Только вот не знаю, какой смысл в таком разговоре."
        g "Положение ясное."
        show renbuhaet:
            "rensitdrink4.png"
            pause 0.5
            "renbuhaet.png" with dissolve
        hide rensitdrink4
        hide table6
        show table6
        g "Стрегобор сидит в колдовской башне, чтобы его достать, тебе придется организовать осаду."
        show rensitdrink2:
            "renbuhaet.png"
            pause 0.5
            "rensitdrink2.png" with dissolve
        hide renbuhaet
        hide table6
        show table6
        g "Если ты в открытую нарушишь закон, Аудоен не станет тебя защищать. "
        g "Войт, стража, весь Блавикен выступят против тебя."
        hide geraltsittalk2
        hide rensitdrink2
        hide table6
        show geraltsit3
        show rensitdrink3
        show table6
        ren "Если выступит весь Блавикен, то жутко пожалеет."
        "Ренфри усмехнулась, показав хищные белые зубки."
        ren "Ты разглядел моих мальчиков?"
        ren "Ручаюсь, они свое дело знают."
        ren "Представляешь себе, что произойдет, если начнется драка между ними и теми девками из стражи, которые то и дело спотыкаются о собственные алебарды?"
        hide geraltsit3
        hide rensitdrink3
        hide table6
        show geraltsittalk2
        show rensitdrink4
        show table6
        g "А ты, Ренфри, воображаешь, что я буду стоять в стороне и спокойно взирать на такую драку?"

        show renbuhaet:
            "rensitdrink4.png"
            pause 0.5
            "renbuhaet.png" with dissolve
        hide rensitdrink4
        hide table6
        show table6
        g "Видишь, я живу у войта?"
        show rensitdrink2:
            "renbuhaet.png"
            pause 0.5
            "rensitdrink2.png" with dissolve
        hide renbuhaet
        show geraltsittalk2
        hide table6
        show table6
        g "При надобности буду рядом с ним."
        hide geraltsittalk2
        hide rensitdrink2
        hide table6
        show geraltsit3
        show rensitdrink
        show table6
        ren "Не сомневаюсь."
        "Посерьезнела Ренфри. "
        ren "Только скорее всего один ты, потому что остальные попрячутся по подвалам."

        ren "Нет на свете бойца, который управился бы с моей вооруженной мечами семеркой."
        ren "Это не под силу ни одному человеку."
        ren "Но, белоголовый, давай не будем пугать друг друга."
        ren "Я сказала - резни и потоков крови можно избежать."
        ren "Конкретно: есть два человека, которым это под силу."
        hide geraltsit3
        show renbuhaet:
            "rensitdrink.png"
            pause 0.5
            "renbuhaet.png" with dissolve
        hide rensitdrink
        hide table6
        show geraltsittalk2
        show table6
        g "Я – само внимание."
        hide geraltsittalk2
        hide renbuhaet
        show rensitdrink2:
            "renbuhaet.png"
            pause 0.5
            "rensitdrink.png" with dissolve
        hide table6
        show geraltsit3
        show table6
        ren "Один - Стрегобор."
        hide renbuhaet
        show rensitdrink2:
            "rensitdrink.png"
            pause 0.1
            "rensittalk.png" with dissolve
        hide table6
        show table8
        with dissolve
        ren "Лично."
        
        hide table8
        hide rensitdrink2
        show rensittalk:
            "rensittalk.png"
            pause 0.1
            "rennaliv.png" with dissolve
        hide table5
        with dissolve

        ren "Он добровольно выйдет из своей башни, я отведу его куда-нибудь на пустырь."
        hide rensittalk
        show rensitdrink:
            "rennaliv.png"
            pause 0.1
            "rensitdrink.png" with dissolve

        show table6
        with dissolve
        hide table5
        ren "А Блавикен снова погрузится в благостную апатию и вскоре забудет обо всем."
        hide geraltsit3
        show renbuhaet:
            "rensitdrink.png"
            pause 0.5
            "renbuhaet.png" with dissolve
        hide rensitdrink
        hide table6
        show geraltsittalk2
        show table6
        g "Стрегобор, возможно, и похож на спятившего, но не до такой же степени."
        hide geraltsittalk2
        show rensitdrink3:
            "renbuhaet.png"
            pause 0.5
            "rensitdrink3.png" with dissolve
        hide renbuhaet
        hide table6
        show geraltsit3
        show table6
        ren "Как знать, ведьмак, как знать. "
        ren "Есть доводы, которые невозможно отвергнуть, и предложения, которые нельзя отбросить."
        ren "К таким, например, относится тридамский ультиматум. "
        ren "Я предъявлю колдуну тридамский ультиматум."
        hide geraltsit3
        show renbuhaet:
            "rensitdrink3.png"
            pause 0.5
            "renbuhaet.png" with dissolve
        hide rensitdrink3
        hide table6
        show geraltsittalk2
        show table6
        g "В чем его суть?"
        hide geraltsittalk2
        show rensitdrink3:
            "renbuhaet.png"
            pause 0.5
            "rensitdrink3.png" with dissolve
        hide renbuhaet
        hide table6
        show geraltsit3
        show table6
        ren "Это маленькая и сладкая тайна."
        hide geraltsit3
        hide renbuhaet
        show rensit:
            "rensitdrink3.png"
            pause 0.1
            "rensit.png" with dissolve
        hide table6
        hide rensitdrink3
        show geraltsittalk2
        show table8
        with dissolve
        g "Пусть так. "
        g "Только сомневаюсь в ее эффективности."
        g "У Стрегобора, стоит ему заговорить о тебе, начинают зубы стучать. "
        g "Ультиматум, который заставил бы его добровольно отдаться в твои прелестные ручки, должен и вправду быть каким-то особым."
        g "Давай-ка перейдем сразу ко второй особе, которая может предотвратить резню в Блавикене."
        g "Попытаюсь угадать, кто это."
        hide geraltsittalk2
        hide rensit
        hide table8
        show geraltsit3
        show rensittalk
        show table8
        ren "Ну-ну."
        ren "Интересно, насколько ты проницателен, белоголовый."
        hide geraltsit3
        hide rensittalk
        hide table8
        show geraltsittalk2
        show rensit
        show table8
        g "Это ты, Ренфри."
        g "Ты сама. "
        g "Ты проявишь воистину княжеское, да что я - королевское великодушие и откажешься от мести."
        g "Я угадал?"
        hide geraltsittalk2
        hide rensit
        hide table8
        show geraltsit2
        show renangry
        with dissolve
        ren "Геральт, я была княжной, но в Крейдене."
        ren "У меня было все, о чем только можно мечтать, даже просить не было нужды. "
        scene renokno
        with dissolve
        ren "Слуги по первому зову, платья, туфельки."
        ren "Трусики из батиста."
        scene renokno2
        with dissolve
        ren "Драгоценности и бижутерия, буланый пони, золотые рыбки в бассейне."
        ren "Куклы и дом для них повместительнее твоей здешней лачуги."
        show renokno3:
            "renokno2.jpg"
            pause 0.5
            "renokno3" with dissolve
            pause 1.5
            "renokno2.jpg" with dissolve
            pause 1.5
            "renokno4.jpg" with dissolve
        ren "И так было до того дня, пока твой Стрегобор и Аридея не приказали егерю отвести меня в лес, зарезать и подать им мои сердце и печень."
        scene renokno5
        with dissolve
        ren "Прелестно, не правда ли?"
        ren "На том и кончилась княжна."
        ren "Платьице разорвалось. "
        scene renokno4
        with dissolve
        ren "А потом были грязь, голод, вонь, палки и пинки."
        ren "Знаешь, какие у меня были волосы?"
        ren "Как шелк и спадали на добрый локоть ниже икр."
        ren "Когда я завшивела, мне обрезали косы ножницами для стрижки овец под самый корень."
        ren "Больше они так и не отросли по-настоящему."
        scene renokno5
        with dissolve
        ren "Я воровала, чтобы не подохнуть с голоду."
        ren "Убивала, чтобы не убили меня."
        ren "Сидела в ямах, не зная, повесят меня утром или только выпорют и выгонят. "
        ren "И все это время моя мачеха и твой колдун преследовали меня, нанимали убийц, пытались отравить."
        scene renokno4
        with dissolve
        ren "Насылали порчу."
        scene renokno5
        with dissolve
        ren "Проявить великодушие?"
        ren "Простить им по-королевски?"
        scene renokno4
        with dissolve
        ren "Я ему по-королевски башку оторву, а может, сначала вырву обе ноги, там видно будет."
        ren "Стрегобор и Аридея, пока могли, преследовали меня, как дикого зверя."
        ren "Потом уже не могли, я сама стала охотником."
        ren "Аридея откинула копыта в собственной постели."
        ren "Для нее я составила особую программу."
        scene renokno2
        with dissolve
        ren "А теперь - для колдуна."
        show renokno3:
            "renokno2.jpg"
            pause 0.5
            "renokno3" with dissolve
            pause 1.5
            "renokno2.jpg" with dissolve
            pause 1.5
            "renokno4.jpg" with dissolve
        ren "Геральт, как ты считаешь, он заслуживает смерти?"
        ren "Ну скажи."
        scene renokno6
        with dissolve
        g "Я не судья. "
        show renokno7:
            "renokno6.jpg" 
            pause 0.5
            "renokno7.jpg" with dissolve
            pause 0.5
            "renokno3" with dissolve
            pause 1.5
            "renokno7.jpg" with dissolve
        g "Я - ведьмак."
        scene renokno
        with dissolve
        ren "Именно что."
        ren "Я сказала, есть два человека, которые могут предотвратить резню в Блавикене."
        scene renokno2
        with dissolve
        ren "Второй - ты."
        ren "Тебя колдун пустит в башню, и ты его убьешь."
        scene renokno7
        with dissolve
        g "Ренфри."
        "Спокойно сказал Геральт."
        g "По пути ко мне ты, случайно, не свалилась с крыши головой вниз?"
        scene room2
        show geraltsit2
        show renangry
        with dissolve
        ren "В конце концов, ведьмак ты или нет, черт побери?!"
        ren "Говорят, ты убил кикимору, привез ее на ослике для оценки."
        ren "Стрегобор хуже кикиморы, она - бездумная скотина и убивает, потому как такой ее боги сотворили."
        ren "Стрегобор - изверг, маньяк, чудовище. "
        ren "Привези его мне на ослике, и я не пожалею золота."
        hide geraltsit2
        hide renangry
        show geraltsittalk2
        show rensit
        show table8
        with dissolve
        g "Я не наемный убийца, Сорокопутка."
        hide geraltsittalk2
        hide rensit
        hide table8
        show geraltsit2
        show rensittalk2
        show table8
        with dissolve
        ren "Верно."
        "Улыбнулась она."
        hide rensittalk2
        hide table8
        show rensittalk
        show table8
        ren "Ты - ведьмак, спаситель людей, которых защищаешь от Зла."
        ren "А в данном случае Зло - это железо и огонь, которые разгуляются здесь, когда мы встанем друг против друга."
        ren "Тебе не кажется, что я предлагаю Меньшее Зло - самое лучшее решение?"
        ren "Даже для этого сукина сына Стрегобора."
        ren "Можешь убить его милосердно, одним движением, случайно."
        ren "Он умрет, не зная, что умирает."
        ren "А я ему этого не гарантирую."
        ren "Совсем наоборот."
        "Геральт молчал."
        ren "Понимаю твои сомнения."
        ren "Но ответ я должна получить немедленно."
        hide geraltsit2
        hide rensittalk2rensit
        hide table8
        show geraltsittalk2
        show rensit
        show table8
        g "Знаешь, почему Стрегобор и княгиня хотели тебя убить тогда, в Крейдене, и после?"
        hide geraltsittalk2
        hide rensittalk
        hide rensit
        hide table8
        show geraltsit2
        show renangry
        with dissolve
        ren "Думаю, это ясно."
        "Взорвалась она."
        ren "Хотели отделаться от первородной дочери Фредефалька, потому что я была наследницей трона."
        ren "Дети Аридеи родились в результате морганатической связи, и у них не было никаких прав на..."
        hide geraltsit2
        hide renangry
        show geraltsittalk2
        show rensit
        show table8
        with dissolve
        g "Я не о том, Ренфри."
        "Девушка опустила голову, но только на мгновение."
        "Глаза у нее разгорелись."
        hide rensit
        hide table8
        hide geraltsittalk2
        show geraltsit2
        show rensittalk
        show table8
        ren "Ну хорошо."
        ren "Якобы я проклята."
        ren "Испорчена еще в лоне матери."
        ren "Я..."
        hide geraltsit2
        hide rensittalk
        show rensit
        show geraltsittalk2
        hide table8
        show table8
        g "Договаривай."
        hide rensit
        hide table8
        hide geraltsittalk2
        show geraltsit2
        show rensittalk
        show table8
        ren "Я – чудовище."
        hide geraltsit2
        hide rensittalk
        show rensit
        show geraltsittalk2
        hide table8
        show table8
        g "А разве нет?"
        "Какое-то мгновение Ренфри казалась беззащитной и надломленной."
        "И очень грустной."
        hide rensit
        hide table8
        hide geraltsittalk2
        show geraltsit2
        show rensittalk
        show table8
        ren "Не знаю, Геральт."
        "Шепнула она, потом черты ее лица снова ожесточились."
        hide rensittalk
        hide table8
        hide geraltsittalk2
        show geraltsit2
        show renangry
        with dissolve
        ren "Да и откуда мне, черт побери, знать?"
        ren "Если я уколю себе палец, идет кровь."
        ren "Ежемесячно тоже... ну, сам понимаешь."
        ren "Переем - болит живот, а перепью - голова."
        ren "Если мне весело - я пою, если грустно - ругаюсь."
        ren "Если кого-то ненавижу - убиваю, а если..."
        ren "А, дьявольщина, довольно. "
        hide geraltsittalk2
        hide renangry
        show geraltsit2
        show rensittalk
        show table8
        with dissolve
        ren "Твой ответ, ведьмак."
        hide geraltsit2
        hide rensittalk
        show rensit
        show geraltsittalk2
        hide table8
        show table8
        g "Мой ответ таков: нет."
        hide rensit
        hide table8
        hide geraltsittalk2
        show geraltsit2
        show rensittalk
        show table8
        ren "Ты помнишь, о чем я говорила?"
        "Спросила она после недолгого молчания. "
        ren "Есть предложения, которые нельзя отвергнуть, последствия бывают страшными. "
        ren "Я тебя серьезно предостерегаю, мое предложение относится именно к таким."
        ren "Подумай как следует."
        hide geraltsit2
        hide rensittalk
        show rensit
        show geraltsittalk2
        hide table8
        show table8
        g "Я подумал как следует."
        g "И отнесись ко мне серьезно, потому что я тоже предостерегаю тебя серьезно."
        hide rensit
        hide table8
        hide geraltsittalk2
        show geraltsit2
        show rensittalk
        show table8
        ren "Геральт, Стрегобор просил тебя убить меня?"
        hide geraltsit2
        hide rensittalk
        show rensit
        show geraltsittalk2
        hide table8
        show table8
        g "Да."
        g "Он полагал, что это будет Меньшее Зло."
        hide rensit
        hide table8
        hide geraltsittalk2
        show geraltsit2
        show rensittalk
        show table8
        ren "И ты отказал ему так же, как и мне?"
        hide geraltsit2
        hide rensittalk
        show rensit
        show geraltsittalk2
        hide table8
        show table8
        g "Так же."
        hide rensit
        hide table8
        hide geraltsittalk2
        show geraltsit2
        show rensittalk
        show table8
        ren "Почему?"
        hide geraltsit2
        hide rensittalk
        show rensit
        show geraltsittalk3
        hide table8
        show table8
        g "Потому что я не верю в Меньшее зло."
        hide rensit
        hide table8
        hide geraltsittalk3
        show geraltsit2
        show rensitmeh
        show table8
        "Ренфри слабо улыбнулась, затем губы у нее искривились в гримасе, очень некрасивой при желтом свете свечи."
        ren "Видишь ли, ты прав, но только отчасти. "
        ren "Существуют просто Зло и Большое Зло, а за ними обоими в тени прячется Очень Большое Зло."
        ren "Очень Большое Зло, Геральт, это такое, которого ты и представить себе не можешь, даже если думаешь, будто уже ничто не в состоянии тебя удивить. "
        ren "И знаешь, Геральт, порой бывает так, что Очень Большое Зло схватит тебя за горло и скажет: «Выбирай, братец, либо я, либо то, которое чуточку поменьше»."
        hide geraltsit2
        hide rensitmeh
        show rensit
        show geraltsittalk3
        hide table8
        show table8
        g "Можно узнать, куда ты клонишь?"
        hide rensit
        hide table8
        hide geraltsittalk3
        show geraltsit2
        show rensittalk2
        show table8
        ren "А никуда."
        ren "Выпила немного, вот и философствую, ищу общие истины."
        hide rensittalk2
        show rensittalk
        hide table8
        show table8
        ren "Одну как раз нашла: Меньшее Зло существует, но мы не в состоянии выбирать его сами."
        ren "Лишь Очень Большое Зло может принудить нас к такому выбору."
        ren "Хотим мы того или нет."
        hide geraltsit2
        hide rensittalk
        show rensit
        show geraltsittalk4
        hide table8
        show table8
        g "Я явно выпил слишком мало."
        "Ехидно усмехнулся ведьмак."
        hide geraltsittalk4
        show geraltsittalk2
        g "А полночь меж тем уже миновала, как и всякая полночь."
        g "Перейдем к конкретным вопросам."
        g "Ты не убьешь Стрегобора в Блавикене, я тебе не дам."
        g "Не позволю, чтобы дело дошло до бойни и резни."
        g "Вторично предлагаю: откажись от мести."
        g "Откажись от намерения убить его."
        g "Таким образом ты докажешь ему, и не только ему, что ты не кровожадное, нечеловеческое чудовище, мутант и выродок."
        g "Докажешь, что он ошибается."
        g "Что причинил тебе Очень Большое Зло своей ошибкой."
        "Ренфри некоторое время смотрела на медальон ведьмака."
        scene renokno
        with dissolve
        ren "А если я скажу, ведьмак, что не умею прощать или отказываться от мести, то это будет равносильно признанию, что он и не только он правы? "
        ren "Верно?"
        ren "Тем самым я докажу, что я все-таки чудовище, нелюдь, демон, проклятый богами? "
        scene renokno2
        with dissolve
        ren "Послушай, ведьмак."
        ren "В самом начале моих скитаний меня приютил один свободный кмет. "
        ren "Я ему понравилась."
        ren "Однако поскольку мне он вовсе не нравился, а совсем даже наоборот."
        ren "То всякий раз, когда он хотел меня взять, он дубасил меня так, что утром я едва сползала с лежанки."
        ren "Однажды я встала затемно и перерезала сердобольному кмету горло."
        ren "Тогда я еще не была такой сноровистой, как теперь, и нож показался мне слишком маленьким."
        show renokno3:
            "renokno2.jpg"
            pause 0.5
            "renokno3" with dissolve
            pause 1.5
            "renokno2.jpg" with dissolve
            pause 1.5
            "renokno4.jpg" with dissolve
        ren "И, понимаешь, Геральт, слушая, как кмет булькает, и видя, как он дрыгает ногами..."
        ren "Я почувствовала, что следы от его палки и кулаков уже не болят и что мне хорошо, так хорошо, что..."
        ren "Я ушла, весело посвистывая, здоровая, радостная и счастливая."
        ren "И потом каждый раз повторялось то же самое."
        ren "Если б было иначе, кто стал бы тратить время на месть?"
        scene renokno7
        with dissolve
        g "Ренфри, независимо от твоих мотивов и соображений ты не уйдешь отсюда посвистывая и не будешь чувствовать себя так хорошо, что..."
        g "Уйдешь не веселой и счастливой, но уйдешь живой."
        g "Завтра утром, как приказал войт."
        g "Я уже тебе это говорил, но повторю."
        g "Ты не убьешь Стрегобора в Блавикене."
        scene renokno
        with dissolve
        ren "Мне жаль тебя."
        "Неожиданно проговорила девушка."
        scene room2
        show geraltsit2
        show renangry
        with dissolve
        ren "Ты утверждаешь, что не существует Меньшего Зла."
        ren "Так вот - ты останешься на площади, на брусчатке, залитой кровью, один-одинешенек, потому что не сумел сделать выбор."
        ren "Не умел, но сделал."
        ren "Ты никогда не будешь знать, никогда не будешь уверен."
        ren "Никогда, слышишь..."
        ren "А платой тебе будет камень и злое слово."
        hide renangry
        show rensittalk
        show table8
        with dissolve
        ren "Мне жаль тебя, ведьмак."
        hide geraltsit2
        hide rensittalk
        show rensit
        show geraltsittalk2
        hide table8
        show table8
        g "А ты?"
        "Спросил ведьмак тихо, почти шепотом."
        hide rensit
        hide table8
        hide geraltsittalk2
        show geraltsit2
        show rensittalk
        show table8
        ren "Я тоже не умею делать выбор."
        hide geraltsit2
        hide rensittalk
        show rensit
        show geraltsittalk2
        hide table8
        show table8
        g "Кто ты?"
        hide rensit
        hide table8
        hide geraltsittalk2
        show geraltsit2
        show rensittalk
        show table8
        ren "Я то, что я есть."
        hide geraltsit2
        hide rensittalk
        show rensit
        show geraltsittalk4
        hide table8
        show table8
        g "Где ты?"
        hide rensit
        hide table8
        hide geraltsittalk4
        show geraltsit4
        show rensittalk
        show table8
        ren "Мне холодно..."
        hide geraltsit4
        hide rensittalk
        show rensit
        show geraltsittalk4
        hide table8
        show table8
        g "Ренфри!"
        hide rensit
        hide table8
        hide geraltsittalk4
        show geraltsit4
        show rensittalk
        show table8
        ren "Ты выиграл."
        "Вдруг резко бросила она."
        ren "Выиграл, ведьмак"
        ren "Завтра рано утром я уеду из Блавикена и никогда не вернусь в этот задрипанный городишко."
        ren "Никогда."
        "..."
        ren "Геральт?"
        hide geraltsit4
        hide rensittalk
        show rensit
        show geraltsittalk4
        hide table8
        show table8
        g "Да?"
        hide rensit
        hide table8
        hide geraltsittalk4
        show geraltsit4
        show rensittalk
        show table8
        ren "Эта чертова крыша очень крутая."
        ren "Я бы лучше вышла от тебя на рассвете."
        ren "В темноте можно упасть и покалечиться."
        ren "Я княжна, у меня нежное тело, я чувствую горошину сквозь тюфяк. "
        ren "Если, конечно, он как следует не набит сеном."
        ren "Ну, как ты думаешь?"
        hide geraltsit4
        hide rensittalk
        show rensit
        show geraltsittalk4
        hide table8
        show table8
        g "Ренфри."
        "Геральт невольно улыбнулся."
        g "То, что ты говоришь, подобает княжне?"
        hide rensit
        hide table8
        hide geraltsittalk4
        show geraltsit4
        show rensittalk
        show table8
        ren "Что ты, ядрена вошь, понимаешь в княжнах?"
        ren "Я была княжной и знаю: вся прелесть жизни в том и состоит, чтобы делать то, что захочется."
        ren "Я что, должна тебе прямо сказать, чего хочу, или сам догадаешься?"
        "Геральт, продолжая улыбаться, не ответил."
        hide rensittalk
        show rensitmeh
        hide table8
        show table8
        ren "Я даже подумать не смею, что не нравлюсь тебе."
        "Поморщилась девушка."
        hide rensitmeh
        show rensittalk3
        hide table8
        show table8
        ren "Уж лучше считать, что ты просто боишься, как бы тебя не постигла судьба свободного кмета"
        ren "Эх, белоголовый!"
        ren "У меня при себе нет ничего острого. "
        hide rensittalk3
        show rensittalk2
        hide table8
        show table8
        ren "Впрочем, проверь сам."
        scene black
        with fade
        "Снаружи в темноте орал кот."
        scene house2
        with fade
        g "Ренфри?"
        ren "Что?"
        g "Это батист?"
        ren "Конечно, черт побери. "
        ren "Княжна я или нет? В конце-то концов?"
        stop music
        scene black
        with fade
        "Проснувшись утром, Геральт решил для себя..."

        menu:
            
            "Поговорить с Кальдемейном":
                jump choice_talk

            "Уйти из города":
                jump choice_uti
            "Месть за Ренфри":
                jump choice_revenge

        label choice_talk:

            $ menu_flag = True
            "Что вопрос с Ренфри решен."
            
            scene house
            show kald6
            show geralt8:
                xalign 1.0
                yalign 1.0
            v "Так что говоришь, Геральт? Она выматывается из города?"
            hide geralt8
            hide kald6
            show kald7
            show geralt7:
                xalign 1.0
                yalign 1.0
            
            g "Да."
            hide geralt7
            hide kald7
            show kald6
            show geralt8:
                xalign 1.0
                yalign 1.0
            
            v "Ну, не думал, что так гладко пойдет."
            v "С этим своим пергаментом да с печатью Аудоена она приперла меня к стенке."
            v "Я прикидывался героем, но, по правде говоря, хрен что мог им сделать."
            hide geralt8
            hide kald6
            show kald7
            show geralt7:
                xalign 1.0
                yalign 1.0
            g "Даже если б они в открытую нарушили закон? Устроили шум, драку?"
            hide geralt7
            hide kald7
            show kald6
            show geralt8:
                xalign 1.0
                yalign 1.0
            v "Понимаешь, Геральт, Аудоен страшно раздражительный король, посылает на эшафот за любую мелочь. "
            v "У меня жена, дочка, мне нравится моя должность. "
            v "Не приходится думать, где утром достать жиру для каши. "
            v "Одним словом, хорошо, что они уезжают. "
            v "Да, Геральт, не думал я. "
            v "Расспрашивал Сотника, трактирщика из «Золотого Двора», о новиградской компании."
            v "Та еще шайка. Некоторых узнали."
            scene house3
            show kald4
            show geralt5
            
            g "Да?"
            hide geralt5
            hide kald4
            show kald3
            show geralt4
            
            v "Вроде они имеют какое-то отношение к бойне в Тридаме."
            hide geralt4
            hide kald3
            show kald4
            show geralt5
            
            g "Где-где?"
            hide geralt5
            hide kald4
            show kald3
            show geralt4
            
            v "В Тридаме. Не слышал?"
            v "Об этом много было шуму. "
            v "Барон из Тридама держал в яме каких-то разбойников."
            v "Их дружки, среди них, кажется, и полукровка Киврил, захватили паром на реке, полный пилигримов."
            v "Послали барону требование: мол, освободи всех."
            v "Барон, дело ясное, отказал, и тогда они принялись убивать паломников по очереди, одного за другим."
            v "Пока барон не смягчился и не выпустил их дружков из ямы, они спустили по течению больше десятка."
            v "Барону за это грозило изгнание, а то и топор: одни заимели на него зуб за то, что он уступил."
            v "Другие подняли шум, что-де очень скверно поступил, что, мол, это был прен..."
            v "Прецендент, или как его там, что, дескать, надо было перестрелять всех там из арбалетов."
            v "Барон на суде толковал, что выбрал Меньшее Зло, потому как..."
            hide geralt4
            hide kald3
            show kald4
            show geralt5
            
            g "Тридамский ультиматум. "
            "Прошептал ведьмак."
            g "Ренфри..."
            hide geralt5
            hide kald4
            show kald3
            show geralt4
            
            v "Что?"
            hide geralt4
            hide kald3
            show kald4
            show geralt5
            
            g "Кальдемейн, ярмарка."
            hide geralt5
            hide kald4
            show kald3
            show geralt4
            
            v "Ну и что?"
            hide geralt4
            hide kald3
            show kald4
            show geralt5
            
            g "Не понимаешь? Она меня обманула."
            hide kald4
            show kald5
            with dissolve
            hide geralt5
            show geralt5
            g "Никуда они не выедут."
            g "Заставят Стрегобора выйти из башни, как заставили барона из Тридама."
            g "Или вынудят меня..."
            scene house
            show kaldfear
            show geralt8:
                xalign 1.0
                yalign 1.0
            v "О боги, Геральт! Сядь!"
            v "Куда ты, Геральт?"
            hide geralt8
            hide kaldfear
            show kaldfear2
            show geralt6:
                xalign 1.0
                yalign 1.0
            g "Надо выбрать Меньшее зло!"
            hide geralt6
            hide kaldfear2
            show kaldfear
            show geralt8:
                xalign 1.0
                yalign 1.0
            v "Геральт! Я запрещаю! "
            v "Как войт запрещаю!"
            v "Стой!"
            scene rinok
            with dissolve
            "На рынке начиналось оживление, погромыхивали тележки и возы, первые перекупщики уже заполняли палатки товаром. "
            "Стучал молоток, пел петух, громко кричали чайки."
            scene rinok2
            show desatka2:
                xalign -0.25
                yalign 1.0
            show kivril2:
                xalign 0.25
                yalign 1.0
            show tavik2:
                xalign 0.35
                yalign 1.0
            show twin3:
                xalign 1.0
                yalign 1.0
            show twin4:
                xalign 1.25
                yalign 1.0
            show nogorn3:
                xalign 0.55
                yalign 1.0
                
            r2 "Намечается чудесный денек."
            hide desatka2
            hide kivril2
            hide tavik2
            hide twin3
            hide twin4
            hide nogorn3
            show desatka3:
                xalign -0.25
                yalign 1.0
            show kivril3:
                xalign 0.25
                yalign 1.0
            show tavik2:
                xalign 0.35
                yalign 1.0
            show twin3:
                xalign 1.0
                yalign 1.0
            show twin4:
                xalign 1.25
                yalign 1.0
            show nogorn3:
                xalign 0.55
                yalign 1.0
            "Киврил косо глянул на него, но смолчал."
            hide desatka2
            hide kivril2
            hide tavik2
            hide twin3
            hide twin4
            hide nogorn3
            show desatka3:
                xalign -0.25
                yalign 1.0
            show kivril2:
                xalign 0.25
                yalign 1.0
            show tavik2:
                xalign 0.35
                yalign 1.0
            show twin3:
                xalign 1.0
                yalign 1.0
            show twin4:
                xalign 1.25
                yalign 1.0
            show nogorn4:
                xalign 0.55
                yalign 1.0
            r1 "Как кони, Тавик?"
            hide desatka2
            hide kivril2
            hide tavik2
            hide twin3
            hide twin4
            hide nogorn3
            show desatka3:
                xalign -0.25
                yalign 1.0
            show kivril2:
                xalign 0.25
                yalign 1.0
            show tavik3:
                xalign 0.35
                yalign 1.0
            show twin3:
                xalign 1.0
                yalign 1.0
            show twin4:
                xalign 1.25
                yalign 1.0
            show nogorn3:
                xalign 0.55
                yalign 1.0
            r4 "Готовы, оседланы. "
            r4 "Киврил, их все еще мало на рынке."
            hide desatka2
            hide kivril2
            hide tavik2
            hide twin3
            hide twin4
            hide nogorn3
            show desatka3:
                xalign -0.25
                yalign 1.0
            show kivril4:
                xalign 0.25
                yalign 1.0
            show tavik2:
                xalign 0.35
                yalign 1.0
            show twin3:
                xalign 1.0
                yalign 1.0
            show twin4:
                xalign 1.25
                yalign 1.0
            show nogorn3:
                xalign 0.55
                yalign 1.0
            r3 "Будет больше."
            hide desatka3
            hide kivril2
            hide tavik2
            hide twin3
            hide twin4
            hide nogorn3
            show desatka3:
                xalign -0.25
                yalign 1.0
            show kivril2:
                xalign 0.25
                yalign 1.0
            show tavik3:
                xalign 0.35
                yalign 1.0
            show twin3:
                xalign 1.0
                yalign 1.0
            show twin4:
                xalign 1.25
                yalign 1.0
            show nogorn3:
                xalign 0.55
                yalign 1.0
            r4 "Надо бы чего пожрать."
            hide desatka3
            hide kivril2
            hide tavik2
            hide twin3
            hide twin4
            hide nogorn3
            show desatka3:
                xalign -0.25
                yalign 1.0
            show kivril4:
                xalign 0.25
                yalign 1.0
            show tavik2:
                xalign 0.35
                yalign 1.0
            show twin3:
                xalign 1.0
                yalign 1.0
            show twin4:
                xalign 1.25
                yalign 1.0
            show nogorn3:
                xalign 0.55
                yalign 1.0
            r3 "Потом."
            hide desatka3
            hide kivril2
            hide tavik2
            hide twin3
            hide twin4
            hide nogorn3
            show desatka3:
                xalign -0.25
                yalign 1.0
            show kivril2:
                xalign 0.25
                yalign 1.0
            show tavik3:
                xalign 0.35
                yalign 1.0
            show twin3:
                xalign 1.0
                yalign 1.0
            show twin4:
                xalign 1.25
                yalign 1.0
            show nogorn3:
                xalign 0.55
                yalign 1.0
            r4 "Как же!"
            r4 "Будет у тебя потом время. И желание."
            hide desatka3
            hide kivril2
            hide tavik2
            hide twin3
            hide twin4
            hide nogorn3
            show desatka2:
                xalign -0.25
                yalign 1.0
            show kivril3:
                xalign 0.25
                yalign 1.0
            show tavik2:
                xalign 0.35
                yalign 1.0
            show twin3:
                xalign 1.0
                yalign 1.0
            show twin4:
                xalign 1.25
                yalign 1.0
            show nogorn3:
                xalign 0.55
                yalign 1.0
            r2 "Гляньте."
            scene geraltugol
            with dissolve
            "Со стороны главной улочки приближался ведьмак, обходил прилавки, направляясь прямо к ним."
            scene rinok2
            show geralt:
                xalign 0.0
                yalign 1.0
            show desatka4:
                xalign 0.15
                yalign 1.0
            show kivril5:
                xalign 0.35
                yalign 1.0
            show tavik2:
                xalign 1.25
                yalign 1.0
            show nogorn3:
                xalign 0.75
                yalign 1.0
            r3 "Ага. Ренфри была права."
            show arbalet
            with dissolve
            show arbalet2
            with dissolve
            show arbalet3
            with dissolve
            r3 "Дай-ка самострел, Ногорн."
            scene kivrilarbalet
            with dissolve
            play audio "prefire.mp3"
            r3 "Ни шага дальше, ведьмак!"
            "Геральт остановился."
            "От группы его отделяло около сорока шагов."
            scene gde
            g "Где Ренфри?"
            scene kivrilarbalet2
            with dissolve
            r3 "У башни. Делает чародею некое предложение."
            r3 "Она знала, что ты придешь."
            r3 "Велено передать тебе две вещи."
            scene govori
            g "Говори. "
            scene kivrilarbalet
            with dissolve
            r3 "Первое - послание, которое звучит так: «Я есть то, что я есть. Выбирай... "
            r3 "Либо я, либо то, другое, меньшее». "
            r3 "Вроде бы ты знаешь, в чем дело."
            scene rinokgeralt
            with dissolve
            play audio "sword.mp3"
            "Ведьмак кивнул, потом поднял руку, ухватил рукоять меча, торчащую над правым плечом."
            "Блеснул клинок, описав круг над его головой."
            "Он медленно направился в сторону группы."
            scene kivrilarbaletsmile
            with dissolve
            r3 "Ну-ну! Она и это предвидела, ведьмак."
            r3 "А посему сейчас ты получишь то второе, что она велела тебе передать."
            scene aim
            with dissolve
            r3 "Прямо меж глаз."
            scene sword1
            with dissolve
            play audio "fire.mp3"
            "Звякнула тетива."
            show renokno3:
                "sword2.jpg"
                pause 0.1
                "sword3" with dissolve
                pause 0.1
                "sword4.jpg" with dissolve
            play audio "arrow.mp3"
            "Ведьмак махнул мечом, послышался протяжный звон металла по металлу."
            scene black
            with dissolve
            play music "walk.mp3"
            "Ведьмак шел."
            r2 "Отбил... Отбил в полете..."
            r3 "Ко мне!"
            stop music
            play music "fight.mp3"
            "Лязгнули мечи, вырываемые из ножен, группа сомкнула плечи, ощетинилась остриями."
            "Ведьмак ускорил шаг, его движения, удивительно плавные и мягкие, перешли в бег."
            "Не прямо, на ощетинившуюся мечами группу, а вбок, обходя ее по сужающейся спирали."
            stop music
            scene rinok5
            with dissolve
            "Разбойники, несмотря на численное преимущество, один за другим пали."
            scene rinok4
            with dissolve
            "На рынок вступила Ренфри."
            scene rinok6
            show renfri
            "Она шла мягким, кошачьим шагом, обходя возки и прилавки. "
            "Толпа, словно рой шершней, гудевшая в улочках и у стен домов, утихла."
            "Геральт стоял неподвижно, держа меч в опущенной руке."
            "Девушка подошла на десять шагов, остановилась."
            "Стало видно, что под кафтанчиком у нее кольчуга, короткая, едва прикрывающая бедра."
            scene renfri2
            with dissolve
            ren "Ты выбрал."
            ren "Ты уверен, что правильно?"
            scene rinok2
            show bloodygeralt:
                xalign 0.25
                yalign 1.0
            show rena:
                xalign 1.0
                yalign 1.0
            g "Здесь не будет второго Тридама."
            hide bloodygeralt
            hide rena
            show bloodygeralt3:
                xalign 0.25
                yalign 1.0
            show rena2:
                xalign 1.0
                yalign 1.0
            ren "И не было бы."
            ren "Стрегобор высмеял меня."
            ren "Сказал, что я могу перебить весь Блавикен и добавить несколько ближайших деревушек, но он все равно из башни не выйдет."
            ren "Что так смотришь?"
            ren "Да, я обманула тебя."
            ren "Я всю жизнь обманывала, если это было необходимо."
            ren "Чего же ради делать исключение для тебя?"
            hide bloodygeralt3
            hide rena2
            show bloodygeralt2:
                xalign 0.25
                yalign 1.0
            show rena:
                xalign 1.0
                yalign 1.0
            g "Уйди, Ренфри!"
            hide bloodygeralt2
            hide rena
            show bloodygeralt3:
                xalign 0.25
                yalign 1.0
            show rena3:
                xalign 1.0
                yalign 1.0
            ren "Нет, Геральт."
            
            show renheh:
                "rena3.png"
                xalign 1.0
                yalign 1.0
                pause 0.1
                "rendostaet.png"
                
                pause 0.5
                "renheh.png" with dissolve
            hide rena3
            play audio "sword.mp3"
            "Рассмеялась она и быстро выхватила меч."
            hide bloodygeralt3
            hide renheh
            show bloodygeralt:
                xalign 0.25
                yalign 1.0
            show renasword:
                xalign 1.0
                yalign 1.0
            g "Ренфри."
            hide bloodygeralt
            hide renasword
            show bloodygeralt3:
                xalign 0.25
                yalign 1.0
            show renasword2:
                xalign 1.0
                yalign 1.0
            ren "Нет, Геральт."
            ren "Ты свой выбор сделал, теперь моя очередь."
            hide bloodygeralt3
            hide renasword2
            show renasword:
                xalign 1.0
                yalign 1.0
            show magic:
                "bloodygeralt3.png"
                xalign 0.25
                yalign 1.0
                pause 0.1
                "magic.png" with dissolve
                xalign 0.0
                yalign 1.0
            play audio "magic.mp3"
            "Геральт отступил, поднял руку, сложив пальцы в знак."
            hide magic
            hide renasword
            show magicoblom:
                xalign 0.0
                yalign 1.0
            show renhehe:
                xalign 1.0
                yalign 1.0
            "Ренфри снова засмеялась, коротко, хрипло."
            ren "Пустое, белоголовый."
            ren "Это меня не берет. Только меч."
            hide magicoblom
            hide renhehe
            show bloodygeralt:
                xalign 0.00
                yalign 1.0
            show renasword:
                xalign 1.0
                yalign 1.0
            g "Отойди, Ренфри."
            g "Отойди."
            g "Если мы скрестим мечи, я... "
            g "Я уже не смогу..."
            hide bloodygeralt
            hide renhehe
            show bloodygeralt3:
                xalign 0.00
                yalign 1.0
            show renasword2:
                xalign 1.0
                yalign 1.0
            ren "Знаю."
            ren "Но я..."
            ren "Я тоже не могу иначе."
            ren "Просто не могу."
            ren "Мы есть то, что мы есть."
            ren "Ты и я."
            scene crest
            play audio "swordfight.mp3"
            "Оппоненты скрестили клинки."
            "Бой был не долгий."
            scene hit
            play audio "hit.mp3"
            "Геральт молниеносно рубанул ее, самым концом меча, через открытое бедро и пах."
            scene black
            with dissolve
            "Она не крикнула."
            "Упала на колено и на бок, отпустила меч, впилась обеими руками в рассеченное бедро."
            "Кровь толчками запульсировала между пальцами."
            "Ручейком стекая на изукрашенный пояс, на лосиные сапоги, на грязную брусчатку."
            "Толпа, втиснутая в улочки, зашевелилась и заорала."
            "Геральт спрятал меч."
            ren "Не уходи."
            "Простонала она, свертываясь в клубок."
            "Геральт не ответил."
            ren "Мне..."
            ren "Холодно..."
            "Он не ответил."
            "Ренфри снова застонала."
            "Кровь юркими струйками заполняла ямки между камнями брусчатки."
            ren "Геральт..."
            ren "Обними меня."
            "Он не ответил."
            "Она отвернулась и замерла, прижавшись щекой к камням."
            "Кинжал с очень острым лезвием, который она до того скрывала своим телом, выскользнул из ее мертвеющих пальцев."
            scene rinok2
            show geralt10
            "Прошла минута, показавшаяся вечностью."
            hide geralt10
            show geralt9
            play audio "hotba.mp3"
            "Ведьмак поднял голову при звуке стучавшего по брусчатке посоха Стрегобора."
            hide geralt9
            show bloodygeralt3:
                xalign 0.00
                yalign 1.0
            show stregobor:
                xalign 1.0
                yalign 1.0
            "Волшебник быстро приближался, обходя трупы стороной."
            hide stregobor
            show bloodygeralt3:
                xalign 0.00
                yalign 1.0
            show stregoborhappytalk:
                xalign 1.0
                yalign 1.0
            s "Ну, бойня!"
            s "Видел, Геральт, все видел в кристалле..."
            s "Невероятно. Сорокопутка мертвая."
            s "Совершенно."
            "Геральт не ответил"
            hide stregoborhappytalk
            show stregoborhappybeardtalk:
                xalign 1.0
                yalign 1.0
            s "Ну, Геральт, иди за повозкой. "
            s "Возьмем ее в башню."
            s "Надо сделать вскрытие."
            "Кто-то, незнакомый ведьмаку, сидящий внутри него, стиснул рукоять меча."
            hide stregoborhappybeardtalk
            hide bloodygeralt3
            show bloodygeralt2:
                xalign 0.00
                yalign 1.0
            show stregoborangry:
                xalign 1.0
                yalign 1.0
            g "Только коснись ее, колдун, и твоя голова окажется на брусчатке."
            hide stregoborangry
            hide bloodygeralt2
            show bloodygeralt3:
                xalign 0.00
                yalign 1.0
            show stregoborangrytalk:
                xalign 1.0
                yalign 1.0
            s "Ты что, Геральт, спятил?"
            s "Да ты ранен, в шоке!"
            s "Вскрытие - единственный способ узнать..."
            hide stregoborhappybeardtalk
            hide bloodygeralt3
            show bloodygeralt2:
                xalign 0.00
                yalign 1.0
            show stregoborangry:
                xalign 1.0
                yalign 1.0
            g "Не прикасайся к ней!"
            hide stregoborangry
            hide bloodygeralt2
            show bloodygeralt3:
                xalign 0.00
                yalign 1.0
            show stregoborangrytalk:
                xalign 1.0
                yalign 1.0
            s "Хорошо!"
            s "Как хочешь!"
            s "Но ты так никогда..."
            hide stregoborhappybeardtalk
            hide bloodygeralt3
            show bloodygeralt2:
                xalign 0.00
                yalign 1.0
            show stregoborangry:
                xalign 1.0
                yalign 1.0
            g "Прочь!"
            hide stregoborangry
            hide bloodygeralt2
            show bloodygeralt4:
                xalign 0.00
                yalign 1.0
            show stregoborangrytalk:
                xalign 1.0
                yalign 1.0
            s "Как хочешь. "
            hide stregoborangrytalk
            show stregoborangrybeard:
                xalign 1.0
                yalign 1.0
            play sound "hitwood.mp3"
            "Маг повернулся, ударил посохом в брусчатку."
            show kald9:
                xalign 0.5
                yalign 1.0
            hide stregoborangrybeard
            show stregobor1:
                xalign 1.0
                yalign 1.0    
            v "Достаточно!!!"
            v "Кончайте мать вашу..."
            "Ведьмак стоял неподвижно."
            hide kald9
            show kald9:
                xalign 0.25
                yalign 1.0
            "Войт подошел к нему."
            v "Это все?"
            v "Так оно выглядит - Меньшее Зло, которое ты выбрал?"
            v "Ты сделал уже все, что считал нужным?"
            hide kald10
            show kald8:
                xalign 0.25
                yalign 1.0
            hide bloodygeralt4
            show bloodygeralt:
                xalign 0.00
                yalign 1.0
            g "Да."
            "С трудом, не сразу ответил Геральт."
            hide kald8
            show kald9:
                xalign 0.25
                yalign 1.0
            hide bloodygeralt
            show bloodygeralt4:
                xalign 0.00
                yalign 1.0
            v "Твоя рана серьезна?"
            hide kald9
            show kald8:
                xalign 0.25
                yalign 1.0
            hide bloodygeralt4
            show bloodygeralt:
                xalign 0.00
                yalign 1.0
            g "Нет."
            hide kald8
            show kald9:
                xalign 0.25
                yalign 1.0
            hide bloodygeralt
            show bloodygeralt4:
                xalign 0.00
                yalign 1.0
            v "В таком случае уходи отсюда."
            hide kald9
            show kald8:
                xalign 0.25
                yalign 1.0
            hide bloodygeralt4
            show bloodygeralt:
                xalign 0.00
                yalign 1.0
            g "Да."
            "Сказал ведьмак. "
            hide bloodygeralt4
            hide bloodygeralt
            show bloodygeralt5:
                xalign 0.00
                yalign 1.0
            "Он еще минуту постоял, избегая взгляда войта. "
            hide stregoborangrybeard
            hide kald8
            hide kald9
            hide stregobor1
            hide bloodygeralt
            hide bloodygeralt5
            show geralt10
            show kald2
            "Потом медленно, очень медленно повернулся."
            hide kald2
            show kald
            v "Геральт!"
            hide geralt10
            show geralt9
            "Ведьмак оглянулся."
            v "Не возвращайся сюда никогда."
            scene black
            with dissolve
            v "Никогда."
            jump choice1_done
        label choice_uti:

            $ menu_flag = False
            scene uhodit
            with fade
            "Что ему не следует лезть в чужие дела. "
            "В скором времени он собрал вещи. "
            "И продолжил свой путь."
            jump choice1_done
        label choice_revenge:

            $ menu_flag = False
            "Что он не допустит издевательств из-за чьих-то выдумок."
            "Ведьмак изначально считал проклятье Черного солнца бредом. "
            "Такие, как Стрегобор, заслуживают суда."
            scene house3
            show kald4
            show geralt4
            "Выходившего на улицу Геральта остановил войт."
            
            hide kald4
            show kald3

            k "Геральт, ты куда направился?"
            hide kald3
            hide geralt4
            show kald4
            show geralt5
            g "Я к Стрегобору по делу."
            g "Личному."
            "Сказал Геральт после недолгой паузы."
            hide kald4
            hide geralt5
            show kald3
            show geralt4
            k "Я бы тоже сходил, мне надо посоветоваться с ним по поводу Ренфри."
            hide kald3
            hide geralt4
            show kald4
            show geralt5
            "Ведьмак понимал, что отвертеться не сможет, и смирился с наличием спутника."
            scene garden
            "Совсем скоро товарищи оказались у Стрегобора в башне."
            show stregobortalk:
                xalign 1.0
                yalign 1.0
           
            show kald7:
                xalign -0.5
                yalign 1.0
            show geralt:
                xalign 0.25
                yalign 1.0
            s "Добрые люди, рад вас видеть. С чем пожаловали ко мне?"
            "Геральт всегда старался скрывать свои эмоции от собеседника, но в этот раз некоторая степень его волнения была видна."
            s "Геральт, ты какой-то не такой."
            s "Что случилось?"
            hide geralt
            hide stregobortalk
            show stregobor1:
                xalign 1.0
                yalign 1.0
            show geraltangrytalk:
                xalign 0.25
                yalign 1.0
            g "Я уже это говорил, я недобрый человек!"
            scene dagger with dissolve
            scene dagger2 with dissolve
            "В эту же секунду ведьмак достал свой кинжал из-за голенища и метнул его в сторону Стрегобора."
            scene dagger3 with dissolve
            play audio "kupol.mp3"
            "Колдун попытался среагировать, проговорив какое-то заклинание."
            
            "Вокруг него появился защитный купол."
            play audio "dagger.mp3"
            show renokno3:
                "dagger6.jpg"
                pause 0.2
                "dagger5" with dissolve
                pause 0.3
                "dagger4.jpg" with dissolve
                pause 0.3
                "dagger7.jpg" with dissolve
                pause 0.2
                "dagger6.jpg" with dissolve
            "Кинжал отскочил от барьера и продолжил свой полет... "
            scene ubili
            play audio "knife.mp3"
            "Остановившись в груди Кальдемейна."
            scene uh
            with dissolve
            play audio "sword.mp3"
            "Геральт, не обратив внимания, достал свой меч из-за спины."
            scene black
            with fade
            play audio "hit.mp3"
            "И, сделав рывок, пронзил Стрегобора насквозь."
            "В саду теперь стояло только одно живое существо."
            jump choice1_done
        return
