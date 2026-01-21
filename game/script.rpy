## Сердце Урала — новая ветвящаяся структура с уроками

## Персонажи
define a = Character("Айгуль")
define elder = Character("Старейшина")
define adzahi = Character("Адзахи")
define sokol = Character("Сокол")
define aysylu = Character("Айсылу")
define n = Character(None)  # рассказчик

## Фоны из папки images
image bg prologue = im.Scale("images/гора_рассвет.png", config.screen_width, config.screen_height)
image bg village = im.Scale("images/деревня_утро.png", config.screen_width, config.screen_height)
image bg forest = im.Scale("images/темный_лес.png", config.screen_width, config.screen_height)
image bg cave = im.Scale("images/пещера.png", config.screen_width, config.screen_height)
image bg shrine = im.Scale("images/озеро_ночь.png", config.screen_width, config.screen_height)
image bg stars = im.Scale("images/звездное_небо_для_загадок_акбузата.jpg", config.screen_width, config.screen_height)

# Дополнительные фоны и спрайты для сна и коня
image bg dream = im.Scale("images/Лунное сияние среди облаков_для_сна.png", config.screen_width, config.screen_height)
image horse silver = "images/Белый конь в грациозном подъеме.png"

## Спрайты: героиня, старейшина, птица, Адзахи
image heroine happy = "images/веселая_главная_героиня.png"
image heroine worried = "images/встревоженная_героиня.png"
image heroine calm = "images/спокойная_героиня.png"
image heroine angry = "images/слегка_злая_героиня.png"

image elder neutral = "images/старейшина.png"

image bird golden = "images/птица_золотая.png"
image sokol calm = "images/сокол.png"
image sokol alert = "images/сокол_настороженный.png"

# Адзахи в двух состояниях
image adzahi calm = "images/дух_еще_не_огненный.png"
image adzahi fire = "images/огненный_дух.png"

# айсылу спрайт
image aysylu = "images/aysylu.png"

# Трансформы для масштабирования и уместного размещения сокола и коня
transform sokol_fit_left:
    xalign 0.2
    yalign 1.0
    zoom 0.6

transform sokol_fit_right:
    xalign 0.8
    yalign 1.0
    zoom 0.6

transform aysylu_A:
    xalign 0.2
    yalign 1.0
    zoom 0.6

transform horse_center_fit:
    xalign 0.5
    yalign 1.0
    zoom 0.7

# Отзеркаленный конь слева от центра
transform horse_left_mirrored:
    xalign 0.35
    yalign 1.0
    zoom 0.7
    xzoom -1.0

# Определение эффекта тряски экрана
transform shake:
    zoom 1.0
    xoffset 0
    yoffset 0
    linear 0.05 xoffset 10
    linear 0.05 yoffset 10
    linear 0.05 xoffset 0
    linear 0.05 yoffset 0
    linear 0.05 xoffset -10
    linear 0.05 yoffset -10
    linear 0.05 xoffset 0
    linear 0.05 yoffset 0
    repeat

## НОВЫЕ ПЕРЕМЕННЫЕ ДЛЯ СИСТЕМЫ УРОКОВ
default trust_dream = False
default navigation_stars = False      # Знание навигации по звёздам
default speech_rhythm = False         # Знание речи/ритма из загадок
default herbs_knowledge = False    # Победа над Аждахой
default dragon_attempts = 0           # Количество попыток боя с драконом

# Переменные для навигации и путей
default navigation_choice = None      # "star"/"sun"/None
default path_choice = None           # "ridge"/"valley"/"cave"/None
default current_location = "village" # Отслеживание текущего местоположения

# Переменные для финальных концовок
default collected_feather = False

