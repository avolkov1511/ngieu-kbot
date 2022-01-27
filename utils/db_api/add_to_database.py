from utils.db_api.db_commands import add_button

import asyncio

from utils.db_api.database import create_db

# Используем эту функцию, чтобы заполнить базу данных
######################Абитуриента#############################
async def add_buttons():
    await add_button(info=f"Нажмите на ссылку чтобы посмотреть:"
                   f"https://docs.google.com/forms/d/e/1FAIpQLSe39win-VLuk4HS_ubUt9wVuZaReFN_cLYeE89p2_p35-4ITA/viewform?embedded=true",
                   category_name="Абитуриентам", category_code="abitur",
                   subcategory_name="Анкета Абитуриента", subcategory_code="anketa-abitur",
                   button="Посмотреть Анкету")
    await add_button(info=f"О Княгининском университете: "
                        f"ngieu.ru/ob_universitete/",
                   category_name="Абитуриентам", category_code="abitur",
                   subcategory_name="Об университете", subcategory_code="about_univer",
                   button="Презентация университета")
    await add_button(info=f"23 апреля 2021 года. День открытых дверей Института информационных систем и технологий связи:"
                        f"https://vk.com/video-34459339_456239344?list=9c8440b7e97889c6b5",
                   category_name="Абитуриентам", category_code="abitur",
                   subcategory_name="Об университете", subcategory_code="about_univer",
                   button="День открытых дверей")
    await add_button(info=f"Пройти профессиональное тестирование: "
                        f"https://forms.yandex.ru/u/6081a700d53799af8d5eccd4/",
                   category_name="Абитуриентам", category_code="abitur",
                   subcategory_name="Об университете", subcategory_code="about_univer",
                   button="Профессиональное тестирование")
    await add_button(info=f"Абитуриентам СПО: "
                        f"https://ngieu.ru/abiturientam-spo/",
                   category_name="Абитуриентам", category_code="abitur",
                   subcategory_name="Уровни образования", subcategory_code="uroven_obrazov",
                   button="СПО")
    await add_button(info=f"Абитуриентам бакалавриата и магистратуры: "
                        f"https://ngieu.ru/abiturientam-bacalavriat_magistratura/",
                   category_name="Абитуриентам", category_code="abitur",
                   subcategory_name="Уровни образования", subcategory_code="uroven_obrazov",
                   button="Бакалавриат и Магистратура")
    await add_button(info=f"Поступающим в аспирантуру: "
                        f"https://ngieu.ru/aspirantura/",
                   category_name="Абитуриентам", category_code="abitur",
                   subcategory_name="Уровни образования", subcategory_code="uroven_obrazov",
                   button="Аспирантура")
    await add_button(info=f"Перейдите на сайт с направлениями:"
                        f"https://ngieu.ru/napravleniya/",
                   category_name="Абитуриентам", category_code="abitur",
                   subcategory_name="Уровни образования", subcategory_code="uroven_obrazov",
                   button="Выбор направления")
    await add_button(info=f"Адрес приема документов:                  606340,Россия,Нижегородская область,г.Княгинино,ул.Октябрьская,д.22А"
                        f"                                                                                Телефон приёмной комиссии:8 831 66 4-15-47; 8 831 27 4-63-10"
                        f"                                                                                E-mail приёмной комиссии: ngiei-pk@mail.ru"
                        f"                                                                                Заместитель председателя приемной комиссии: Жанна Владимировна Касимова"
                        f"                                                                                Ответственный секретарь приемной комиссии: Кирилов Максим Николаевич",
                   category_name="Абитуриентам", category_code="abitur",
                   subcategory_name="Поступающим", subcategory_code="postup",
                   button="Контакты приёмной комиссии")
    await add_button(info=f"Перечень документов, необходимых для поступления:                                          "
                        f"https://ngieu.ru/perechen_documentov/",
                   category_name="Абитуриентам", category_code="abitur",
                   subcategory_name="Поступающим", subcategory_code="postup",
                   button="Необходимые документы")
    await add_button(info=f"Информация о вступительных испытаниях:                                                "
                        f"https://ngieu.ru/vstupitelnyye_ispytaniya/",
                   category_name="Абитуриентам", category_code="abitur",
                   subcategory_name="Поступающим", subcategory_code="postup",
                   button="Вступительные испытания")
    await add_button(info=f"Информация о стоимости:                                                  "
                        f"https://ngieu.ru/stoimost-obucheniya/",
                   category_name="Абитуриентам", category_code="abitur",
                   subcategory_name="Поступающим", subcategory_code="postup",
                   button="Стоимость обучения")
    await add_button(info=f"Перейти на сайт приёмной компании:                                                  "
                        f"pk.ngiei.ru",
                   category_name="Абитуриентам", category_code="abitur",
                   subcategory_name="Поступающим", subcategory_code="postup",
                   button="Приёмная компания")
    ######################Абитуриента#############################
    ######################Студентам#############################
    await add_button(info=f"Перейти на сайт:                                                  "
                        f"https://ngieu.ru/stud_ofo/",
                   category_name="Студентам", category_code="student",
                   subcategory_name="Очная форма обучения", subcategory_code="ochka",
                   button="Информация для студентов очной формы обучения")
    await add_button(info=f"Перейти на сайт:                                                  "
                        f"https://ngieu.ru/stud_zfo/",
                   category_name="Студентам", category_code="student",
                   subcategory_name="Заочная форма обучения", subcategory_code="zaochka",
                   button="Информация для студентов заочной формы обучения")
    await add_button(info=f"Перейти на Moodle:                                                  "
                        f"https://ngiei.mcdir.ru/",
                   category_name="Студентам", category_code="student",
                   subcategory_name="Образовательная среда", subcategory_code="obr-sreda",
                   button="Электронная информационно-образовательная среда")
    await add_button(info=f"Перейти на Mirapolis VR:                                                  "
                        f"https://b23259.vr.mirapolis.ru/mira/",
                   category_name="Студентам", category_code="student",
                   subcategory_name="Образовательная среда", subcategory_code="obr-sreda",
                   button="Платформа для дистанционных занятий")
    await add_button(info=f"Перейти на Urait:                                                  "
                        f"https://urait.ru/",
                   category_name="Студентам", category_code="student",
                   subcategory_name="Образовательная среда", subcategory_code="obr-sreda",
                   button="Электронная библиотечная система “Юрайт”")
    await add_button(info=f"Перейти на сайт:                                                  "
                        f"https://msrabota.ru/info/interv-yu-nedeli/all",
                   category_name="Студентам", category_code="student",
                   subcategory_name="Образовательная среда", subcategory_code="obr-sreda",
                   button="Новости науки, искусства и техники")
    ##############Студентам№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№
    #######################Университетская жизнь######################
    await add_button(info=f"Перейти в группу с новостями:                                                  "
                        f"https://vk.com/ngieu",
                   category_name="Университетская жизнь", category_code="univer-life",
                   subcategory_name="Новости", subcategory_code="news",
                   button="Княгининский университет в Вконтакте")
    await add_button(info=f"Перейти на MixMedia:                                                  "
                        f"https://vk.com/mixmedia1",
                   category_name="Университетская жизнь", category_code="univer-life",
                   subcategory_name="Новости", subcategory_code="news",
                   button="Молодежное СМИ университета")
    await add_button(info=f"Перейти в YouTube:                                                  "
                        f"https://www.youtube.com/channel/UClEXc9s17LQe0bjE52xd9jw?view_as=subscriber",
                   category_name="Университетская жизнь", category_code="univer-life",
                   subcategory_name="Новости", subcategory_code="news",
                   button="Княгининский университет в YouTube")
    await add_button(info=f"Перейти в Instagram:                                                  "
                        f"https://www.instagram.com/knyagininouniversity/",
                   category_name="Университетская жизнь", category_code="univer-life",
                   subcategory_name="Новости", subcategory_code="news",
                   button="Княгининский университет в Instagram")
    await add_button(info=f"Перейти в Вконтакте:                                                  "
                        f"https://vk.com/knyagininotv",
                   category_name="Университетская жизнь", category_code="univer-life",
                   subcategory_name="Новости", subcategory_code="news",
                   button="Новости Княгинино")

