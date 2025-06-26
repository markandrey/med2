from django.shortcuts import render
from . models import Patient, MedicalCard


# patients = [
#     {
#         "id": 1,
#         "last_name": "Иванов",
#         "first_name": "Иван",
#         "middle_name": "Иванович",
#         "birth_date": "15.05.1980",
#         "last_visit": "2024-03-10T09:15:00",
#         "diagnosis": "Гипертония 2 степени",
#         "allerg": "иАПФ - кашель",
#         "anamn": "Повышение АД с 30 лет, максимальные цифры 180/100 мм рт. ст. ОИМ, ОНМК отрицает."
#     },
#     {
#         "id": 2,
#         "last_name": "Петрова",
#         "first_name": "Мария",
#         "middle_name": "Сергеевна",
#         "birth_date": "22.11.1975",
#         "last_visit": "2024-03-12T14:30:00",
#         "diagnosis": "Сахарный диабет 2 типа"
#     },
#     {
#         "id": 3,
#         "last_name": "Сидоров",
#         "first_name": "Алексей",
#         "middle_name": "Дмитриевич",
#         "birth_date": "03.04.1992",
#         "last_visit": "2024-03-11T16:45:00",
#         "diagnosis": "Бронхиальная астма"
#     },
#     {
#         "id": 4,
#         "last_name": "Кузнецова",
#         "first_name": "Елена",
#         "middle_name": "Владимировна",
#         "birth_date": "30.07.1988",
#         "last_visit": "2024-03-09T11:20:00",
#         "diagnosis": "Остеохондроз шейного отдела"
#     },
#     {
#         "id": 5,
#         "last_name": "Смирнов",
#         "first_name": "Дмитрий",
#         "middle_name": "Анатольевич",
#         "birth_date": "12.09.1970",
#         "last_visit": "2024-03-08T13:10:00",
#         "diagnosis": "ИБС, стенокардия напряжения"
#     },
#     {
#         "id": 6,
#         "last_name": "Фёдорова",
#         "first_name": "Анна",
#         "middle_name": "Павловна",
#         "birth_date": "05.02.1983",
#         "last_visit": "2024-03-07T10:45:00",
#         "diagnosis": "Хронический гастрит"
#     },
#     {
#         "id": 7,
#         "last_name": "Николаев",
#         "first_name": "Артём",
#         "middle_name": "Игоревич",
#         "birth_date": "18.06.1995",
#         "last_visit": "2024-03-06T15:20:00",
#         "diagnosis": "Аллергический ринит"
#     },
#     {
#         "id": 8,
#         "last_name": "Васнецова",
#         "first_name": "Ольга",
#         "middle_name": "",
#         "birth_date": "25.01.1978",
#         "last_visit": "2024-03-05T12:00:00",
#         "diagnosis": "Варикозная болезнь"
#     },
#     {
#         "id": 9,
#         "last_name": "Козлов",
#         "first_name": "Михаил",
#         "middle_name": "Викторович",
#         "birth_date": "14.08.1965",
#         "last_visit": "2024-03-04T17:30:00",
#         "diagnosis": "ХОБЛ"
#     },
#     {
#         "id": 10,
#         "last_name": "Антонова",
#         "first_name": "Светлана",
#         "middle_name": "Борисовна",
#         "birth_date": "07.12.1990",
#         "last_visit": "2024-03-03T08:45:00",
#         "diagnosis": "Вегетососудистая дистония"
#     },
#     {
#         "id": 11,
#         "last_name": "Громов",
#         "first_name": "Павел",
#         "middle_name": "Александрович",
#         "birth_date": "29.03.1982",
#         "last_visit": "2024-03-02T14:15:00",
#         "diagnosis": "Остеоартроз коленных суставов"
#     },
#     {
#         "id": 12,
#         "last_name": "Белова",
#         "first_name": "Екатерина",
#         "middle_name": "Олеговна",
#         "birth_date": "11.05.1973",
#         "last_visit": "2024-03-01T16:50:00",
#         "diagnosis": "Желчнокаменная болезнь"
#     },
#     {
#         "id": 13,
#         "last_name": "Давыдов",
#         "first_name": "Сергей",
#         "middle_name": "",
#         "birth_date": "08.10.1987",
#         "last_visit": "2024-02-28T09:30:00",
#         "diagnosis": "Грыжа межпозвоночного диска"
#     },
#     {
#         "id": 14,
#         "last_name": "Орлова",
#         "first_name": "Татьяна",
#         "middle_name": "Николаевна",
#         "birth_date": "19.04.1991",
#         "last_visit": "2024-02-27T13:40:00",
#         "diagnosis": "Мигрень"
#     },
#     {
#         "id": 15,
#         "last_name": "Тихонов",
#         "first_name": "Андрей",
#         "middle_name": "Валерьевич",
#         "birth_date": "23.07.1976",
#         "last_visit": "2024-02-26T11:25:00",
#         "diagnosis": "Подагра"
#     },
#     {
#         "id": 16,
#         "last_name": "Соколова",
#         "first_name": "Виктория",
#         "middle_name": "Анатольевна",
#         "birth_date": "01.09.1984",
#         "last_visit": "2024-02-25T15:10:00",
#         "diagnosis": "Хронический пиелонефрит"
#     },
#     {
#         "id": 17,
#         "last_name": "Лебедев",
#         "first_name": "Константин",
#         "middle_name": "Сергеевич",
#         "birth_date": "16.12.1968",
#         "last_visit": "2024-02-24T10:20:00",
#         "diagnosis": "Атеросклероз сосудов"
#     },
#     {
#         "id": 18,
#         "last_name": "Морозова",
#         "first_name": "Наталья",
#         "middle_name": "Владимировна",
#         "birth_date": "27.02.1979",
#         "last_visit": "2024-02-23T14:55:00",
#         "diagnosis": "Остеопороз"
#     },
#     {
#         "id": 19,
#         "last_name": "Ковалёв",
#         "first_name": "Денис",
#         "middle_name": "Павлович",
#         "birth_date": "09.06.1993",
#         "last_visit": "2024-02-22T08:40:00",
#         "diagnosis": "Сколиоз 2 степени"
#     },
#     {
#         "id": 20,
#         "last_name": "Зайцева",
#         "first_name": "Людмила",
#         "middle_name": "Игоревна",
#         "birth_date": "04.11.1986",
#         "last_visit": "2024-02-21T12:30:00",
#         "diagnosis": "Хронический тонзиллит"
#     },
#     {
#         "id": 21,
#         "last_name": "Борисов",
#         "first_name": "Роман",
#         "middle_name": "Алексеевич",
#         "birth_date": "13.08.1972",
#         "last_visit": "2024-02-20T16:15:00",
#         "diagnosis": "Язвенная болезнь желудка"
#     },
#     {
#         "id": 22,
#         "last_name": "Киселёва",
#         "first_name": "Алина",
#         "middle_name": "Олеговна",
#         "birth_date": "22.05.1994",
#         "last_visit": "2024-02-19T09:50:00",
#         "diagnosis": "Анемия железодефицитная"
#     },
#     {
#         "id": 23,
#         "last_name": "Макаров",
#         "first_name": "Владислав",
#         "middle_name": "Денисович",
#         "birth_date": "07.01.1989",
#         "last_visit": "2024-02-18T13:25:00",
#         "diagnosis": "Грыжа пищеводного отверстия"
#     },
#     {
#         "id": 24,
#         "last_name": "Полякова",
#         "first_name": "Юлия",
#         "middle_name": "Викторовна",
#         "birth_date": "30.04.1981",
#         "last_visit": "2024-02-17T11:10:00",
#         "diagnosis": "Дискинезия желчевыводящих путей"
#     },
#     {
#         "id": 25,
#         "last_name": "Гусев",
#         "first_name": "Александр",
#         "middle_name": "Геннадьевич",
#         "birth_date": "17.10.1974",
#         "last_visit": "2024-02-16T15:45:00",
#         "diagnosis": "Хронический простатит"
#     },
#     {
#         "id": 26,
#         "last_name": "Филиппова",
#         "first_name": "Евгения",
#         "middle_name": "Андреевна",
#         "birth_date": "12.03.1987",
#         "last_visit": "2024-02-15T08:30:00",
#         "diagnosis": "Эндометриоз"
#     },
#     {
#         "id": 27,
#         "last_name": "Дмитриев",
#         "first_name": "Максим",
#         "middle_name": "Ильич",
#         "birth_date": "26.07.1990",
#         "last_visit": "2024-02-14T12:20:00",
#         "diagnosis": "Синдром раздражённого кишечника"
#     },
#     {
#         "id": 28,
#         "last_name": "Семёнова",
#         "first_name": "Анастасия",
#         "middle_name": "Романовна",
#         "birth_date": "19.09.1983",
#         "last_visit": "2024-02-13T16:05:00",
#         "diagnosis": "Хронический цистит"
#     },
#     {
#         "id": 29,
#         "last_name": "Тарасов",
#         "first_name": "Артём",
#         "middle_name": "Васильевич",
#         "birth_date": "03.12.1977",
#         "last_visit": "2024-02-12T09:40:00",
#         "diagnosis": "Псориаз"
#     },
#     {
#         "id": 30,
#         "last_name": "Воробьёва",
#         "first_name": "Дарья",
#         "middle_name": "Сергеевна",
#         "birth_date": "14.06.1996",
#         "last_visit": "2024-02-11T13:15:00",
#         "diagnosis": "Бронхит курильщика"
#     }
# ]


def get_patients(request):

    patients = Patient.objects.select_related('medical_card').all()

    context = {
        'title': 'Список пациентов',
        'content': 'Список недавно просмотренных пациентов',
        'patients': patients,
    }
    return render(request, 'patients/patients_list.html', context)


def case_history(request):
    context = {
        'title': 'О пациенте',
        'content': 'Все данные пациента',
        'text_on_page': 'Далеко-далеко за словесными горами в стране, гласных и согласных живут рыбные тексты. Коварный встретил пор, составитель снова собрал даже рукопись от всех? Предупредила буквоград правилами его вдали. Продолжил путь парадигматическая вопроса всеми себя?',
    }
    return render(request, 'patients/case_history.html', context)