label start:
    scene bg dream with fade
    show horse silver at horse_center_fit
    if renpy.loadable("audio/bashkirskaya-narodnaya-kuray-bayas.mp3"):
        play music "audio/bashkirskaya-narodnaya-kuray-bayas.mp3" fadein 1.0
    elif renpy.loadable("audio/ambient_steppe.ogg"):
        play music "audio/ambient_steppe.ogg" fadein 1.0
    
    n "Ночью Айгуль увидела сон: серебряный конь взмыл среди лунных облаков. Голос позвал её к {color=#FFD700}Сердцу Урала{/color} — древнему месту, где горы держат память народа."
    n "С того дня деревня живёт тревогой: воды мелеют, пастбища сохнут. {color=#FFD700}Сердцу нужен голос{/color}, чтобы его услышали снова."
    n "Конь из сна лишь указал дорогу. Идти придётся Айгуль."
    
    menu:
        "Довериться белому коню из сна":
            $ trust_dream = True
            jump village_meeting
        "Отмахнуться от сна":
            $ trust_dream = False
            jump forest_start

label forest_start:
    scene bg forest with fade
    show heroine angry at right
    a "Сон — пустяки. Я сама решу свою судьбу."
    n "Тропа повела её через туманные чащи, но где-то вдалеке всё равно слышалось ржание."
    jump village_ritual

label village_ritual:
    scene bg village with dissolve
    show heroine worried at right
    n "Айгуль поняла, что нужна подготовка. В деревне она заложила основу для будущего путешествия."
    jump lore_stone

label lore_stone:
    scene bg village with dissolve
    show heroine calm at right
    n "У старого камня были выбиты знаки: 'Слушай, говори, благодари'. Так учили проводники, когда шли к Сердцу."
    n "Айгуль провела ладонью по резам и прошептала благодарность дороге."
    jump village_meeting

label village_meeting:
    scene bg village with dissolve
    show elder neutral at left
    show heroine calm at right
    elder "Сон — не случайность. Сердце Урала глохнет, потому что люди перестали его слушать. Если оно затихнет, реки иссякнут."
    elder "Твоя задача — дойти до святилища и взять {color=#FFD700}{b}Перо Памяти{/b}{/color}. Там горы услышат тебя, если ты услышишь их."
    elder "Но сначала нужно подготовиться. Есть {color=#FFD700}{b}три урока{/b}{/color}, которые помогут тебе в пути."
    jump lesson_stars

# УРОК 1: ЗВЁЗДЫ (НАВИГАЦИЯ)
label lesson_stars:
    scene bg stars with dissolve
    show elder neutral at left
    show heroine calm at right
    elder "Первый урок — {color=#FFD700}{b}навигация по звёздам{/b}{/color}. В горах солнце может обмануть, но звёзды никогда не лгут."
    elder "На Урале особенно важны три созвездия: Большая Медведица, Малая Медведица и Кассиопея."
    hide elder
    hide heroine
    menu:
        "Внимательно изучить расположение звёзд":
            elder "Посмотри на Большую Медведицу — семь ярких звёзд в форме ковша."
            elder "Проведи линию от двух крайних звёзд ковша — она укажет на Полярную звезду."
            elder "Полярная звезда — это конец ручки Малой Медведицы. Она всегда указывает на север."
            elder "А Кассиопея похожа на букву W — она помогает найти Полярную звезду, если Большая Медведица скрыта."
            elder "Запомни: высота Полярной звезды над горизонтом равна твоей широте. На Урале это примерно 55 градусов."
            
            n "Айгуль долго смотрела на небо, запоминая узор созвездий. Старейшина терпеливо объяснял каждый знак."
            elder "В горах звёзды — твой единственный надёжный компас. Солнце может обмануть в ущельях."
            
            # ТЕСТ ЗНАНИЙ ПО ЗВЁЗДАМ
            elder "Теперь проверим, что ты запомнила. Как найти Полярную звезду, если видна Большая Медведица?"
            
            menu:
                "Провести линию от двух крайних звёзд ковша":
                    elder "Правильно! А теперь скажи — что делать, если Большая Медведица скрыта облаками?"
                    
                    menu:
                        "Искать Кассиопею — букву W":
                            elder "Отлично! И последний вопрос — на какой высоте над горизонтом искать Полярную звезду на Урале?"
                            
                            menu:
                                "Примерно 55 градусов":
                                    elder "Превосходно! Ты действительно изучила звёздную навигацию."
                                    $ navigation_stars = True
                                    show heroine happy
                                    n "Айгуль почувствовала уверенность — теперь она знает, как читать звёздную карту."
                                    hide elder
                                    
                                "Около 90 градусов":
                                    elder "Нет, 90 градусов — это прямо над головой. На Урале Полярная звезда ниже."
                                    $ navigation_stars = False
                                    show heroine worried
                                    
                                "Примерно 30 градусов":
                                    elder "Нет, 30 градусов — это слишком низко. Подумай о широте Урала."
                                    $ navigation_stars = False
                                    show heroine worried
                        "Искать другую звезду":
                            elder "Нет, Кассиопея похожа на букву W и помогает найти Полярную звезду."
                            $ navigation_stars = False
                            show heroine worried
                "Искать самую яркую звезду":
                    elder "Нет, нужно провести линию от двух крайних звёзд ковша Большой Медведицы."
                    $ navigation_stars = False
                    show heroine worried
            
        "Поверхностно ознакомиться":
            elder "Звёзды — это древняя мудрость наших предков. Но если ты не готова учиться..."
            n "Айгуль кивнула, но не вникла в детали. Звёзды казались слишком сложными для изучения."
            $ navigation_stars = False
            show heroine worried
    
    jump meet_sokol