######################Здоровье, питание и спорт##################################
    await add_button(info=f"Перейти в сайт:                                                  "
                        f"https://xn--80aesfpebagmfblc0a.xn--p1ai/information/",
                   category_name="Здоровье, питание и спорт", category_code="zd-pit-sport",
                   subcategory_name="Здоровье", subcategory_code="zd",
                   button="Важное: Короновирус")
    await add_button(info=f"Столовая университета находится в Первом учебном корпусе на первом этаже."
                   f"Приходите! Мы вас ждём!",
                   category_name="Здоровье, питание и спорт", category_code="zd-pit-sport",
                   subcategory_name="Где поесть", subcategory_code="pit",
                   button="Столовая университета")
    await add_button(info=f"Перейти в группу Вконтаке:"
                        f"https://vk.com/smallitaly",
                   category_name="Здоровье, питание и спорт", category_code="zd-pit-sport",
                   subcategory_name="Где поесть", subcategory_code="pit",
                   button="Пиццерия “Маленькая Италия“")
    await add_button(info=f"Перейти в группу Вконтаке:"
                        f"https://vk.com/xk_kng",
                   category_name="Здоровье, питание и спорт", category_code="zd-pit-sport",
                   subcategory_name="Спорт", subcategory_code="sport",
                   button="ХК КНЯГИНИНО")







loop = asyncio.get_event_loop()
loop.run_until_complete(create_db())
loop.run_until_complete(add_buttons())
