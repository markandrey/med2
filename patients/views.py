from django.shortcuts import render


patients = [
    {
        "id": 1,
        "last_name": "Иванов",
        "first_name": "Иван",
        "middle_name": "Иванович",
        "birth_date": "15.05.1980",
        "medical_card": "A12345",
        "last_visit": "2023-10-20T14:30:00",
        "diagnosis": "Гипертония"
    },
    {
        "id": 2,
        "last_name": "Петрова",
        "first_name": "Мария",
        "middle_name": "Сергеевна",
        "birth_date": "22.11.1975",
        "medical_card": "B67890",
        "last_visit": "2023-10-22T09:15:00",
        "diagnosis": "Сахарный диабет 2 типа"
    },
    {
        "id": 3,
        "last_name": "Сидоров",
        "first_name": "Алексей",
        "middle_name": "",
        "birth_date": "03.04.1992",
        "medical_card": "C54321",
        "last_visit": "2023-10-21T16:45:00",
        "diagnosis": "Бронхиальная астма"
    },
    {
        "id": 4,
        "last_name": "Кузнецова",
        "first_name": "Елена",
        "middle_name": "Владимировна",
        "birth_date": "30.07.1988",
        "medical_card": "D09876",
        "last_visit": "2023-10-19T11:20:00",
        "diagnosis": "Остеохондроз"
    },
    {
        "id": 5,
        "last_name": "Смирнов",
        "first_name": "Дмитрий",
        "middle_name": "Анатольевич",
        "birth_date": "12.09.1970",
        "medical_card": "E67890",
        "last_visit": "2023-10-18T13:10:00",
        "diagnosis": "ИБС"
    }
]




def get_patients(request):
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