label meet_sokol:
    scene bg forest with fade
    show heroine calm at right
    show sokol calm at sokol_fit_left
    sokol "Крылья ведут меня по перевалам. Я — Сокол. Знаю тропы к Сердцу."
    sokol "Но сначала тебе нужно пройти ещё два урока. Без них путь будет опасен."
    jump lesson_riddles

# УРОК 2: ЗАГАДКИ (РЕЧЬ И РИТМ)
label lesson_riddles:
    scene bg forest with dissolve
    show sokol calm at sokol_fit_left
    show heroine calm at right
    sokol "Второй урок — {color=#FFD700}{b}загадки{/b}{/color}. Они учат не только думать, но и чувствовать ритм речи."
    sokol "В горах эхо — твой друг, если ты знаешь, как с ним говорить."
    sokol "Наши предки-башкиры говорили: 'Кто знает загадки — тот знает язык гор'."
    
    # Загадка 1 - башкирская
    sokol "Слушай первую загадку: 'Без корня растёт, без крыльев летает, без языка говорит'?"
    
    menu:
        "Тень":
            n "Правильно! Тень растёт от света, летает с тобой, говорит жестами."
            n "Айгуль почувствовала ритм башкирской речи — плавный, как горный ручей."
            $ speech_rhythm = True
            show heroine happy
            
        "Эхо":
            n "Близко, но не то. Эхо не растёт — оно только повторяет."
            $ speech_rhythm = False
            show heroine worried
            
        "Дым":
            n "Интересно, но дым не говорит — он только показывает направление ветра."
            $ speech_rhythm = False
            show heroine worried
    
    # Загадка 2 (если первая решена)
    if speech_rhythm:
        sokol "Отлично! Ты чувствуешь ритм. Вторая загадка: 'Что становится больше, когда его делишь'?"
        
        menu:
            "Секрет":
                n "Верно! Секрет становится больше, когда ты делишься им с другими."
                n "Айгуль почувствовала, как ритм загадок вошёл в её речь."
                
            "Тень":
                n "Не совсем. Подумай о том, что можно разделить и что от этого увеличится."
                $ speech_rhythm = False
                show heroine worried
                
            "Время":
                n "Интересная мысль, но время не становится больше от деления."
                $ speech_rhythm = False
                show heroine worried
    
    # Загадка 3 (если обе решены)
    if speech_rhythm:
        sokol "Превосходно! Последняя загадка: 'Днём спит, ночью бодрствует, глазами не видит'?"
        
        menu:
            "Сова":
                n "Правильно! Сова днём спит, ночью охотится, но видит в темноте."
                n "Айгуль поняла: загадки учат не только логике, но и чувствовать ритм башкирского языка."
                sokol "Теперь ты знаешь, как говорить с эхом гор. Ритм твоей речи будет резонировать с камнями."
                
            "Летучая мышь":
                n "Близко, но летучая мышь видит ушами, а не глазами."
                $ speech_rhythm = False
                show heroine worried
                
            "Ночной цветок":
                n "Красивая мысль, но цветок не спит днём — он просто закрывается."
                $ speech_rhythm = False
                show heroine worried
    
    if speech_rhythm:
        n "Сокол кивнул одобрительно. Айгуль научилась чувствовать ритм и структуру башкирской речи."
        
        # ТЕСТ ЗНАНИЙ РИТМА РЕЧИ
        sokol "Теперь проверим, поняла ли ты ритм. Повтори за мной фразу с правильным ритмом:"
        sokol "'Горы говорят тихо, но их голос силён'"
        
        menu:
            "Повторить с правильным ритмом":
                n "Айгуль повторила фразу, чувствуя ритм каждого слова."
                sokol "Хорошо! А теперь скажи — как изменится эхо, если говорить слишком быстро?"
                
                menu:
                    "Эхо станет невнятным":
                        sokol "Правильно! А если говорить слишком медленно?"
                        
                        menu:
                            "Эхо будет прерывистым":
                                sokol "Отлично! Ты действительно поняла ритм речи."
                                sokol "Ритм речи — это ключ к пониманию гор. Эхо будет твоим союзником."
                                hide sokol
                                
                            "Эхо станет громче":
                                sokol "Нет, громкость не зависит от скорости. Подумай о ритме."
                                $ speech_rhythm = False
                                show heroine worried
                                
                            "Эхо исчезнет":
                                sokol "Нет, эхо не исчезнет, но будет звучать неестественно."
                                $ speech_rhythm = False
                                show heroine worried
                    "Эхо станет громче":
                        sokol "Нет, громкость не зависит от скорости. Подумай о ритме."
                        $ speech_rhythm = False
                        show heroine worried
                        
                    "Эхо исчезнет":
                        sokol "Нет, скорость влияет на ясность эха. Подумай о ритме."
                        $ speech_rhythm = False
                        show heroine worried
            "Повторить без ритма":
                sokol "Ритм — это основа. Без него слова остаются пустыми звуками."
                $ speech_rhythm = False
                show heroine worried
    else:
        n "Сокол покачал головой. 'Ритм речи — это ключ к пониманию гор. Без него эхо останется глухим'."
    
    jump ridge_path

label ridge_path:
    scene bg forest with dissolve
    show sokol calm at sokol_fit_left
    show heroine calm at right
    sokol "Теперь выбирай путь. Но помни — навигация важна. Как будешь ориентироваться?"
    
    menu:
        "По звёздам":
            $ navigation_choice = "star"
            if navigation_stars:
                n "Айгуль уверенно указала на север по звёздам. Сокол одобрительно кивнул."
                jump path_choice_star
            else:
                n "Айгуль попыталась найти звёзды, но не знала, как их читать."
                jump navigation_lost
        
        "По солнцу":
            $ navigation_choice = "sun"
            n "Айгуль решила довериться солнцу, но в горах оно может обмануть."
            jump navigation_lost

label navigation_lost:
    scene bg forest with fade
    show heroine worried at right
    n "Без правильной навигации Айгуль заблудилась. Пришлось идти окольным путём через броды."
    jump river_ford

label path_choice_star:
    scene bg forest with dissolve
    show sokol calm at sokol_fit_left
    show heroine calm at right
    sokol "Дальше два пути: по гребню — быстрый, но открытый ветрам; в расселине — длиннее, но тише."
    sokol "Или можно спуститься к пещерам — укрыться от ветра."
    hide sokol
    
    menu:
        "Идти по гребню":
            $ path_choice = "ridge"
            n "Ветер хлестал лицо, но взгляд Айгуль оставался уверенным."
            jump lesson_herbs
            
        "Идти в расселину":
            $ path_choice = "valley"
            n "Тень скал укрыла их. Шаги стали ровнее, дыхание — глубже."
            jump lesson_herbs
            
        "Спуститься к пещерам":
            $ path_choice = "cave"
            n "Они нашли тёмный вход в пещеру, где ветер стих."
            jump lesson_herbs

label river_ford:
    scene bg forest with dissolve
    show heroine worried at right
    n "У реки течение было быстрым. Без правильной навигации пришлось искать брод дольше."
    $ path_choice = "ford"
    jump lesson_herbs

# УРОК 3: ТРАВЫ (ЗНАНИЯ О ЛЕЧЕБНЫХ СВОЙСТВАХ)
label lesson_herbs:
    scene bg forest with dissolve
    show heroine calm at right
    n "На пути Айгуль встретила мудрую башкирскую травницу Айсылу, которая поделилась древними знаниями о горных растениях."
    
    # Появляется травница
    show aysylu at aysylu_A
    
    aysylu "Добро пожаловать, дочь гор! Я Айсылу, хранительница тайн уральских трав."
    aysylu "Наши предки знали: каждая трава на Урале — это дар Земли-Матери. Учись читать их язык."
    
    menu:
        "Внимательно изучить свойства трав":
            aysylu "Отлично! Начнём с {color=#FFD700}{b}трёх главных трав Урала{/b}{/color}."
            
            aysylu "Первая — Зверобой (ҡыҙыл үлән). Его называют 'травой от 99 болезней'."
            aysylu "Листья зверобоя, если растереть их в ладонях, дают красный сок. Он лечит раны и успокаивает боль."
            aysylu "Но главное — зверобой защищает от злых духов и очищает душу."
            
            aysylu "Вторая — Душица (медвежья трава). Она растёт на солнечных склонах."
            aysylu "Отвар душицы снимает жар, успокаивает кашель и лечит болезни сердца."
            aysylu "А если подышать паром душицы — она очистит лёгкие от горной пыли."
            
            aysylu "Третья — Сабельник (ҡыҙыл тамыр). Его корни красные, как кровь."
            aysylu "Сабельник — самая сильная трава против жара и огня. Он может охладить даже дыхание дракона."
            aysylu "Но будь осторожна: сабельник ядовит, если не знать, как его готовить."
            
            aysylu "Теперь рецепт охлаждающего отвара: возьми листья душицы, добавь щепотку зверобоя и каплю сока сабельника."
            aysylu "Залей кипятком и дай настояться до тех пор, пока вода не станет золотистой."
            aysylu "Этот отвар защитит тебя от любого жара — и от солнца, и от огненного дыхания."
            
            n "Айгуль внимательно слушала каждое слово. Травница показала, как различать растения по листьям, запаху и месту произрастания."
            
            # ТЕСТ ЗНАНИЙ ТРАВ
            aysylu "Теперь проверим, что ты запомнила. Какая трава самая сильная против жара и огня?"
            
            menu:
                "Сабельник (ҡыҙыл тамыр)":
                    aysylu "Правильно! А теперь скажи — что даёт зверобой, если растереть его листья?"
                    
                    menu:
                        "Красный сок":
                            aysylu "Отлично! И последний вопрос — как называется трава, которая растёт на солнечных склонах?"
                            
                            menu:
                                "Душица (медвежья трава)":
                                    aysylu "Превосходно! Ты действительно изучила свойства трав."
                                    $ herbs_knowledge = True
                                    show heroine happy
                                    aysylu "Ты готова! Теперь ты знаешь язык трав. Они станут твоими союзниками в горах."
                                    hide aysylu
                                    hide heroine
                                    
                                "Зверобой":
                                    aysylu "Нет, зверобой растёт везде. Подумай о той, что любит солнце."
                                    $ herbs_knowledge = False
                                    show heroine worried
                                    
                                "Сабельник":
                                    aysylu "Нет, сабельник растёт в тенистых местах. Какая трава называется медвежьей?"
                                    $ herbs_knowledge = False
                                    show heroine worried
                        "Зелёный сок":
                            aysylu "Нет, зверобой даёт красный сок при растирании."
                            $ herbs_knowledge = False
                            show heroine worried
                            
                        "Белый сок":
                            aysylu "Нет, зверобой даёт красный сок при растирании."
                            $ herbs_knowledge = False
                            show heroine worried
                "Зверобой":
                    aysylu "Нет, зверобой лечит раны, но сабельник с красными корнями — самая сильная против огня."
                    $ herbs_knowledge = False
                    show heroine worried
                    
                "Душица":
                    aysylu "Нет, душица снимает жар, но сабельник с красными корнями — самая сильная против огня."
                    $ herbs_knowledge = False
                    show heroine worried
            
        "Поверхностно ознакомиться":
            aysylu "Жаль. Травы — это не просто растения, это живые существа с душой."
            aysylu "Без понимания их природы они не поделятся с тобой своей силой."
            n "Айгуль кивнула, но не запомнила детали. Травы казались слишком сложными для изучения."
            $ herbs_knowledge = False
            show heroine worried
            aysylu "Возможно, в следующий раз ты будешь готовы слушать мудрость предков."
    
    jump route_continuation

label route_continuation:
    # Продолжение пути в зависимости от выбранной дороги
    if path_choice == "ridge":
        jump ridge_continuation
    elif path_choice == "valley":
        jump valley_continuation
    elif path_choice == "cave":
        jump cave_continuation
    elif path_choice == "ford":
        jump ford_continuation

label ridge_continuation:
    scene bg forest with dissolve
    show heroine calm at right
    n "Продолжение пути по гребню. Ветер усилился, но Айгуль шла уверенно."
    jump echo_valley

label valley_continuation:
    scene bg forest with dissolve
    show heroine calm at right
    n "Дорога через низину была спокойной. Впереди виднелся каменный мост."
    jump stone_bridge

label stone_bridge:
    scene bg forest with dissolve
    show heroine calm at right
    n "Туман стелился над ущельем. Старый каменный мост держался на честном слове."
    
    menu:
        "Перейти быстро":
            n "Камни поскрипывали, но путь выдержал."
            jump echo_valley
            
        "Подождать и проверить опоры":
            n "Айгуль укрепила пару плит и перешла осторожно."
            jump echo_valley

label cave_continuation:
    scene bg cave with dissolve
    show heroine worried at right
    n "Пещера уходила глубоко под гору. Своды отзывались редкими каплями."
    
    menu:
        "Идти глубже, искать знак Сердца":
            n "Шаги отдавались эхом, коридор сузился. Камни осыпались под ногой."
            jump ending_cave_collapse
            
        "Развести огонь и переждать":
            n "Тепло вернуло сосредоточенность; эхо подсказало путь наружу."
            jump echo_valley

label ford_continuation:
    scene bg forest with dissolve
    show heroine worried at right
    n "Тропа от реки вела через густые заросли. Впереди виднелся каменный мост."
    jump stone_bridge

label ending_cave_collapse:
    scene bg cave with fade
    show heroine angry at right
    n "Не заметив трещину, Айгуль спровоцировала обвал. Её путь к Сердцу прервался у подземной стены."
    n "Иногда горы требуют терпения. Сегодня она проиграла."
    return

label echo_valley:
    scene bg forest with dissolve
    show heroine calm at right
    n "В узкой долине любой шёпот отзывался громом. Здесь легче всего понять, что горы ждут не силы, а внимания."
    
    menu:
        "Использовать ритм речи":
            if speech_rhythm:
                n "Айгуль использовала знания о ритме речи. Эхо послушно ответило и расчистило путь."
                jump echo_success
            else:
                n "Айгуль попыталась говорить ритмично, но без знаний это не сработало."
                show heroine worried
                jump echo_quiet
                
        "Идти тихо":
            n "Айгуль выбрала тихий путь через долину."
            jump echo_quiet

label echo_success:
    scene bg forest with dissolve
    show heroine happy at right
    n "Эхо послушно расступилось. Путь к лунной поляне был чист."
    jump moonlit_clearing

label echo_quiet:
    scene bg forest with dissolve
    show heroine calm at right
    n "Тихий путь тоже вёл к цели, но медленнее."
    jump moonlit_clearing

label moonlit_clearing:
    scene bg dream with fade
    show heroine calm at right
    show horse silver at horse_left_mirrored
    n "Под луной трава серебрилась. Конь выглядел уже не сном — живым спутником."
    n "Впереди вспыхнул жар — дорогу преградил Адзахи."
    jump dragon_battle

# БОЙ С АЖДАХОЙ
label dragon_battle:
    scene bg cave with dissolve
    show adzahi calm at left
    show heroine worried at right
    adzahi "Горы шептали твоё имя, путница. Перо не твоё. Вернись, пока жар не обожжёт дыхание."
    a "Я иду по своей воле. Мне нужно, чтобы Сердце услышало людей снова."
    adzahi "Сон — лишь дверь. За дверью — жар. Пройдёшь ли без ключа?"
    
    $ dragon_attempts += 1
    n "Айгуль вспомнила свои знания: навигацию по звёздам, ритм речи, свойства трав."
    
    menu:
        "Использовать эхо долины":
            jump echo_strategy
            
        "Использовать травы":
            jump herbs_strategy
            
        "Довериться Соколу":
            jump sokol_strategy
            
        "Лоб в лоб":
            jump brute_strategy

label echo_strategy:
    if speech_rhythm:
        n "Айгуль использовала знание ритма речи. Эхо усилило её защиту, и пламя отступило."
        jump dragon_victory
    else:
        n "Без знания ритма речи эхо срывается и не помогает."
        show heroine worried
        jump dragon_defeat

label herbs_strategy:
    if herbs_knowledge:
        n "Айгуль применила охлаждающий отвар из трав. Пламя Адзахи стало слабее."
        jump dragon_victory
    else:
        n "Без знаний о травах смесь не получается, и защита не работает."
        show heroine worried
        jump dragon_defeat

label sokol_strategy:
    # Сокол всегда помогает, если Айгуль дошла до этого момента
    n "Сокол показал точную позицию для атаки. Айгуль использовала его подсказку."
    jump dragon_victory

label brute_strategy:
    n "Айгуль ринулась в лобовую атаку. Это требует особой удачи."
    # Шанс на победу даже без знаний
    $ victory_score = 0
    if navigation_stars:
        $ victory_score += 1
    if speech_rhythm:
        $ victory_score += 1
    if herbs_knowledge:
        $ victory_score += 1
    
    if victory_score >= 1:  # Нужно хотя бы одно знание
        jump dragon_victory
    else:
        show heroine angry
        jump dragon_defeat

label dragon_victory:
    scene bg cave with dissolve
    show adzahi calm at left
    show heroine happy at right
    adzahi "Ты слышишь, когда горы говорят тихо. Тогда и огню не нужен крик."
    a "Я не пришла побеждать. Мне нужна {color=#FFD700}{b}тропа к Сердцу{/b}{/color}, чтобы вернуть слушание."
    adzahi "Тропа не бывает чужой. Она либо внутри, либо нигде. Покажи её делом."
    adzahi "Тропа открыта тому, кто знает, зачем идёт. {color=#FFD700}{b}Перо ждёт{/b}{/color}."
    n "Огонь сжался в тёплую искру и растворился в камне."
    $ dragon_defeated = True
    hide adzahi
    hide heroine
    jump feather_doubt

label dragon_defeat:
    scene bg cave with fade
    show adzahi fire at left with shake
    show heroine angry at right with shake
    adzahi "Ключа нет — значит, будешь стучать ладонью."
    n "Пламя ударило вперёд. Айгуль не смогла противостоять жаркому дыханию дракона."
    n "Но поражение — это тоже урок. Можно вернуться и лучше подготовиться."
    hide adzahi
    hide heroine
    jump defeat_paths

label defeat_paths:
    scene bg village with fade
    show heroine worried at right
    n "Айгуль вернулась в деревню. Поражение показало, что нужны дополнительные знания."
    
    menu:
        "Повторить урок навигации по звёздам":
            if not navigation_stars:
                jump lesson_stars
            else:
                n "Ты уже знаешь навигацию по звёздам."
                jump defeat_paths
                
        "Повторить урок загадок и ритма":
            if not speech_rhythm:
                jump lesson_riddles
            else:
                n "Ты уже знаешь ритм речи."
                jump defeat_paths
                
        "Повторить урок трав":
            if not herbs_knowledge:
                jump lesson_herbs
            else:
                n "Ты уже знаешь свойства трав."
                jump defeat_paths
                
        "Попробовать снова с текущими знаниями":
            jump dragon_battle

label feather_doubt:
    scene bg shrine with dissolve
    show bird golden at truecenter
    show heroine worried at right
    n "У подножия скалы мерцало {color=#FFD700}{b}Перо — знак Сердца{/b}{/color}. Рука дрогнула: сомнение ещё жило в ней."
    
    menu:
        "Взять перо":
            $ collected_feather = True
            jump choose_ending
            
        "Отступить":
            return

label choose_ending:
    # Логика концовок на основе знаний и выборов
    if navigation_stars and speech_rhythm and herbs_knowledge:
        jump ending_harmony
    elif path_choice == "ridge" and not navigation_stars:
        jump ending_fall
    elif not navigation_stars and not speech_rhythm and not herbs_knowledge:
        jump ending_lost
    elif not navigation_stars and path_choice != "ridge":
        jump ending_solo
    elif navigation_stars and path_choice != "cave":
        jump ending_pathfinders
    else:
        jump ending_reflection

label ending_harmony:
    scene bg shrine with fade
    show horse silver at horse_left_mirrored
    show heroine calm at right
    n "Айгуль бережно взяла Перо. Она изучила {color=#FFD700}{b}все три урока{/b}{/color} и применила их мудро."
    n "Сердце Урала бьётся в унисон с её сердцем. Гармония восстановлена."
    hide heroine
    hide horse silver
    return

label ending_fall:
    scene bg forest with fade
    show heroine angry at right
    n "Гребень оказался слишком коварным без знания навигации."
    n "Айгуль оступилась и была вынуждена вернуться, так и не добравшись до Сердца."
    hide heroine
    return

label ending_lost:
    scene bg forest with fade
    show heroine worried at right
    n "Без знаний уроков тропы смешались, и ночь забрала дорогу."
    n "Иногда дорога назад — тоже урок. В этот раз она проиграла."
    hide heroine
    return

label ending_solo:
    scene bg forest with fade
    show heroine angry at right
    n "Она прошла путь одна, медленно и осторожно, не полагаясь ни на чьи крылья."
    n "Сердце Урала приняло её упорство, но путь остался каменным."
    hide heroine
    return

label ending_pathfinders:
    scene bg shrine with dissolve
    show heroine calm at right
    show sokol calm at sokol_fit_left
    n "Вместе со знанием навигации она выбрала верные камни моста и дорогу через туман."
    n "Сердце Урала распахнуло тропы для тех, кто умеет доверять и учиться."
    hide heroine
    hide sokol
    return

label ending_reflection:
    scene bg dream with dissolve
    show heroine worried at right
    n "Айгуль держит Перо и слушает шорохи травы. Ответ ещё не оформился, но путь продолжается."
    n "Иногда тишина — тоже выбор."
    hide heroine
    return
